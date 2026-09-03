# CONTEXT — TrackFlow: Agent Observability (Part 1)

> This document covers Part 1 only. Part 2 (control) reuses the same entities and agent identifiers defined here.

## 1. Introduction

The ticket comes from **Andrés Kim**, CTO. TrackFlow Tech now runs two agents in production with zero shared visibility: the **first-line CX agent** that Valentina Cruz's team relies on for tracking, returns, and frequent questions, and the **multi-agent proposal pipeline** that processes RFPs (warehousing, last mile, reverse logistics) for Miguel Torres's Commercial team. Andrés is tired of finding out something is wrong from a WhatsApp message between Los Angeles and Zaragoza instead of from the system itself.

## 2. Agents You're Observing

| `agent_id` | Name | Type | Owner / Area | Participates in |
|---|---|---|---|---|
| `first_line_cx` | First-line CX agent | Single-agent, conversational | Valentina Cruz — Customer Experience | `chat_session` flows |
| `rfp_pipeline` | Commercial proposal pipeline | Multi-agent (orchestrator, generators, evaluators, synthesizer) | Miguel Torres — Commercial | `rfp_workflow` flows |

Don't change either agent's internal logic — you're only instrumenting the points where they already act, to emit and persist events.

## 3. Flow Types and `action_type` Taxonomy

| `flow_type` | Description | Typical `action_type` sequence |
|---|---|---|
| `chat_session` | A single conversation between a client (B2B brand or B2C recipient) and `first_line_cx` | `query` (retrieve relevant tracking/policy context) → `tool_call` (if it looks up a shipment or return) → `deliver` (final answer) |
| `rfp_workflow` | One commercial RFP going through intake, drafting, and evaluation | `query` (classify/extract from PDF) → `tool_call` (fetch department data) → `draft_start` / `write` (department section drafted) → `evaluate` (evaluator pass) → `deliver` (synthesizer hands off the consolidated draft) |

Use the `department_id` values already defined for TrackFlow's RFP pipeline — `warehouse`, `lastmile`, `reverse` — as part of the task payload whenever a step belongs to a specific department's generator or evaluator.

## 4. Entity Fields Specific to TrackFlow

- **Agent.needs_intervention** must turn `true` automatically when: a `chat_session` has been in `query`/`tool_call` for more than 20 seconds without a `deliver`, or an `rfp_workflow` task has looped through `evaluate` more than the configured retry limit without producing a passing evaluation.
- **Flow.triggered_by**: for `chat_session`, the client's inbound message; for `rfp_workflow`, the RFP ticket being registered (reuse the same `ticket_id` your pipeline already generates).
- Currency (USD for US clients, EUR for Spain-based clients) is determined by the RFP's `client_country` — not something this milestone's payloads need to duplicate.

## 5. Suggested SSE Events

```json
{"event": "agent_step", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0509", "task_id": "task_2044", "action_type": "write", "department_id": "warehouse"}}
{"event": "agent_status_changed", "data": {"agent_id": "first_line_cx", "flow_id": "chat_0698", "status": "running"}}
{"event": "agent_status_changed", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0509", "status": "waiting_for_human"}}
```

## 6. Constraints

- Field, agent, and `action_type` names must match this document exactly — don't invent parallel identifiers.
- Do not surface or duplicate the department-level approval logic from the RFP pipeline here — this panel only observes; approval already lives in that milestone's own flow.
- Persist every task even if no SSE client is connected when it happens.
