# GreenPatch Co-op — Resilient Telemetry Pipeline (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-milestone-data-pipeline-build`. Same spine (Prefect flows/tasks, retries, caching, idempotency, script execution, API endpoints), different domain. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**GreenPatch Co-op** runs a tool-lending app for community gardens. Yesterday you approved a design doc for a nightly telemetry ETL. Today you implement it with Prefect in a throwaway demo repo or local folder — not the graded company monorepo.

Starting spec: the mini design below replaces `PIPELINE_DESIGN.md`.

### Scope note

| Graded project (`ai-eng-milestone-data-pipeline-build`) | This class example                   |
| ------------------------------------------------------- | ------------------------------------ |
| Company CONTEXT + inventory monorepo                    | Fictional GreenPatch CONTEXT (below) |
| Full CTO ticket + script execution                      | Same phases, smaller dataset         |
| Commit to student monorepo fork                         | Local demo only                      |

---

## Mini design (use instead of PIPELINE_DESIGN.md)

**Source:** `public.telemetry_events` — events `reservation_created`, `checkout_validation_failed`, `tool_threshold_low`, `login_failed`.

**Destination:** `reporting.daily_tool_metrics` with grain `(report_date, tool_id)`.

**Idempotency:** upsert on `(report_date, tool_id)`.

**Optional step:** export `data/eval/latest_run.json` snapshot — failure must not stop load.

**Schedule:** nightly cron `0 3 * * *` UTC (comment: low traffic after midnight).

---

## What to build

Create `data/pipelines/pipeline.py` with:

### Phase 1 — Flows and tasks

- [ ] `@flow` `greenpatch_telemetry_etl_flow` with tasks: extract → transform → load.
- [ ] Optional `@task` `export_eval_snapshot` invoked with `return_state=True`.

### Phase 2 — Resilience

- [ ] `retries=2` on extract (DB) with comment.
- [ ] One task failure handled explicitly in the flow with `return_state=True`.
- [ ] Cached transform with `cache_expiration=timedelta(hours=1)` and comment on cache key.

### Phase 3 — Idempotency

- [ ] Load upserts — second run same date range = same row count.
- [ ] Log run metadata (start, end, records, status, errors) to `data/eval/pipeline_runs.jsonl`.

### Phase 4 — Script execution

- [ ] Add `if __name__ == "__main__"` block that invokes the main flow.
- [ ] Verify `python data/pipelines/pipeline.py` runs without errors.

### Phase 5 — API stub (optional in class)

- [ ] Two FastAPI routes or plain functions simulating `GET /pipeline/runs/latest` and `POST /pipeline/runs` importing from `pipeline.py`.

---

## Verify together

- [ ] Three+ tasks, not one big script.
- [ ] Optional task failure does not abort main flow.
- [ ] Second run over same window produces no duplicate metrics rows.
- [ ] Run log has ≥5 fields per execution.
- [ ] Names reference GreenPatch tables/events — not generic placeholders.

---

## Discussion questions

1. Why cache the transform task but not the extract task?
2. What happens if `export_eval_snapshot` fails but load succeeded — should status be `success` or `partial`?
3. How would you change the design if GreenPatch needed hourly instead of nightly runs?
