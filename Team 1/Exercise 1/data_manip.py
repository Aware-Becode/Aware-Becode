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

def name_to_jobid(postings,skilljob,skilldim):
    job_id = postings.query("job_title_short == 'Data Engineer'")['job_id'].tolist()
    filtered = skilljob[skilljob['job_id'].isin(job_id)]
    merged = filtered.merge(skilldim,on = 'skill_id')
    return merged
def top_10(merged_frame):
    top_10_skills = (merged_frame
                 .groupby('skills')['skill_id']
                 .count()
                 .reset_index()
                 .rename(columns={'skill_id': 'demand_count'})
                 .sort_values('demand_count', ascending=False)
                 .head(10))
    return top_10_skills
frame = name_to_jobid(postings_fact,skills_job,skills_dim)
top10 = top_10(frame)
print(top10)
