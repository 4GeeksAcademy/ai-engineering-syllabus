# EduTrack v2 — Analysis Report (REFERENCE SOLUTION)

---

## Q1 — All enrollments (INNER JOIN)

Result: 16 enrollments

| Student         | Course                 | Completion |
| --------------- | ---------------------- | ---------- |
| Emily Watson    | Intro to Python        | 85%        |
| Emily Watson    | Web Design Basics      | 60%        |
| Emily Watson    | Advanced Python        | 40%        |
| Klaus Weber     | Intro to Python        | 92%        |
| Klaus Weber     | Data Analysis with SQL | 78%        |
| Priya Sharma    | Digital Marketing 101  | 70%        |
| Priya Sharma    | Intro to Python        | 55%        |
| Lucia Fernandes | Web Design Basics      | 5%         |
| Lucia Fernandes | Digital Marketing 101  | 3%         |
| Lucia Fernandes | Advanced Python        | 0%         |
| Pierre Dubois   | UI/UX Fundamentals     | 0%         |
| Pierre Dubois   | Data Analysis with SQL | 20%        |
| Marco Rossi     | Advanced Python        | 95%        |
| Marco Rossi     | Intro to Python        | 88%        |
| Yuki Nakamura   | Data Analysis with SQL | 45%        |
| Yuki Nakamura   | UI/UX Fundamentals     | 0%         |

---

## Q2 — Students who passed at least one course

Result: 6 rows

| Name         | Email                             | Passed course          |
| ------------ | --------------------------------- | ---------------------- |
| Emily Watson | emily.watson@student.edutrack.com | Intro to Python        |
| Klaus Weber  | klaus.weber@student.edutrack.com  | Intro to Python        |
| Klaus Weber  | klaus.weber@student.edutrack.com  | Data Analysis with SQL |
| Marco Rossi  | marco.rossi@student.edutrack.com  | Advanced Python        |
| Marco Rossi  | marco.rossi@student.edutrack.com  | Intro to Python        |
| Priya Sharma | priya.sharma@student.edutrack.com | Digital Marketing 101  |

---

## Q3 — Average completion by instructor

Result: 4 rows

| Instructor         | Average completion |
| ------------------ | ------------------ |
| Marta López        | 66.1%              |
| Carlos Vega        | 40.0%              |
| Lucia Prades       | 36.5%              |
| Pending assignment | 0.0%               |

---

## Q4 — Students with no enrollments (LEFT JOIN)

Result: 1 student

| Name          | Email                              |
| ------------- | ---------------------------------- |
| Giulia Romano | giulia.romano@student.edutrack.com |

---

## Q5 — Courses with no enrollments (LEFT JOIN)

Result: 1 course

| Course title    | Instructor   |
| --------------- | ------------ |
| Email Campaigns | Lucia Prades |

---

## Q6 — Students enrolled in more than one course

Result: 7 students

| Student         | Number of courses |
| --------------- | ----------------- |
| Emily Watson    | 3                 |
| Lucia Fernandes | 3                 |
| Klaus Weber     | 2                 |
| Priya Sharma    | 2                 |
| Pierre Dubois   | 2                 |
| Marco Rossi     | 2                 |
| Yuki Nakamura   | 2                 |

---

## Q7 — Total revenue by category (course price)

Result (highest to lowest):

| Category    | Total revenue |
| ----------- | ------------- |
| Programming | $409.93       |
| Data        | $179.97       |
| Design      | $169.96       |
| Marketing   | $59.98        |

---

## Q8 — Students per instructor

Result:

| Instructor         | Students |
| ------------------ | -------- |
| Marta López        | 7        |
| Carlos Vega        | 5        |
| Pending assignment | 2        |
| Lucia Prades       | 2        |

---

## Q9 — Enrollments with orphaned `student_id`

Result: 0 rows

> Every `student_id` in `enrollments` matches a row in `students`. Referential integrity holds.

---

## Q10 — Enrollments with orphaned `course_id`

Result: 0 rows

> Every `course_id` in `enrollments` matches a row in `courses`. Referential integrity holds.
