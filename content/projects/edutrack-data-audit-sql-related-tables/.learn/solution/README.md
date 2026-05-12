# EduTrack Data Audit — Related Tables (Reference Solution)

## Purpose

This folder is the **reference solution** for the normalized EduTrack schema (`students`, `courses`, `enrollments`). Students load `edutrack_v2.sql` in Supabase, model relationships, then submit `queries.sql`, `analysis_report.md`, and `diagram.png`.

## Solution files

| File                                         | Role                                                                                                                                                                   |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`queries.sql`](./queries.sql)               | Ten queries (Q1–Q10): INNER JOIN, LEFT JOIN for gaps, aggregates with `GROUP BY` / `HAVING`, and orphan checks. Each query uses at least one join, with no subqueries. |
| [`analysis_report.md`](./analysis_report.md) | Expected result shapes and sample outputs after running the queries against the seeded dataset.                                                                        |

The ER diagram is a **student deliverable** and is not duplicated here.

## Query map (rubric alignment)

1. **Q1** — INNER JOIN: every enrollment with student name, course title, completion %.
2. **Q2** — INNER JOIN: students with `passed = true`, with course title.
3. **Q3** — INNER JOIN + aggregation: average `completion_percentage` per `instructor_name`, highest first.
4. **Q4** — LEFT JOIN: students with no matching enrollment (`e.id IS NULL`).
5. **Q5** — LEFT JOIN: courses with no matching enrollment.
6. **Q6** — INNER JOIN + `GROUP BY` + `HAVING`: students enrolled in more than one course.
7. **Q7** — Revenue by `category` using `SUM(c.monthly_fee)` joined through enrollments (current course price, not historical payment fields).
8. **Q8** — Enrollment rows per instructor (student-seat count via `COUNT(e.id)`).
9. **Q9** — Orphan `student_id`: `enrollments` LEFT JOIN `students` where `s.id IS NULL`.
10. **Q10** — Orphan `course_id`: `enrollments` LEFT JOIN `courses` where `c.id IS NULL`.

## Indicative pattern (LEFT JOIN anti-join)

```sql
SELECT s.name, s.email
FROM students s
LEFT JOIN enrollments e ON e.student_id = s.id
WHERE e.id IS NULL;
```

## Validation notes

- Run all statements in the Supabase SQL editor against the provided `edutrack_v2.sql` dump.
- Confirm row counts and representative rows match your `analysis_report.md` sections.
- Ensure the student diagram names foreign keys using the `table_name_id` convention described in the project README.
