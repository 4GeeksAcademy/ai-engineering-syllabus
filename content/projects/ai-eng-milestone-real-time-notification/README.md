# Milestone — Real-Time Systems: SSE Notifications (Part 1 of 2)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/notification)** before writing any code — it defines the operational events, field names, and company-specific constraints for this part.

---

## 🎯 Your challenge

> 📌 You're building on **your copy** of the **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** for the company you were assigned at the start of the course — not a new repository.

You already have a working central API, a reporting pipeline feeding business metrics, and the multi-agent RFP generation system with checkpointing your team shipped last week. That system registers every new proposal request (RFP) as a ticket that needs processing — but right now, the only way anyone finds out a new ticket arrived is by manually refreshing the dashboard. The sales team filed an **RFI**: they want to know why nobody notices a new RFP until someone checks the screen out of curiosity. Your tech lead turned that question into a **ticket** for your squad: replace that manual refresh with a flow that pushes the notification to the frontend the moment an RFP ticket is registered.

The brief is concrete. Your manager summarizes it like this:

> "Every RFP that comes in is money on the table, and right now nobody finds out until they open the dashboard on their own. I need the screen to show it by itself the moment a new RFP ticket is registered, without anyone having to refresh. And if someone's connection drops, it should reconnect without them having to reload the page."

Some requirements are left implicit in this brief, and you'll need to identify them carefully: the notification must be distinguishable from other event types already on your dashboard (it's not just another generic event), it must indicate at least which RFP ticket arrived and that it needs processing, and it must degrade gracefully if the client loses connection — not silently stop notifying.

**Out of scope for this part:** this deliverable requires no calls to a model or agent. This is a communication layer, not an AI layer — that comes in Part 2.

---

## 🌱 How to Start the Project

Keep working on the fork of your company's monorepo that you've been using since Milestone. If for some reason you don't have your fork yet, create it now from the [base monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Create a new branch from your main branch: `feature/sse-notifications`.
2. Locate the service and dashboard view that currently depend on polling — you will extend those paths, not create a parallel app or a delivery folder.
3. Check your `CONTEXT-company.md` to confirm how an RFP ticket is represented (fields, initial status) — that defines what the real-time notification must carry.
4. Add any new dependencies with `uv add` (backend) / your UI package manager as already used in the monorepo — never with `pip install` or `pipenv`.
5. Implement under the existing layout: SSE in `services/`, consumer UI in `uis/`, tests in `tests/`.

If you need a refresher on how to set up a project, check out [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 What You Need to Do

**Backend (`services/`)**

- [ ] Implement an SSE endpoint that emits an event every time a new RFP ticket is registered in the system
- [ ] Define an explicit event name (e.g. `rfp_ticket_created`) and a consistent payload with at least the ticket identifier and its initial status (avoid a generic "message"-type event)
- [ ] Correctly configure the SSE connection's headers and keep-alive so it doesn't close prematurely (`Content-Type: text/event-stream`, and keep-alive comment frames as needed)
- [ ] Protect the stream with the **same JWT** used by the backoffice API — unauthenticated clients must not receive events

⚠️ **IMPORTANT:** field names, entities, and domain values in your implementation must match what's specified in your CONTEXT.md. A generic implementation that ignores the context will not be accepted.

**Frontend (`uis/`)**

- [ ] Refactor the existing dashboard view that currently requires a manual reload so it shows a new RFP ticket arriving in real time, consuming the SSE stream
- [ ] Consume the stream using `fetch` + `ReadableStream` (or your stack's equivalent), sending the JWT (e.g. `Authorization: Bearer …`). Do **not** rely on `EventSource` alone — it cannot set custom auth headers cleanly, which is why `fetch` is required here
- [ ] Implement reconnection with progressive backoff when the connection drops
- [ ] Implement at least one **recovery strategy** so events registered while disconnected are not silently lost. Acceptable options (pick one and document it): `Last-Event-ID` / short server-side replay; refetch the ticket list on reconnect and use SSE only for events after that; or an equivalent approach. Deduplicate so the same ticket never appears twice in the UI
- [ ] The notification for a new RFP ticket is visually distinguishable from other dashboard data and doesn't require reloading the page or re-fetching all the data on every event

**Testing (`tests/`)**

- [ ] Test the SSE endpoint itself: assert response headers include `text/event-stream`, the wire uses a named `event:` (e.g. `rfp_ticket_created`), and `data:` is JSON matching the required payload shape / CONTEXT fields — not only an abstract dict unit test detached from the SSE framing
- [ ] Test, or documented manual verification, of reconnection + recovery after a dropped connection (backoff fires, missed tickets are recovered or explicitly handled, no duplicate UI for the same `ticket_id`)

---

## 🎁 Optional: Another Real-Time Notification Case

The RFP ticket is your required deliverable. If you want extra practice (this is not required to pass this part), you can implement **a second type of push notification**, reusing the same SSE endpoint with a new event name. Pick at most one of these, whichever best fits what you've already built and your CONTEXT:

- **Business metric threshold alert** — notify when a metric from your reporting pipeline crosses the critical threshold your CONTEXT defines for your company (for example, a sales drop, a no-show rate, or a billing denial rate, as applicable).
- **Agent escalation** — notify when a conversation is escalated from agent to human, so whoever is supervising sees it appear on the dashboard without reloading.
- **Operational inactivity alert** — notify when a process or location fails to register expected activity within a defined period (for example, no sales registered within a time window, or a vacancy left unfilled past the expected deadline).

If you implement one of these, it must meet the same technical bar as the RFP notification: named event, structured payload, and compatible with the reconnection logic you already built.

---

## 🤔 Design Questions

Before considering your implementation done, think through and document your answers to these questions in your PR:

- If two people on the sales team open the dashboard at the same time, should each SSE connection be independent, or should they share some intermediate layer? What would happen if 50 people opened it at once?
- Which recovery strategy did you choose for tickets registered while disconnected (`Last-Event-ID` / short replay, refetch-then-SSE, or equivalent), and how do you prevent duplicates after reconnect?
- Why is SSE the right tool for notifying that a ticket arrived, and not WebSockets? At what point would that stop being true — for example, if you wanted someone to be able to react to the ticket from the same channel?

---

## ✅ What We Will Evaluate

- [ ] The dashboard shows the new RFP ticket notification automatically, with no manual action from the user
- [ ] Dropping and restoring the network connection triggers reconnection within the backoff scheme, applies the documented recovery strategy, and does not duplicate notifications already received
- [ ] The SSE endpoint requires the same JWT as the backoffice; the client sends it via `fetch` (not bare `EventSource`)
- [ ] The SSE endpoint uses a named event with a structured payload for the RFP ticket, not a single generic message type; tests cover `text/event-stream`, event name, and JSON `data` shape
- [ ] No calls to a model or agent exist anywhere in this part's implementation
- [ ] Field and entity names match what's defined in your company's CONTEXT.md

---

## 📦 How to Submit This Project

This is Part 1 of 2 of Milestone. Submit it with its own Pull Request against your main branch — don't wait until Part 2 is ready.

1. Commit and push your `feature/sse-notifications` branch (code lives in `services/`, `uis/`, and `tests/` — do **not** create a separate delivery folder)
2. Open a Pull Request describing what you implemented and how to test the SSE stream
3. Include your answers to the Design Questions in the PR description
4. Request a review from your tech lead

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Learn more about our [programs](https://4geeksacademy.com/us/coding-bootcamps) in [Full-Stack Software Development](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Data Science & Machine Learning](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering).
