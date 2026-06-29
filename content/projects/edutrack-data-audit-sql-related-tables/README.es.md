# Auditoría de Datos en EduTrack — Tablas Relacionadas

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/sql-multi-table-project/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are also available in [English](./README.md)._

**Antes de comenzar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto.

<!-- endhide -->

---

## 🎯 Tu reto

El equipo de ingeniería de EduTrack ha normalizado la base de datos. Lo que antes era una única tabla plana `enrollments` es ahora un esquema relacional completo: estudiantes, cursos e inscripciones son entidades separadas, cada una con su propia tabla y vinculadas por claves foráneas.

La responsable de operaciones ha vuelto con un nuevo conjunto de preguntas — pero esta vez, ninguna puede responderse mirando una sola tabla.

> **De:** Responsable de Operaciones, EduTrack  
> **Para:** Analista de datos (contratado externo)  
> **Asunto:** Re: Auditoría de base de datos — Q3 (esquema normalizado)
>
> Hola de nuevo,
>
> El equipo de desarrollo acaba de terminar la migración al nuevo esquema. Adjuntamos el archivo `.sql` actualizado.
>
> Ahora que los datos están bien estructurados, nos gustaría retomar algunas preguntas de la vez anterior — y añadir algunas nuevas que antes no eran posibles:
>
> - ¿Qué estudiantes están inscritos en más de un curso? Queremos sus nombres y cuántos cursos están cursando.
> - ¿Qué cursos no tienen ninguna inscripción? Puede que los archivemos.
> - ¿Cuál es el porcentaje de completado medio por instructor?
> - ¿Qué estudiantes han aprobado al menos un curso? Muestra su nombre y el título del curso que aprobaron.
> - ¿Hay inscripciones vinculadas a un estudiante o curso que ya no existe en la base de datos? (Revisión de integridad de datos.)
> - ¿Qué categoría genera más ingresos teniendo en cuenta el precio actual del curso?
>
> Como la vez anterior, por favor rellena el `analysis_report.md` con tus resultados.
>
> Gracias

Antes de escribir ninguna consulta, necesitas entender cómo se relacionan las tres tablas entre sí. Empieza leyendo el esquema con atención y dibuja el diagrama entidad-relación en [diagram.4geeks.com](https://diagram.4geeks.com). Ese diagrama es tu primer entregable.

Las respuestas están en los datos — solo necesitas saber qué tablas unir.

---

## 🌱 Cómo iniciar el proyecto

1. Descarga el archivo [edutrack_v2.sql](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/refs/heads/main/content/projects/edutrack-data-audit-sql-related-tables/edutrack_v2.sql) desde la plataforma.
2. Inicia sesión en [Supabase](https://supabase.com) y crea un nuevo proyecto (o reutiliza el del proyecto anterior).
3. Ve al **SQL Editor** y ejecuta el contenido completo de `edutrack_v2.sql` para crear y poblar el esquema normalizado.
4. Verifica la importación ejecutando `SELECT * FROM enrollments LIMIT 5;`, `SELECT * FROM students LIMIT 5;` y `SELECT * FROM courses LIMIT 5;`.
5. Ve a [diagram.4geeks.com](https://diagram.4geeks.com) y modela las tres tablas y sus relaciones antes de escribir ninguna consulta.
6. Crea `queries.sql` para tus consultas y rellena `analysis_report.md` con tus resultados.

---

## 💻 Qué debes hacer

### Diagrama Entidad-Relación

- [ ] Modelar las tres tablas (`students`, `courses`, `enrollments`) en [diagram.4geeks.com](https://diagram.4geeks.com), incluyendo claves primarias, claves foráneas y tipos de relación (1:1, 1:n, n:m)
- [ ] Exportar o hacer una captura del diagrama e incluirla en el repositorio como `diagram.png`

### Consultas — INNER JOIN

- [ ] Listar todas las inscripciones mostrando el nombre completo del estudiante, el título del curso y su porcentaje de completado
- [ ] Mostrar el nombre y email de los estudiantes que han aprobado al menos un curso, junto con el título del curso que aprobaron
- [ ] Calcular el porcentaje de completado medio por instructor, ordenado de mayor a menor

### Consultas — LEFT JOIN (detección de datos faltantes)

- [ ] Encontrar todos los estudiantes que **no tienen ninguna inscripción** — se registraron en la plataforma pero nunca se apuntaron a un curso
- [ ] Encontrar todos los cursos que **no tienen ninguna inscripción** — existen en el catálogo pero nadie se ha apuntado

### Consultas — Agregación entre tablas

- [ ] Contar cuántos cursos tiene inscrito cada estudiante; mostrar solo los estudiantes inscritos en **más de un curso**
- [ ] Calcular los ingresos totales por categoría usando el precio del curso de la tabla `courses` (`monthly_fee`), no el pago histórico de `enrollments`
- [ ] Mostrar cada instructor junto con el número de estudiantes inscritos actualmente en sus cursos

### Consultas — Integridad de datos

- [ ] Comprobar si hay inscripciones cuyo `student_id` no corresponde a ningún estudiante existente (registros huérfanos)
- [ ] Comprobar si hay inscripciones cuyo `course_id` no corresponde a ningún curso existente (registros huérfanos)

### Informe de análisis

- [ ] Completar el archivo `analysis_report.md`, rellenando el resultado de cada consulta en la sección correspondiente

⚠️ **IMPORTANTE:** Cada consulta debe usar al menos un JOIN. No uses subconsultas — todos los resultados deben obtenerse uniendo tablas directamente. No uses herramientas de IA para generar tus consultas SQL.

---

## ✅ Qué vamos a evaluar

- [ ] El diagrama E/R está presente como `diagram.png` y representa correctamente las tres tablas, sus claves y los tipos de relación
- [ ] Las 10 consultas están presentes en `queries.sql` y se ejecutan sin errores en Supabase
- [ ] Las consultas INNER JOIN devuelven únicamente filas donde existe coincidencia en ambas tablas
- [ ] Las consultas LEFT JOIN muestran correctamente las filas sin coincidencia en la tabla derecha
- [ ] El nombrado de claves foráneas sigue la convención `nombre_tabla_id` en el diagrama
- [ ] GROUP BY + HAVING se usa correctamente para filtrar resultados agregados
- [ ] `analysis_report.md` tiene todas las secciones rellenadas con los resultados reales de las consultas

> Nota: El comportamiento del borrado en cascada se cubre en la teoría de hoy pero no es requerido en las consultas.

---

## 📦 Cómo entregar

1. Sube `queries.sql`, `analysis_report.md` y `diagram.png` a un repositorio de GitHub.
2. Comparte el enlace del repositorio con tu instructor siguiendo sus instrucciones.
3. Asegúrate de que los tres archivos estén en la raíz del repositorio y que el repo sea público.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
