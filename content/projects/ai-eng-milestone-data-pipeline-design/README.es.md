# Hito 6 — Diseño de un Pipeline de Desempeño de Negocio (1/3)

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuyentes](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-empresa.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/06-telemetry-data-pipelines/data-pipelines)** antes de escribir una sola línea — ahí encontrarás el entregable de negocio, la audiencia, la frecuencia, los KPIs a medir y las métricas obligatorias que este pipeline debe producir.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu propia copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la compañía seleccionada al inicio del curso — no en un repositorio nuevo.

En las últimas semanas capturaste eventos de telemetría, los almacenaste en `telemetry_events`, y construiste un reporte técnico — volumen de eventos, tasa de errores, latencia — para tu propio equipo de ingeniería. **Ese sistema se queda exactamente como está.** No vas a tocar `telemetry_events`, `services/telemetry/analysis.py`, ni el endpoint `GET /telemetry/report` en este hito.

Hoy tu tech lead te pide algo distinto: un pipeline de datos **nuevo**, diseñado desde cero, cuyo único trabajo es convertir esa misma telemetría en datos que describan cómo está funcionando el negocio — el tipo de números que leería un gerente de departamento o el CEO, no el tipo que usa un ingeniero para depurar un servicio.

> > **Brief Técnico — Pipeline de Desempeño de Negocio (Fase de Diseño)**
> >
> > Antes de escribir una sola línea de código de orquestación, necesito que documentes el diseño de un nuevo pipeline de datos. Este no es para nosotros — es para el lado de negocio: el equipo de liderazgo que ha estado pidiendo un reporte de verdad en lugar de un PDF que alguien arma a mano cada semana.
> >
> > Este es un pipeline **nuevo**, construido sobre la telemetría que ya tienes. Tu tabla `telemetry_events`, tu reporte técnico, y el endpoint `GET /telemetry/report` no cambian — siguen sirviendo a ingeniería exactamente igual que antes. Lo que vas a construir ahora lee de la misma fuente pero produce un tipo de salida distinto: números sobre los que un stakeholder no técnico puede actuar.
> >
> > Entregable: un documento de diseño en Markdown, commiteado al monorepo. Todavía no hay código de orquestación — primero el diseño, después la implementación.

### ¿Qué hace robusto a un pipeline de datos?

Un pipeline de datos no es simplemente un script que mueve datos de un lugar a otro. Un pipeline de producción tiene etapas bien definidas, maneja fallos de forma predecible, y puede auditarse. Los tres atributos clave que separan un pipeline robusto de uno que "simplemente funciona" son:

- **Idempotencia**: correr el pipeline dos veces sobre los mismos datos produce el mismo resultado — sin duplicados, sin corrupción.
- **Observabilidad**: cada corrida deja suficientes rastros para saber qué pasó, cuándo, y por qué.
- **Recuperabilidad**: cuando el pipeline falla a mitad de camino, la siguiente corrida sabe exactamente dónde retomar.

Estos tres atributos son lo que tu documento de diseño debe demostrar que pensaste a fondo.

### Construye este pipeline alrededor de una necesidad real de negocio

Un pipeline de datos no es infraestructura por sí misma — y este mucho menos. Su única razón de existir es una pregunta de negocio que tu `CONTEXT-company.md` ya acota por ti, pero que hoy nadie responde de forma confiable.

Antes de diseñar las etapas de extracción, transformación o carga, lee tu `CONTEXT-company.md` del contexto de data pipelines — nombra el entregable de negocio concreto que tu compañía necesita, para quién es, con qué frecuencia, los KPIs exactos que debe calcular (ver su sección "KPIs a medir"), y qué métricas obligatorias los alimentan. (Esto es la continuación de lo que tu `CONTEXT-company.md` de telemetría ya adelantaba en su sección 4, "Cómo estas métricas conectan con el futuro" — este es ese momento, ahora concretado.)

Diseña el pipeline para producir exactamente los datos que ese entregable necesita — con la frescura, granularidad y rastro de auditoría correctos. No inventes un KPI genérico; el que tu compañía necesita ya está acotado en `CONTEXT-company.md`.

