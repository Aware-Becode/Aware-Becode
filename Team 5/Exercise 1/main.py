import pandas as pd

company_df = pd.read_csv("./../data/company_dim.csv")
job_postings_df = pd.read_csv("./../data/job_postings_fact.csv")
skills_df = pd.read_csv("./../data/skills_dim.csv")
skills_job_df = pd.read_csv("./../data/skills_job_dim.csv")

# print(company_df.info())
# print(job_postings_df.info())
# print(skills_df.info())
# print(skills_job_df.info())

# print(company_df.head())

# Exercise 1 — Top 10 most in-demand skills for remote Data Engineers

# Step 1: Filter for remote Data Engineer postings
de_remote = job_postings_df[
    (job_postings_df["job_title_short"] == "Data Engineer") &
    (job_postings_df["job_work_from_home"] == True)
][["job_id"]]

# Step 2: Join to skills bridge table
de_skills = de_remote.merge(skills_job_df, on="job_id")

# Step 3: Join to skills dimension
de_skills = de_skills.merge(skills_df[["skill_id", "skills"]], on="skill_id")

# Step 4: Count and rank
top10 = (
    de_skills["skills"]
    .value_counts()
    .head(10)
    .reset_index()
    .rename(columns={"count": "demand_count"})
)

print(top10)