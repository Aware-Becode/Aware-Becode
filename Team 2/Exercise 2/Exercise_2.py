import pandas as pd
import numpy as np
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt



jobs = pd.read_csv("data/job_postings_fact.csv", sep = ";")
skills = pd.read_csv("data/skills_dim.csv", sep = ";")
skills_job = pd.read_csv("data/skills_job_dim.csv", sep = ";")

merged = jobs.merge(skills_job, on= "job_id")
merged = merged.merge(skills, on= "skill_id")

filtered = merged[
    (merged["job_work_from_home"] == True) &
    (merged["job_title_short"].str.contains("Data Engineer",
                                            case = False, na = False)&
    merged["salary_year_avg"].notna()                                        )
]
grouped = filtered.groupby("skills")["salary_year_avg"].agg(median = "median", count = "count")
top_10 = grouped.sort_values(by = "median", ascending = False).head(10)

print(top_10)

fig, axes = plt.subplots(ncols =2)

sns.barplot(data = top_10, x = "median", y = "skills", ax = axes[0])
axes[0].set_title("Highest Paying Skills")
axes[0].set_xlabel("Median Salary")
axes[0].set_ylabel("Skills")

sns.barplot(data = top_10, x = "count", y = "skills", ax = axes[1])
axes[1].set_title("Skills demand")
axes[1].set_xlabel("count")
axes[1].set_ylabel("Skills")

for i, v in enumerate(top_10["count"]):
    axes[1].text(v+2, i , str(v), va = 'center')

plt.tight_layout()
plt.show()