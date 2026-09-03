# Milestone — Real-Time Systems: Agent Control (Part 2 of 2)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/agent-control)** before writing a single line of code — it defines which control actions apply to each of your company's agents and which fields your implementation is expected to use. Part 1 entities and agent ids live under [`agent-observability/`](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/agent-observability); this CONTEXT only adds control semantics on top of them.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

You already built the panel that **shows** the status of your agents and which actions would be available given that status. The problem now is that "available" is just a label: if an agent gets stuck in a loop, the only real way to stop it today is to restart the entire service — which also kills any other agent that's working fine at that moment.

Your tech lead turns this into a **ticket**, a direct follow-up to the previous one:

> **Context:** The panel already tells us when an agent needs intervention, but we can't do anything about it without affecting the whole system.
>
> **What I need you to build:**
>
> - The actions the panel already shows as "available" need to actually **execute**: pause, resume, and cancel a specific agent, without touching the others.
> - Pausing an agent mid-flow, with several steps already done, must **not lose its progress** — it must be resumable later from where it left off, not from scratch.
> - Cancel must be clearly distinct from pause: cancel is final, it cannot be resumed.
> - Anyone on the team with the panel open must see the result of an action **immediately**, without refreshing — even if several people are looking at the same agent at once.
> - **Who** executed each action and when must be recorded as part of that task's history.
>
> **Acceptance criterion:** a stuck agent can be paused without affecting the rest of the system, and its task history (the one you already built) clearly reflects that it was paused, by whom, and whether it was later resumed or cancelled.
>
> — Your tech lead

Some requirements are left implicit: pause and cancel **are not the same action in disguise** — they carry different guarantees, and your Part 1 data model must be able to represent both unambiguously; executing a control action must be **broadcast to all connected clients**, not just the one who triggered it, since several people on the team may be looking at the same panel; and this is operational control — a kill switch — it does not replace or interfere with the business-approval checkpoints your multi-agent flow already has internally.

### 📚 Complementary knowledge: kill switch vs. business approval

You already saw this distinction in Part 1, but now it really matters: the control you're implementing here is **operational** — any authorized member of the technical team can pause or cancel an agent because something looks wrong with its execution, without needing to understand what business decision it was making. It's a **kill switch**, not an approval. The **business approval** your multi-agent flow already implements is different: it's executed by the person who owns that specific decision, and it answers "is this output okay to go out?", not "is this process running correctly?". Both can coexist on the same execution: an agent can be correctly waiting on a business approval (that's not a failure), and an operator can still decide to cancel it if, for example, it's been waiting too long.

**Out of scope for this part:** don't duplicate or replace the existing business-approval logic in your multi-agent flow — your new control actions coexist with it, they don't replace it.

---

## 🌱 How to Start the Project

Continue on the same working branch of your company's monorepo. Part 1 ([Agent Observability](../ai-eng-milestone-real-time-agent-observability)) must already be merged or available on your branch — you extend that panel, you don't rebuild it.

1. Create a new branch from your main branch: `feature/agent-control-websocket`.
2. Before writing code, decide how your Part 1 **Agent** entity will unambiguously represent the difference between "paused" (resumable) and "cancelled" (terminal) — don't merge them into a single status field without distinction.
3. Identify where your multi-agent system already uses checkpointing to resume executions — you'll **reuse that mechanism** so pause/resume actually works, not build a new one from scratch.
4. Check your `CONTEXT-company.md` under `content/contexts/10-realtime/agent-control/` to confirm which control actions apply to each of your company's agents.
5. Add new dependencies with `uv add` — never with `pip install` or `pipenv`.
6. Implement within the existing structure: WebSocket + control logic in `services/`, panel in `uis/backoffice`, tests in `tests/`.

---

## 💻 What You Need to Do

**Data model (`services/`)**

- [ ] Extend your **Agent** entity to unambiguously represent the `paused` (resumable) and `cancelled` (terminal) states, distinct from each other and from `running`/`failed`/`completed`
- [ ] Every executed control action is recorded in the Part 1 **Task** history: which action, who executed it (`actor_id`), timestamp
- [ ] A flow containing a cancelled agent reflects that status at the **Flow** level too, not only at the individual agent level

