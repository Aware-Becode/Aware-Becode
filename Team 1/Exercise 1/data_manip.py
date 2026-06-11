import pandas as pd
postings_fact = pd.read_csv(r"C:\Users\danuk\OneDrive\bureaubc\aware challenge\Team 1\job_postings_fact.csv", sep=None, engine='python')
skills_dim = pd.read_csv(r"C:\Users\danuk\OneDrive\bureaubc\aware challenge\Team 1\skills_dim.csv", sep=None, engine='python')
skills_job = pd.read_csv(r"C:\Users\danuk\OneDrive\bureaubc\aware challenge\Team 1\skills_job_dim.csv", sep=None, engine='python')
company_dim = pd.read_csv(r"C:\Users\danuk\OneDrive\bureaubc\aware challenge\Team 1\company_dim.csv", sep=None, engine='python')
job_id = postings_fact.query("job_title_short == 'Data Engineer'")['job_id'].tolist()
skills_filtered = skills_job[skills_job['job_id'].isin(job_id)]
skills_merged = skills_filtered.merge(skills_dim, on='skill_id')
top_10_skills = (skills_merged
                 .groupby('skills')['skill_id']
                 .count()
                 .reset_index()
                 .rename(columns={'skill_id': 'demand_count'})
                 .sort_values('demand_count', ascending=False)
                 .head(10))

print(top_10_skills)
print(postings_fact.describe())
print(postings_fact.info())