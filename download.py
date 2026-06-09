import pandas as pd


def main()
    urls = {
        "company_dim": "https://storage.googleapis.com/sql_de/company_dim.csv",
        "skills_dim": "https://storage.googleapis.com/sql_de/skills_dim.csv",
        "job_postings_fact": "https://storage.googleapis.com/sql_de/job_postings_fact.csv",
        "skills_job_dim": "https://storage.googleapis.com/sql_de/skills_job_dim.csv",
    }

    for name, url in urls.items():
        print(f"Téléchargement de {name}...")
        df = pd.read_csv(url)
        df.to_csv(f"data/{name}.csv", index=False)
        print(f"✅ {name}.csv sauvegardé ({len(df)} lignes)")


if __name__ == "__main__":
    main()
