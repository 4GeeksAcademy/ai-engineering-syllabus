-- ============================================================
-- EduTrack v2 — Normalized database
-- ============================================================
-- This is the standardised version of the EduTrack schema.
-- The `enrollments` table no longer contains the instructor’s name
-- directly: this information is now stored in `courses`.
--
-- Instructions: 
-- 1. Open your project’s SQL Editor in Supabase
-- 2. Paste the entire contents of this file and run it
-- 3. Check with:
--      SELECT * FROM students LIMIT 5;
--      SELECT * FROM courses LIMIT 5;
--      SELECT * FROM enrollments LIMIT 5;
-- ============================================================


-- ------------------------------------------------------------
-- ESQUEMA
-- ------------------------------------------------------------
DROP TABLE IF EXISTS enrollments;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;

CREATE TABLE students (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(150) NOT NULL UNIQUE,
    signup_date DATE         NOT NULL
);

CREATE TABLE courses (
    id              SERIAL PRIMARY KEY,
    title           VARCHAR(150) NOT NULL,
    category        VARCHAR(50)  NOT NULL,
    instructor_name VARCHAR(100),           -- puede ser NULL (pendiente de asignación)
    monthly_fee     DECIMAL(6,2) NOT NULL
);

CREATE TABLE enrollments (
    id                    SERIAL PRIMARY KEY,
    student_id            INTEGER      NOT NULL REFERENCES students(id),
    course_id             INTEGER      NOT NULL REFERENCES courses(id),
    enrollment_date       DATE         NOT NULL,
    completion_percentage INTEGER      NOT NULL DEFAULT 0,
    passed                BOOLEAN      NOT NULL DEFAULT FALSE,
    monthly_fee_paid      DECIMAL(6,2) NOT NULL
);


-- ------------------------------------------------------------
-- DATOS: students
-- (Sin cuentas de prueba importadas: solo estudiantes @student.edutrack.com)
-- ------------------------------------------------------------
INSERT INTO students (id, name, email, signup_date) VALUES
(1,  'Emily Watson',      'emily.watson@student.edutrack.com',    '2024-01-15'),
(2,  'Klaus Weber',       'klaus.weber@student.edutrack.com',     '2024-01-20'),
(3,  'Lucia Fernandes',   'lucia.fernandes@student.edutrack.com', '2024-02-03'),
(4,  'Marco Rossi',       'marco.rossi@student.edutrack.com',     '2024-02-10'),
(5,  'Yuki Nakamura',     'yuki.nakamura@student.edutrack.com',   '2024-03-05'),
(6,  'Pierre Dubois',     'pierre.dubois@student.edutrack.com',   '2024-03-18'),
(7,  'Priya Sharma',      'priya.sharma@student.edutrack.com',    '2024-04-01'),
(8,  'Giulia Romano',     'giulia.romano@student.edutrack.com',   '2024-05-07');
-- Giulia Romano (id=8) no tiene inscripciones — útil para LEFT JOIN

-- ------------------------------------------------------------
-- DATOS: courses
-- ------------------------------------------------------------
INSERT INTO courses (id, title, category, instructor_name, monthly_fee) VALUES
(1, 'Intro to Python',        'Programming', 'Marta López',  49.99),
(2, 'Web Design Basics',      'Design',      'Carlos Vega',  39.99),
(3, 'Data Analysis with SQL', 'Data',        'Marta López',  59.99),
(4, 'Digital Marketing 101',  'Marketing',   'Lucia Prades', 29.99),
(5, 'Advanced Python',        'Programming', 'Carlos Vega',  69.99),
(6, 'UI/UX Fundamentals',     'Design',      'Pending assignment', 44.99),
(7, 'Email Campaigns',        'Marketing',   'Lucia Prades', 19.99);
-- Email Campaigns (id=7) no tiene inscripciones — útil para LEFT JOIN

-- ------------------------------------------------------------
-- DATOS: enrollments
-- (Datos ya limpios: sin inscripciones de cuentas de prueba, sin instructor NULL en enrollments)
-- ------------------------------------------------------------
INSERT INTO enrollments (id, student_id, course_id, enrollment_date, completion_percentage, passed, monthly_fee_paid) VALUES
(1,  1, 1, '2024-03-10', 85, TRUE,  49.99),
(2,  1, 2, '2024-04-15', 60, FALSE, 39.99),
(3,  2, 1, '2024-03-12', 92, TRUE,  49.99),
(4,  2, 3, '2024-05-01', 78, TRUE,  59.99),
(5,  3, 2, '2024-06-20',  5, FALSE, 39.99),
(6,  3, 4, '2024-07-01',  3, FALSE, 29.99),
(7,  4, 5, '2024-02-14', 95, TRUE,  69.99),
(8,  4, 1, '2024-08-09', 88, TRUE,  49.99),
(9,  5, 3, '2024-09-03', 45, FALSE, 59.99),
(10, 5, 6, '2024-10-11',  0, FALSE, 44.99),
(11, 6, 6, '2024-11-05',  0, FALSE, 44.99),
(12, 7, 4, '2024-12-01', 70, TRUE,  29.99),
(13, 7, 1, '2025-01-10', 55, FALSE, 49.99),
(14, 6, 3, '2025-02-20', 20, FALSE, 59.99),
(15, 1, 5, '2025-03-05', 40, FALSE, 69.99),
(16, 3, 5, '2025-04-01',  0, FALSE, 69.99);
-- student_id 8 (Giulia Romano) no tiene ninguna inscripción — dejado así intencionalmente
