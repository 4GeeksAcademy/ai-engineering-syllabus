# Auditoría de Datos en EduTrack

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/sql-single-table-project/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de comenzar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto.

<!-- endhide -->

---

## 🎯 Tu reto

EduTrack es una plataforma de aprendizaje online en crecimiento que lleva dos años en operación. Su equipo ha estado registrando inscripciones manualmente a través de distintos canales — un formulario web, un equipo de ventas y una integración con terceros — y la calidad de los datos nunca ha sido revisada formalmente.

Te han contratado como analista de datos externo. La responsable de operaciones de la plataforma te ha enviado el siguiente mensaje:

> **De:** Responsable de Operaciones, EduTrack  
> **Para:** Analista de datos (contratado externo)  
> **Asunto:** Auditoría de base de datos — Q3
>
> Hola,
>
> Necesitamos hacer una revisión completa de nuestra tabla `enrollments` antes de comenzar el ciclo de reportes del Q3. Concretamente:
>
> - Sospechamos que hay estudiantes con un progreso muy bajo — nos gustaría identificarlos.
> - Algunos registros fueron importados desde un sistema antiguo e incluyen cuentas de prueba (`@test.com`) cuyas inscripciones deben eliminarse.
> - Un lote de inscripciones de una integración con un partner llegó sin el campo del instructor — esos registros deben corregirse.
> - También falta al menos una inscripción que fue confirmada por correo pero nunca fue registrada — por favor añádela.
> - Necesitamos cifras agregadas por categoría de curso: ingresos totales cobrados, promedio de completado y qué categorías tienen peor rendimiento.
>
> Por favor, documenta todo en un informe de análisis escrito — no solo las consultas, sino los resultados reales. Necesitamos poder compartirlo con el equipo sin que tengan que ejecutar SQL.
>
> Gracias

Recibirás un archivo `.sql` que crea y puebla la base de datos. Impórtalo en Supabase y empieza el análisis.

La tabla con la que trabajarás es `enrollments`, que registra cada combinación estudiante-curso junto con datos de progreso y pago. Las tablas `students` y `courses` también están presentes en el esquema — **no las modifiques** en esta fase. Todo tu análisis vive dentro de `enrollments`.

Este tipo de auditoría aparece constantemente en startups. Cuanto más limpia esté la base de datos antes del reporting, más fiables serán los resultados.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no parte de una plantilla de código: creas un repositorio vacío y dentro un archivo SQL con tus consultas y un informe en Markdown con tus hallazgos.