**Backend — WebSocket and control (`services/`)**

- [ ] Implement a WebSocket channel to send control commands (`pause`, `resume`, `cancel`) targeted at a specific agent/execution
- [ ] `pause` must use your multi-agent system's existing checkpointing to persist the exact point of execution; `resume` picks up from there, not from the start
- [ ] `cancel` is terminal: once cancelled, an agent cannot be resumed — only a new execution can be started
- [ ] Use a **pub/sub** pattern: when an action is executed on an agent, every client subscribed to that agent (or that flow) receives the update, not just the one who sent the command
- [ ] Validate that the requested action is valid for the agent's current status (e.g., you can't "resume" an agent that was never paused) and respond with a clear error if it isn't
- [ ] Protect the WebSocket channel with the same JWT as the rest of the backoffice, and derive `actor_id` from that identity — never trust a field sent by the client

⚠️ **IMPORTANT:** action names, statuses, and fields must match what's specified in your `CONTEXT-company.md`. A generic implementation that ignores the context will not be accepted.

**Frontend (`uis/backoffice`)**

- [ ] In the agent detail view (from Part 1), the actions that were previously informational only are now **functional buttons**: pause, resume, cancel, enabled/disabled based on current status
- [ ] When an action executes, the panel reflects the result in real time via WebSocket — without reloading the page
- [ ] If more than one client/tab has the same agent open, both must be updated when either one executes an action
- [ ] The agent's task history (from Part 1) clearly shows when a task was interrupted by a pause or cancellation, and who executed it
- [ ] WebSocket reconnection with state recovery — if the client disconnects and reconnects, it must be able to recover the agent's current status, not end up out of sync

**Testing (`tests/`)**

- [ ] `pause` test: verifies the checkpoint is persisted and the agent's status changes to `paused`
- [ ] `resume` test: verifies execution resumes from the correct checkpoint, not from the start
- [ ] `cancel` test: verifies the agent ends up in a terminal state and a later `resume` attempt is rejected
- [ ] State-transition validation test: invalid actions for the current status return an error instead of executing silently
- [ ] Pub/sub test: verifies an action executed by one client propagates to other clients subscribed to the same agent
- [ ] Audit test: every control action is recorded with `actor_id` and timestamp in the corresponding task's history

---

## 🤔 Design Questions

- Why do `pause` and `cancel` need different guarantees in your system? What would break if you treated them as the same action with two names?
- How did you prevent two simultaneous control commands on the same agent (e.g., two people pausing and resuming almost at the same time) from leaving the state inconsistent?
- An agent can be waiting on a business approval and, at the same time, be a candidate for an operational control action — how does your panel distinguish which of the two is happening?
- What did you decide to do with a flow's child agents/tasks when the parent agent is cancelled?

---

## ✅ What We Will Evaluate

- [ ] `pause`, `resume`, and `cancel` genuinely work on a specific agent, without affecting other running agents
- [ ] `pause` reuses existing checkpointing and `resume` correctly picks up from that point, not from scratch
- [ ] `cancel` is terminal, and a later `resume` attempt is rejected with a clear error
- [ ] Actions are broadcast via pub/sub: every client subscribed to the agent/flow sees the change in real time, not just the one who triggered it
- [ ] Invalid state transitions are explicitly rejected, not silently ignored
- [ ] Every control action is audited in the task history: which action, who (`actor_id` derived from the JWT, not from the client), when
- [ ] A flow's status correctly reflects when one of its agents was cancelled
- [ ] The WebSocket channel requires the same JWT as the rest of the backoffice
- [ ] WebSocket reconnection recovers the agent's real status, without desync
- [ ] The existing business-approval logic was not duplicated or altered
- [ ] Action, status, and field names match `CONTEXT-company.md`

---

## 📦 How to Submit

This is Part 2 of 2 of the Milestone. Submit it with its own Pull Request against your main branch.

1. Commit and push your `feature/agent-control-websocket` branch
2. Open a Pull Request describing what you implemented and how to test it
3. Include your answers to the Design Questions in the PR description
4. Request a review from your tech lead

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
