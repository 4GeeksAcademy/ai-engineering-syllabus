# EduTrack Data Audit

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/sql-single-table-project/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

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

This project does not require a code repository — your deliverable is a SQL file with your queries and a Markdown report with your findings.

1. Download the provided [edutrack.sql](edutrack.sql) file from the platform.
2. Log in to [Supabase](https://supabase.com) and create a new project.
3. Go to **SQL Editor** and run the full contents of `edutrack.sql` to create and populate the database.
4. Verify the import succeeded by running `SELECT * FROM enrollments LIMIT 5;`.
5. Create a new file called `queries.sql` where you'll write and save all your queries.
6. Create a new file called `analysis_report.md` where you'll document your findings.

> 💡 Tip: Before running any UPDATE or DELETE, always run a SELECT with the same WHERE clause first to confirm you're targeting the right rows.

---

## 💻 What You Need to Do

### Database Setup

- [ ] Import `edutrack.sql` into a Supabase project successfully
- [ ] Verify that the `enrollments`, `students`, and `courses` tables exist and contain data

### Queries — Reading and Filtering

- [ ] List all enrollments for the course `'Intro to Python'`, showing student name, email, and completion percentage
- [ ] Retrieve all enrollments where `completion_percentage` is less than 10 — these are potential dropouts
- [ ] Find all enrollments where the instructor field is `NULL`
- [ ] List the 5 students with the highest `completion_percentage` who have **not** yet passed (`passed = false`)
- [ ] Show all enrollments created in the last year, ordered by `enrollment_date` descending

### Queries — Data Corrections

- [ ] **INSERT** the missing enrollment record provided in the brief (student name, email, course, date, and initial values are specified in the `edutrack.sql` comments)
- [ ] **UPDATE** all enrollments where `instructor` is `NULL` — assign the default value `'Pending assignment'`
- [ ] **DELETE** all enrollments tied to the imported test accounts (`@test.com`) — confirm the affected rows with a SELECT first

### Queries — Aggregation and Reporting

- [ ] Count the number of enrollments grouped by `category`
- [ ] Calculate the average `completion_percentage` grouped by `course_title`, ordered from lowest to highest
- [ ] Show only the courses with **more than 3 enrollments** (use `HAVING`)
- [ ] Calculate total revenue (`SUM` of `monthly_fee_paid`) grouped by `category`, ordered from highest to lowest

### Analysis Report

- [ ] Complete the `analysis_report.md` file included in the repository, filling in the result of each query in the corresponding section

The report follows a fixed structure — one section per query. Your job is to fill in the numbers and lists that your SQL returned. Example of the expected format:

```markdown
## Enrollments in 'Intro to Python'

Result: 10

## Enrollments by category

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

1. Push `queries.sql` and `analysis_report.md` to a GitHub repository.
2. Share the repository link with your instructor following their instructions.
3. Make sure both files are at the root of the repository and that the repo is public.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/sql-single-table-project/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
