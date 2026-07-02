# GreenPatch Co-op — Telemetry Pipeline Design (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-milestone-data-pipeline-design`. Same spine (current state, ETL purpose, data flow diagram, update/dedup strategy, idempotency, execution log, Prefect mapping), different domain. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**GreenPatch Co-op** runs a tool-lending app for community gardens. You already capture four telemetry events (`reservation_created`, `checkout_validation_failed`, `tool_threshold_low`, `login_failed`) into a Postgres table and generate weekly Pandas CSVs for utilization and abandonment rates. Ops wants a production pipeline before dashboard launch — design only, no Prefect code yet.

In one session, draft a **mini `data/PIPELINE_DESIGN.md`** — no code.

### Scope note

| Graded project (`ai-eng-milestone-data-pipeline-design`) | This class example                       |
| -------------------------------------------------------- | ---------------------------------------- |
| Company monorepo                                         | Fictional GreenPatch scenario (below)    |
| Full CTO brief + Prefect mapping                         | Same section headings, smaller narrative |
| Commit to student monorepo                               | Local markdown only                      |

---

## Scenario data

**Telemetry already captured:**

| Event                        | Storage                   |
| ---------------------------- | ------------------------- |
| `reservation_created`        | `public.telemetry_events` |
| `checkout_validation_failed` | `public.telemetry_events` |
| `tool_threshold_low`         | `public.telemetry_events` |
| `login_failed`               | `public.telemetry_events` |

**Existing reports:** Pandas notebook exports `weekly_utilization.csv` and `reservation_abandonment.csv`.

**KPIs:** tool utilization rate, reservation abandonment rate, return compliance.

**Entities:** `Tool`, `Reservation`, `Checkout`, `Member`.

---

## What to build

Create `data/PIPELINE_DESIGN.md` (throwaway folder or demo repo) with these sections:

### 1. Current State

- [ ] List the four events, where they live, and which Pandas reports exist.
- [ ] Name at least two limitations (no run log, full-table scan, no idempotent re-run, etc.).

### 2. Purpose

- [ ] One sentence: what business problem the pipeline solves for GreenPatch ops.

### 3. Extraction format

- [ ] Source table, JSON envelope format, nightly batch cadence.

### 4. Data flow diagram

- [ ] Mermaid or ASCII: extract → transform → load with real table names (`telemetry_events`, `reporting.daily_tool_metrics`).

### 5. Update / dedup strategy

- [ ] How to skip already-processed `eventId` values.
- [ ] How to upsert daily aggregates when late events arrive.

### 6. Idempotency plan

- [ ] Failure mid-load and safe retry (watermark, staging, transactional upsert).
- [ ] Explain second-run behavior — not just "re-run."

### 7. Execution log (minimum five fields)

| Field                             | Why it matters         |
| --------------------------------- | ---------------------- |
| `run_id`                          | Trace one execution    |
| `watermark_from` / `watermark_to` | Audit processed window |
| `rows_extracted`                  | Detect empty batches   |
| `status`                          | Alerting               |

Add at least one more field with type and justification.

### 8. Prefect mapping

- [ ] Name ≥2 flows (e.g. nightly ETL + backfill).
- [ ] Name ≥3 tasks aligned with ETL stages.
- [ ] List relevant states and at least one block (e.g. Supabase credentials).

---

## Verify together

- [ ] Current State references real events from the scenario data — not generic placeholders.
- [ ] Diagram shows three ETL stages with table names.
- [ ] Idempotency describes concrete second-run behavior.
- [ ] Prefect names map to pipeline stages, not abstract concepts only.
- [ ] No Python/Prefect implementation files — design doc only.

---

## Discussion questions

1. Why is a watermark better than reading the full `telemetry_events` table every night?
2. What breaks if you advance the watermark before the load transaction commits?
3. Which GreenPatch event fits a stream path vs batch path in a future implementation — and does that affect the design doc?
