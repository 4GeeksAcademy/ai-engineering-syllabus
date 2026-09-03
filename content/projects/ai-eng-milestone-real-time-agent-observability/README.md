# Milestone — Real-Time Systems: Agent Observability (Part 1 of 2)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/agent-observability)** before writing a single line of code — it defines which agents of your company you're observing, the expected event names, and the specific fields for your implementation.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

You already have agents running in production: a conversational assistant that answers the team's questions, and a multi-agent system that processes full workflows with several steps and internal validations. The problem is that right now, the only way to know what either one is doing at any given moment is to check logs manually.

Your tech lead forwards you an **RFI** that came in from operations and turns it into a **ticket** for your squad:

> **Context:** We have no visibility into what our agents are doing while they're running, and no reliable history of what they already did. When something goes wrong, we find out from an angry user, not from the system.
>
> **What I need you to build** — a panel that includes, at minimum:
>
> - A **list of all registered agents**: identifier, name, which flow(s) it participates in, current status, and whether it needs intervention.
> - The **detail view of an agent**, including which actions would be available on it given its current status.
> - Inside that detail, the **last 5 flows** it participated in, its status in each one, and, within each flow, the tasks that agent executed there.
> - A **quick log of the last 10 tasks** executed by that agent, regardless of which flow.
> - An option to see the **full paginated history** of executions across all agents, not just the most recent ones.
> - Besides the agent-centric view, a **flow-centric view**: the flows that have run, and once inside one, the detail of which agents participated, their status, and what each one did within that flow.
>
> **Acceptance criterion:** given the identifier of any task, anyone on the team should be able to unambiguously reconstruct which flow originated it, what triggered it, which tasks it derived, and what the previous and next steps were.
>
> — Your tech lead

Some requirements are left implicit and you'll need to identify them carefully: the data schema must work for **more than one type of agent** (a single-step conversational one, and one with multiple nodes and sub-tasks); an agent can participate in **several different flows** over time, so "flow" and "agent" are two related entities, not one; every task must retain **where it came from** (what triggered it) and **what it produced** (derived tasks), forming a chain traceable by identifiers; and the history must **survive after execution ends** — it isn't just a live view that disappears on refresh.

### 📚 Complementary knowledge: observability vs. control vs. business approval

It's easy to conflate three different things. **Observability** is simply being able to see and reconstruct what happened — this project, including showing which actions _would_ be available. **Operational control** is being able to actually _execute_ those actions (pause, resume, kill an agent) — that's [Part 2](../ai-eng-milestone-real-time-agent-control). **Business approval** is when a human signs off on a specific decision before it executes — something your multi-agent system already handles internally with its own control points. This part of the project is only the first one: **look and understand, don't touch yet**.

**Out of scope for this part:** you can _display_ which actions would be available given the agent's current status (e.g., a "pause available" or "requires approval" tag), but don't implement actually executing those actions — that's [Part 2](../ai-eng-milestone-real-time-agent-control). Don't touch the existing internal approval logic in your multi-agent flow either; this panel observes it from the outside, it doesn't replace it.

---

## 🌱 How to Start the Project

Continue on the fork of your company's monorepo you've been using since the start of the course. If for some reason you don't have your fork yet, create it now from the [base monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Create a new branch from your main branch: `feature/agent-observability-sse`.
2. Before writing code, sketch out (even on paper) the data model: what an **agent** is, what a **flow/execution** is, what a **task/step** is, and how they relate. Most mistakes in this project come from not clearly separating these three entities.
3. Locate the points in your backend where your agents already emit steps, tool calls, or status changes — you'll extend those points, not rewrite the agents' logic.
4. Check your `CONTEXT-company.md` under `content/contexts/10-realtime/agent-observability/` to confirm which agents and flows you need to observe.
5. Add new dependencies with `uv add` — never with `pip install` or `pipenv`.
6. Implement within the existing structure: SSE + persistence in `services/`, panel in `uis/backoffice`, tests in `tests/`.

---

## 💻 What You Need to Do

**Data model (`services/`)**

- [ ] Define an **Agent** entity: identifier, name, flow(s) it can participate in, current status, flag for whether it needs intervention
- [ ] Define a **Flow/Execution** entity: identifier, flow type, status, what triggered it (`triggered_by`), participating agents
- [ ] Define a **Task/Step** entity: identifier, which flow and agent it belongs to, `action_type` (`query`, `write`, `draft_start`, `tool_call`, `deliver`, or another one defined in your CONTEXT), what triggered it (`trigger` — a prior task or an external event), tasks derived from it, a reference to the previous step and the next step
- [ ] Every task must be **persisted** so its full chain (trigger → task → derived tasks → next step) is reconstructible after the flow has ended

