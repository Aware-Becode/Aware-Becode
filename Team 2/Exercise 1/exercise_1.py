"""
Aware-Becode: Data Engineer Skills Analysis
Implements exercises 1 using pandas to analyze job market data
"""

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
DATA_PATH = Path(__file__).parent / "data"

company_dim = pd.read_csv(DATA_PATH / "company_dim.csv", sep=";")
job_postings_fact = pd.read_csv(DATA_PATH / "job_postings_fact.csv", sep=";")
skills_dim = pd.read_csv(DATA_PATH / "skills_dim.csv", sep=";")
skills_job_dim = pd.read_csv(DATA_PATH / "skills_job_dim.csv", sep=";")

print("Data loaded successfully!")
print(f"Job postings: {len(job_postings_fact)}")
print(f"Skills: {len(skills_dim)}")
print(f"Skill-job relationships: {len(skills_job_dim)}")
print()

# ============================================================================p
# EXERCISE 1: Most in-demand skills for data engineers (remote)
# ============================================================================

def exercise_1():
    """
    Find the top 10 in-demand skills for data engineers in remote positions.
    """
    print("=" * 70)
    print("EXERCISE 1: Most In-Demand Skills for Data Engineers (Remote)")
    print("=" * 70)
    
    # Filter for data engineers in remote positions
    data_engineers = job_postings_fact[
        (job_postings_fact['job_title_short'].str.contains('Data Engineer', case=False, na=False)) &
        (job_postings_fact['job_work_from_home'] == True)
    ]
    
    print(f"Found {len(data_engineers)} remote Data Engineer positions")
    
    # Join with skills
    merged = data_engineers.merge(skills_job_dim, on='job_id')
    merged = merged.merge(skills_dim, on='skill_id')
    
    # Count skill occurrences
    skill_demand = merged.groupby('skills').size().reset_index(name='demand_count')
    top_10 = skill_demand.nlargest(10, 'demand_count')
    
    print("\nTop 10 In-Demand Skills:")
    print(top_10.to_string(index=False))
    


  

    # Set the visual style
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))

    # Create horizontal bar plot
    ax = sns.barplot(
        x='demand_count', 
        y='skills', 
        data=top_10, 
        palette='viridis' # Beautiful color gradient
    )

    # Add data labels to the end of each bar
    for container in ax.containers:
        ax.bar_label(container, padding=5, fontweight='bold')

    # Titles and Labels
    plt.title('Top 10 In-Demand Skills for Remote Data Engineers', fontsize=14, pad=15, fontweight='bold')
    plt.xlabel('Number of Job Postings (Demand Count)', fontsize=12)
    plt.ylabel('Skills', fontsize=12)

    # Clean up the borders
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    
    # Display the plot
    plt.show()



exercise_1()