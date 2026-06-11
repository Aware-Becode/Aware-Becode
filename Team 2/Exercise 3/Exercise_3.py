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

def exercise_3():
    
    """
    Find the most optimal skills balancing both demand and salary.
    Uses a ranking column combining demand count and median salary
    with natural log transformation.
    """
    print("=" * 70)
    print("EXERCISE 3: Most Optimal Skills (Demand & Salary Balance)")
    print("=" * 70)
    
    # Filter for data engineers in remote positions with specified salaries
    data_engineers = job_postings_fact[
        (job_postings_fact['job_title_short'].str.contains('Data Engineer', case=False, na=False)) &
        (job_postings_fact['job_work_from_home'] == True) &
        (job_postings_fact['salary_year_avg'].notna())
    ]
    
    print(f"Analyzing {len(data_engineers)} positions with salary data")
    
    # Join with skills
    merged = data_engineers.merge(skills_job_dim, on='job_id')
    merged = merged.merge(skills_dim, on='skill_id')
    
    # Calculate metrics for each skill
    skill_metrics = merged.groupby('skills').agg(
        demand_count=('job_id', 'count'),
        median_salary=('salary_year_avg', 'median')
    ).reset_index()
    
    # Create optimal ranking: combine demand and salary using natural log
    # This balances high-salary outliers with widely-demanded skills
    skill_metrics['optimal_score'] = (
        np.log(skill_metrics['demand_count'] + 1) + 
        np.log(skill_metrics['median_salary'] + 1)
    )
    
    # Sort by optimal score
    top_optimal = skill_metrics.sort_values('optimal_score', ascending=False).head(10)
    
    # Round for better readability
    top_optimal = top_optimal.copy()
    top_optimal['median_salary'] = top_optimal['median_salary'].round(2)
    top_optimal['optimal_score'] = top_optimal['optimal_score'].round(2)
    
    print("\nTop 10 Most Optimal Skills (Demand × Salary Balance):")
    print(top_optimal.to_string(index=False))
    print()
    
    return top_optimal

exercise_3()
