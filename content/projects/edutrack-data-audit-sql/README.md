# EduTrack Data Audit

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/sql-single-table-project/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your challenge

EduTrack is a growing online learning platform that has been operating for two years. Their team has been adding enrollments manually through different channels — a web form, a sales team, and a third-party integration — and the data quality has never been formally reviewed.

You've been brought in as a data analyst contractor. The platform's operations lead has sent you the following brief:

> **From:** Operations Lead, EduTrack  
> **To:** Data Analyst (contractor)  
> **Subject:** Database audit — Q3
>
> Hi,
>
> We need a full health check of our `enrollments` table before we start the Q3 reporting cycle. Specifically:
>
> - We suspect there are students with suspiciously low progress — we'd like to identify them.
> - Some records were imported from an old system and contain test accounts (`@test.com`) whose enrollments should be removed.
> - A batch of enrollments from a partner integration came in without the instructor field filled in — those need to be corrected.
> - We're also missing at least one enrollment that was confirmed by email but never entered — please add it.
> - We need aggregated numbers by course category: total revenue collected, average completion, and which categories are underperforming.
>
> Please document everything in a written analysis report — not just the queries, but the actual findings. We need to be able to share this with the team without them having to run SQL.
>
> Thanks

You've been given a `.sql` file that creates and populates the database. Import it into Supabase and get to work.

The table you'll be working with is `enrollments`, which tracks every student-course pairing along with progress and payment data. The `students` and `courses` tables are also present in the schema — **do not modify them** at this stage. Your entire analysis lives inside `enrollments`.

This is the kind of audit task that comes up constantly in startups. The cleaner the data going into reporting, the more trustworthy the output.

---

## 🌱 How to Start the Project

This project does not start from a code template: you create an empty repository and, inside it, a SQL file with your queries and a Markdown report with your findings.

1. Download the provided [edutrack.sql](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/refs/heads/main/content/projects/edutrack-data-audit-sql/edutrack.sql) file.
2. Log in to [Supabase](https://supabase.com) and create a new project.
3. Go to **SQL Editor** and run the full contents of `edutrack.sql` to create and populate the database.
4. Verify the import succeeded by running `SELECT * FROM enrollments LIMIT 5;`.
5. Create an empty repository on GitHub and add two files at its root: `queries.sql` (your queries) and `analysis_report.md` (your results). Supabase does not store files: use it only to run and test your queries.
6. Every time a query works in Supabase, copy it into `queries.sql` with a comment indicating its number (e.g. `-- Q6: missing enrollment`), and write down the result in `analysis_report.md`.

> 💡 Tip: Before running any UPDATE or DELETE, always run a SELECT with the same WHERE clause first to confirm you're targeting the right rows.

---

## 💻 What You Need to Do

> Run the queries **in order (Q1 → Q12)**. The aggregations (Q9–Q12) must be calculated **after** the data corrections (Q6–Q8), because their results change when records are added or deleted.

### Database Setup

- [ ] Import `edutrack.sql` into a Supabase project successfully
- [ ] Verify that the `enrollments`, `students`, and `courses` tables exist and contain data

### Queries — Reading and Filtering

- [ ] **Q1.** List all enrollments for the course `'Intro to Python'`, showing student name, email, and completion percentage
- [ ] **Q2.** Retrieve all enrollments where `completion_percentage` is less than 10 — these are potential dropouts
- [ ] **Q3.** Find all enrollments where the instructor field is `NULL`
- [ ] **Q4.** List the 5 students with the highest `completion_percentage` who have **not** yet passed (`passed = false`)
- [ ] **Q5.** Show all enrollments with an `enrollment_date` on or after `'2024-07-01'`, ordered by `enrollment_date` descending

### Queries — Data Corrections

- [ ] **Q6.** **INSERT** the missing enrollment record provided in the brief (student name, email, course, date, and initial values are specified in the comments of `edutrack.sql`)
- [ ] **Q7.** **UPDATE** all enrollments where `instructor` is `NULL` — assign the default value `'Pending assignment'`
- [ ] **Q8.** **DELETE** all enrollments tied to the imported test accounts (`@test.com`) — confirm the affected rows with a SELECT first

### Queries — Aggregation and Reporting

- [ ] **Q9.** Count the number of enrollments grouped by `category`
- [ ] **Q10.** Calculate the average `completion_percentage` grouped by `course_title`, ordered from lowest to highest
- [ ] **Q11.** Show only the courses with **more than 3 enrollments** (use `HAVING`)
- [ ] **Q12.** Calculate total revenue (`SUM` of `monthly_fee_paid`) grouped by `category`, ordered from highest to lowest

### Analysis Report

- [ ] Complete the `analysis_report.md` file included in the repository, filling in the result of each query in the corresponding section

The report follows a fixed structure — one section per query. Your job is to fill in the numbers and lists that your SQL returned. Example of the expected format:

```markdown
## Q1 — Enrollments in 'Intro to Python'

Result: 10

## Q9 — Enrollments by category

Result:

- Programming: 45
- Design: 23
- Data: 18
- Marketing: 12
```

⚠️ **IMPORTANT:** Do not use AI tools to generate your SQL queries. Write each one yourself. The goal is to build the muscle memory for reading and constructing SQL — that only happens through your own hands.

---

## ✅ What We Will Evaluate

- [ ] All 12 queries are present in `queries.sql` and execute without errors in Supabase
- [ ] SELECT queries return the correct rows and columns based on the specified conditions
- [ ] The INSERT adds the correct record with all required fields
- [ ] The UPDATE targets only the NULL instructor rows and assigns the correct default value
- [ ] The DELETE removes only `@test.com` records and no other rows
- [ ] GROUP BY queries produce correct aggregations (count, average, sum)
- [ ] HAVING is used correctly to filter aggregated results
- [ ] `analysis_report.md` has a section for every query with the actual result filled in (not left blank)

> Note: The structure or content of the `students` and `courses` tables is not evaluated in this project — only work done on `enrollments` will be assessed.

---

## 📦 How to Submit

1. Make sure the final version of `queries.sql` and `analysis_report.md` is saved (commit and push) in your repository.
2. Make sure both files are at the root of the repository and that the repo is public.
3. Submit the repository link in this view.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/sql-single-table-project/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
