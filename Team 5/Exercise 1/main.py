import pandas as pd
import matplotlib.pyplot as plt

company_df = pd.read_csv("./../data/company_dim.csv")
job_postings_df = pd.read_csv("./../data/job_postings_fact.csv")
skills_df = pd.read_csv("./../data/skills_dim.csv")
skills_job_df = pd.read_csv("./../data/skills_job_dim.csv")
# Reading each file and storing the content of each one in a DataFrame.

# Filter for remote Data Engineer job postings
de_remote = job_postings_df[
    (job_postings_df["job_title_short"] == "Data Engineer") &
    # Keep only job postings with the title "Data Engineer"
    (job_postings_df["job_work_from_home"] == True)
    # And the ones where you can work at home.
][["job_id"]]
# Keep only the job_id column after filtering

# Now we are joining DE Skills with job tables
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

ax = top10.plot.bar(x="skills", y="demand_count", legend=False)
ax.set_xlabel("Skills")
ax.set_ylabel("Demand Count")
ax.set_title("Top 10 Skills for Remote Data Engineers")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()