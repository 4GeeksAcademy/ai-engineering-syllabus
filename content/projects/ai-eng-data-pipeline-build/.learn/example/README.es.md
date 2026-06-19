# GreenPatch Co-op — Pipeline de telemetría resiliente (Ejemplo de clase)

> **Para instructores:** Escenario paralelo en aula para `ai-eng-data-pipeline-build`. Misma columna vertebral (flows/tasks Prefect, reintentos, caché, idempotencia, deployment, endpoints API), dominio distinto. Los estudiantes siguen el enunciado completo del monorepo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**GreenPatch Co-op** gestiona una app de préstamo de herramientas para huertos comunitarios. Ayer aprobaste un documento de diseño para un ETL nocturno de telemetría. Hoy lo implementas con Prefect en un repo demo desechable o carpeta local — no el monorepo evaluable de la empresa.

Especificación de partida: el mini diseño de abajo sustituye a `PIPELINE_DESIGN.md`.

### Nota de alcance

| Proyecto evaluable (`ai-eng-data-pipeline-build`) | Este ejemplo de clase               |
| ------------------------------------------------- | ----------------------------------- |
| CONTEXT de empresa + monorepo de inventario       | CONTEXT ficticio GreenPatch (abajo) |
| Ticket completo del CTO + deployment Docker       | Mismas fases, dataset más pequeño   |
| Commit al fork del monorepo del estudiante        | Solo demo local                     |

---

## Mini diseño (usar en lugar de PIPELINE_DESIGN.md)

**Origen:** `public.telemetry_events` — eventos `reservation_created`, `checkout_validation_failed`, `tool_threshold_low`, `login_failed`.

**Destino:** `reporting.daily_tool_metrics` con grano `(report_date, tool_id)`.

**Idempotencia:** upsert sobre `(report_date, tool_id)`.

**Paso opcional:** exportar snapshot `data/eval/latest_run.json` — el fallo no debe detener la carga.

**Schedule:** cron nocturno `0 3 * * *` UTC (comentario: tráfico bajo tras medianoche).

---

## Qué construir

Crear `data/pipelines/pipeline.py` con:

### Fase 1 — Flows y tasks

- [ ] `@flow` `greenpatch_telemetry_etl_flow` con tasks: extract → transform → load.
- [ ] `@task(allow_failure=True)` opcional `export_eval_snapshot`.

### Fase 2 — Resiliencia

- [ ] `retries=2` en extract (BD) con comentario.
- [ ] Una task con `raise_on_failure=False` manejada en el flow.
- [ ] Transform con caché `cache_expiration=timedelta(hours=1)` y comentario sobre la clave.

### Fase 3 — Idempotencia

- [ ] Load hace upsert — segunda ejecución mismo rango = mismo conteo de filas.
- [ ] Registrar metadatos de ejecución (inicio, fin, registros, estado, errores) en `data/eval/pipeline_runs.jsonl`.

### Fase 4 — Deployment (demo)

- [ ] Documentar comando de deployment en comentario o stub `prefect.yaml` — Docker completo opcional en clase.

### Fase 5 — Stub API (opcional en clase)

- [ ] Dos rutas FastAPI o funciones simulando `GET /pipeline/runs/latest` y `POST /pipeline/runs` importando desde `pipeline.py`.

---

## Verificar juntos

- [ ] Tres o más tasks, no un script monolítico.
- [ ] Fallo en task opcional no aborta el flow principal.
- [ ] Segunda ejecución misma ventana no duplica filas de métricas.
- [ ] Log de ejecución con ≥5 campos por run.
- [ ] Nombres referencian tablas/eventos GreenPatch — no placeholders genéricos.

---

## Preguntas de discusión

1. ¿Por qué cachear la task de transform pero no la de extract?
2. Si `export_eval_snapshot` falla pero load tuvo éxito — ¿estado `success` o `partial`?
3. ¿Cómo cambiarías el diseño si GreenPatch necesitara runs horarios en lugar de nocturnos?
