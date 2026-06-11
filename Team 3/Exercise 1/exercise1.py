import duckdb

con = duckdb.connect()

con.execute("""
    CREATE VIEW jobs AS
    SELECT * FROM read_csv_auto('data/job_postings_fact.csv', delim=';', header=true);
""")
con.execute("""
    CREATE VIEW skills_job AS
    SELECT * FROM read_csv_auto('data/skills_job_dim.csv', delim=';', header=true);
""")
con.execute("""
    CREATE VIEW skills AS
    SELECT * FROM read_csv_auto('data/skills_dim.csv', delim=';', header=true);
""")
result = con.execute("""
    SELECT
        s.skills,
        COUNT(*) AS demand_count
    FROM jobs j
    JOIN skills_job sj ON j.job_id = sj.job_id
    JOIN skills s      ON sj.skill_id = s.skill_id
    WHERE j.job_title_short = 'Data Engineer'
      AND j.job_work_from_home = true
    GROUP BY s.skills
    ORDER BY demand_count DESC
    LIMIT 10
""").df()

print(result)