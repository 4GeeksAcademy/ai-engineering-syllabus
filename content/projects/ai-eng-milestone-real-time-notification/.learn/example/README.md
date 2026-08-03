# Harbor Desk — Live Ticket Board (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-milestone-real-time-notification`. Same spine (SSE named event, structured payload, keep-alive, `fetch` + `ReadableStream`, progressive backoff reconnect). Different domain than company CONTEXT agents. Students still follow the full brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Harbor Desk** is a marina operations board. Slip bookings and maintenance tickets are already created via a tiny HTTP API — but the wall display only updates when someone hits refresh. Tonight’s demo: when a new **maintenance ticket** is registered, every open board pushes a live notification without a full reload. If Wi‑Fi blips, the board reconnects on its own.

### Scope note

| Graded project (`ai-eng-milestone-real-time-notification`) | This class example                                        |
| ---------------------------------------------------------- | --------------------------------------------------------- |
| Company monorepo + RFP ticket from CONTEXT                 | Harbor Desk marina board only                             |
| Hook into existing RFP registration path                   | Stub `POST /tickets` that publishes the event             |
| Full company dashboard refactor                            | Single HTML/JS board page                                 |
| CONTEXT field fidelity (client, location, service_type, …) | Fixed demo fields: `ticket_id`, `slip`, `issue`, `status` |
| Company PR + design questions                              | Live demo + 2 automated tests                             |

---

## Teaching spine (must hit live)

1. **Publish on create** — registering a ticket emits an event (no polling cron)
2. **Named SSE event** — `event: maintenance_ticket_created` (not generic `message`)
3. **Structured JSON payload** — at least id + initial status
4. **Keep-alive** — comment frames so the stream stays open
5. **Client = `fetch` + `ReadableStream`** — parse frames in a loop
6. **Backoff reconnect** — drop network → reconnect without duplicate toasts for same id
7. **No model/agent** — pure communication layer

---

## Seed payload (indicative)

```json
{
  "ticket_id": "mnt_0042",
  "slip": "B-17",
  "issue": "pump_out_clogged",
  "status": "open",
  "created_at": "2026-07-24T18:05:00Z"
}
```

Wire frame:

```text
event: maintenance_ticket_created
data: {"ticket_id":"mnt_0042","slip":"B-17","issue":"pump_out_clogged","status":"open","created_at":"2026-07-24T18:05:00Z"}
```

---

## What to build

### 1. Backend

- [ ] `POST /tickets` creates a ticket with `status: open` and publishes to an in-process bus
- [ ] `GET /events/stream` returns `text/event-stream` with named events + keep-alive
- [ ] Unit test: published payload includes `ticket_id` and `status`

### 2. Frontend board

- [ ] Open stream with `fetch` + `ReadableStream`
- [ ] Show a visually distinct card/toast when `maintenance_ticket_created` arrives
- [ ] On disconnect: progressive backoff reconnect; skip already-seen `ticket_id`s

### 3. Demo script (live)

1. Open two browser tabs on the board
2. `POST` a new ticket → both tabs show the notification
3. Kill network briefly → reconnect resumes; same ticket does not toast twice

---

## Out of scope for the example

- WebSockets / bidirectional chat (Part 2)
- LLM agents, RAG, or RFP pipelines
- Company CONTEXT companies (Brasaland, HealthCore, …)