**Backend — API and stream (`services/`)**

- [ ] SSE endpoint that emits an event for every step or status change of an active agent (`agent_step`, `agent_status_changed`), including `action_type`
- [ ] Endpoint: **list of registered agents** (id, name, flow(s), status, `needs_intervention`)
- [ ] Endpoint: **agent detail**, including which actions would be available given its current status
- [ ] Endpoint: an agent's **last 5 flows**, with status per flow and that agent's tasks within each one
- [ ] Endpoint: an agent's **last 10 tasks** (quick log, not grouped by flow)
- [ ] Endpoint: **full paginated log** of executions across all agents
- [ ] Endpoint: **list of executed flows**, and a flow's detail with its participating agents, each one's status, and actions performed
- [ ] Protect all endpoints and the stream with the same JWT used by the backoffice

⚠️ **IMPORTANT:** event names, agents, `action_type`, and fields must match what's specified in your `CONTEXT-company.md`. A generic implementation that ignores the context will not be accepted.

**Frontend (`uis/backoffice`)**

- [ ] **Agent list** view: id, name, flow(s), status, visual "needs intervention" indicator
- [ ] **Agent detail** view: current status, available actions (informational only, not executable yet), last 5 flows with their status and the agent's tasks in each, last 10 tasks as a log
- [ ] **Full paginated log** view, filterable at least by agent or by flow
- [ ] **Flow list** and **flow detail** views: participating agents, each one's status, actions performed
- [ ] For any individual task, it must be clearly visible: what triggered it, what tasks it derived, and what the previous/next step in the chain is
- [ ] The agent list and agent detail update in real time via SSE; the log/history views can be on-demand (they don't need to be streaming)
- [ ] Consume the stream with `fetch` + `ReadableStream` (or your stack's equivalent), sending the JWT (e.g. `Authorization: Bearer …`). Do **not** rely on `EventSource` alone — it cannot set custom auth headers cleanly
- [ ] Reconnection with progressive backoff and recovery of missed events

**Bonus (optional, does not block acceptance)**

- [ ] Represent a flow as a **visual graph**: nodes = tasks or agents, edges = trigger → derived / previous step → next. A sophisticated library isn't required; even a diagram generated from the identifier chain counts.

**Testing (`tests/`)**

- [ ] SSE endpoint test: headers, event name, shape of the `data` JSON
- [ ] Tests for the agent list and agent detail endpoints
- [ ] Flow endpoint test: given a `flow_id`, correctly returns all its participating agents and tasks in order
- [ ] Traceability test: given any `task_id`, its trigger, derived tasks, and previous/next steps can be retrieved unambiguously
- [ ] Paginated log test: verifies chronological order and that pagination doesn't duplicate or skip records

---

## 🤔 Design Questions

- How did you model the relationship between Agent, Flow, and Task? Why that cardinality and not another?
- How did you represent "what triggered this task"? Is it always another task, or can it also be an external event (e.g., a ticket arriving)?
- If an agent participates in two different flows at the same time, how does your panel avoid mixing their tasks?
- What choice did you make so the list of available actions is informational now, but easy to wire to real execution in Part 2?

---

## ✅ What We Will Evaluate

- [ ] The three entities (Agent, Flow, Task) exist and function, with correctly modeled relationships
- [ ] The agent list shows id, name, flow(s), status, and `needs_intervention`, updated in real time
- [ ] The agent detail correctly shows available actions per status, last 5 flows with nested tasks, and last 10 tasks as a log
- [ ] The full paginated log works without duplicating or skipping records
- [ ] The flow view correctly shows participating agents, their status, and their actions within that flow
- [ ] Given any `task_id`, its trigger, derived tasks, and previous/next steps can be reconstructed
- [ ] The schema works for at least two agents with different architectures (simple conversational and multi-agent)
- [ ] All endpoints and the stream require the same JWT as the rest of the backoffice
- [ ] No real execution of any control action was implemented in this part — only what would be available is shown
- [ ] Event, agent, flow, and `action_type` names match `CONTEXT-company.md`

---

## 📦 How to Submit

This is Part 1 of 2 of the Milestone. Submit it with its own Pull Request against your main branch — don't wait for Part 2 to be ready.

1. Commit and push your `feature/agent-observability-sse` branch
2. Open a Pull Request describing what you implemented and how to test it
3. Include your answers to the Design Questions in the PR description
4. Request a review from your tech lead

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
