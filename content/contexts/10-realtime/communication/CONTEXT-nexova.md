# CONTEXT — Nexova: Real-Time Systems (Parts 1 and 2)

> This document applies to Parts 1 and 2 of this project. It assumes your multi-agent RFP generation system is already working — this isn't a redesign of that system, just adding real-time communication on top of it.

## 1. Introduction

The RFP ticket is opened by **Marcos Ibáñez's** team, Sales Director — they're the ones who today find out about a new proposal by checking the dashboard on their own. They're who will see the real-time notification you're building in this part.

## 2. The RFP Ticket You're Notifying About

Reuse exactly the same entities you already defined for the RFP system:

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `intake_complete`, `drafting`, `under_evaluation`, `waiting_for_approval`, `done`, `discarded`)
- **RFP metadata**: `client_name`, `client_hq` (Spain/Miami), `services_requested`, `scope`, `deadline`, `budget_range`, `departments_needed`

The real-time notification must fire the exact moment a new ticket enters the system with `status = analyzing` — meaning the document was classified as a valid RFP and the flow starts processing it.

## 3. Suggested Payload for the `rfp_ticket_created` Event

```json
{
  "event": "rfp_ticket_created",
  "data": {
    "ticket_id": "tkt_0341",
    "rfp_id": "rfp_0127",
    "client_name": "NubeSoft",
    "client_hq": "Miami",
    "services_requested": ["soporte"],
    "status": "analyzing",
    "created_at": "2026-07-24T14:32:00Z"
  }
}
```

You don't need to include the full document content or the per-department sections — just enough for whoever is watching the dashboard to know what arrived and decide whether it needs their attention now.

## 4. Optional Case, Grounded in Real Nexova Data

If you decide to implement the README's optional case, here are two starting points already defined for your company — you don't need to invent the threshold:

- **Business metric threshold alert**: Nexova already has this rule defined at the executive level — if any KPI falls below a threshold, leadership is notified immediately. You can emit a `kpi_threshold_alert` event when your reporting pipeline detects this condition, using whatever threshold you define for the KPI you pick (for example, the sales pipeline).
- **Agent escalation**: Nexova's Customer Support team already has this rule defined — if a ticket goes unattended for more than X hours, it's reassigned and the supervisor is notified. You can emit a `support_ticket_escalated` event with at least `support_ticket_id` and the hours elapsed without attention.

## 5. Constraints

- Field names must exactly match what you already used in the RFP system — don't invent new names for the same entities.

---

## 6. Part 2 — Real-Time Chat

### 6.1 Which Agent You're Connecting

The agent you're exposing over WebSocket is the **first-line support agent** from Roberto Díaz's Customer Support area: the one that currently resolves queries from Nexova's outsourcing clients. Don't change its logic or its tools — only the channel it talks to the user through.

### 6.2 Chat Session Entity

- **ChatSession**: `session_id`, `agent_id` (`first_line_support`), `user_id` (the client chatting), `client_id`, `status` (`active`, `interrupted`, `closed`), `created_at`

### 6.3 Suggested Events Over the WebSocket

Follow the same naming discipline you used in Part 1 — explicit events, structured payload:

```json
{"event": "token_chunk", "data": {"session_id": "chat_0157", "token": "Sure", "sequence": 4}}
{"event": "interrupt_requested", "data": {"session_id": "chat_0157", "new_input": "actually my question was about the invoice"}}
{"event": "generation_completed", "data": {"session_id": "chat_0157", "message_id": "msg_0322"}}
```

### 6.4 Pub/Sub Pattern

Use one channel per session (for example, `chat.<session_id>`) so the producer (the agent generating tokens) stays decoupled from the consumers (subscribed WebSocket connections). Redis isn't required for this deliverable — an in-memory mechanism is acceptable if your implementation runs in a single process.
