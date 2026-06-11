import pandas as pd

company_df = pd.read_csv("./../data/company_dim.csv")
job_postings_df = pd.read_csv("./../data/job_postings_fact.csv")
skills_df = pd.read_csv("./../data/skills_dim.csv")
skills_job_df = pd.read_csv("./../data/skills_job_dim.csv")

print(company_df.head())