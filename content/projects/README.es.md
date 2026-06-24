# Diseño del pipeline de datos de la compañía

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de comenzar**: Lee tu **[CONTEXT-empresa.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** antes de escribir cualquier cosa — define los datos específicos de tu empresa, los eventos de telemetría que has capturado y los KPIs que ya has calculado.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Has pasado las últimas semanas capturando eventos de telemetría, almacenándolos en base de datos y generando informes básicos con Pandas. Ahora tu tech lead quiere algo más: un pipeline de datos que sea robusto, auditable y que tu equipo pueda ejecutar con confianza en producción.

Tu CTO te ha enviado este brief a través del gestor de tareas del equipo:

> > **Brief técnico — Pipeline de datos (Diseño)**
> >
> > Antes de escribir una sola línea de código de orquestación, necesito que documentes el diseño del pipeline de datos de nuestra plataforma. El equipo de datos ha recibido una RFP interna del área de operaciones: quieren saber exactamente cómo fluyen los datos desde que se capturan en la aplicación hasta que llegan a los dashboards. También quieren garantías sobre idempotencia y auditabilidad antes de aprobar el paso a producción.
> >
> > Entregable: un documento de diseño en Markdown dentro del monorepo. Sin código de orquestación todavía — primero el diseño, luego la implementación.

### ¿Qué es un pipeline de datos robusto?

Un pipeline de datos no es simplemente un script que mueve información de un sitio a otro. Un pipeline de producción tiene etapas bien definidas, maneja fallos de forma predecible y puede ser auditado. Los tres atributos clave que distinguen un pipeline robusto de uno que "simplemente funciona" son:

- **Idempotencia**: ejecutar el pipeline dos veces sobre los mismos datos produce el mismo resultado, sin duplicados ni corrupción.
- **Observabilidad**: cada ejecución deja trazas suficientes para saber qué pasó, cuándo y por qué.
- **Recuperabilidad**: cuando el pipeline falla a mitad de camino, la siguiente ejecución sabe exactamente desde dónde retomar.

Estos tres atributos son los que tu documento de diseño debe demostrar que has pensado en profundidad.

---

## 🌱 Cómo Empezar

1. Haz un `git pull` en tu fork del monorepo para asegurarte de tener el estado más reciente.
2. Explora la carpeta [`data/`](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/tree/main/data) del monorepo — contiene las subcarpetas `raw/`, `process/`, `pipelines/` y `eval/` que usarás a lo largo de este módulo.
3. Crea el archivo `data/pipelines/PIPELINE_DESIGN.md` — ahí va tu documento de diseño.
4. Lee tu `CONTEXT-empresa.md` para identificar qué eventos de telemetría tienes disponibles, qué KPIs ya calculas y cuáles son los requisitos específicos de tu empresa.

> **Nota sobre las herramientas:** Hoy introduces **Prefect** como framework de orquestación — flows, tasks, estados y bloques de configuración. Tu documento de diseño debe reflejar cómo organizarías tu pipeline usando estos conceptos, aunque la implementación en código llega en los próximos días.

---

## 💻 Qué Debes Hacer

### Fase 1 — Análisis del estado actual

- [ ] Documenta en una sección "Estado actual" los datos que ya tienes: qué eventos de telemetría has capturado, dónde están almacenados y qué informes ya generas con Pandas.
- [ ] Identifica las limitaciones de tu implementación actual: ¿qué pasa si el script falla a mitad de ejecución? ¿puedes saber si los datos ya fueron procesados?

### Fase 2 — Diseño del pipeline

- [ ] Define el **propósito** del pipeline en una frase concreta: qué problema resuelve y qué valor entrega a tu empresa.
- [ ] Especifica el **formato de extracción**: de dónde vienen los datos (tabla, endpoint, fichero), en qué formato llegan y con qué frecuencia se actualizan.
- [ ] Diseña el **flujo de datos** con un diagrama en texto o Mermaid con al menos tres etapas claramente separadas: extracción, transformación y carga.
- [ ] Describe cómo manejarías una fuente que **actualiza registros existentes** en lugar de insertar siempre nuevos — explica la estrategia concreta para evitar duplicados en tu caso.

### Fase 3 — Resiliencia e idempotencia

- [ ] Define la estrategia de **idempotencia**: si el pipeline falla durante la fase de carga y se vuelve a ejecutar, explica exactamente cómo garantizas que los datos ya cargados no se corrompen ni se duplican.
- [ ] Diseña el **log de ejecución**: especifica los campos mínimos que registrarías en cada ejecución (inicio, fin, registros procesados, estado, errores) y explica por qué cada campo es necesario para auditar el pipeline en producción.

### Fase 4 — Mapa a Prefect

- [ ] Mapea tu diseño a los conceptos de Prefect: identifica cuáles serían tus **flows**, cuáles serían tus **tasks** y qué **estados** (Running, Completed, Failed) son relevantes para tu pipeline.
- [ ] Indica qué configuración o credenciales gestionarías como **bloques de Prefect** (por ejemplo, la conexión a Supabase).

⚠️ **IMPORTANTE:** El diseño debe ser específico para los datos de tu empresa. Los nombres de eventos, KPIs, tablas y entidades deben coincidir con lo especificado en tu `CONTEXT-empresa.md`. Un diseño genérico que ignore el contexto de tu empresa no será aceptado.

---

## ✅ Qué Evaluaremos

- [ ] El documento `data/pipelines/PIPELINE_DESIGN.md` existe en el monorepo y está escrito en Markdown legible.
- [ ] El propósito del pipeline está definido en una frase concreta que menciona el negocio de la empresa, no solo la tecnología.
- [ ] El diagrama de flujo muestra al menos tres etapas diferenciadas (extracción, transformación, carga) con el nombre de las entidades o tablas reales de la empresa.
- [ ] La estrategia para manejar actualizaciones de registros existentes está documentada con un mecanismo concreto (ej.: upsert por clave primaria, marca de tiempo de última modificación, tabla de control).
- [ ] La estrategia de idempotencia es explícita: describe qué ocurre en la segunda ejecución tras un fallo en la carga, no solo qué sería deseable.
- [ ] El log de ejecución especifica al menos cinco campos con el nombre del campo, el tipo de dato y la justificación de por qué ese campo es necesario para auditoría.
- [ ] El mapa a Prefect identifica al menos dos flows y tres tasks con nombres concretos alineados con las etapas del pipeline.
- [ ] El diseño es coherente con los eventos de telemetría y KPIs definidos en el `CONTEXT-empresa.md`.

---

## 📦 Cómo Entregar

1. Asegúrate de que `data/pipelines/PIPELINE_DESIGN.md` está en tu fork del monorepo.
2. Haz commit con el mensaje: `feat: add pipeline design document`.
3. Sube los cambios a tu repositorio en GitHub y comparte la URL con tu tech lead.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