1. Descarga el archivo [edutrack.sql](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/refs/heads/main/content/projects/edutrack-data-audit-sql/edutrack.sql) desde este enlace.
2. Inicia sesión en [Supabase](https://supabase.com) y crea un nuevo proyecto.
3. Ve al **SQL Editor** y ejecuta el contenido completo de `edutrack.sql` para crear y poblar la base de datos.
4. Verifica que la importación fue exitosa ejecutando `SELECT * FROM enrollments LIMIT 5;`.
5. Crea un repositorio vacío en GitHub y agrega en su raíz dos archivos: `queries.sql` (tus consultas) y `analysis_report.md` (tus resultados). Supabase no guarda archivos: úsalo solo para ejecutar y probar las consultas.
6. Cada vez que una consulta funcione en Supabase, cópiala a `queries.sql` con un comentario que indique su número (ej. `-- Q6: inscripción faltante`.) y anota el resultado en `analysis_report.md`.

> 💡 Consejo: Antes de ejecutar cualquier UPDATE o DELETE, ejecuta siempre un SELECT con la misma condición WHERE para confirmar que estás apuntando a las filas correctas.

---

## 💻 Qué debes hacer

### Configuración de la base de datos

- [ ] Importar `edutrack.sql` en un proyecto de Supabase correctamente
- [ ] Verificar que las tablas `enrollments`, `students` y `courses` existen y contienen datos
- [ ] Ejecuta las consultas **en orden (Q1 → Q12)**. Las agregaciones (Q9–Q12) deben calcularse **después** de las correcciones (Q6–Q8), porque sus resultados cambian si se agregan o borran registros.

### Consultas — Lectura y filtrado

- [ ] **Q1.** Listar todas las inscripciones del curso `'Intro to Python'`, mostrando nombre del estudiante, email y porcentaje de completado
- [ ] **Q2.** Obtener todas las inscripciones donde `completion_percentage` sea menor que 10 — estos son posibles abandonos
- [ ] **Q3.** Encontrar todas las inscripciones donde el campo instructor sea `NULL`
- [ ] **Q4.** Listar los 5 estudiantes con mayor `completion_percentage` que todavía **no han aprobado** (`passed = false`)
- [ ] **Q5.** Mostrar todas las inscripciones con `enrollment_date` desde el `'2024-07-01'`, ordenadas por `enrollment_date` descendente

### Consultas — Corrección de datos

- [ ] **Q6.** **INSERT** del registro de inscripción faltante indicado en el brief (el nombre del estudiante, email, curso, fecha y valores iniciales están especificados en los comentarios del archivo `edutrack.sql`)
- [ ] **Q7.** **UPDATE** de todas las inscripciones donde `instructor` sea `NULL` — asignar el valor por defecto `'Pending assignment'`
- [ ] **Q8.** **DELETE** de todas las inscripciones ligadas a las cuentas de prueba importadas (`@test.com`) — confirmar las filas afectadas con un SELECT previo

### Consultas — Agregación e informe

- [ ] **Q9.** Contar el número de inscripciones agrupado por `category`
- [ ] **Q10.** Calcular el promedio de `completion_percentage` agrupado por `course_title`, ordenado de menor a mayor
- [ ] **Q11.** Mostrar únicamente los cursos con **más de 3 inscripciones** (usar `HAVING`)
- [ ] **Q12.** Calcular los ingresos totales (`SUM` de `monthly_fee_paid`) agrupados por `category`, ordenados de mayor a menor

### Informe de análisis

- [ ] Escribir en `analysis_report.md` una sección por cada consulta (Q1 a Q12) con el resultado real que devolvió

El informe sigue una estructura fija — una sección por consulta. Tu tarea es escribir los números y listas que devolvió tu SQL. Ejemplo del formato esperado:

```markdown
## Q1 - Inscripciones en 'Intro to Python'

Resultado: 10

## Q9 - Inscripciones por categoría

Resultado:

- Programming: 45
- Design: 23
- Data: 18
- Marketing: 12
```

⚠️ **IMPORTANTE:** No utilices herramientas de IA para generar tus consultas SQL. Escribe cada una tú mismo. El objetivo es desarrollar el músculo de lectura y construcción de SQL — eso solo ocurre con tus propias manos.

---

## ✅ Qué vamos a evaluar

- [ ] Las 12 consultas están presentes en `queries.sql` y se ejecutan sin errores en Supabase
- [ ] Las consultas SELECT devuelven las filas y columnas correctas según las condiciones especificadas
- [ ] El INSERT añade el registro correcto con todos los campos requeridos
- [ ] El UPDATE afecta únicamente a las filas con instructor `NULL` y asigna el valor por defecto correcto
- [ ] El DELETE elimina únicamente los registros con `@test.com` y ningún otro
- [ ] Las consultas con GROUP BY producen las agregaciones correctas (count, average, sum)
- [ ] HAVING se utiliza correctamente para filtrar resultados agregados
- [ ] `analysis_report.md` tiene una sección para cada consulta con el resultado real completado (no en blanco)

> Nota: La estructura o contenido de las tablas `students` y `courses` no se evalúa en este proyecto — solo se evaluará el trabajo realizado sobre `enrollments`.

---

## 📦 Cómo entregar

1. Asegúrate de que la versión final de `queries.sql` y `analysis_report.md` esté guardada (commit y push) en tu repositorio.
2. Asegúrate de que ambos archivos estén en la raíz del repositorio y que el repo sea público.
3. Entrega el enlace en esta vista.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
