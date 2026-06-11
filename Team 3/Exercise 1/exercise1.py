import pandas as pd
import os

os.chdir(os.path.join(os.path.dirname(__file__), "..", ".."))

jobs       = pd.read_csv("data/job_postings_fact.csv", sep=";")
skills_job = pd.read_csv("data/skills_job_dim.csv", sep=";")
skills     = pd.read_csv("data/skills_dim.csv", sep=";")

remote_de = jobs[
    (jobs["job_title_short"] == "Data Engineer")
    & (jobs["job_work_from_home"] == True)
]

merged = remote_de.merge(skills_job, on="job_id").merge(skills, on="skill_id")

top10 = (
    merged.groupby("skills")["job_id"]
    .count()
    .reset_index(name="demand_count")
    .sort_values("demand_count", ascending=False)
    .head(10)
)

print(top10)