**Este es un pipeline nuevo, no un reemplazo.** El reporte técnico de telemetría que construiste antes sigue respondiendo preguntas técnicas para ingenieros (volumen, errores, latencia). Este pipeline responde una pregunta distinta, para una audiencia distinta, y su resultado vive en tablas y endpoints distintos. Nada del proyecto anterior cambia.

Cuando escribas el propósito del pipeline en la Fase 2, nombra el entregable de negocio al que apuntas y la(s) métrica(s) obligatoria(s) que lo alimentan. Si una etapa de tu diseño no sostiene ese entregable, cuestiona si pertenece a la v1.

---

## 🌱 Cómo Empezar

1. Corre `git pull` en tu copia del monorepo para asegurarte de tener el estado más reciente.
2. Explora la carpeta [`data/`](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/tree/main/data) del monorepo — contiene las subcarpetas `raw/`, `process/`, `pipelines/`, y `eval/` que usarás a lo largo de este módulo. El código de orquestación vivirá en `data/pipelines/`; los scripts de transformación reutilizables en `data/process/`; los endpoints HTTP que consultan o disparan el pipeline vivirán en `services/` e importarán desde `data/pipelines/` — no al revés.
3. Crea el archivo `data/pipelines/PIPELINE_DESIGN.md` — ahí va tu documento de diseño.
4. Lee tu `CONTEXT-company.md` del contexto de data pipelines — su sección "KPIs a medir" nombra los números exactos que este pipeline debe producir, y también indica la audiencia, la frecuencia, la agregación requerida, y la tabla de destino. (Las métricas obligatorias que alimentan esos KPIs son las de tu `CONTEXT-company.md` de telemetría, ya familiar del hito anterior.)
5. El resultado de este pipeline **no** pertenece a `telemetry_events`. Todas las tablas de destino nuevas viven bajo un esquema dedicado `reporting`, nombradas `reporting.business_metrics` — y se exponen a través de un módulo nuevo `services/reporting/`, separado de `services/telemetry/` y del endpoint `GET /telemetry/report`.

> **Nota sobre herramientas:** Hoy se te introduce **Prefect** como framework de orquestación — flows, tasks, states, y bloques de configuración. Tu documento de diseño debe reflejar cómo organizarías tu pipeline usando estos conceptos, aunque la implementación en código llega en los próximos días.

---

## 💻 Qué Necesitas Hacer

### Fase 1 — Análisis del estado actual

- [ ] Documenta en una sección "Estado Actual" lo que ya tienes: los eventos de telemetría capturados hasta ahora, dónde se almacenan, y qué responde ya tu reporte técnico existente para ingeniería.
- [ ] Identifica la brecha: ¿qué pregunta de negocio de tu `CONTEXT-company.md` sigue sin ser respondida por ese reporte técnico, y requeriría un pipeline dedicado?

### Fase 2 — Diseño del pipeline

- [ ] Define el **propósito** del pipeline en una sola frase concreta: nombra el entregable de negocio específico al que apuntas (ej. "producir el consolidado diario que alimenta el reporte ejecutivo semanal de [rol]"), el/los KPI(s) que calcula (de la sección "KPIs a medir" de tu `CONTEXT-company.md`), y la(s) métrica(s) obligatoria(s) de tu CONTEXT de telemetría sobre la que se construye.
- [ ] Especifica el **formato de extracción**: tu fuente es `telemetry_events` (más cualquier otra tabla de dominio existente que necesites) — en qué formato llega el dato, y con qué frecuencia se actualiza.
- [ ] Diseña el **flujo de datos** con un diagrama de texto o Mermaid que muestre al menos tres etapas claramente separadas: extracción, transformación, y carga.
- [ ] Describe cómo manejarías una fuente que **actualiza registros existentes** en lugar de siempre insertar nuevos — explica la estrategia concreta para evitar duplicados en tu caso específico.
- [ ] Nombra la(s) **tabla(s) de destino nueva(s)** bajo el esquema `reporting` (`reporting.business_metrics`) donde vivirá el resultado de este pipeline, y el/los **endpoint(s) nuevo(s) en `services/reporting/`** que lo expondrán — explícitamente separados de `telemetry_events` y de `GET /telemetry/report`.

### Fase 3 — Resiliencia e idempotencia

