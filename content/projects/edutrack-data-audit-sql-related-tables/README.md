# EduTrack Data Audit — Related Tables

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/sql-multi-table-project/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

EduTrack's engineering team has normalized the database. What used to be a single flat `enrollments` table is now a proper relational schema: students, courses, and enrollments are separate entities, each with their own table and linked by foreign keys.

The operations lead has come back with a new set of questions — but this time, none of them can be answered by looking at one table alone.

> **From:** Operations Lead, EduTrack  
> **To:** Data Analyst (contractor)  
> **Subject:** Re: Database audit — Q3 (normalized schema)
>
> Hi again,
>
> The dev team just finished migrating to the new schema. We've attached the updated `.sql` file.
>
> Now that the data is properly structured, we'd like to revisit some of the questions from last time — and add a few new ones that weren't possible before:
>
> - Which students are enrolled in more than one course? We want their names and how many courses they're taking.
> - Which courses have no enrollments at all? We might want to archive them.
> - What's the average completion percentage per instructor?
> - Which students have passed at least one course? Show their name and the course title.
> - Are there any enrollments linked to a student or course that no longer exists in the database? (Data integrity check.)
> - Which category brings in the most revenue when we factor in the actual course price?
>
> As before, please fill in the `analysis_report.md` with your results.
>
> Thanks

Before writing any query, you'll need to understand how the three tables relate to each other. Start by reading the schema carefully and drawing the entity-relationship diagram on [diagram.4geeks.com](https://diagram.4geeks.com). That diagram is your first deliverable.

The answers are in the data — you just need to know which tables to join.

---

## 🌱 How to Start the Project

1. Download the provided [edutrack_v2.sql](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/refs/heads/main/content/projects/edutrack-data-audit-sql-related-tables/edutrack_v2.sql) file from the platform.
2. Log in to [Supabase](https://supabase.com) and create a new project (or reuse the one from the previous project).
3. Go to **SQL Editor** and run the full contents of `edutrack_v2.sql` to create and populate the normalized schema.
4. Verify the import by running `SELECT * FROM enrollments LIMIT 5;`, `SELECT * FROM students LIMIT 5;` and `SELECT * FROM courses LIMIT 5;`.
5. Go to [diagram.4geeks.com](https://diagram.4geeks.com) and model the three tables and their relationships before writing any query.
6. Create `queries.sql` for your queries and fill in `analysis_report.md` with your results.

---

## 💻 What You Need to Do

### Entity-Relationship Diagram

- [ ] Model the three tables (`students`, `courses`, `enrollments`) in [diagram.4geeks.com](https://diagram.4geeks.com), including primary keys, foreign keys, and relationship types (1:1, 1:n, n:m)
- [ ] Export or screenshot the diagram and include it in the repository as `diagram.png`

### Queries — INNER JOIN

- [ ] List every enrollment showing the student's full name, the course title, and their completion percentage
- [ ] Show the name and email of students who have passed at least one course, along with the title of the course they passed
- [ ] Calculate the average completion percentage per instructor, ordered from highest to lowest

### Queries — LEFT JOIN (detecting missing data)

- [ ] Find all students who have **no enrollments** — they registered on the platform but never signed up for a course
- [ ] Find all courses that have **no enrollments** — they exist in the catalog but no one has signed up

### Queries — Aggregation across tables

- [ ] Count how many courses each student is enrolled in; show only students enrolled in **more than one course**
- [ ] Calculate total revenue per category using the course price from the `courses` table (`monthly_fee`), not the historical payment in `enrollments`
- [ ] Show each instructor alongside the number of students currently enrolled in their courses

### Queries — Data integrity

- [ ] Check for enrollments where the `student_id` does not match any existing student (orphaned records)
- [ ] Check for enrollments where the `course_id` does not match any existing course (orphaned records)

### Analysis Report

- [ ] Complete the `analysis_report.md` file, filling in the result of each query in the corresponding section

⚠️ **IMPORTANT:** Every query must use at least one JOIN. Do not use subqueries — all results must be obtained by joining tables directly. Do not use AI tools to generate your SQL queries.

---

## ✅ What We Will Evaluate

- [ ] The ER diagram is present as `diagram.png` and correctly represents the three tables, their keys, and relationship types
- [ ] All 10 queries are present in `queries.sql` and execute without errors in Supabase
- [ ] INNER JOIN queries return only rows where the match exists in both tables
- [ ] LEFT JOIN queries correctly surface rows with no match on the right side
- [ ] Foreign key naming follows the `table_name_id` convention in the diagram
- [ ] GROUP BY + HAVING is used correctly to filter aggregated results
- [ ] `analysis_report.md` has every section filled in with actual query results

> Note: Cascade delete behavior is covered in theory today but is not required in the queries.

---

## 📦 How to Submit

1. Push `queries.sql`, `analysis_report.md`, and `diagram.png` to a GitHub repository.
2. Share the repository link with your instructor following their instructions.
3. Make sure all three files are at the root of the repository and that the repo is public.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/sql-multi-table-project/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
