# CONTEXT — TrackFlow: Real-Time Systems (Parts 1 and 2)

> This document applies to Parts 1 and 2 of this project. It assumes your multi-agent RFP generation system is already working — this isn't a redesign of that system, just adding real-time communication on top of it.

## 1. Introduction

The RFP ticket is opened by **Miguel Torres's** team, Commercial Director — they're the ones who today find out about a new proposal by checking the dashboard on their own. They're who will see the real-time notification you're building in this part.

## 2. The RFP Ticket You're Notifying About

Reuse exactly the same entities you already defined for the RFP system:

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `waiting_for_approval`, `drafting`, `under_evaluation`, `done`, `discarded`)
- **RFP metadata**: `client_name`, `client_country`, `services_requested`, `monthly_volume`, `deadline`, `budget_range`, `departments_needed`

The real-time notification must fire the exact moment a new ticket enters the system with `status = analyzing` — meaning the document was classified as a valid RFP and the flow starts processing it.

## 3. Suggested Payload for the `rfp_ticket_created` Event

```json
{
  "event": "rfp_ticket_created",
  "data": {
    "ticket_id": "tkt_0225",
    "rfp_id": "rfp_0071",
    "client_name": "Northline Apparel",
    "client_country": "US",
    "services_requested": ["warehouse", "lastmile"],
    "status": "analyzing",
    "created_at": "2026-07-24T14:32:00Z"
  }
}
```

You don't need to include the full document content or the per-department sections — just enough for whoever is watching the dashboard to know what arrived and decide whether it needs their attention now.

## 4. Optional Case, Grounded in Real TrackFlow Data

If you decide to implement the README's optional case, here are two starting points already defined for your company — you don't need to invent the threshold:

- **Business metric threshold alert**: TrackFlow already has this rule defined — if the delivery SLA falls below 90% in either country, Thomas (CEO) and Ana (Warehouse Operations) are notified immediately. You can emit an `sla_threshold_alert` event when your reporting pipeline detects this condition.
- **Agent escalation**: TrackFlow's Customer Experience team already has this rule defined — sentiment detection identifies frustrated customers before they escalate and automatically assigns them to a senior agent. You can emit a `ticket_escalated_to_senior` event with at least `ticket_id` and the reason for escalation.

## 5. Constraints

- Field names must exactly match what you already used in the RFP system — don't invent new names for the same entities.

---

## 6. Part 2 — Real-Time Chat

### 6.1 Which Agent You're Connecting

The agent you're exposing over WebSocket is the **First-line CX agent** from Valentina Cruz's area: the one that currently resolves tracking queries, return status, and frequent questions. Don't change its logic or its tools — only the channel it talks to the user through.

### 6.2 Chat Session Entity

- **ChatSession**: `session_id`, `agent_id` (`first_line_cx`), `user_id` (the client chatting), `client_id`, `status` (`active`, `interrupted`, `closed`), `created_at`

### 6.3 Suggested Events Over the WebSocket

Follow the same naming discipline you used in Part 1 — explicit events, structured payload:

```json
{"event": "token_chunk", "data": {"session_id": "chat_0219", "token": "Your", "sequence": 7}}
{"event": "interrupt_requested", "data": {"session_id": "chat_0219", "new_input": "wait, I want to make a return, not track my order"}}
{"event": "generation_completed", "data": {"session_id": "chat_0219", "message_id": "msg_0450"}}
```

### 6.4 Pub/Sub Pattern

Use one channel per session (for example, `chat.<session_id>`) so the producer (the agent generating tokens) stays decoupled from the consumers (subscribed WebSocket connections). Redis isn't required for this deliverable — an in-memory mechanism is acceptable if your implementation runs in a single process.
