# Milestone 10 — Real-Time Systems (Part 1 of 2): SSE Notifications

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/notification)** before writing any code — it defines the operational events, field names, and company-specific constraints for this part.

---

## 🎯 The Challenge

> 📌 You're building on **your copy** of the **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** for the company you were assigned at the start of the course — not a new repository.

You already have a working central API, a reporting pipeline feeding business metrics, and the multi-agent RFP generation system with checkpointing your team shipped last week. That system registers every new proposal request (RFP) as a ticket that needs processing — but right now, the only way anyone finds out a new ticket arrived is by manually refreshing the dashboard. The sales team filed an **RFI**: they want to know why nobody notices a new RFP until someone checks the screen out of curiosity. Your tech lead turned that question into a **ticket** for your squad: replace that manual refresh with a flow that pushes the notification to the frontend the moment an RFP ticket is registered.

The brief is concrete. Your manager summarizes it like this:

> "Every RFP that comes in is money on the table, and right now nobody finds out until they open the dashboard on their own. I need the screen to show it by itself the moment a new RFP ticket is registered, without anyone having to refresh. And if someone's connection drops, it should reconnect without them having to reload the page."

Some requirements are left implicit in this brief, and you'll need to identify them carefully: the notification must be distinguishable from other event types already on your dashboard (it's not just another generic event), it must indicate at least which RFP ticket arrived and that it needs processing, and it must degrade gracefully if the client loses connection — not silently stop notifying.

**Out of scope for this part:** this deliverable requires no calls to a model or agent. This is a communication layer, not an AI layer — that comes in Part 2.

---

## 🌱 Getting Started

1. Locate the service and dashboard view in your copy of the monorepo that currently depend on polling.
2. If you don't yet have a fork of your company's monorepo, create one now from [the base repository](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) before continuing.
3. Check your `CONTEXT-company.md` to confirm how an RFP ticket is currently represented in your system (fields, initial status) — that defines what information the real-time notification needs to carry.
4. Create a working branch for this part.

---

## 💻 What You Need to Do

**Backend (`services/`)**

- [ ] Implement an SSE endpoint that emits an event every time a new RFP ticket is registered in the system
- [ ] Define an explicit event name (e.g. `rfp_ticket_created`) and a consistent payload with at least the ticket identifier and its initial status (avoid a generic "message"-type event)
- [ ] Correctly configure the SSE connection's headers and keep-alive so it doesn't close prematurely

⚠️ **IMPORTANT:** field names, entities, and domain values in your implementation must match what's specified in your CONTEXT.md. A generic implementation that ignores the context will not be accepted.

**Frontend (`uis/`)**

- [ ] Refactor the existing dashboard view that currently requires a manual reload so it shows a new RFP ticket arriving in real time, consuming the SSE stream
- [ ] Consume the stream using `fetch` + `ReadableStream` (or your stack's equivalent mechanism)
- [ ] Implement reconnection with progressive backoff when the connection drops
- [ ] The notification for a new RFP ticket is visually distinguishable from other dashboard data and doesn't require reloading the page or re-fetching all the data

**Testing (`tests/`)**

- [ ] Unit test(s) verifying the structure of the payload emitted by the SSE endpoint
- [ ] Test, or documented manual verification, of reconnection behavior after a dropped connection

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
- What happens if an RFP ticket is registered while a user is disconnected? Is the notification lost, or is there a way to recover it on reconnect?
- Why is SSE the right tool for notifying that a ticket arrived, and not WebSockets? At what point would that stop being true — for example, if you wanted someone to be able to react to the ticket from the same channel?

---

## ✅ What We Will Evaluate

- [ ] The dashboard shows the new RFP ticket notification automatically, with no manual action from the user
- [ ] Dropping and restoring the network connection triggers a reconnection within the implemented backoff scheme, without duplicating notifications already received
- [ ] The SSE endpoint uses a named event with a structured payload for the RFP ticket, not a single generic message type
- [ ] No calls to a model or agent exist anywhere in this part's implementation
- [ ] Field and entity names match what's defined in your company's CONTEXT.md

---

## 📦 How to Submit

1. Commit and push your work to your fork of the monorepo, inside this project's folder (`parte-1-realtime-sse/`).
2. Open a Pull Request against your own main branch (don't wait until Part 2 is ready — this part is submitted independently).
3. Include your answers to the Design Questions in the PR description.
4. Request review from your tech lead.

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Learn more about our [programs](https://4geeksacademy.com/us/coding-bootcamps) in [Full-Stack Software Development](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Data Science & Machine Learning](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering).
