# 📡 Referencia de llamadas API para estudiantes (BreatheCode)

_Estas notas también están en [inglés](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/openclaw-integration/STUDENT_API_CALLS_REFERENCE.md)._

Este documento resume los endpoints orientados a estudiantes de **4Geeks Academy**: método, ruta, parámetros y forma de las respuestas. No incluye ejemplos de código ni cuerpos de ejemplo; para esquemas detallados, consulta la documentación OpenAPI enlazada al final.

> 💡 **Empieza por aquí**
> Si vas a automatizar o integrar algo, lee primero **Autenticación** y **Parámetros esenciales previos**. Te ahorrará errores 401 y filtros vacíos.

---

## 📑 Índice rápido

Usa búsqueda en el archivo (**Ctrl+F** / **Cmd+F**) con la palabra clave de la columna izquierda si quieres saltar rápido.

| Sección                  | De qué va                          |
| ------------------------ | ---------------------------------- |
| 🔐 Autenticación         | Token y rutas públicas             |
| 🌐 Base URL              | Dónde vive la API                  |
| 🎯 Parámetros esenciales | `academy_id`, `cohort_id`, slug    |
| 🎓 Admissions            | Tú, cohortes, syllabus             |
| ✅ Assignments           | Tareas y entregas                  |
| 🏆 Certificates          | Certificados                       |
| 📊 Activity              | Tu actividad y la del cohorte      |
| 📚 Registry              | Lecciones, ejercicios, tecnologías |
| 📅 Events                | Eventos                            |
| 📋 Enumeraciones         | Estados y tipos                    |
| 📖 Glosario mini         | Endpoint, query, slug, asset       |

---

## 🔐 Autenticación

La mayoría de los endpoints exigen un token en la cabecera **Authorization**, con el prefijo literal **Token** seguido de un espacio y el valor del token.

El token se obtiene mediante inicio de sesión en **POST** `/v1/auth/login` (público).

Los endpoints catalogados como públicos no requieren token.

> 🚨 **Seguridad**
> No compartas tu token en repos públicos, capturas de pantalla ni chats. Trátalo como una contraseña: variables de entorno o gestores secretos, nunca hardcodeado en el repositorio.

---

## 🌐 Base URL

En producción la API suele servirse desde **https://breathecode.herokuapp.com**. En otros entornos la base puede variar.

> 📝 **Entornos**
> Si tu bootcamp usa otra instancia, confirma la URL base con tu instructor o con el equipo técnico antes de desplegar integraciones.

---

## 🎯 Parámetros esenciales previos

Antes de filtrar por academia o cohorte conviene resolver:

- **academy_id** — Identificador numérico de la academia del estudiante. Suele obtenerse del primer elemento de **profile_academy** en la respuesta de usuario actual.
- **cohort_id** y **cohort.slug** — Identificador numérico y slug textual del cohorte. El cohorte activo suele ser el que tiene **educational_status** igual a **ACTIVE** en la lista de cohortes del estudiante.

> 💡 **Atajo mental**
> Piensa en **academy_id** como “¿en qué campus?” y en **cohort_id** / **slug** como “¿en qué cohorte curso?” Muchas listas se filtran mejor con uno u otro según el endpoint.

---

## 🎓 Admissions — usuario y cohortes

### 👤 Usuario actual

- **GET** `/v1/admissions/user/me`
- **Parámetros de ruta o query:** ninguno obligatorio.
- **Respuesta:** objeto de usuario con identificador, email, nombre, y relaciones de perfil; incluye **profile_academy** con academias vinculadas (cada una con **academy** con **id**, **name**, **slug**, etc.).

### 📋 Mis cohortes

- **GET** `/v1/admissions/academy/cohort/me`
- **Query opcional:** **academy** (id de academia); **educational_status** (por ejemplo **ACTIVE**, **GRADUATED**, **SUSPENDED**, **DROPPED**).
- **Respuesta:** arreglo de inscripciones a cohorte; cada ítem incluye objeto **cohort** (**id**, **name**, **slug**, **schedule**, etc.), **role**, **educational_status**, **created_at**.

### 📖 Syllabus público

- **GET** `/v1/admissions/public/syllabus`
- **Autenticación:** no requerida.
- **Respuesta:** syllabi públicos.

---

## ✅ Assignments — tareas y entregas

> 📝 **Flujo típico**
> Consultar tareas → actualizar URLs si aplica → **entregar** con el endpoint **deliver** cuando esté lista para revisión. El orden exacto puede depender de las reglas de tu syllabus.

### 📥 Listar mis tareas

- **GET** `/v1/assignment/user/me/task`
- **Query útil:** **task_status** (**PENDING**, **DONE**, **APPROVED**, **REJECTED**); **task_type** (**PROJECT**, **EXERCISE**, **LESSON**); **cohort** (id de cohorte); **limit** y **offset** para paginación.
- **Respuesta:** lista de tareas asignadas con estado, tipo, fechas y metadatos de revisión.

### 🔍 Detalle de una tarea

- **GET** `/v1/assignment/task/{task_id}`
- **Parámetro de ruta:** **task_id** (numérico).
- **Respuesta:** detalle completo de la tarea (descripción, puntuación, feedback, etc.).

### ✏️ Actualizar una tarea

- **PUT** `/v1/assignment/task/{task_id}`
- **Parámetro de ruta:** **task_id**.
- **Cuerpo:** típicamente URLs de entrega, por ejemplo repositorio (**github_url**) y despliegue (**live_url**); el esquema exacto figura en OpenAPI.

