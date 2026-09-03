# CONTEXT — Brasaland: Agent Observability (Part 1)

> This document covers Part 1 only. Part 2 (control) reuses the same entities and agent identifiers defined here.

## 1. Introduction

The ticket comes from **Nicolás Park**, CTO. Brasaland Digital now has two agents running in production, and nobody outside the engineering team can tell what either one is doing at any given moment: the **Manager support agent** that Felipe Guerrero's Operations team uses daily, and the **multi-agent proposal pipeline** that processes corporate RFPs (catering contracts, co-branding, event concessions) for Camila Ospina's Marketing team. Nicolás wants a panel his team can open when something feels slow or stuck, without having to SSH into a server and grep logs.

## 2. Agents You're Observing

| `agent_id` | Name | Type | Owner / Area | Participates in |
|---|---|---|---|---|
| `manager_support` | Manager support agent | Single-agent, conversational | Felipe Guerrero — Operations | `chat_session` flows |
| `rfp_pipeline` | Corporate proposal pipeline | Multi-agent (orchestrator, generators, evaluators, synthesizer) | Camila Ospina — Marketing | `rfp_workflow` flows |

Don't change either agent's internal logic — you're only instrumenting the points where they already act, to emit and persist events.

## 3. Flow Types and `action_type` Taxonomy

| `flow_type` | Description | Typical `action_type` sequence |
|---|---|---|
| `chat_session` | A single conversation between a location manager and `manager_support` | `query` (retrieve relevant context) → `tool_call` (if it looks up a location's data) → `deliver` (final answer) |
| `rfp_workflow` | One corporate RFP going through intake, drafting, and evaluation | `query` (classify/extract from PDF) → `tool_call` (fetch department data) → `draft_start` / `write` (department section drafted) → `evaluate` (evaluator pass) → `deliver` (synthesizer hands off the consolidated draft) |

Use the `department_id` values already defined for Brasaland's RFP pipeline — `marketing`, `operaciones`, `procurement`, `training` — as part of the task payload whenever a step belongs to a specific department's generator or evaluator.

## 4. Entity Fields Specific to Brasaland

- **Agent.needs_intervention** must turn `true` automatically when: a `chat_session` has been in `query`/`tool_call` for more than 20 seconds without a `deliver`, or an `rfp_workflow` task has looped through `evaluate` more than the configured retry limit without producing a passing evaluation.
- **Flow.triggered_by**: for `chat_session`, the location manager's message; for `rfp_workflow`, the RFP ticket being registered (reuse the same `ticket_id` your pipeline already generates).
- Currency and location fields (`COP`/`USD`, Colombia/Florida) are not part of this milestone's payloads — don't add them unless a task genuinely needs them for context.

## 5. Suggested SSE Events

```json
{"event": "agent_step", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0142", "task_id": "task_0891", "action_type": "draft_start", "department_id": "marketing"}}
{"event": "agent_status_changed", "data": {"agent_id": "manager_support", "flow_id": "chat_0231", "status": "running"}}
{"event": "agent_status_changed", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0142", "status": "waiting_for_human"}}
```

## 6. Constraints

- Field, agent, and `action_type` names must match this document exactly — don't invent parallel identifiers.
- Do not surface or duplicate the department-level approval logic from the RFP pipeline here — this panel only observes; approval already lives in that milestone's own flow.
- Persist every task even if no SSE client is connected when it happens.
