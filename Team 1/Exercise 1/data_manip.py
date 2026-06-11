import pandas as pd

company_dim = pd.read_csv(r"C:\Users\danuk\OneDrive\bureaubc\company_dim.csv", sep=None, engine='python')
postings_fact = pd.read_csv(r"C:\Users\danuk\OneDrive\bureaubc\job_postings_fact.csv", sep=None, engine='python')
print(company_dim)
print(postings_fact)