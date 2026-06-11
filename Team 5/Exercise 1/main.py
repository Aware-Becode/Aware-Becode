import pandas as pd

company_df = pd.read_csv("./../data/company_dim.csv")
job_postings_df = pd.read_csv("./../data/job_postings_fact.csv")
skills_df = pd.read_csv("./../data/skills_dim.csv")
skills_job_df = pd.read_csv("./../data/skills_job_dim.csv")

# Searching for remote Data Engineer postings
de_remote = job_postings_df[
    (job_postings_df["job_title_short"] == "Data Engineer") &
    (job_postings_df["job_work_from_home"] == True)
][["job_id"]]

# Now weare joining DE Skills with job table
de_skills = de_remote.merge(skills_job_df, on="job_id")

# Getting skills
de_skills = de_skills.merge(skills_df[["skill_id", "skills"]], on="skill_id")

# Count and rank
top10 = (
    de_skills["skills"]
    .value_counts()
    .head(10)
    .reset_index()
    .rename(columns={"count": "demand_count"})
)

print(top10)