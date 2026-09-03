# CONTEXT — Nexova: Real-Time Systems (Part 2)

> It assumes your existing support agent is already working — this isn't a redesign of that agent, just changing the channel it talks to the user through.

## 1. Introduction

The request comes from **Roberto Díaz's** Customer Support area — the team that runs the first-line support agent for Nexova's outsourcing clients. Today an end customer of those clients sends a message, waits, and gets the full answer in one shot. If the agent is answering the wrong topic (invoice vs another issue), they can't correct course until the reply finishes. Roberto turned that into a ticket: stream tokens in real time and let the user interrupt mid-response so support feels like a live conversation, not a batch reply. The people who will use what you build are those **clients** chatting with the first-line support agent.

## 2. Which Agent You're Connecting

The agent you're exposing over WebSocket is the **first-line support agent** from Roberto Díaz's Customer Support area: the one that currently resolves queries from Nexova's outsourcing clients. Don't change its logic or its tools — only the channel it talks to the user through.

## 3. Chat Session Entity

- **ChatSession**: `session_id`, `agent_id` (`first_line_support`), `user_id` (the client chatting), `client_id`, `status` (`active`, `interrupted`, `closed`), `created_at`

Use `session_id` (and the same value as LangGraph `thread_id` if you checkpoint) on the WebSocket handshake so a reconnect can rehydrate the conversation.

Authenticate the WebSocket with the **same JWT** as the backoffice API (and Part 1 SSE). Prefer `?token=` on the URL and/or a first client auth frame — reject before chat events if missing or invalid.

## 4. Suggested Events Over the WebSocket

Use explicit event names and structured payloads (same naming discipline as Part 1 — not the same RFP/SSE schemas):

```json
{"event": "token_chunk", "data": {"session_id": "chat_0157", "token": "Sure", "sequence": 4}}
{"event": "interrupt_requested", "data": {"session_id": "chat_0157", "new_input": "actually my question was about the invoice"}}
{"event": "generation_interrupted", "data": {"session_id": "chat_0157", "message_id": "msg_0321", "status": "interrupted"}}
{"event": "generation_completed", "data": {"session_id": "chat_0157", "message_id": "msg_0322"}}
{"event": "session_snapshot", "data": {"session_id": "chat_0157", "messages": []}}
{"event": "user_message", "data": {"session_id": "chat_0157", "text": "..."}}

```

Also support reconnect rehydrate (`session_snapshot`) and inbound user turns (`user_message`) — required for handshake restore and chat input.

## 5. Pub/Sub Pattern

Use one channel per session (for example, `chat.<session_id>`) so the producer (the agent generating tokens) stays decoupled from the consumers (subscribed WebSocket connections). Redis isn't required for this deliverable — an in-memory mechanism is acceptable if your implementation runs in a single process.

## 6. Constraints

- Field and entity names for the chat session must match this CONTEXT — don't invent parallel ids for the same session.
- Do not mix Part 1 RFP ticket notification payloads into the WebSocket chat contract.
