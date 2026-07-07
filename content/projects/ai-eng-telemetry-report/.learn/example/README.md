# Maple Street Library — Telemetry Report (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-telemetry-report`. Same spine (Pandas pipeline, grouped metrics, `GET /telemetry/report`, 60s cache), different domain. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Maple Street Library** has `telemetry_events` seeded with desk activity (checkouts, failures). Build a tiny report API — no dashboard UI.

### Scope note

| Graded project (`ai-eng-telemetry-report`) | This class example          |
| ------------------------------------------ | --------------------------- |
| Company CONTEXT KPIs via Phase 1 plan      | 2 fixed library metrics     |
| Full monorepo `services/telemetry/`        | Mini `library-api` module   |
| Optional auth_failure_rate                 | Skip auth metric            |
| ≥20 real rows required                     | 10+ seeded rows OK for demo |

**Mini KPIs:**

1. Checkouts per day (`book_checkout_completed`)
2. Failed checkouts per day (`book_checkout_failed`)

---

## What to build

### 1. `library_api/telemetry/analysis.py`

- [ ] `checkouts_per_day(start_date, end_date)` → list of `{ date, count }`
- [ ] `checkout_failures_per_day(start_date, end_date)` → list of `{ date, count }`
- [ ] Load with SQL filter on `event_type` (+ `IN` for ratio metrics) and `timestamp` range; refine `tags` in Pandas
- [ ] `pd.to_datetime(..., utc=True)` before `groupby('date')`
- [ ] No row loops for aggregation

### 2. `GET /telemetry/report`

- [ ] Optional `start_date`, `end_date`; default last 7 days
- [ ] Response:

```json
{
  "period": { "from": "...", "to": "..." },
  "metrics": {
    "checkouts_per_day": [...],
    "checkout_failures_per_day": [...]
  }
}
```

- [ ] In-memory cache, TTL 60 seconds

### 3. Verify

- [ ] Hit endpoint twice within 60s — second call should not re-query DB (log or breakpoint)
- [ ] Each metric array has **multiple days or explicit zeros** — not one global number

---

## Verify together

- [ ] `curl "/telemetry/report"` returns valid JSON with grouped rows
- [ ] Changing `start_date` changes period and metric rows
- [ ] Pandas path visible in `analysis.py`, not inlined in route handler

---

## Discussion questions

1. What goes wrong if you `groupby` on timestamp strings?
2. Why cache a 60s report instead of recomputing every request?
3. When is a global count misleading compared to per-day grouping?
