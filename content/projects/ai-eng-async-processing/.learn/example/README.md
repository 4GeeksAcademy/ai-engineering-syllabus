# Photo Booth Prints — Async SMS Confirmations (Class Example)

> **For instructors:** Not the student project. Same spine as `ai-eng-async-processing`: enqueue off request cycle, worker, exponential backoff, DLQ, idempotency key, queryable status. Domain = event photo booth sending SMS when print ready.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

Photo booth API today calls SMS gateway inside `POST /sessions/{id}/notify`. Gateway blips → customer never gets "your print is ready" and request times out. Move notify to queue; user gets instant 202.

### Scope note

One session, one endpoint, mocked SMS provider. Redis + RQ or Celery OK. Skip Flower and full monorepo. Students follow full brief in root `README.md`.

---

## What to build

### Queue + worker

- [ ] `POST /sessions/{id}/notify` → 202 + `task_id`
- [ ] Worker sends SMS via stub `SmsGateway.send(phone, message)`
- [ ] Worker process separate from API

### Resilience

- [ ] Max 3 retries, exponential backoff (e.g. 2s, 4s, 8s)
- [ ] Failed tasks → DLQ list/table with `task_id`, `error`, `attempts`

### Idempotency

- [ ] Header `Idempotency-Key: session-{id}-notify`
- [ ] Second enqueue same key → same `task_id`, gateway called once

### Status

- [ ] `GET /tasks/{task_id}` → `pending` | `in_progress` | `completed` | `failed`, `retry_count`

---

## Verify together

- [ ] Happy path: notify → poll → `completed`
- [ ] Stub fails 2 times then succeeds → `retry_count: 2`
- [ ] Stub always fails → DLQ + `failed`
- [ ] Duplicate POST same key → provider mock `call_count == 1`

---

## Discussion questions

1. Why 202 beats blocking until SMS gateway responds?
2. When retry succeeds on provider but ACK lost, how does idempotency key save you?
3. Who monitors DLQ in production — and what alert fires?
