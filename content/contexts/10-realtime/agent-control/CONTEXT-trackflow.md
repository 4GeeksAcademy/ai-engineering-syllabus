# CONTEXT — TrackFlow: Agent Control (Part 2)

> This document assumes Part 1's Agent, Flow, and Task entities and identifiers (`first_line_cx`, `rfp_pipeline`, `warehouse`/`lastmile`/`reverse`) are already in place. It only adds control semantics on top of them.

## 1. Introduction

Andrés Kim's ticket follows directly from Part 1: the panel now flags agents that need intervention, but stopping one still means restarting the whole service — and with operations split between Los Angeles and Zaragoza, that's an outsized cost for a single stuck agent. He wants any engineer, in either location, to be able to pause, resume, or cancel a single agent's run without touching others.

## 2. Control Actions per Agent

| `agent_id` | `pause` means | `resume` means | `cancel` means |
|---|---|---|---|
| `first_line_cx` | Stop generating the current response mid-stream; the chat session is held open | The operator releases the hold, generation continues — no checkpoint replay needed | End the chat session; the client sees it as closed |
| `rfp_pipeline` | Persist a LangGraph checkpoint at the current node; the flow's execution halts | Resume graph execution from that exact checkpoint | The flow moves to a terminal `cancelled` state; no further nodes run, and it cannot be resumed |

`pause`/`resume` on `rfp_pipeline` must reuse the same checkpointing mechanism that already supports human-in-the-loop approval in that pipeline — you are not building a second checkpoint system.

## 3. Who Can Execute Control Actions

Any authenticated backoffice user with an engineering or operations role, regardless of which country they're logged in from, can execute `pause`, `resume`, and `cancel`. This is deliberately broader than the RFP pipeline's own department approval permissions — control access and business approval access are two different permission sets, don't merge them.

## 4. Suggested WebSocket Command Schema

```json
{"command": "pause", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0509"}}
{"command": "cancel", "data": {"agent_id": "first_line_cx", "flow_id": "chat_0698"}}
{"event": "control_applied", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0509", "action": "cancel", "actor_id": "user_0207", "timestamp": "2026-03-12T16:18:44Z"}}
```

## 5. Constraints

- Field, action, and status names must match this document exactly.
- Cancelling an `rfp_workflow` mid-flow must mark the flow itself as `cancelled`, and every department task still `pending` under it must be marked accordingly — don't leave orphaned tasks in a stale `running` state.
- Do not implement or alter the department-level approval actions that already exist in the RFP pipeline — those remain a separate, business-level concern from this milestone's operator-level `pause`/`resume`/`cancel`.
