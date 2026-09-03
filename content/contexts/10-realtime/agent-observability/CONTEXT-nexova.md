# CONTEXT — Nexova: Agent Observability (Part 1)

> This document covers Part 1 only. Part 2 (control) reuses the same entities and agent identifiers defined here.

## 1. Introduction

The ticket comes from **Sergio Molina**, CTO. Nexova has two agents live in production with no shared way to check on them: the **first-line support agent** that Roberto Díaz's Customer Support team relies on to resolve outsourcing clients' queries, and the **multi-agent proposal pipeline** that processes RFPs (headhunting, outsourced support, corporate training) for Marcos Ibáñez's Sales team. Sergio wants his team to be able to see, at a glance, whether either agent is behaving.

## 2. Agents You're Observing

| `agent_id` | Name | Type | Owner / Area | Participates in |
|---|---|---|---|---|
| `first_line_support` | First-line support agent | Single-agent, conversational | Roberto Díaz — Customer Support | `chat_session` flows |
| `rfp_pipeline` | Sales proposal pipeline | Multi-agent (orchestrator, generators, evaluators, synthesizer) | Marcos Ibáñez — Sales | `rfp_workflow` flows |

Don't change either agent's internal logic — you're only instrumenting the points where they already act, to emit and persist events.

## 3. Flow Types and `action_type` Taxonomy

| `flow_type` | Description | Typical `action_type` sequence |
|---|---|---|
| `chat_session` | A single conversation between an outsourcing client and `first_line_support` | `query` (retrieve relevant knowledge base context) → `tool_call` (if it looks up a ticket or account) → `deliver` (final answer) |
| `rfp_workflow` | One sales RFP going through intake, drafting, and evaluation | `query` (classify/extract from PDF) → `tool_call` (fetch department data) → `draft_start` / `write` (department section drafted) → `evaluate` (evaluator pass) → `deliver` (synthesizer hands off the consolidated draft) |

Use the `department_id` values already defined for Nexova's RFP pipeline — `seleccion`, `capacitacion`, `soporte` — as part of the task payload whenever a step belongs to a specific department's generator or evaluator.

## 4. Entity Fields Specific to Nexova

- **Agent.needs_intervention** must turn `true` automatically when: a `chat_session` has been in `query`/`tool_call` for more than 20 seconds without a `deliver`, or an `rfp_workflow` task has looped through `evaluate` more than the configured retry limit without producing a passing evaluation.
- **Flow.triggered_by**: for `chat_session`, the client's inbound message; for `rfp_workflow`, the RFP ticket being registered (reuse the same `ticket_id` your pipeline already generates).
- Currency (EUR for Spain-based clients, USD for Miami-based clients) is determined by the RFP's `client_country` — not something this milestone's payloads need to duplicate.

## 5. Suggested SSE Events

```json
{"event": "agent_step", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0318", "task_id": "task_1205", "action_type": "evaluate", "department_id": "seleccion"}}
{"event": "agent_status_changed", "data": {"agent_id": "first_line_support", "flow_id": "chat_0447", "status": "running"}}
{"event": "agent_status_changed", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0318", "status": "failed"}}
```

## 6. Constraints

- Field, agent, and `action_type` names must match this document exactly — don't invent parallel identifiers.
- Do not surface or duplicate the department-level approval logic from the RFP pipeline here — this panel only observes; approval already lives in that milestone's own flow.
- Persist every task even if no SSE client is connected when it happens.