- [ ] Define tu **estrategia de idempotencia**: si el pipeline falla durante la fase de carga y se vuelve a correr, explica exactamente cómo garantizas que los datos ya cargados no se corrompen ni se duplican.
- [ ] Diseña tu **log de ejecución**: especifica los campos mínimos que registrarías en cada corrida (hora de inicio, hora de fin, registros procesados, estado, errores) y explica por qué cada campo es necesario para auditar el pipeline en producción.

### Fase 4 — Mapeo a Prefect

- [ ] Mapea tu diseño a conceptos de Prefect: identifica qué partes serían **flows**, cuáles serían **tasks**, y qué **states** (Running, Completed, Failed) son relevantes para tu pipeline.
- [ ] Indica qué configuración o credenciales manejarías como **Prefect blocks** (por ejemplo, la conexión a Supabase).

### Fase 5 — Integración con la aplicación (solo diseño)

- [ ] Esboza el/los **endpoint(s) nuevo(s) en `services/reporting/`** que el lado de negocio usará para consultar el/los KPI(s) resultante(s) y/o disparar una corrida — mantenidos separados de `services/telemetry/` y del endpoint `GET /telemetry/report`.
- [ ] Para cada endpoint, indica qué **función o flow en `data/pipelines/`** va a llamar — ninguna lógica de ETL pertenece a `services/`.

⚠️ **IMPORTANTE:** Los nombres de campos, IDs de entidad, y valores específicos de dominio en tu diseño deben coincidir con el vocabulario de dominio de tu compañía en el monorepo. Un diseño genérico que ignore el modelo de datos de tu compañía no será aceptado.

---

## ❓ Preguntas para Ayudarte a Diseñar el Pipeline

Antes de escribir `PIPELINE_DESIGN.md`, responde por escrito — aunque sea como borrador — cómo manejarías cada caso en **tu** monorepo.

### Idempotencia

1. **Duplicados en el origen** — ¿Cómo evitas contar la misma acción dos veces en `telemetry_events` y en tus agregados de negocio? ¿Qué campo del envelope es tu clave de deduplicación, y en qué capa?

   <details>
   <summary>Ver ejemplo y pista</summary>

   Un operador confirma `outbound_order_created` dos veces en 300 ms; llegan dos filas con el mismo `eventId` pero distintos timestamps de recepción.

   **Pista:** upsert sobre `eventId` en la ingesta.

   </details>

2. **Reintento después de un fallo** — Si el pipeline muere durante la carga con datos parciales insertados, ¿qué pasa cuando lo vuelves a correr? ¿Cómo garantizas el mismo resultado que una corrida limpia?

   <details>
   <summary>Ver ejemplo y pista</summary>

   La corrida de las 02:00 cargó 847 de 1,412 filas en tu nueva tabla de reporting y falló por un timeout de Supabase.

   **Pista:** upsert por clave de partición diaria.

   </details>

3. **Eventos tardíos** — ¿Cómo recalculas una métrica de negocio diaria ya publicada cuando llega un evento retrasado, sin inflar los números ni perder el rastro de auditoría?

   <details>
   <summary>Ver ejemplo y pista</summary>

   A las 23:50 se almacena un evento `stock_waste_registered` con un `timestamp` de mediodía; el agregado de ese día ya está en el reporte.

   **Pista:** recalcular la ventana; registrar la corrida que invalida.

   </details>

### Observabilidad

4. **Silencio vs. ausencia real** — ¿Cómo distingues actividad cero de una captura fallida o de un pipeline que nunca corrió? ¿Qué señales mínimas registrarías?

   <details>
   <summary>Ver ejemplo y pista</summary>

   Entre las 14:00 y las 15:00 no hay eventos relevantes registrados, pero el negocio siguió operando con normalidad.

   **Pista:** heartbeat más alerta de silencio.

   </details>

5. **Trazabilidad de la recolección** — ¿Qué rastros reconstruyen el camino evento → reporte de negocio y detectan huecos, ráfagas, o desfases de intervalo?

   <details>
   <summary>Ver ejemplo y pista</summary>

   Tu métrica se dispara a las 09:00 y se aplana a las 09:15 — ¿actividad real o un batch que procesó dos ventanas a la vez?

   **Pista:** correlacionar `requestId` y `run_id`.

   </details>

