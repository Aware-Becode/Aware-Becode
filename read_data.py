import pandas as pd


def main():
    company_dim = pd.read_csv("data/company_dim.csv")
    skills_dim = pd.read_csv("data/skills_dim.csv")
    job_postings_fact = pd.read_csv("data/job_postings_fact.csv")
    skills_job_dim = pd.read_csv("data/skills_job_dim.csv")

    print("=== company_dim ===")
    print(company_dim.head())
    print(company_dim.shape)

    print("\n=== skills_dim ===")
    print(skills_dim.head())
    print(skills_dim.shape)

    print("\n=== job_postings_fact ===")
    print(job_postings_fact.head())
    print(job_postings_fact.shape)

    print("\n=== skills_job_dim ===")
    print(skills_job_dim.head())
    print(skills_job_dim.shape)

if __name__ == "__main__":
    main()