# CONTEXT — Brasaland: Agent Control (Part 2)

> This document assumes Part 1's Agent, Flow, and Task entities and identifiers (`manager_support`, `rfp_pipeline`, `marketing`/`operaciones`/`procurement`/`training`) are already in place. It only adds control semantics on top of them.

## 1. Introduction

Nicolás Park's ticket is a direct follow-up: the panel already tells the team when an agent needs intervention, but doing anything about it still means restarting the whole service. He wants operators — anyone on the engineering team, not just himself — to be able to pause, resume, or cancel one agent's run without affecting the other.

## 2. Control Actions per Agent

| `agent_id` | `pause` means | `resume` means | `cancel` means |
|---|---|---|---|
| `manager_support` | Stop generating the current response mid-stream; the chat session is held open | Not applicable in the same sense — a paused chat is simply resumed by the operator releasing it, no checkpoint replay needed | End the chat session; the manager sees it as closed and must start a new one |
| `rfp_pipeline` | Persist a LangGraph checkpoint at the current node; the flow's execution halts | Resume graph execution from that exact checkpoint | The flow moves to a terminal `cancelled` state; no further nodes run, and it cannot be resumed |

`pause`/`resume` on `rfp_pipeline` must reuse the same checkpointing mechanism that already supports human-in-the-loop approval in that pipeline — you are not building a second checkpoint system.

## 3. Who Can Execute Control Actions

Any authenticated backoffice user with an engineering or operations role (not limited to Nicolás) can execute `pause`, `resume`, and `cancel`. This is deliberately broader than the RFP pipeline's own approval permissions — control access and business approval access are two different permission sets, don't merge them.

## 4. Suggested WebSocket Command Schema

```json
{"command": "pause", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0142"}}
{"command": "cancel", "data": {"agent_id": "manager_support", "flow_id": "chat_0231"}}
{"event": "control_applied", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0142", "action": "pause", "actor_id": "user_0089", "timestamp": "2026-03-11T14:02:03Z"}}
```

## 5. Constraints

- Field, action, and status names must match this document exactly.
- Cancelling an `rfp_workflow` mid-flow must mark the flow itself as `cancelled`, and every department task still `pending` under it must be marked accordingly — don't leave orphaned tasks in a stale `running` state.
- Do not implement or alter the department-level approval actions (`approve`, `request_changes`) that already exist in the RFP pipeline — those remain a separate, business-level concern from this milestone's operator-level `pause`/`resume`/`cancel`.
