# Message Queues and Async Tasks — Reference Solution

This reference solution defines the expected quality bar for the async task queue in the student's company monorepo fork. The deliverable is a **producer/consumer architecture** — the API enqueues; a separate Celery worker consumes.

---

## Expected file layout

| Area              | Path (indicative)                            | Purpose                                              |
| ----------------- | -------------------------------------------- | ---------------------------------------------------- |
| Celery app        | `services/celery_app.py`                     | Celery instance, broker/backend config, task imports |
| Async tasks       | `services/tasks/` or `services/tasks.py`     | `@app.task` definitions with retry + timeout         |
| DLQ persistence   | `services/dlq.py` + migration                | Record exhausted tasks in database                   |
| Task status API   | `services/app/routers/tasks.py` (or similar) | `GET /tasks/{task_id}`                               |
| Modified endpoint | Existing slow route in student's API         | Returns `202` + `task_id` immediately                |
| Docker            | `docker-compose.yml`                         | `redis`, `flower`, optional `worker` service         |
| Env               | `.env` / compose env                         | `REDIS_URL=redis://redis:6379/0`                     |

---

## Architecture overview

```mermaid
flowchart LR
  subgraph client [Client]
    C[HTTP client]
  end
  subgraph api [FastAPI — Producer]
    EP[Heavy endpoint]
    TS[GET /tasks/task_id]
    EP -->|apply_async| BROKER
    TS -->|AsyncResult| BROKER
  end
  subgraph broker [Redis]
    BROKER[(Broker + Result backend)]
  end
  subgraph worker [Celery Worker — Consumer]
    W[celery worker process]
    T[@app.task]
    W --> T
    T --> DB[(App database)]
    T -->|on max_retries| DLQ[(dlq_tasks table)]
  end
  subgraph monitor [Observability]
    F[Flower :5555]
  end
  C -->|POST heavy op| EP
  C -->|poll status| TS
  BROKER --> W
  BROKER --> F
```

**Separation rule:** `celery -A services.celery_app worker` runs as its own process. It must not be started inside FastAPI's lifespan or on the main Uvicorn thread.

---

## Infrastructure — Docker Compose (indicative)

```yaml
services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --maxmemory-policy noeviction

  flower:
    image: mher/flower:2.0
    ports:
      - "5555:5555"
    environment:
      CELERY_BROKER_URL: redis://redis:6379/0
    depends_on:
      - redis

  # Optional: dedicated worker container
  worker:
    build: .
    command: celery -A services.celery_app worker --loglevel=info
    environment:
      REDIS_URL: redis://redis:6379/0
    depends_on:
      - redis
```

**Rules:**

- `noeviction` on Redis — queued messages must not be evicted under memory pressure.
- Do not share the same Redis DB index for cache and queue unless namespaces are isolated and eviction policy is safe.

---

## Celery module — expected configuration

```python
# services/celery_app.py (indicative)
import os
from celery import Celery

REDIS_URL = os.environ["REDIS_URL"]

celery_app = Celery(
    "company_api",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    task_track_started=True,
    task_time_limit=300,          # hard kill after 5 min
    task_soft_time_limit=240,
    result_expires=86400,
)
```

Import tasks so the worker discovers them:

```python
celery_app.autodiscover_tasks(["services.tasks"])
```

---

## Async task — retries, backoff, lightweight payload

```python
# services/tasks/report_tasks.py (indicative)
import logging
from celery import shared_task
from celery.exceptions import MaxRetriesExceededError
from services.celery_app import celery_app
from services.dlq import record_dlq_entry

logger = logging.getLogger(__name__)

@celery_app.task(
    bind=True,
    max_retries=3,
    default_retry_delay=10,  # base; overridden per retry with exponential backoff
)
def generate_report_task(self, report_id: str):
    """Heavy work — receives only report_id, not the full dataset."""
    started = time.monotonic()
    attempt = self.request.retries + 1
    try:
        # fetch report_id from DB, run slow aggregation...
        result = run_report_generation(report_id)
        duration_ms = int((time.monotonic() - started) * 1000)
        logger.info(
            "task_id=%s attempt=%s status=success duration_ms=%s",
            self.request.id, attempt, duration_ms,
        )
        return {"report_id": report_id, "rows": result}
    except Exception as exc:
        duration_ms = int((time.monotonic() - started) * 1000)
        logger.error(
            "task_id=%s attempt=%s status=failure duration_ms=%s error=%s",
            self.request.id, attempt, duration_ms, exc,
        )
        try:
            countdown = 10 * (2 ** self.request.retries)  # 10, 20, 40 seconds
            raise self.retry(exc=exc, countdown=countdown)
        except MaxRetriesExceededError:
            record_dlq_entry(
                task_id=self.request.id,
                attempt=attempt,
                error_message=str(exc),
            )
            raise
```

**Message payload rule:** pass `report_id`, `batch_id`, or `file_path` — never the full CSV, image bytes, or telemetry batch inline.

---

## Dead Letter Queue — data model

When `max_retries` is exhausted, persist an audit row:

| Column          | Type      | Notes                          |
| --------------- | --------- | ------------------------------ |
| `id`            | PK        | Auto-increment or UUID         |
| `task_id`       | string    | Celery task UUID               |
| `task_name`     | string    | e.g. `generate_report_task`    |
| `attempt`       | int       | Final attempt number (4th try) |
| `error_message` | text      | Last exception message         |
| `created_at`    | timestamp | When DLQ record was written    |

### Indicative migration (PostgreSQL)

