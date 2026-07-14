# CONTEXT — HealthCore (Business Performance Pipeline)

## Data Pipeline Projects (Design · Implementation · Subflows & Tests)

<!-- hide -->

_Estas instrucciones están [disponibles en español](./CONTEXT-healthcore-pipeline.es.md)._

<!-- endhide -->

This file is self-contained: it gives you everything you need to scope, build, and test the business performance pipeline for HealthCore, without having to go hunting through other documents. It builds directly on the mandatory metrics already defined in your `CONTEXT-healthcore.md` (telemetry) — read that first if you haven't.

> ⚠️ **Regulatory note (HIPAA / UK GDPR):** this pipeline aggregates supply-chain data only. As with the telemetry system, no output of this pipeline may contain patient identifiers, diagnoses, or any real or simulated PHI — everything here is aggregated by `clinic` and `department`, never by patient.

---

## 1. The business deliverable

Dr. Okonkwo (CEO) wants a **monthly board-ready pack** she can review without her team spending two days consolidating spreadsheets — comparing supply cost and stockout risk across the network's 12 clinics, US and UK.

> **Target deliverable:** a monthly, per-clinic, per-country rollup of supply cost, stockout activity, and expiry risk — the "Monthly Clinic Supply Performance Report."

This is the **one concrete deliverable** your pipeline exists to produce. Everything in your `PIPELINE_DESIGN.md` should trace back to it.

**Audience:** Dr. Okonkwo (CEO) and Claire (Chief Compliance Officer) — non-technical stakeholders who need numbers, not raw events.
**Cadence:** monthly (ready by the first working day of the month, matching the existing "automated board reporting pack" expectation leadership already has).

---

## 2. KPIs to Measure

**These are the KPIs this pipeline exists to produce.** Everything else in this document — source events, aggregation logic, table schema — is implementation detail in service of these four numbers. If you're unsure what to build next, come back to this list.

| KPI                            | What it measures                                                                                     | Why it matters to HealthCore                                                                              |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------|
| **Supply Cost per Clinic**       | How much a clinic spent purchasing medical supplies during the month.                                    | Shows where spending concentrates across the network and feeds cross-clinic purchasing decisions.              |
| **Supply Consumption Volume**    | How many supply-consumption events a clinic recorded during the month, by department.                    | The operational-activity signal — helps distinguish a genuinely busy clinic from a data-capture gap.           |
| **Critical Stockout Frequency**  | How many times during the month a clinic ran below the minimum threshold for a supply.                   | A patient-safety and compliance risk signal Marcus and Claire need to act on quickly.                          |
| **Expiry Risk Count**           | How many supply batches at a clinic were flagged as approaching their expiry date during the month.       | A waste and compliance risk signal — flags supply that needs to be used or disposed of before it expires.      |

Everything below this point exists only to compute these four numbers correctly, reliably, and auditable.

---

## 3. Source data

> **A quick schema check first:** this pipeline needs a cost value on `inbound_order_created` (e.g. a `unit_cost` or `total_cost` field in `properties`) to compute supply cost. If your telemetry schema from the earlier milestone doesn't have one yet, add it now — it's a natural extension of an existing mandatory event, not a new event type. As always, this field describes a supply cost, never a patient.

Your source is `telemetry_events`, filtered to the mandatory metrics already defined in your telemetry CONTEXT:

| `event_type`                | Feeds which KPI(s)                     |
| -------------------------------- | --------------------------------------------- |
| `inbound_order_created`        | Supply Cost per Clinic                         |
| `outbound_order_created`       | Supply Consumption Volume                       |
| `stock_threshold_triggered`    | Critical Stockout Frequency                     |
| `supply_expiry_flagged`        | Expiry Risk Count                               |

You don't need any event outside this list for v1 — resist the urge to widen scope. In particular, do not join against any patient-level table.

---

## 4. Required aggregation

- **Grain:** one row per `clinic_id` per calendar month (`month_start` = the first day of the month, UTC).
- **Dimensions:** `clinic_id`, `country` (`US`/`UK`), `month_start`.
- **Computed fields per row (each maps directly to a KPI from section 2):**
  - `total_supply_cost` — Supply Cost per Clinic: sum of `inbound_order_created` costs for the month
  - `supply_consumption_count` — Supply Consumption Volume: count of `outbound_order_created` for the month
  - `critical_stockout_count` — Critical Stockout Frequency: count of `stock_threshold_triggered` for the month
  - `expiry_risk_count` — Expiry Risk Count: count of `supply_expiry_flagged` for the month
  - `currency` — `USD` or `GBP`, matching the clinic's country. **Do not convert currencies in this pipeline** — that is a v2 concern once you have an FX rate source.

---

## 5. Destination table

Create this table under a dedicated `reporting` schema — never write into `telemetry_events`:

```sql
create table reporting.monthly_clinic_supply_performance (
  id uuid primary key default gen_random_uuid(),
  clinic_id text not null,
  country text not null,
  month_start date not null,
  total_supply_cost numeric not null default 0,
  supply_consumption_count integer not null default 0,
  critical_stockout_count integer not null default 0,
  expiry_risk_count integer not null default 0,
  currency text not null,
  computed_at timestamptz not null default now(),
  unique (clinic_id, month_start)
);
```

The `unique (clinic_id, month_start)` constraint is what your idempotency strategy (upsert) should rely on.

---

## 6. New reporting endpoint

Expose this pipeline's output through a **new** module, `services/reporting/`, separate from `services/telemetry/`:

- `GET /reporting/monthly-clinic-supply-performance` — accepts optional `month_start` (defaults to the most recent computed month); returns all clinics for that month:

```json
{
  "month_start": "2026-07-01",
  "clinics": [
    {
      "clinic_id": "austin-north",
      "country": "US",
      "total_supply_cost": 18420.50,
      "supply_consumption_count": 340,
      "critical_stockout_count": 1,
      "expiry_risk_count": 4,
      "currency": "USD"
    }
  ]
}
```

- `GET /reporting/pipeline-runs/latest` — status and metadata of the last pipeline run (this can be the same pattern you'll reuse for any future pipeline).
- `POST /reporting/pipeline-runs` — triggers a manual run.

---

## 7. Business constraints

- No field in this pipeline's output — table, endpoint response, or log — may ever contain a patient identifier, diagnosis, or any real or simulated PHI. Aggregation stays at the `clinic`/`department` level.
- Never mix currencies in a single aggregate row — `USD` (US clinics) and `GBP` (UK clinics) are reported separately, side by side, not summed together.
- This pipeline reads `telemetry_events` **read-only**. It never writes back to it.
- `services/telemetry/analysis.py` and `GET /telemetry/report` are out of scope for this milestone — do not modify them.