### 🚀 Entregar una tarea

- **POST** `/v1/assignment/task/{task_id}/deliver`
- **Parámetro de ruta:** **task_id**.
- **Respuesta:** según contrato del endpoint en Swagger (marcar tarea como entregada para revisión).

---

## 🏆 Certificates

### 📜 Listar certificados

- **GET** `/v1/certificate/`
- **Query opcional:** **cohort** (id de cohorte).
- **Respuesta:** colección de certificados del usuario (filtrable por cohorte).

### 🔗 Certificado por token

- **GET** `/v1/certificate/{token}`
- **Parámetro de ruta:** **token** único del certificado.
- **Autenticación:** pública (no token).
- **Respuesta:** datos del certificado identificado por ese token.

> 🚧 **Enlaces públicos**
> El token en la URL identifica el certificado. Quien tenga el enlace puede verlo sin iniciar sesión: comparte solo por canales seguros.

---

## 📊 Activity

### 🙋 Mi actividad

- **GET** `/v1/activity/me`
- **Query opcional:** **cohort** (id o slug según uso en tu instancia); **date_start** y **date_end** en formato fecha (por ejemplo **YYYY-MM-DD**).
- **Respuesta:** actividad de aprendizaje del usuario (tiempo, ejercicios, etc., según modelo expuesto por la API).

### 👥 Actividad del cohorte

- **GET** `/v1/activity/cohort/{cohort_id}`
- **Parámetro de ruta:** **cohort_id** puede ser id numérico o slug del cohorte.
- **Respuesta:** actividad agregada o por miembros del cohorte (comparación de progreso).

---

## 📚 Registry — contenido educativo

### 🔎 Buscar assets (lecciones, ejercicios, proyectos)

- **GET** `/v1/registry/asset`
- **Query útil:** **asset_type** (**LESSON**, **EXERCISE**, **PROJECT**); **technologies** (slug de tecnología, por ejemplo python, react, javascript); **difficulty** (**BEGINNER**, **EASY**, **INTERMEDIATE**, **HARD**); **like** (texto de búsqueda); **limit**.
- **Respuesta:** lista de assets que cumplen filtros.

> 💡 **Explorar el catálogo**
> Combina **asset_type** + **technologies** para practicar justo el stack que estás viendo en clase, o sube la dificultad poco a poco.

### 📄 Detalle de asset

- **GET** `/v1/registry/asset/{asset_slug}`
- **Parámetro de ruta:** **asset_slug** (identificador legible del recurso).
- **Respuesta:** asset completo (readme, tecnologías, dificultad, repositorio, etc.).

### ✨ Mis assets

- **GET** `/v1/registry/asset/me`
- **Respuesta:** assets creados o modificados por el usuario.

### 🛠️ Tecnologías

- **GET** `/v1/registry/technology`
- **Query opcional:** **like** (búsqueda por nombre); **limit**.
- **Respuesta:** catálogo de tecnologías disponibles en la plataforma.

---

## 📅 Events

### 🎟️ Eventos

- **GET** `/v1/events/all`
- **Query opcional:** **academy** (id de academia); **upcoming** (booleano, por ejemplo solo futuros); **limit**.
- **Respuesta:** lista de eventos según filtros.

---

## 📋 Enumeraciones y convenciones útiles

### 🎓 Estados educativos (**educational_status**)

- **ACTIVE** — Cursando.
- **GRADUATED** — Graduado.
- **SUSPENDED** — Suspendido.
- **DROPPED** — Baja / abandonado.

### ✅ Estados de tarea (**task_status**)

- **PENDING** — Pendiente.
- **DONE** — Completada por el estudiante.
- **APPROVED** — Aprobada en revisión.
- **REJECTED** — Rechazada; requiere correcciones.

### 🧩 Tipos de tarea (**task_type**)

- **LESSON** — Lección.
- **EXERCISE** — Ejercicio.
- **PROJECT** — Proyecto.
- **QUIZ** — Cuestionario.

### 📄 Paginación

Muchos listados admiten **limit** (cantidad de resultados) y **offset** (desplazamiento desde el inicio).

### 🔒 Filtrado por contexto

Los datos suelen limitarse automáticamente a cohortes en los que el usuario está inscrito, según políticas del backend.

### ⏱️ Rate limiting y caché

Conviene cachear respuestas estables y evitar ráfagas de peticiones idénticas; los límites exactos dependen de la instancia.

> ⚠️ **No martilles la API**
> Si tu script hace cientos de llamadas iguales por segundo, puedes chocar con límites o degradar el servicio para todos. Reutiliza datos en memoria o en disco cuando tenga sentido.

---

## 📖 Glosario mini

| Término      | Significado rápido                                                                |
| ------------ | --------------------------------------------------------------------------------- |
| **Endpoint** | Ruta concreta de la API (método + URL).                                           |
| **Query**    | Parámetros después de `?` en la URL.                                              |
| **Slug**     | Identificador legible en minúsculas y guiones (ej. nombre del cohorte en la URL). |
| **Asset**    | Pieza de contenido: lección, ejercicio o proyecto en el registro.                 |

---

### 🙌 ¿Siguiente paso?

Abre **Swagger**, elige un endpoint que ya uses en la plataforma (por ejemplo “mis tareas”) y compara los campos de la respuesta con lo que ves en el LMS. Así conectas la teoría de esta guía con la práctica.
