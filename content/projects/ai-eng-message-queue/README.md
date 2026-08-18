# Message Queues and Async Tasks

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

---

## 🎯 Your challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

Your company has a production API and a working data pipeline. But some operations still block the request-response cycle: processing a batch of records, generating a report, sending bulk notifications. While those operations run, the API cannot respond to other users. Your tech lead has filed the following ticket:

> > **Ticket #DEV-55 — Async Task Queue with Redis and Celery**
> >
> > We need to decouple heavy operations from the API. When an endpoint receives a request that involves long-running work, it must enqueue the task and immediately return a `task_id` to the client. An independent worker processes the queue. The client can check the status of their task at any time.
> >
> > **Acceptance criteria:**
> >
> > - Redis runs as a broker in Docker. The API and workers connect to the same broker.
> > - At least one existing operation in your API — the slowest one — is converted into an async task via Celery.
> > - The endpoint that receives the request returns `202 Accepted` with a `task_id` immediately, without waiting for the task to finish.
> > - A `GET /tasks/{task_id}` endpoint exists that returns the current task status (`pending`, `started`, `success`, `failure`) and the result when available.
> > - If a task fails three times, it moves to a Dead Letter Queue (DLQ). The failure is recorded with `task_id`, attempt number, and error message.
> > - Workers run as separate processes, not inside the FastAPI process.
> > - Flower is running and accessible for monitoring the queue during development.

### 📚 Complementary Knowledge — The Producer / Consumer Pattern

The key conceptual shift in this project is understanding that **enqueueing a task and executing a task are the responsibilities of two separate processes**.

```
Client → API (Producer) → Redis (Broker) → Worker (Consumer) → Result
```

- **Producer**: the API receives the request, creates a message, and deposits it in the queue. Returns immediately.
- **Broker**: Redis acts as a persistent intermediary. If the worker goes down, messages are not lost.
- **Consumer (Worker)**: an independent process that listens to the queue, picks up messages one at a time, and processes them.

Three rules that always apply in this pattern:

1. **Keep messages lightweight.** Never put a full blob (image, document, data batch) in the message. Pass the `id` or the path — the worker fetches it itself.
2. **ACK only after success.** The message is confirmed as processed only when the worker finishes successfully. If the worker fails first, the message goes back to the queue for retry.
3. **Every task has a timeout.** A worker that never finishes blocks the pool. Always define a maximum execution time.

---

## 🌱 How to Start the Project

1. Add Redis to your `docker-compose.yml` as a broker service. Use the official image and expose it on the standard port.
2. Install the required dependencies with `uv add celery redis flower`.
3. Create the Celery module in your monorepo (`services/celery_app.py` or similar) and configure it to point to Redis as both broker and result backend.
4. Identify the endpoint or operation in your API that takes the longest to respond — that is the candidate to convert into an async task.
5. Start a worker with `celery -A services.celery_app worker` and verify it connects to the broker before modifying any endpoint.

---

## 💻 What You Need to Do

### Infrastructure

- [ ] Redis added to `docker-compose.yml` with the official image, port `6379` exposed, and `noeviction` memory policy.
- [ ] Flower added to `docker-compose.yml` as a monitoring service, accessible on port `5555`.
- [ ] The API and workers connect to the same Redis instance. The connection URL is read from an environment variable (`REDIS_URL`).

### Celery module (`services/`)

- [ ] Create the Celery instance with Redis as both broker and result backend.
- [ ] Define at least one async task (`@app.task`) encapsulating the heavy operation identified in your API.
- [ ] Configure automatic retries with `max_retries=3` and exponential backoff (increasing `countdown` between attempts).
- [ ] Implement a Dead Letter Queue: when a task exceeds `max_retries`, record in the database the `task_id`, attempt number, error, and timestamp.

### API endpoints

- [ ] The endpoint that previously executed the heavy operation now enqueues the task and returns `202 Accepted` with `{"task_id": "..."}` immediately.
- [ ] Create the `GET /tasks/{task_id}` endpoint that queries the task status in Redis and returns `{"task_id": "...", "status": "...", "result": ...}`.
- [ ] The `status` field reflects the actual Celery states: `pending`, `started`, `success`, `failure`.

### Worker

- [ ] The worker runs as an independent process (not inside the FastAPI process).
- [ ] The worker is documented in the monorepo README: how to start it, how to stop it.

### Observability

- [ ] Each task logs: `task_id`, attempt, resulting status, and execution duration.
- [ ] Failures additionally log the full error message.
- [ ] Flower is accessible and shows queued, in-progress, and completed tasks.

---

## ✅ What We Will Evaluate

- [ ] Redis runs in Docker and workers connect to it without configuration errors.
- [ ] The modified endpoint returns `202 Accepted` with `task_id` in under 200ms, regardless of the task duration.
- [ ] `GET /tasks/{task_id}` returns the correct status at each phase of the task lifecycle.
- [ ] Automatic retries are configured with backoff: no immediate retry after a failure.
- [ ] After three consecutive failures, the task appears in the DLQ with `task_id`, attempt number, and error message recorded in the database.
- [ ] The worker is a separate process: stopping the API does not stop the worker or lose queued messages.
- [ ] Messages in the queue contain only identifiers or references — no large data payloads.
- [ ] Flower is running and shows at least one completed task and one failed task during the demonstration.

---

## 📦 How to Submit

1. Make sure all checklist items are completed.
2. Push your branch to the repository.
3. Open a **Pull Request** from your branch to `main`.
4. In the PR body include:
   - The endpoint selected for conversion to an async task and the justification for that choice.
   - A screenshot of Flower showing at least one completed task and one in the DLQ.
   - A log snippet of an execution with a retry.
5. Add the `async-tasks` label to the PR before submitting it for review.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
