# Signal Yard — Agent Watch Board (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-milestone-real-time-agent-observability`. Same spine (Agent / Flow / Task, persist-then-SSE, named `agent_step` / `agent_status_changed`, JWT-style auth optional in demo, informational available-actions, traceable task chain). Different domain than company CONTEXT agents. Students still follow the full brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Signal Yard** is a fictional rail freight night desk. Two systems already run:

- `yard_desk` — a single conversational bot that answers shift questions (`chat_session`)
- `inbound_wave` — a multi-step inbound receiving workflow (`rail_wave`) with inspect → classify → assign → deliver

Tonight’s demo: a watch board that lists both agents, opens an agent detail (last flows + last tasks), lists waves, and reconstructs any `task_id` chain. **Look only** — do not implement pause/kill.

### Scope note

| Graded project (`ai-eng-milestone-real-time-agent-observability`) | This class example                               |
| ----------------------------------------------------------- | ------------------------------------------------ |
| Company monorepo + CONTEXT agents / `action_type`           | Signal Yard only                                 |
| Instrument real LangGraph / RFP pipeline                    | Stub runners that emit tasks                     |
| Full `uis/backoffice` + company JWT                         | One HTML/JS board; demo token OK                 |
| CONTEXT `needs_intervention` rules                          | Simple: stuck > 20s on `query` without `deliver` |
| Company PR + design questions                               | Live demo + 5 automated tests                    |

---

## Teaching spine (must hit live)

1. **Three entities** — Agent ≠ Flow ≠ Task
2. **Two architectures, one schema** — conversational + multi-step
3. **Persist first, then SSE** — kill the tab, reload, history still there
4. **Named events** — `agent_step`, `agent_status_changed` (not generic `message`)
5. **Task chain** — trigger, derived, prev, next reconstructible by `task_id`
6. **Informational actions only** — show `pause` as available; do not execute it
7. **Backoff reconnect** — drop stream → reconnect; no duplicate rows for same `task_id`

---

## Seed agents (indicative)

| `agent_id`     | Type           | `flow_type`    |
| -------------- | -------------- | -------------- |
| `yard_desk`    | Conversational | `chat_session` |
| `inbound_wave` | Multi-step     | `rail_wave`    |

Typical `action_type` on `rail_wave`: `query` → `tool_call` → `write` → `deliver`.

Sample SSE frames:

```text
event: agent_step
data: {"agent_id":"inbound_wave","flow_id":"wave_07","task_id":"task_21","action_type":"write"}

event: agent_status_changed
data: {"agent_id":"yard_desk","flow_id":"chat_03","status":"running"}
```

---

## What to build

### 1. Data + API

- [ ] Persist Agent, Flow, Task (trigger / derived / prev / next)
- [ ] `GET /agents`, `GET /agents/{id}` (include informational `available_actions`)
- [ ] `GET /agents/{id}/flows?limit=5`, `GET /agents/{id}/tasks?limit=10`
- [ ] `GET /flows`, `GET /flows/{id}`, `GET /tasks/{id}`, paginated `GET /log`
- [ ] `GET /events/stream` as `text/event-stream`

### 2. Stub runners (not a real LLM)

- [ ] `POST /demo/chat` starts a `chat_session` and emits 2–3 tasks
- [ ] `POST /demo/wave` starts a `rail_wave` with ≥3 tasks and at least one derived child
- [ ] Optional: delay a `query` > 20s so `needs_intervention` flips

### 3. Board UI

- [ ] Agent list with intervention flag
- [ ] Agent detail: last 5 flows nested, last 10 tasks flat
- [ ] Flow detail + task chain fields visible
- [ ] SSE updates list/detail; `fetch` + `ReadableStream`; backoff + dedupe

### 4. Tests

| #   | Scenario     | Expect                                                  |
| --- | ------------ | ------------------------------------------------------- |
| 1   | SSE frame    | `text/event-stream` + named `event:` + JSON `data`      |
| 2   | Agent list   | Both seed agents; `needs_intervention` boolean          |
| 3   | Flow detail  | All tasks in order for `wave_07` (or created id)        |
| 4   | Traceability | Given a middle `task_id`, prev/next/trigger/derived set |
| 5   | Pagination   | Two pages of log: no overlap, no gap                    |

---

## Demo script (live)

1. Open two board tabs
2. `POST /demo/wave` → both tabs update agent status; flow appears
3. Open a `task_id` → chain visible
4. Refresh → history still there
5. Kill network briefly → reconnect; same `task_id` not duplicated

---

## Out of scope for the example

- Pause / resume / kill (Part 2)
- Company CONTEXT companies (Brasaland, HealthCore, Nexova, TrackFlow)
- Real RFP PDF pipeline or RAG agent rewrite
