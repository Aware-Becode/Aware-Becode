import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def exercise_2():
  """
    Highest-paying skills for data engineers
  """
  job_postings = pd.read_csv('../assets/job_postings_fact.csv', sep=';')
  job_postings = job_postings[['job_id', 'job_title', 'job_work_from_home', 'salary_rate', 'salary_year_avg', 'salary_hour_avg' ]]

  # Filtering for data engineer job titles and remote jobs
  job_postings = job_postings[job_postings['job_title'].str.contains('data engineer', case=False, na=False) 
                              & job_postings['job_work_from_home'] == True]
  
  # Fillter the row including salary_year_avg and salary_hour_avg are null
  # Keep rows that have either yearly or hourly salary
  job_postings = job_postings[
    job_postings['salary_year_avg'].notna() |
    job_postings['salary_hour_avg'].notna()
  ]

  # Create a comparable annual salary column
  job_postings['salary_annualized'] = (
    job_postings['salary_year_avg']
    .fillna(job_postings['salary_hour_avg'] * 40 * 52)
  )
  job_postings = job_postings[['job_id', 'job_title', 'job_work_from_home', 'salary_annualized' ]]

  # Merging with skills_job_dim to get the skills associated with each job 
  skills_job = pd.read_csv('../assets/skills_job_dim.csv', sep=';')
  jobs = pd.merge(
    job_postings,
    skills_job[['job_id','skill_id']],
    on='job_id',
    how='left'   
  )

  skills = pd.read_csv('../assets/skills_dim.csv', sep=';')
  jobs_with_skill_name = pd.merge(
    jobs,
    skills[['skill_id', 'skills']],
    on='skill_id',
    how='left'   
  )

  # Highest-paying skills for data engineers
  highest_paying_skill = (
    jobs_with_skill_name
    .groupby('skills')['salary_annualized']
    .median()
    .sort_values(ascending=False)
  ).head(10)

  ax = highest_paying_skill.plot(
    kind='bar',
    figsize=(10, 6)
  )

  ax.set_title('Top 10 Highest-Paying Skills for Data Engineers (Remote Jobs)')
  ax.set_xlabel('Skills')
  ax.set_ylabel('Average Annual Salary (€)')

  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()
  plt.show()  

exercise_2()