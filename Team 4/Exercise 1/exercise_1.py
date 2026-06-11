# def df_enriched == pd.merge(
#     df,
#     customers_dim[['customer_id','tier','signup_year']],
#     on='customer_id',        # key present in both DataFrames
#     how='inner'
# )

import pandas as pd

def exercise_1():
  """
    Most in-demand skills for data engineers
  """
  skills = pd.read_csv('../assets/skills_dim.csv', sep=';')
  print(skills.head(3))

  job_postings = pd.read_csv('../assets/job_postings_fact.csv', sep=';')

  print(job_postings.head(3))
exercise_1()