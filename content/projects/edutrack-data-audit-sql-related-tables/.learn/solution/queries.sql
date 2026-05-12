-- ============================================================
-- EduTrack v2 — Multi-table queries — REFERENCE SOLUTION
-- ============================================================


-- ------------------------------------------------------------
-- Q1 — INNER JOIN: all enrollments with student and course
-- ------------------------------------------------------------
SELECT s.name, c.title, e.completion_percentage
FROM enrollments e
JOIN students s ON s.id = e.student_id
JOIN courses c  ON c.id = e.course_id
ORDER BY s.name;


-- ------------------------------------------------------------
-- Q2 — INNER JOIN: students who passed at least one course
-- ------------------------------------------------------------
SELECT s.name, s.email, c.title
FROM enrollments e
JOIN students s ON s.id = e.student_id
JOIN courses c  ON c.id = e.course_id
WHERE e.passed = TRUE;


-- ------------------------------------------------------------
-- Q3 — INNER JOIN + GROUP BY: average completion by instructor
-- ------------------------------------------------------------
SELECT c.instructor_name, ROUND(AVG(e.completion_percentage), 1) AS avg_completion
FROM enrollments e
JOIN courses c ON c.id = e.course_id
GROUP BY c.instructor_name
ORDER BY avg_completion DESC;


-- ------------------------------------------------------------
-- Q4 — LEFT JOIN: students with no enrollments
-- ------------------------------------------------------------
SELECT s.name, s.email
FROM students s
LEFT JOIN enrollments e ON e.student_id = s.id
WHERE e.id IS NULL;


-- ------------------------------------------------------------
-- Q5 — LEFT JOIN: courses with no enrollments
-- ------------------------------------------------------------
SELECT c.title, c.instructor_name
FROM courses c
LEFT JOIN enrollments e ON e.course_id = c.id
WHERE e.id IS NULL;


-- ------------------------------------------------------------
-- Q6 — INNER JOIN + GROUP BY + HAVING: students in more than one course
-- ------------------------------------------------------------
SELECT s.name, COUNT(e.course_id) AS course_count
FROM enrollments e
JOIN students s ON s.id = e.student_id
GROUP BY s.name
HAVING COUNT(e.course_id) > 1
ORDER BY course_count DESC;


-- ------------------------------------------------------------
-- Q7 — INNER JOIN + GROUP BY: revenue by category (courses.monthly_fee)
-- ------------------------------------------------------------
SELECT c.category, ROUND(SUM(c.monthly_fee), 2) AS total_revenue
FROM enrollments e
JOIN courses c ON c.id = e.course_id
GROUP BY c.category
ORDER BY total_revenue DESC;


-- ------------------------------------------------------------
-- Q8 — INNER JOIN + GROUP BY: enrolled students per instructor
-- ------------------------------------------------------------
SELECT c.instructor_name, COUNT(e.id) AS student_count
FROM enrollments e
JOIN courses c ON c.id = e.course_id
GROUP BY c.instructor_name
ORDER BY student_count DESC;


-- ------------------------------------------------------------
-- Q9 — Integrity: enrollments with orphaned student_id
-- ------------------------------------------------------------
SELECT e.id, e.student_id
FROM enrollments e
LEFT JOIN students s ON s.id = e.student_id
WHERE s.id IS NULL;


-- ------------------------------------------------------------
-- Q10 — Integrity: enrollments with orphaned course_id
-- ------------------------------------------------------------
SELECT e.id, e.course_id
FROM enrollments e
LEFT JOIN courses c ON c.id = e.course_id
WHERE c.id IS NULL;
