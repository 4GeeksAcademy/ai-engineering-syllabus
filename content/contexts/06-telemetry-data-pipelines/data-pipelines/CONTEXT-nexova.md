# CONTEXT — Nexova (Business Performance Pipeline)

## Data Pipeline Projects (Design · Implementation · Subflows & Tests)

<!-- hide -->

_Estas instrucciones están [disponibles en español](./CONTEXT-nexova-pipeline.es.md)._

<!-- endhide -->

This file is self-contained: it gives you everything you need to scope, build, and test the business performance pipeline for Nexova, without having to go hunting through other documents. It builds directly on the mandatory metrics already defined in your `CONTEXT-nexova.md` (telemetry) — read that first if you haven't.

---

## 1. The business deliverable

Laura (CEO) wants a **weekly report** she can open without calling Elena or Patricia, comparing how each office is doing on training material investment and delivery — the two things L&D keeps raising but that nobody currently tracks centrally across Valencia and Miami.

> **Target deliverable:** a weekly, per-office, per-programme rollup of material cost, kits delivered, and material shortage activity — the "Weekly Office & Programme Performance Report."

This is the **one concrete deliverable** your pipeline exists to produce. Everything in your `PIPELINE_DESIGN.md` should trace back to it.

**Audience:** Laura (CEO) and Elena (L&D Manager) — non-technical stakeholders who need numbers, not raw events.
**Cadence:** weekly (fresh as of Monday morning, matching the existing "automated weekly report" expectation leadership already has).

---

## 2. KPIs to Measure

**These are the KPIs this pipeline exists to produce.** Everything else in this document — source events, aggregation logic, table schema — is implementation detail in service of these four numbers. If you're unsure what to build next, come back to this list.

| KPI                            | What it measures                                                                                          | Why it matters to Nexova                                                                                  |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Material Cost per Office/Programme** | How much an office spent acquiring training or onboarding material for a given programme during the week. | Shows where L&D investment concentrates, and whether it matches enrolment demand.                              |
| **Kits Delivered**             | How many kits or certificates were actually delivered to clients, candidates, consultants, or agents during the week. | The adoption signal — spending on material only matters if it reaches the people who need it.                 |
| **Shortage Frequency**         | How many times during the week a programme's material stock ran below the configured minimum.            | A leading indicator that Elena needs to reprint or reorder before a large enrolment wave is affected.          |
| **Cost Variance Frequency**    | How many times during the week a material supplier's cost spiked abnormally versus its historical price.  | Signals when Elena and Laura need to renegotiate or find an alternate supplier.                                |

Everything below this point exists only to compute these four numbers correctly, reliably, and auditable.

---

## 3. Source data

> **A quick schema check first:** this pipeline needs a cost value on `inbound_order_created` (e.g. a `unit_cost` or `total_cost` field in `properties`) to compute material cost. If your telemetry schema from the earlier milestone doesn't have one yet, add it now — it's a natural extension of an existing mandatory event, not a new event type.

Your source is `telemetry_events`, filtered to the mandatory metrics already defined in your telemetry CONTEXT:

| `event_type`                  | Feeds which KPI(s)                        |
| -------------------------------- | ---------------------------------------------- |
| `inbound_order_created`        | Material Cost per Office/Programme             |
| `outbound_order_created`       | Kits Delivered                                 |
| `stock_threshold_triggered`    | Shortage Frequency                              |
| `kit_cost_variance_detected`   | Cost Variance Frequency                         |

You don't need any event outside this list for v1 — resist the urge to widen scope.

---

## 4. Required aggregation

- **Grain:** one row per `office` per `programme_id` per ISO week (`week_start` = the Monday of that week, UTC).
- **Dimensions:** `office` (`valencia`/`miami`), `programme_id`, `week_start`.
- **Computed fields per row (each maps directly to a KPI from section 2):**
  - `total_material_cost` — Material Cost per Office/Programme: sum of `inbound_order_created` costs for the week, in the office's local currency
  - `kits_delivered_count` — Kits Delivered: count of `outbound_order_created` for the week
  - `shortage_events_count` — Shortage Frequency: count of `stock_threshold_triggered` for the week
  - `cost_variance_events_count` — Cost Variance Frequency: count of `kit_cost_variance_detected` for the week
  - `currency` — `EUR` or `USD`, matching the office. **Do not convert currencies in this pipeline** — that is a v2 concern once you have an FX rate source.

---

## 5. Destination table

Create this table under a dedicated `reporting` schema — never write into `telemetry_events`:

```sql
create table reporting.weekly_office_program_performance (
  id uuid primary key default gen_random_uuid(),
  office text not null,
  programme_id text not null,
  week_start date not null,
  total_material_cost numeric not null default 0,
  kits_delivered_count integer not null default 0,
  shortage_events_count integer not null default 0,
  cost_variance_events_count integer not null default 0,
  currency text not null,
  computed_at timestamptz not null default now(),
  unique (office, programme_id, week_start)
);
```

The `unique (office, programme_id, week_start)` constraint is what your idempotency strategy (upsert) should rely on.

---

## 6. New reporting endpoint

Expose this pipeline's output through a **new** module, `services/reporting/`, separate from `services/telemetry/`:

- `GET /reporting/weekly-office-program-performance` — accepts optional `week_start` (defaults to the most recent computed week); returns all office/programme combinations for that week:

```json
{
  "week_start": "2026-07-13",
  "entries": [
    {
      "office": "valencia",
      "programme_id": "b2b-sales",
      "total_material_cost": 1240.50,
      "kits_delivered_count": 18,
      "shortage_events_count": 1,
      "cost_variance_events_count": 0,
      "currency": "EUR"
    }
  ]
}
```

- `GET /reporting/pipeline-runs/latest` — status and metadata of the last pipeline run (this can be the same pattern you'll reuse for any future pipeline).
- `POST /reporting/pipeline-runs` — triggers a manual run.

---

## 7. Business constraints

- Never mix currencies in a single aggregate row — `EUR` (Valencia) and `USD` (Miami) are reported separately, side by side, not summed together.
- This pipeline reads `telemetry_events` **read-only**. It never writes back to it.
- `services/telemetry/analysis.py` and `GET /telemetry/report` are out of scope for this milestone — do not modify them.
