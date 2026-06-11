import pandas as pd

company_dim = pd.read_csv("./../data/company_dim.csv")
job_postings = pd.read_csv("./../data/job_postings_fact.csv")
skills_dim = pd.read_csv("./../data/skills_dim.csv")
skills_job_dim = pd.read_csv("./../data/skills_job_dim.csv")

#Merging the tables
df1 = pd.merge(
    job_postings,
    skills_job_dim,
    on='job_id',
    how='inner'
)

skills_enriched = pd.merge(
    df1,
    skills_dim,
    on='skill_id',
    how='inner'
)

data_eng = skills_enriched[
    (skills_enriched['job_title_short'] == 'Data Engineer') &
    (skills_enriched['salary_year_avg'].notna())
].dropna(subset=['salary_year_avg'])

filtered_data = (
    data_eng
    .groupby(['skills', 'job_title_short', 'job_work_from_home'], observed=True)
    .agg(
        salary_median=('salary_year_avg', 'median'),
        skill_count=('skill_id', 'count')
    )
    .sort_values('job_work_from_home', ascending=False)
    .sort_values('salary_median', ascending = False)
    .reset_index()
)
print(filtered_data)