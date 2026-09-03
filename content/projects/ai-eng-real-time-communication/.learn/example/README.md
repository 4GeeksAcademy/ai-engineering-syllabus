# Lighthouse Desk — Streaming Help Chat (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-real-time-communication`. Same spine (WebSocket, token stream, true interrupt, pub/sub per session, backoff reconnect). Different domain than company CONTEXT agents. Students still follow the full brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Lighthouse Desk** is a tiny marina help bot. Today the clerk types a question, waits, and gets the whole answer at once — if the bot drifts off-topic, they wait until it finishes. Tonight’s demo: answers appear **token by token**, and the clerk can **interrupt mid-reply** with a correction. A second “supervisor” tab watching the same session sees the same stream without calling the bot twice.

### Scope note

| Graded project (`ai-eng-real-time-communication`) | This class example                                      |
| ----------------------------------------------------------- | ------------------------------------------------------- |
| Company monorepo + existing support agent                   | Stub “bot” that yields fake tokens (or a tiny LLM call) |
| Stream abort (cancel task); HITL `interrupt()` optional     | `asyncio` cancel + new turn with new prompt             |
| Full company chat UI                                        | Single HTML/JS page + optional second tab               |
| CONTEXT `ChatSession` / agent_id fidelity                   | Fixed demo: `session_id`, `status`                      |
| Company PR + design questions                               | Live demo + 2 automated tests                           |

---

## Teaching spine (must hit live)

1. **Why WebSocket** — client must send while server still streaming (SSE insufficient)
2. **Token events** — named `token_chunk`, not one blob at the end
3. **Pub/sub** — one producer, many WS consumers on `chat.<session_id>`
4. **True abort** — cancel generation task (no more tokens); keep partial as `interrupted`; next reply = new turn with `new_input`
5. **Live typing UI** — append tokens as they arrive
6. **Reconnect + rehydrate** — drop socket → same `session_id` → restore history, not empty chat
7. **Do not rebuild the “agent”** — only the channel (stub bot OK for class)

---

## Seed events (indicative)

```json
{"event": "token_chunk", "data": {"session_id": "chat_demo_1", "token": "Slip ", "sequence": 1}}
{"event": "interrupt_requested", "data": {"session_id": "chat_demo_1", "new_input": "I meant slip B-17, not A-3"}}
{"event": "generation_interrupted", "data": {"session_id": "chat_demo_1", "message_id": "msg_00", "status": "interrupted"}}
{"event": "generation_completed", "data": {"session_id": "chat_demo_1", "message_id": "msg_01"}}
```

---

## What to build

### 1. Backend

- [ ] `WS /ws/chat/{session_id}` — accept, subscribe to in-memory bus
- [ ] On `user_message`: start token producer; publish `token_chunk` frames
- [ ] On `interrupt_requested`: stop producer; start new generation with `new_input`
- [ ] Unit test: event contract for token / interrupt / completed

### 2. Frontend

- [ ] Connect WebSocket; append tokens into the assistant bubble
- [ ] Send interrupt when user submits while streaming
- [ ] Progressive backoff reconnect on drop

### 3. Demo script (live)

1. Open clerk tab + supervisor tab on same `session_id`
2. Ask a long question → both see tokens stream
3. Interrupt mid-stream with a correction → both see stop + new answer
4. Kill network briefly → reconnect resumes session

---

## Out of scope for the example

- Company RFP SSE (Part 1 graded project)
- Real LangGraph company agent / MCP tools
- Redis backplane (in-memory pub/sub is enough)
