import pandas as pd

#company_dim = pd.read_csv("./data/company_dim.csv",sep=";")
job_postings_fact = pd.read_csv("./data/job_postings_fact.csv",sep=";")
skills_dim = pd.read_csv("./data/skills_dim.csv",sep=";")
skills_job_dim = pd.read_csv("./data/skills_job_dim.csv",sep=";")

# filter on salaray_rate that exist and job title is data engineer
job_postings_fact_with_salary = job_postings_fact[(~job_postings_fact["salary_rate"].isna()) & (job_postings_fact["job_title_short"] == "Data Engineer")]

skills = pd.merge(skills_dim,skills_job_dim,how='right',on="skill_id")
skills_job = pd.merge(skills,job_postings_fact_with_salary,how="right",on="job_id")

skills_job['salary'] = skills_job['salary_year_avg']

skills_job['salary_mean'] = skills_job.groupby('skills')['salary'].transform('mean')

print(skills_job.sort_values("salary_mean",ascending=False).drop_duplicates(subset="skills").head(10))

