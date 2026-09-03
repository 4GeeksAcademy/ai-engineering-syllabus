# Signal Yard — Operator Kill Switch (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-milestone-real-time-agent-control`. Same spine (pause ≠ cancel, checkpoint/hold resume, WebSocket commands, pub/sub fan-out, JWT-derived `actor_id` audit). Builds on the Part 1 Signal Yard watch board. Students still follow the full brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

Part 1's **Signal Yard** board already shows `yard_desk` and `inbound_wave` with informational available-actions. Tonight: those buttons **work**. An operator pauses a stuck wave without restarting the whole desk process; resume continues from the last stub checkpoint; cancel is final. Two open boards must update when either fires a command.

### Scope note

| Graded project (`ai-eng-milestone-real-time-agent-control`) | This class example                         |
| ----------------------------------------------------------- | ------------------------------------------ |
| Company monorepo + Part 1 observability panel               | Signal Yard only                           |
| Real LangGraph checkpointer reuse                           | In-memory stub checkpoint dict             |
| Company JWT + eng/ops roles                                 | Demo token → fixed `actor_id`              |
| CONTEXT cascade of pending department tasks                 | Mark child tasks `cancelled` in stub store |
| Company PR + design questions                               | Live demo + 6 automated tests              |

---

## Teaching spine (must hit live)

1. **Pause ≠ cancel** — different statuses and guarantees
2. **Resume from hold/checkpoint** — not from step 0
3. **WebSocket commands** — `pause` / `resume` / `cancel` with named replies
4. **Pub/sub** — two tabs, one command, both update
5. **Audit** — Task history shows action + `actor_id` + time
6. **Invalid transitions rejected** — resume while `running` fails loud
7. **Reconnect** — refetch agent status, then resubscribe

---

## Seed (indicative)

| `agent_id`     | Pause means                          | Cancel means                            |
| -------------- | ------------------------------------ | --------------------------------------- |
| `yard_desk`    | Hold chat generation                 | Close session                           |
| `inbound_wave` | Save stub checkpoint at current step | Terminal; pending child tasks cancelled |

```json
{"command": "pause", "data": {"agent_id": "inbound_wave", "flow_id": "wave_07"}}
{"event": "control_applied", "data": {"agent_id": "inbound_wave", "flow_id": "wave_07", "action": "pause", "actor_id": "demo_op", "timestamp": "2026-03-12T09:41:17Z"}}
```

---

## What to build

### 1. Control API / WS

- [ ] WebSocket endpoint accepting commands; reject bad transitions
- [ ] Stub checkpoint on `inbound_wave` pause; resume reads it
- [ ] Cancel marks flow + pending children; later resume rejected
- [ ] Broadcast `control_applied` to all subscribers

### 2. Board UI

- [ ] Enable/disable pause / resume / cancel from status
- [ ] Apply remote `control_applied` without reload
- [ ] Show control rows in task history

### 3. Tests

| #   | Scenario           | Expect                                  |
| --- | ------------------ | --------------------------------------- |
| 1   | Pause wave         | Status `paused`; checkpoint key present |
| 2   | Resume             | Continues after checkpoint step         |
| 3   | Cancel then resume | Resume rejected                         |
| 4   | Invalid transition | Error, status unchanged                 |
| 5   | Two WS clients     | Both receive `control_applied`          |
| 6   | Audit              | History has `actor_id`                  |

---

## Demo script (live)

1. Start a `rail_wave` from Part 1 stubs
2. Open two boards → pause from tab A → tab B updates
3. Resume → wave continues
4. Cancel another wave → resume fails
5. Disconnect WS → reconnect → status matches server

---

## Out of scope for the example

- Real LangGraph / RFP HITL approval wiring
- Company CONTEXT companies
- Token streaming chat WebSocket (post-grad communication project)
