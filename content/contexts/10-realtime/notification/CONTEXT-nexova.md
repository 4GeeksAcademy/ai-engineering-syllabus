# CONTEXT — Nexova: Real-Time Systems (Part 1)

> This document applies to Part 1 of this project. It assumes your multi-agent RFP generation system is already working — this isn't a redesign of that system, just adding real-time notification on top of it.

## 1. Introduction

The RFP ticket is opened by **Marcos Ibáñez's** team, Sales Director — they're the ones who today find out about a new proposal by checking the dashboard on their own. They're who will see the real-time notification you're building in this part.

## 2. The RFP Ticket You're Notifying About

Reuse exactly the same entities you already defined for the RFP system:

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `intake_complete`, `drafting`, `under_evaluation`, `waiting_for_approval`, `done`, `discarded`)
- **RFP metadata**: `client_name`, `client_hq` (Spain/Miami), `services_requested`, `scope`, `deadline`, `budget_range`, `departments_needed`

The real-time notification must fire the exact moment a new ticket enters the system with `status = analyzing` — meaning the document was classified as a valid RFP and the flow starts processing it.

## 3. Suggested SSE wire format for `rfp_ticket_created`

SSE uses a named `event:` line and a JSON `data:` body (ticket fields only — not a nested `{"event","data"}` envelope):

```text
event: rfp_ticket_created
data: { "ticket_id": "tkt_0341", "rfp_id": "rfp_0127", "client_name": "NubeSoft", "client_hq": "Miami", "services_requested": ["soporte"], "status": "analyzing", "created_at": "2026-07-24T14:32:00Z" }

```

You don't need to include the full document content or the per-department sections — just enough for whoever is watching the dashboard to know what arrived and decide whether it needs their attention now.

## 4. Optional Case, Grounded in Real Nexova Data

If you decide to implement the README's optional case, here are two starting points already defined for your company — you don't need to invent the threshold:

- **Business metric threshold alert**: Nexova already has this rule defined at the executive level — if any KPI falls below a threshold, leadership is notified immediately. You can emit a `kpi_threshold_alert` event when your reporting pipeline detects this condition, using whatever threshold you define for the KPI you pick (for example, the sales pipeline).
- **Agent escalation**: Nexova's Customer Support team already has this rule defined — if a ticket goes unattended for more than X hours, it's reassigned and the supervisor is notified. You can emit a `support_ticket_escalated` event with at least `support_ticket_id` and the hours elapsed without attention.

## 5. Constraints

- Field names must exactly match what you already used in the RFP system — don't invent new names for the same entities.
- Part 2 (WebSocket chat) lives under `10-realtime/communication/` — do **not** copy the RFP `Ticket` schema into that CONTEXT; reuse naming discipline only.
