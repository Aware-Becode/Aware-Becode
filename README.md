# Aware-Becode

Aware@Becode Exercices

## 🧩 Problem & Context

Job market analysts need to answer questions like:

- 🎯 **Most in-demand:** *Which skills are most in-demand for data engineers?*
- 💰 **Highest paid:** *Which skills command the highest salaries?*
- ⚖️ **Best trade-off:** *What is the optimal skill set balancing demand and compensation?*

This project analyzes a **data warehouse** built using a star schema design. The warehouse structure consists of:

![Data Warehouse Schema](Images/1_2_Data_Warehouse.png)

- **Fact Table:** `job_postings_fact` - Central table containing job posting details (job titles, locations, salaries, dates, etc.)
- **Dimension Tables:**
  - `company_dim` - Company information linked to job postings
  - `skills_dim` - Skills catalog with skill names and types
- **Bridge Table:** `skills_job_dim` - Resolves the many-to-many relationship between job postings and skills

By querying across these interconnected tables, I extracted insights about skill demand, salary patterns, and optimal skill combinations for data engineering roles.

## 📝 Exercises

### Exercise 1 — Most in-demand skills for data engineers

**Question:** *What are the most in-demand skills for data engineers?*

- Join job postings to the inner join table similar to query 2.
- Identify the top 10 in-demand skills for data engineers.
- Focus on remote job postings.

**Why?** Retrieves the top 10 skills with the highest demand in the remote job market, providing insights into the most valuable skills for data engineers seeking remote work.

### Exercise 2 — Highest-paying skills for data engineers

**Question:** *What are the highest-paying skills for data engineers?*

- Calculate the median salary for each skill required in data engineer positions.
- Focus on remote positions with specified salaries.
- Include skill frequency to identify both salary and demand.

**Why?** Helps identify which skills command the highest compensation while also showing how common those skills are, providing a more complete picture for skill development priorities.

### Exercise 3 — Most optimal skills (balancing demand and salary)

**Question:** *What are the most optimal skills for data engineers — balancing both demand and salary?*

- Create a ranking column that combines demand count and median salary to identify the most valuable skills.
- Focus only on remote Data Engineer positions with specified annual salaries.

**Why?**

- This approach highlights skills that balance market demand and financial reward. It weights core skills appropriately instead of letting rare, outlier skills distort the results.
- The natural log transformation ensures that both high-salary and widely in-demand skills surface as the most practical and valuable to learn for data engineering careers.
