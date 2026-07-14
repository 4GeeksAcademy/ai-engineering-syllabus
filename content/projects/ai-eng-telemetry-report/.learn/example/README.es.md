# Biblioteca Maple Street — Reporte técnico de telemetría (Ejemplo de clase)

> **Para instructores:** Escenario paralelo en aula para `ai-eng-telemetry-report`. Misma columna vertebral (pipeline Pandas, ≥3 métricas operacionales, `GET /telemetry/report`, caché 60s), dominio distinto. Los estudiantes siguen el enunciado completo del monorepo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Biblioteca Maple Street** tiene `telemetry_events` con actividad del mostrador (préstamos, fallos, page views). Construye una API de **reporte técnico** mínima — sin dashboard de negocio.

### Nota de alcance

| Proyecto evaluable (`ai-eng-telemetry-report`)  | Este ejemplo de clase          |
| ----------------------------------------------- | ------------------------------ |
| ≥3 métricas técnicas/operacionales              | 3 métricas fijas de biblioteca |
| Monorepo completo `services/telemetry/`         | Módulo mini `library-api`      |
| auth_failure_rate + dashboard visual opcionales | Omitir extras                  |
| ≥20 filas reales                                | 10+ filas seed OK para demo    |

**Mini métricas operacionales:**

1. Eventos por día y tipo (`book_checkout_completed`, `book_checkout_failed`, `page_viewed`)
2. Tasa de fallo de préstamo por día (`book_checkout_failed` / todos los intentos)
3. Page views por día (`page_viewed`)

---

## Qué construir

### 1. `library_api/telemetry/analysis.py`

- [ ] `events_per_day(start_date, end_date)` → lista de `{ date, event_type, count }`
- [ ] `checkout_failure_rate_per_day(start_date, end_date)` → lista de `{ date, failure_rate }`
- [ ] `page_views_per_day(start_date, end_date)` → lista de `{ date, count }`
- [ ] Carga con filtro SQL en `event_type` (+ `IN` para métricas de ratio) y rango `timestamp`; refina `tags` en Pandas
- [ ] `pd.to_datetime(..., utc=True)` antes de `groupby('date')`
- [ ] Sin loops por filas para agregar

### 2. `GET /telemetry/report`

- [ ] `start_date`, `end_date` opcionales; por defecto últimos 7 días
- [ ] Respuesta:

```json
{
  "period": { "from": "...", "to": "..." },
  "metrics": {
    "events_per_day": [...],
    "checkout_failure_rate_per_day": [...],
    "page_views_per_day": [...]
  }
}
```

- [ ] Caché en memoria, TTL 60 segundos

### 3. Verificar

- [ ] Dos llamadas en 60s — la segunda no debe reconsultar BD (log o breakpoint)
- [ ] Cada métrica tiene **varios días o ceros explícitos** — no un número global único
- [ ] Sin framing de ventas/conversión/ingresos en nombres o preguntas

---

## Verificar juntos

- [ ] `curl "/telemetry/report"` devuelve JSON válido con filas agrupadas
- [ ] Cambiar `start_date` cambia period y filas de métricas
- [ ] Lógica Pandas en `analysis.py`, no inline en el handler de ruta

---

## Preguntas de discusión

1. ¿Qué falla si haces `groupby` sobre strings de timestamp?
2. ¿Por qué cachear 60s en lugar de recalcular cada request?
3. ¿Por qué esto es un reporte técnico y no un dashboard de negocio?