```sql
CREATE TABLE dlq_tasks (
  id SERIAL PRIMARY KEY,
  task_id VARCHAR(64) NOT NULL UNIQUE,
  task_name VARCHAR(128) NOT NULL,
  attempt INT NOT NULL,
  error_message TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

`record_dlq_entry()` lives in `services/dlq.py` — called only from the task's `MaxRetriesExceededError` handler.

---

## API endpoints

### Modified heavy endpoint → `202 Accepted`

```python
# Before: synchronous, blocks for seconds
# After:
@router.post("/reports/{report_id}/generate")
def enqueue_report(report_id: str):
    task = generate_report_task.delay(report_id)  # lightweight ID only
    return JSONResponse(
        status_code=202,
        content={"task_id": task.id},
    )
```

**Latency target:** response in under 200ms — only enqueue + return, no heavy I/O.

### `GET /tasks/{task_id}`

Map Celery `AsyncResult` states to the project contract:

| Celery state | API `status` |
| ------------ | ------------ |
| `PENDING`    | `pending`    |
| `STARTED`    | `started`    |
| `SUCCESS`    | `success`    |
| `FAILURE`    | `failure`    |

```python
from celery.result import AsyncResult
from services.celery_app import celery_app

STATUS_MAP = {
    "PENDING": "pending",
    "STARTED": "started",
    "SUCCESS": "success",
    "FAILURE": "failure",
}

@router.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    result = AsyncResult(task_id, app=celery_app)
    status = STATUS_MAP.get(result.status, "pending")
    payload = {"task_id": task_id, "status": status, "result": None}
    if status == "success":
        payload["result"] = result.result
    elif status == "failure":
        payload["result"] = str(result.result)  # or error detail
    return payload
```

### Indicative response samples

**Enqueue:**

```json
HTTP/1.1 202 Accepted
{"task_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"}
```

**Polling lifecycle:**

```json
{"task_id": "a1b2...", "status": "pending", "result": null}
{"task_id": "a1b2...", "status": "started", "result": null}
{"task_id": "a1b2...", "status": "success", "result": {"report_id": "rpt_42", "rows": 1284}}
```

---

## Worker process

Start independently of FastAPI:

```bash
# Terminal 1 — API
uvicorn services.app.main:app --reload

# Terminal 2 — Worker
celery -A services.celery_app worker --loglevel=info

# Terminal 3 — Flower (or via docker-compose)
celery -A services.celery_app flower --port=5555
```

Document in monorepo README:

- How to start/stop the worker
- Required env vars (`REDIS_URL`)
- That stopping the API does not stop the worker or drain the queue

---

## Observability — log contract

Every task execution should log:

```
task_id=<uuid> attempt=<n> status=<success|failure> duration_ms=<ms>
```

On failure, add `error=<message>`.

Retry example:

```
2025-06-26T10:00:01Z ERROR task_id=abc123 attempt=1 status=failure duration_ms=1203 error=Connection refused
2025-06-26T10:00:11Z ERROR task_id=abc123 attempt=2 status=failure duration_ms=1198 error=Connection refused
2025-06-26T10:00:31Z INFO  task_id=abc123 attempt=3 status=success duration_ms=4521
```

Flower should show:

- At least one `SUCCESS` task
- At least one `FAILURE` task (or task that landed in DLQ after retries)

---

## Validation evidence

A complete submission should demonstrate:

1. `docker compose up redis flower` — Redis reachable on `6379`, Flower on `5555`
2. Modified endpoint returns `202` with `task_id` in under 200ms
3. `GET /tasks/{task_id}` shows correct status through `pending` → `started` → `success`
4. Forced failure triggers retries with increasing delay (not immediate back-to-back)
5. After 3 failures: row in `dlq_tasks` with `task_id`, `attempt`, `error_message`
6. Worker runs in separate terminal/container — API restart does not kill queued work
7. Task message contains only IDs/references (verify in Flower task args)
8. PR includes: endpoint choice + justification, Flower screenshot, retry log snippet, `async-tasks` label

---

## Common mistakes (incomplete submissions)

- Running Celery worker inside FastAPI `lifespan` or as a background thread
- Synchronous endpoint still blocks — returns `200` with full result instead of `202` + `task_id`
- No exponential backoff — retries fire immediately and hammer a failing dependency
- Large payload in task args (full JSON batch, file contents)
- No `task_time_limit` — zombie task blocks worker pool
- DLQ only in logs, not persisted to database
- Redis with `allkeys-lru` eviction — queued messages disappear under memory pressure
- Same Redis DB used for cache and queue without isolation
- `GET /tasks/{task_id}` returns raw Celery state names (`PENDING`) instead of contract values
- Flower not running or not demonstrated in PR

---

## Evaluation checklist

- [ ] Redis in Docker with `noeviction`, port `6379`
- [ ] Flower accessible on port `5555`
- [ ] `REDIS_URL` env var shared by API and worker
- [ ] Celery app with Redis broker + result backend
- [ ] At least one `@app.task` with `max_retries=3` and exponential backoff
- [ ] DLQ table + `record_dlq_entry` on exhausted retries
- [ ] Slowest endpoint converted to `202` + `task_id`
- [ ] `GET /tasks/{task_id}` with mapped status values
- [ ] Worker as separate process, documented in README
- [ ] Structured logs: `task_id`, attempt, status, duration
- [ ] Lightweight messages (IDs only)
- [ ] PR evidence: endpoint justification, Flower screenshot, retry log, `async-tasks` label

---

## Reviewer notes

- Which endpoint gets converted varies per company BRIEFING — grade against the student's justification, not a fixed route name.
- Task implementation details (report generation, batch processing, notification send) depend on prior milestones — evaluate queue mechanics, not business logic specifics.
- `mher/flower` vs `celery flower` both acceptable if monitoring works on `:5555`.
- DLQ can be a dedicated Celery queue **or** a database table — this project requires the **database record** with `task_id`, attempt, and error.
