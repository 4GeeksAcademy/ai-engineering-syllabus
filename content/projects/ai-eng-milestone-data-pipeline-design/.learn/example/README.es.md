# GreenPatch Co-op — Diseño de pipeline de telemetría (Ejemplo de clase)

> **Para instructores:** Escenario paralelo en aula para `ai-eng-milestone-data-pipeline-design`. Misma columna vertebral (estado actual, propósito ETL, diagrama de flujo, estrategia de actualización/dedup, idempotencia, log de ejecución, mapa a Prefect), dominio distinto. Los estudiantes siguen el enunciado completo del monorepo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**GreenPatch Co-op** gestiona una app de préstamo de herramientas para huertos comunitarios. Ya capturas cuatro eventos de telemetría (`reservation_created`, `checkout_validation_failed`, `tool_threshold_low`, `login_failed`) en una tabla Postgres y generas CSV semanales con Pandas para utilización y abandono de reservas. Operaciones quiere un pipeline de producción antes del lanzamiento de dashboards — solo diseño, sin código Prefect todavía.

En una sesión, redacta un **mini `data/PIPELINE_DESIGN.md`** — sin código.

### Nota de alcance

| Proyecto evaluable (`ai-eng-milestone-data-pipeline-design`) | Este ejemplo de clase                              |
| ------------------------------------------------------------ | -------------------------------------------------- |
| Monorepo de la empresa                                       | Escenario ficticio GreenPatch (abajo)              |
| Brief completo del CTO + mapa Prefect                        | Mismos encabezados de sección, narrativa más corta |
| Commit al monorepo del estudiante                            | Solo Markdown local                                |

---

## Datos del escenario

**Telemetría ya capturada:**

| Evento                       | Almacenamiento            |
| ---------------------------- | ------------------------- |
| `reservation_created`        | `public.telemetry_events` |
| `checkout_validation_failed` | `public.telemetry_events` |
| `tool_threshold_low`         | `public.telemetry_events` |
| `login_failed`               | `public.telemetry_events` |

**Informes existentes:** notebook Pandas exporta `weekly_utilization.csv` y `reservation_abandonment.csv`.

**KPIs:** tasa de utilización de herramientas, tasa de abandono de reservas, cumplimiento de devoluciones.

**Entidades:** `Tool`, `Reservation`, `Checkout`, `Member`.

---

## Qué construir

Crear `data/PIPELINE_DESIGN.md` (carpeta de demo o repo desechable) con estas secciones:

### 1. Estado actual

- [ ] Lista los cuatro eventos, dónde viven y qué informes Pandas existen.
- [ ] Nombra al menos dos limitaciones (sin log de ejecución, scan completo de tabla, re-ejecución no idempotente, etc.).

### 2. Propósito

- [ ] Una frase: qué problema de negocio resuelve el pipeline para ops de GreenPatch.

### 3. Formato de extracción

- [ ] Tabla origen, formato JSON del envelope, cadencia batch nocturna.

### 4. Diagrama de flujo de datos

- [ ] Mermaid o ASCII: extracción → transformación → carga con nombres reales (`telemetry_events`, `reporting.daily_tool_metrics`).

### 5. Estrategia de actualización / dedup

- [ ] Cómo omitir `eventId` ya procesados.
- [ ] Cómo hacer upsert de agregados diarios cuando llegan eventos tardíos.

### 6. Plan de idempotencia

- [ ] Fallo a mitad de carga y reintento seguro (watermark, staging, upsert transaccional).
- [ ] Explica comportamiento en la segunda ejecución — no solo "volver a ejecutar."

### 7. Log de ejecución (mínimo cinco campos)

| Campo                             | Por qué importa           |
| --------------------------------- | ------------------------- |
| `run_id`                          | Trazar una ejecución      |
| `watermark_from` / `watermark_to` | Auditar ventana procesada |
| `rows_extracted`                  | Detectar lotes vacíos     |
| `status`                          | Alertas                   |

Añade al menos un campo más con tipo y justificación.

### 8. Mapa a Prefect

- [ ] Nombra ≥2 flows (p. ej. ETL nocturno + backfill).
- [ ] Nombra ≥3 tasks alineadas con etapas ETL.
- [ ] Lista estados relevantes y al menos un block (p. ej. credenciales Supabase).

---

## Verificar juntos

- [ ] Estado actual referencia eventos reales de los datos del escenario — no placeholders genéricos.
- [ ] Diagrama muestra tres etapas ETL con nombres de tablas.
- [ ] Idempotencia describe comportamiento concreto en la segunda ejecución.
- [ ] Nombres Prefect mapean a etapas del pipeline, no solo conceptos abstractos.
- [ ] Sin archivos Python/Prefect — solo documento de diseño.

---

## Preguntas de discusión

1. ¿Por qué un watermark es mejor que leer la tabla `telemetry_events` completa cada noche?
2. ¿Qué falla si avanzas el watermark antes de que confirme la transacción de carga?
3. ¿Qué evento de GreenPatch encaja en stream vs batch en una implementación futura — y afecta eso al documento de diseño?