6. **Crecimiento vs. pérdida de datos** — Si el volumen de eventos varía de un día a otro, ¿cómo sabes si el negocio está creciendo o si estás perdiendo o duplicando mediciones?

   <details>
   <summary>Ver ejemplo y pista</summary>

   Lunes: 12,000 eventos; domingos: 800 — ¿patrón normal de actividad o fallos intermitentes de `POST /telemetry`?

   **Pista:** comparar eventos contra sesiones activas o locales que reportan.

   </details>

### Recuperabilidad

7. **Caída de base de datos** — ¿Dónde retomas si la conexión se cae a mitad del pipeline? ¿Qué checkpoint persistes?

   <details>
   <summary>Ver ejemplo y pista</summary>

   Pandas terminó de agrupar por entidad, pero Supabase falló en el `INSERT` a la tabla de reporting.

   **Pista:** checkpoint de fase en `pipeline_runs`.

   </details>

8. **Buffer en el frontend** — ¿Tiene sentido bufferear eventos offline en el navegador? ¿Qué riesgos introduce, y qué capa debería asumirlos?

   <details>
   <summary>Ver ejemplo y pista</summary>

   Un operador pierde WiFi por 20 minutos; el navegador guarda 45 eventos en `localStorage` y los envía en un solo lote al reconectar.

   **Pista:** buffer del cliente; deduplicación del lado del servidor.

   </details>

9. **Reintento de transmisión** — ¿Cómo diseñas reintentos sobre `POST /telemetry` sin romper la idempotencia? ¿Qué respuesta del servidor significa "ya almacenado" vs. "reintentar"?

   <details>
   <summary>Ver ejemplo y pista</summary>

   El cliente recibe un timeout, reintenta, pero el servidor ya había persistido el evento en el primer request (lento).

   **Pista:** `Idempotency-Key`; devolver 200 si ya existe.

   </details>

### Transversal

10. **Corridas concurrentes** — ¿Qué observas, cómo evitas condiciones de carrera en la carga, y cómo te recuperas cuando el cron y un disparo manual desde `services/` se solapan?

    <details>
    <summary>Ver ejemplo y pista</summary>

    El flujo programado empieza a las 02:00; a las 02:05 alguien hace clic en "Correr pipeline ahora" en el backoffice.

    **Pista:** lock por ventana; `run_id` único.

    </details>

---

## ✅ Qué Vamos a Evaluar

- [ ] El archivo `data/pipelines/PIPELINE_DESIGN.md` existe en el monorepo y está escrito en Markdown legible.
- [ ] El propósito del pipeline está definido en una sola frase concreta que nombra el entregable de negocio y el/los KPI(s) del `CONTEXT-company.md` de la compañía — no un KPI genérico o técnico.
- [ ] El diseño no modifica `telemetry_events`, `services/telemetry/analysis.py`, ni `GET /telemetry/report` — el resultado del nuevo pipeline vive en tablas nuevas bajo un esquema `reporting` y se expone a través de un módulo nuevo `services/reporting/`.
- [ ] El diagrama de flujo de datos muestra al menos tres etapas distintas (extracción, transformación, carga) con los nombres reales de entidad o tabla de la compañía.
- [ ] La estrategia para manejar actualizaciones a registros existentes está documentada con un mecanismo concreto (ej. upsert por clave primaria, timestamp de última modificación, tabla de control).
- [ ] La estrategia de idempotencia es explícita: describe qué pasa en la segunda corrida después de un fallo en la fase de carga, no solo lo que sería deseable.
- [ ] El log de ejecución especifica al menos cinco campos con el nombre del campo, tipo de dato, y justificación de por qué ese campo es necesario para auditoría.
- [ ] El mapeo a Prefect identifica al menos dos flows y tres tasks con nombres concretos alineados con las etapas del pipeline.
- [ ] El diseño documenta al menos dos endpoints planeados en `services/reporting/` (consulta de estado y disparo manual) y nombra las funciones de `data/pipelines/` que cada uno importará.
- [ ] El diseño es consistente con los eventos de telemetría y las métricas obligatorias ya definidas en el archivo CONTEXT de la compañía.

---

## 📦 Cómo Entregar

1. Asegúrate de que `data/pipelines/PIPELINE_DESIGN.md` esté commiteado en tu copia del monorepo.
2. Haz commit con el mensaje: `feat: add business performance pipeline design document`.
3. Sube tus cambios a tu repositorio de GitHub y comparte la URL con tu tech lead.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuyentes](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
