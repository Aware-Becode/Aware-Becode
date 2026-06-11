# Aware-Becode
 
## 🚀 Git Workflow — Mini Tutorial

This section walks you through the full collaboration flow used in this repo: clone, branch, commit, pull request, review, merge.

### 1️⃣ Clone the repository

Clone the repo to your local machine:

```bash
git clone https://github.com/Aware-Becode/Aware-Becode.git
cd Aware-Becode
```
⚠️ Before committing anything, create a .gitignore and add your venv/ and data/ directories to it.
> 💡 If you have `gh` (GitHub CLI) installed and authenticated, you can also run:
> `gh repo clone Aware-Becode/Aware-Becode`

### 2️⃣ Create a feature branch

Never work directly on `main`. Create a branch for your change:

```bash
git checkout main
git pull                                  # always start from up-to-date main
git checkout -b feat/my-exercise          # name reflects what you are doing
```

> 💡 **Branch naming convention**
> - `feat/...` for a new feature or exercise
> - `fix/...` for a bug fix
> - `docs/...` for documentation only

### 3️⃣ Commit your work locally

Stage and commit your changes with a clear message:

```bash
git add path/to/file.sql                  # stage specific files
git status                                # confirm what is staged
git commit -m "feat(exercise-1): add top-10 in-demand skills query"
```

> 💡 **Commit message convention** (Conventional Commits): `type(scope): description`
> Common types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.

### 4️⃣ Push your branch and open a Pull Request

Push the branch to GitHub:

```bash
git push -u origin feat/my-exercise
```

Then open a Pull Request:

- **Via GitHub website** — go to the repo on github.com, click the yellow banner "Compare & pull request" that appears, fill in title and description, click **Create pull request**.
- **Via CLI** — `gh pr create --fill` (uses your last commit message) or `gh pr create` (opens an editor).

A good PR includes:
- A descriptive title.
- A short **Summary** of what changed and why.
- A **Test plan** explaining how to verify the change.

### 5️⃣ Review a Pull Request

When a classmate opens a PR, review it:

1. On github.com, open the PR → tab **Files changed**.
2. Read each change. Click any line to add an **inline comment**.
3. At the top right, click **Review changes** and choose:
   - **Comment** — leave feedback without blocking.
   - **Approve** ✅ — the change looks good to merge.
   - **Request changes** ❌ — something must be fixed before merging.
4. Discuss in the **Conversation** tab until the author updates the PR.

> 💡 You cannot approve your own PR — you need someone else to review yours.

### 6️⃣ Merge into `main`

Once the PR is approved and all comments are resolved:

1. On the PR page, click **Merge pull request** → **Confirm merge**.
2. Click **Delete branch** to keep the repo tidy.
3. Locally, sync your `main`:

```bash
git checkout main
git pull
git branch -d feat/my-exercise            # remove the local branch
```

🎉 Your work is now on `main` and visible to everyone.

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

## 📦 Data Sources

You have **two options** to grab the dataset.

### Option A — Bundle (Proton Drive)

Download the full dataset (all 4 CSVs) in one go:

🔗 https://drive.proton.me/urls/YZXX8RKEEC#axcxe39gsLM4

### Option B — Direct download (Google Cloud Storage)

Fetch each CSV individually:

- 🏢 [`company_dim.csv`](https://storage.googleapis.com/sql_de/company_dim.csv)
- 🛠️ [`skills_dim.csv`](https://storage.googleapis.com/sql_de/skills_dim.csv)
- 💼 [`job_postings_fact.csv`](https://storage.googleapis.com/sql_de/job_postings_fact.csv)
- 🔗 [`skills_job_dim.csv`](https://storage.googleapis.com/sql_de/skills_job_dim.csv)

> 💡 Quick download with `curl`:
> ```bash
> mkdir -p data && cd data
> curl -O https://storage.googleapis.com/sql_de/company_dim.csv
> curl -O https://storage.googleapis.com/sql_de/skills_dim.csv
> curl -O https://storage.googleapis.com/sql_de/job_postings_fact.csv
> curl -O https://storage.googleapis.com/sql_de/skills_job_dim.csv
> ```

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

## 👥 Teams & Submission

Students are split into **5 teams**. Each team has a dedicated folder at the root of the repository, with one sub-folder per exercise:

```
Team 1/
├── Exercise 1/
├── Exercise 2/
└── Exercise 3/
Team 2/
├── Exercise 1/
├── Exercise 2/
└── Exercise 3/
...
Team 5/
├── Exercise 1/
├── Exercise 2/
└── Exercise 3/
```

### 📌 Submission rules

- Every team **must commit its solutions in the folder matching its team number and the exercise number**.
  - Example: Team 3's solution for Exercise 2 goes in `Team 3/Exercise 2/`.
- Add your SQL files, notebooks, or any supporting files inside the right sub-folder.
- **Do not modify another team's folder.** Stay inside your own team's directory.
- Follow the [🚀 Git Workflow](#-git-workflow--mini-tutorial) above: branch → commit → pull request → review → merge.

> 💡 The `.gitkeep` files are placeholders that let Git track empty folders. You can leave them or delete them once you have committed your own files in the folder.
