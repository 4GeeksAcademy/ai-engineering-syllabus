# CONTEXT — TrackFlow: Real-Time Systems (Part 2)

> It assumes your existing support agent is already working — this isn't a redesign of that agent, just changing the channel it talks to the user through.

## 1. Introduction

The request comes from **Valentina Cruz's** area, Customer Experience — the team that runs the first-line CX agent for tracking, returns, and frequent questions. Today a client sends a message, waits, and gets the full answer in one shot. If the agent is answering the wrong intent (tracking when they meant a return), they can't redirect it until the reply finishes. Valentina turned that into a ticket: stream the answer token by token and let the client interrupt mid-response so the chat feels like a real conversation. The people who will use what you build are the **clients** (B2B brands and B2C parcel recipients) chatting with that agent.

## 2. Which Agent You're Connecting

The agent you're exposing over WebSocket is the **First-line CX agent** from Valentina Cruz's area: the one that currently resolves tracking queries, return status, and frequent questions. Don't change its logic or its tools — only the channel it talks to the user through.

## 3. Chat Session Entity

- **ChatSession**: `session_id`, `agent_id` (`first_line_cx`), `user_id` (the client chatting), `client_id`, `status` (`active`, `interrupted`, `closed`), `created_at`

Use `session_id` (and the same value as LangGraph `thread_id` if you checkpoint) on the WebSocket handshake so a reconnect can rehydrate the conversation.

## 4. Suggested Events Over the WebSocket

Use explicit event names and structured payloads (same naming discipline as Part 1 — not the same RFP/SSE schemas):

```json
{"event": "token_chunk", "data": {"session_id": "chat_0219", "token": "Your", "sequence": 7}}
{"event": "interrupt_requested", "data": {"session_id": "chat_0219", "new_input": "wait, I want to make a return, not track my order"}}
{"event": "generation_interrupted", "data": {"session_id": "chat_0219", "message_id": "msg_0449", "status": "interrupted"}}
{"event": "generation_completed", "data": {"session_id": "chat_0219", "message_id": "msg_0450"}}
```

## 5. Pub/Sub Pattern

Use one channel per session (for example, `chat.<session_id>`) so the producer (the agent generating tokens) stays decoupled from the consumers (subscribed WebSocket connections). Redis isn't required for this deliverable — an in-memory mechanism is acceptable if your implementation runs in a single process.

## 6. Constraints

- Field and entity names for the chat session must match this CONTEXT — don't invent parallel ids for the same session.
- Do not mix Part 1 RFP ticket notification payloads into the WebSocket chat contract.
