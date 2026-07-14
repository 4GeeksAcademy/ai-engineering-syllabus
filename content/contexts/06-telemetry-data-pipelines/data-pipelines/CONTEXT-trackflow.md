# CONTEXT — TrackFlow (Business Performance Pipeline)

## Data Pipeline Projects (Design · Implementation · Subflows & Tests)

<!-- hide -->

_Estas instrucciones están [disponibles en español](./CONTEXT-trackflow-pipeline.es.md)._

<!-- endhide -->

This file is self-contained: it gives you everything you need to scope, build, and test the business performance pipeline for TrackFlow, without having to go hunting through other documents. It builds directly on the mandatory metrics already defined in your `CONTEXT-trackflow.md` (telemetry) — read that first if you haven't.

---

## 1. The business deliverable

Thomas (CEO) wants a **weekly report** he can open without calling Ana or Miguel, comparing how each warehouse is performing per client — the thing his directors currently spend hours assembling by hand every Sunday night.

> **Target deliverable:** a weekly, per-warehouse, per-client rollup of throughput, stockout activity, and inventory accuracy — the "Weekly Warehouse & Client Performance Report."

This is the **one concrete deliverable** your pipeline exists to produce. Everything in your `PIPELINE_DESIGN.md` should trace back to it.

**Audience:** Thomas (CEO) and Ana (Head of Warehouse Operations) — non-technical stakeholders who need numbers, not raw events.
**Cadence:** weekly (fresh as of Monday morning, matching the existing "automated weekly executive report" expectation leadership already has).

---

## 2. KPIs to Measure

**These are the KPIs this pipeline exists to produce.** Everything else in this document — source events, aggregation logic, table schema — is implementation detail in service of these four numbers. If you're unsure what to build next, come back to this list.

| KPI                        | What it measures                                                                                     | Why it matters to TrackFlow                                                                              |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------|
| **Inbound Volume**           | How many units of a client's goods a warehouse received during the week.                                | Shows incoming workload per warehouse and client — the basis for capacity planning (Ana).                    |
| **Outbound Throughput**      | How many orders a warehouse picked and dispatched for a client during the week.                          | The processing-capacity signal — how much a warehouse is actually able to move, not just receive.            |
| **Stockout Frequency**       | How many times during the week a client's SKU at a warehouse fell below the configured minimum.          | An early warning before a client-facing stockout occurs — Miguel needs this to manage client expectations.    |
| **Discrepancy Rate**         | The share of the week's outbound orders associated with a detected inventory discrepancy.                | The inventory-accuracy signal — flags which warehouse/client combinations need an audit.                     |

Everything below this point exists only to compute these four numbers correctly, reliably, and auditable.

---

## 3. Source data

Your source is `telemetry_events`, filtered to the mandatory metrics already defined in your telemetry CONTEXT:

| `event_type`                     | Feeds which KPI(s)                       |
| ------------------------------------ | ---------------------------------------------- |
| `inbound_order_created`            | Inbound Volume                                  |
| `outbound_order_created`           | Outbound Throughput, Discrepancy Rate (denominator) |
| `stock_threshold_triggered`        | Stockout Frequency                              |
| `inventory_discrepancy_detected`   | Discrepancy Rate (numerator)                    |

You don't need any event outside this list for v1 — resist the urge to widen scope.

---

## 4. Required aggregation

- **Grain:** one row per `warehouse` per `client_id` per ISO week (`week_start` = the Monday of that week, UTC).
- **Dimensions:** `warehouse` (`los_angeles`/`zaragoza`), `client_id`, `week_start`.
- **Computed fields per row (each maps directly to a KPI from section 2):**
  - `inbound_units_count` — Inbound Volume: sum of quantities from `inbound_order_created` for the week
  - `outbound_orders_count` — Outbound Throughput: count of `outbound_order_created` for the week
  - `stockout_events_count` — Stockout Frequency: count of `stock_threshold_triggered` for the week
  - `discrepancy_events_count` — supporting count of `inventory_discrepancy_detected` for the week
  - `discrepancy_rate` — Discrepancy Rate: `discrepancy_events_count / outbound_orders_count` (0 if no orders that week)

There is no currency dimension here — this deliverable is operational (volume and accuracy), not cost-based.

---

## 5. Destination table

Create this table under a dedicated `reporting` schema — never write into `telemetry_events`:

```sql
create table reporting.weekly_warehouse_client_performance (
  id uuid primary key default gen_random_uuid(),
  warehouse text not null,
  client_id text not null,
  week_start date not null,
  inbound_units_count integer not null default 0,
  outbound_orders_count integer not null default 0,
  stockout_events_count integer not null default 0,
  discrepancy_events_count integer not null default 0,
  discrepancy_rate numeric not null default 0,
  computed_at timestamptz not null default now(),
  unique (warehouse, client_id, week_start)
);
```

The `unique (warehouse, client_id, week_start)` constraint is what your idempotency strategy (upsert) should rely on.

---

## 6. New reporting endpoint

Expose this pipeline's output through a **new** module, `services/reporting/`, separate from `services/telemetry/`:

- `GET /reporting/weekly-warehouse-client-performance` — accepts optional `week_start` (defaults to the most recent computed week); returns all warehouse/client combinations for that week:

```json
{
  "week_start": "2026-07-13",
  "entries": [
    {
      "warehouse": "los_angeles",
      "client_id": "fashion-co",
      "inbound_units_count": 4200,
      "outbound_orders_count": 980,
      "stockout_events_count": 3,
      "discrepancy_events_count": 2,
      "discrepancy_rate": 0.002
    }
  ]
}
```

- `GET /reporting/pipeline-runs/latest` — status and metadata of the last pipeline run (this can be the same pattern you'll reuse for any future pipeline).
- `POST /reporting/pipeline-runs` — triggers a manual run.

---

## 7. Business constraints

- Each row belongs to a single client — never aggregate across clients within the same row.
- This pipeline reads `telemetry_events` **read-only**. It never writes back to it.
- `services/telemetry/analysis.py` and `GET /telemetry/report` are out of scope for this milestone — do not modify them.
