import pandas as pd
import matplotlib.pyplot as plt

def exercise_1():
  """
    Most in-demand skills for data engineers
  """
  job_postings = pd.read_csv('../assets/job_postings_fact.csv', sep=';')
  job_postings = job_postings[['job_id', 'job_title', 'job_work_from_home']]

  # Filtering for data engineer job titles and remote jobs
  job_postings = job_postings[job_postings['job_title'].str.contains('data engineer', case=False, na=False) 
                              & job_postings['job_work_from_home'] == True]
  
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

  # Count skills and sort by most in-demand
  skill_counts = jobs_with_skill_name['skills'].value_counts().sort_values(ascending=False)
  top_10_skills = skill_counts.head(10)
  print(top_10_skills)  

  # Drawing chart to show the top 10 skills for data engineers
  plt.figure(figsize=(10,6))
  top_10_skills.plot(kind='bar')
  plt.title('Top 10 In-Demand Skills for Data Engineers (Remote Jobs)')
  plt.xlabel('Skills')
  plt.ylabel('Number of Job Postings')
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()
  plt.show()  

exercise_1()