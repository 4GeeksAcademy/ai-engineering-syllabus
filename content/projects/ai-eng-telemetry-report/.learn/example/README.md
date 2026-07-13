# Maple Street Library — Telemetry Technical Report (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-telemetry-report`. Same spine (Pandas pipeline, ≥3 operational metrics, `GET /telemetry/report`, 60s cache), different domain. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Maple Street Library** has `telemetry_events` seeded with desk activity (checkouts, failures, page views). Build a tiny **technical** report API — no business dashboard.

### Scope note

| Graded project (`ai-eng-telemetry-report`)    | This class example          |
| --------------------------------------------- | --------------------------- |
| ≥3 technical/operational metrics              | 3 fixed library metrics     |
| Full monorepo `services/telemetry/`           | Mini `library-api` module   |
| Optional auth_failure_rate + visual dashboard | Skip extras                 |
| ≥20 real rows required                        | 10+ seeded rows OK for demo |

**Mini operational metrics:**

1. Events per day by type (`book_checkout_completed`, `book_checkout_failed`, `page_viewed`)
2. Failure rate per day (`book_checkout_failed` / all checkout attempts)
3. Page views per day (`page_viewed`)

---

## What to build

### 1. `library_api/telemetry/analysis.py`

- [ ] `events_per_day(start_date, end_date)` → list of `{ date, event_type, count }`
- [ ] `checkout_failure_rate_per_day(start_date, end_date)` → list of `{ date, failure_rate }`
- [ ] `page_views_per_day(start_date, end_date)` → list of `{ date, count }`
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
    "events_per_day": [...],
    "checkout_failure_rate_per_day": [...],
    "page_views_per_day": [...]
  }
}
```

- [ ] In-memory cache, TTL 60 seconds

### 3. Verify

- [ ] Hit endpoint twice within 60s — second call should not re-query DB (log or breakpoint)
- [ ] Each metric array has **multiple days or explicit zeros** — not one global number
- [ ] No sales/conversion/revenue framing in metric names or questions

---

## Verify together

- [ ] `curl "/telemetry/report"` returns valid JSON with grouped rows
- [ ] Changing `start_date` changes period and metric rows
- [ ] Pandas path visible in `analysis.py`, not inlined in route handler

---

## Discussion questions

1. What goes wrong if you `groupby` on timestamp strings?
2. Why cache a 60s report instead of recomputing every request?
3. Why is this a technical report and not a business dashboard?
