# CONTEXT — Brasaland (Business Performance Pipeline)

## Data Pipeline Projects (Design · Implementation · Subflows & Tests)

<!-- hide -->

_Estas instrucciones están [disponibles en español](./CONTEXT-brasaland-pipeline.es.md)._

<!-- endhide -->

This file is self-contained: it gives you everything you need to scope, build, and test the business performance pipeline for Brasaland, without having to go hunting through other documents. It builds directly on the mandatory metrics already defined in your `CONTEXT-brasaland.md` (telemetry) — read that first if you haven't.

---

## 1. The business deliverable

Mariana (CEO) wants a **weekly report** she can open every Monday without calling anyone, comparing how each of the 14 locations is performing on cost and waste — the two levers Felipe and Lucía keep raising but that nobody currently tracks centrally.

> **Target deliverable:** a weekly, per-location, per-country rollup of purchase cost, waste cost, and stockout activity — the "Weekly Location Cost & Waste Report."

This is the **one concrete deliverable** your pipeline exists to produce. Everything in your `PIPELINE_DESIGN.md` should trace back to it.

**Audience:** Mariana (CEO) and Felipe (Operations Director) — non-technical stakeholders who need numbers, not raw events.
**Cadence:** weekly (the data should be fresh as of Monday morning, matching the existing "automated weekly report" expectation the leadership team already has).

---

## 2. KPIs to Measure

**These are the KPIs this pipeline exists to produce.** Everything else in this document — source events, aggregation logic, table schema — is implementation detail in service of these five numbers. If you're unsure what to build next, come back to this list.

| KPI                          | What it measures                                                                                                       | Why it matters to Brasaland                                                                       |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Purchase Cost per Location** | How much a location spent buying ingredients from suppliers during the week.                                          | Shows where spending concentrates, and feeds cross-location purchasing negotiations (Lucía).          |
| **Waste Cost per Location**    | How much a location lost to expired product, kitchen error, or theft during the week, in monetary terms.               | Waste is a direct hit to margin — this is the number Felipe needs to prioritize audits.               |
| **Waste Ratio**                | Waste cost as a share of purchase cost for that location and week.                                                     | The efficiency signal: a location can spend a lot and still be efficient if waste stays low, or spend little and still be a problem if waste is high relative to its own purchases. |
| **Stockout Frequency**        | How many times during the week a location's stock of some ingredient fell below the configured minimum.                | A leading indicator of service risk — frequent stockouts mean the kitchen may run out of a key ingredient mid-service. |
| **Price Alert Frequency**     | How many times during the week an ingredient's cost spiked abnormally versus its historical price.                     | Signals when Lucía needs to renegotiate or find an alternate supplier before the cost trend compounds.  |

Everything below this point exists only to compute these five numbers correctly, reliably, and auditable.

---

## 3. Source data

> **A quick schema check first:** this pipeline needs a cost value on `inbound_order_created` and `stock_waste_registered` (e.g. a `unit_cost` or `total_cost` field in `properties`) to compute purchase and waste cost. If your telemetry schema from the earlier milestone doesn't have one yet, add it now — it's a natural extension of an existing mandatory event, not a new event type.

Your source is `telemetry_events`, filtered to the mandatory metrics already defined in your telemetry CONTEXT:

| `event_type`                        | Feeds which KPI(s)                                                  |
| -------------------------------------- | ----------------------------------------------------------------------- |
| `inbound_order_created`              | Purchase Cost per Location                                              |
| `outbound_order_created`             | (operational volume only — not a KPI in this report, but useful context for anomaly checks) |
| `stock_waste_registered`             | Waste Cost per Location, Waste Ratio                                    |
| `stock_threshold_triggered`          | Stockout Frequency                                                      |
| `ingredient_price_variance_detected` | Price Alert Frequency                                                   |

You don't need any event outside this list for v1 — resist the urge to widen scope.

---

## 4. Required aggregation

- **Grain:** one row per `location_id` per ISO week (`week_start` = the Monday of that week, UTC).
- **Dimensions:** `location_id`, `country` (`CO`/`US`), `week_start`.
- **Computed fields per row (each maps directly to a KPI from section 2):**
  - `total_purchase_cost` — Purchase Cost per Location: sum of `inbound_order_created` costs for the week, in the location's local currency
  - `total_waste_cost` — Waste Cost per Location: sum of `stock_waste_registered` costs for the week
  - `waste_ratio` — Waste Ratio: `total_waste_cost / total_purchase_cost` (0 if no purchases that week)
  - `stockout_events_count` — Stockout Frequency: count of `stock_threshold_triggered` for the week
  - `price_alert_events_count` — Price Alert Frequency: count of `ingredient_price_variance_detected` for the week
  - `currency` — `COP` or `USD`, matching the location's country. **Do not convert currencies in this pipeline** — that is a v2 concern once you have an FX rate source.

---

## 5. Destination table

Create this table under a dedicated `reporting` schema — never write into `telemetry_events`:

```sql
create table reporting.weekly_location_performance (
  id uuid primary key default gen_random_uuid(),
  location_id text not null,
  country text not null,
  week_start date not null,
  total_purchase_cost numeric not null default 0,
  total_waste_cost numeric not null default 0,
  waste_ratio numeric not null default 0,
  stockout_events_count integer not null default 0,
  price_alert_events_count integer not null default 0,
  currency text not null,
  computed_at timestamptz not null default now(),
  unique (location_id, week_start)
);
```

The `unique (location_id, week_start)` constraint is what your idempotency strategy (upsert) should rely on.

---

## 6. New reporting endpoint

Expose this pipeline's output through a **new** module, `services/reporting/`, separate from `services/telemetry/`:

- `GET /reporting/weekly-location-performance` — accepts optional `week_start` (defaults to the most recent computed week); returns all locations for that week:

```json
{
  "week_start": "2026-07-13",
  "locations": [
    {
      "location_id": "medellin-centro",
      "country": "CO",
      "total_purchase_cost": 8420000,
      "total_waste_cost": 610000,
      "waste_ratio": 0.072,
      "stockout_events_count": 2,
      "price_alert_events_count": 1,
      "currency": "COP"
    }
  ]
}
```

- `GET /reporting/pipeline-runs/latest` — status and metadata of the last pipeline run (this can be the same pattern you'll reuse for any future pipeline).
- `POST /reporting/pipeline-runs` — triggers a manual run.

---

## 7. Business constraints

- Never mix currencies in a single aggregate row — `COP` and `USD` locations are reported separately, side by side, not summed together.
- This pipeline reads `telemetry_events` **read-only**. It never writes back to it.
- `services/telemetry/analysis.py` and `GET /telemetry/report` are out of scope for this milestone — do not modify them.
