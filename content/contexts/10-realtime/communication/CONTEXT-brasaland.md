# CONTEXT — Brasaland: Real-Time Systems (Part 2)

> It assumes your existing support agent is already working — this isn't a redesign of that agent, just changing the channel it talks to the user through.

## 1. Introduction

The request comes from **Felipe Guerrero's** team, Operations — the same area that owns the Manager support agent used by location managers across Brasaland's sites. Today a manager sends a question, waits, and gets the full answer in one shot. If the agent drifts (wrong location, wrong supplier schedule), they can't correct it until the reply finishes. Felipe turned that into a ticket: make the conversation feel live — tokens as they are generated, and the ability to interrupt mid-response and redirect without reloading or starting from scratch. The people who will use what you build are the **location managers** chatting with that agent.

## 2. Which Agent You're Connecting

The agent you're exposing over WebSocket is the **Manager support agent**: the one that answers frequent operational questions from location managers in the selected base language. Don't change its logic or its tools — only the channel it talks to the user through.

## 3. Chat Session Entity

- **ChatSession**: `session_id`, `agent_id` (`manager_support`), `user_id` (the location manager chatting), `location_id`, `status` (`active`, `interrupted`, `closed`), `created_at`

Use `session_id` (and the same value as LangGraph `thread_id` if you checkpoint) on the WebSocket handshake so a reconnect can rehydrate the conversation.

Authenticate the WebSocket with the **same JWT** as the backoffice API (and Part 1 SSE). Prefer `?token=` on the URL and/or a first client auth frame — reject before chat events if missing or invalid.

## 4. Suggested Events Over the WebSocket

Use explicit event names and structured payloads (same naming discipline as Part 1 — not the same RFP/SSE schemas):

```json
{"event": "token_chunk", "data": {"session_id": "chat_0044", "token": "For", "sequence": 12}}
{"event": "interrupt_requested", "data": {"session_id": "chat_0044", "new_input": "wait, I asked about the Miami location"}}
{"event": "generation_interrupted", "data": {"session_id": "chat_0044", "message_id": "msg_0090", "status": "interrupted"}}
{"event": "generation_completed", "data": {"session_id": "chat_0044", "message_id": "msg_0091"}}
{"event": "session_snapshot", "data": {"session_id": "chat_0044", "messages": []}}
{"event": "user_message", "data": {"session_id": "chat_0044", "text": "..."}}

```

Also support reconnect rehydrate (`session_snapshot`) and inbound user turns (`user_message`) — required for handshake restore and chat input.

## 5. Pub/Sub Pattern

Use one channel per session (for example, `chat.<session_id>`) so the producer (the agent generating tokens) stays decoupled from the consumers (subscribed WebSocket connections). Redis isn't required for this deliverable — an in-memory mechanism is acceptable if your implementation runs in a single process.

## 6. Constraints

- Field and entity names for the chat session must match this CONTEXT — don't invent parallel ids for the same session.
- Do not mix Part 1 RFP ticket notification payloads into the WebSocket chat contract.
