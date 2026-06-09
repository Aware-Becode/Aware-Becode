import pandas as pd


def main():

# ── 1. company_dim ────────────────────────────────────────────────
    company_dim = pd.read_csv("./data/company_dim.csv")

    company_dim = company_dim.astype({
        "company_id": "Int64",   # nullable integer (PRIMARY KEY)
        "name":        "string",
        "link":        "string",
        "link_google": "string",
        "thumbnail":   "string",
    })

    print("company_dim:", company_dim.shape)
    print(company_dim.dtypes, "\n")


    # ── 2. skills_dim ─────────────────────────────────────────────────
    skills_dim = pd.read_csv("./data/skills_dim.csv")

    skills_dim = skills_dim.astype({
        "skill_id": "Int64",
        "skills":   "string",
        "type":     "string",
    })

    print("skills_dim:", skills_dim.shape)
    print(skills_dim.dtypes, "\n")


    # ── 3. job_postings_fact ──────────────────────────────────────────
    job_postings_fact = pd.read_csv(
        "./data/job_postings_fact.csv",
        parse_dates=["job_posted_date"],   # TIMESTAMP
    )

    job_postings_fact = job_postings_fact.astype({
        "job_id":               "Int64",
        "company_id":           "Int64",
        "job_title_short":      "string",
        "job_title":            "string",
        "job_location":         "string",
        "job_via":              "string",
        "job_schedule_type":    "string",
        "job_work_from_home":   "boolean",  # BOOLEAN
        "search_location":      "string",
        "job_no_degree_mention":"boolean",
        "job_health_insurance": "boolean",
        "job_country":          "string",
        "salary_rate":          "string",
        "salary_year_avg":      "float64",  # DOUBLE
        "salary_hour_avg":      "float64",
    })

    print("job_postings_fact:", job_postings_fact.shape)
    print(job_postings_fact.dtypes, "\n")


    # ── 4. skills_job_dim (bridge table) ─────────────────────────────
    skills_job_dim = pd.read_csv("./data/skills_job_dim.csv")

    skills_job_dim = skills_job_dim.astype({
        "skill_id": "Int64",
        "job_id":   "Int64",
    })

    print("skills_job_dim:", skills_job_dim.shape)
    print(skills_job_dim.dtypes, "\n")


    # ── 5. Vérifications basiques ─────────────────────────────────────

    # Pas de doublons sur les clés primaires
    assert company_dim["company_id"].is_unique, "Doublons dans company_dim.company_id"
    assert skills_dim["skill_id"].is_unique,    "Doublons dans skills_dim.skill_id"
    assert job_postings_fact["job_id"].is_unique,"Doublons dans job_postings_fact.job_id"
    assert skills_job_dim.duplicated(subset=["skill_id","job_id"]).sum() == 0, \
        "Doublons dans skills_job_dim (skill_id, job_id)"

    # Intégrité référentielle
    orphan_jobs = ~job_postings_fact["company_id"].isin(company_dim["company_id"])
    assert not orphan_jobs.any(), f"{orphan_jobs.sum()} jobs sans company correspondante"

    orphan_skills = ~skills_job_dim["skill_id"].isin(skills_dim["skill_id"])
    assert not orphan_skills.any(), f"{orphan_skills.sum()} skill_ids orphelins dans skills_job_dim"

    orphan_job_refs = ~skills_job_dim["job_id"].isin(job_postings_fact["job_id"])
    assert not orphan_job_refs.any(), f"{orphan_job_refs.sum()} job_ids orphelins dans skills_job_dim"

    print("✅ Toutes les vérifications sont passées.")

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