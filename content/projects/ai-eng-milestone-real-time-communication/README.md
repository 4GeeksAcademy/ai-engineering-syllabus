# Milestone 10 — Real-Time Systems (Part 2 of 2): WebSocket Chat Streaming

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/communication)** before writing any code — it defines which agent you're connecting and what event conventions you already used in Part 1.

---

## 🎯 The Challenge

> 📌 You're building on **your copy** of the **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** for the company you were assigned at the start of the course — not a new repository.

In Part 1 you solved half the problem: the backend tells the frontend when something happens, without anyone having to ask. But that notification only flows one way. Your company's support agent works the same way today: the user sends a message, waits, and gets the full response all at once. If the agent is heading down the wrong path, the user has no way to say so until it finishes responding.

The support team filed an **RFI**: they want to know why the chat doesn't feel like a real conversation. Your tech lead turned it into a **ticket** for your squad:

> **Context:** the support agent already exists and works — you won't touch its internal logic or its tools.
> **What I need you to build:** the agent's response arriving token by token in real time, and the user being able to interrupt it mid-response and redirect it, without waiting for it to finish.
> **Acceptance criteria:** the channel must be bidirectional (the client also sends data, not just receives), tokens must stream as they're generated, and an interruption must genuinely stop the ongoing generation — not just ignore the response once it arrives.

Some requirements are left implicit, and you'll need to identify them carefully: SSE (what you used in Part 1) is no longer enough because the client needs to talk back while the server keeps sending data; token streaming and interrupt handling need to coexist on the same channel without stepping on each other; and the connection must recover if it drops, just like in Part 1, but now in both directions.

**Out of scope for this part:** you're not building a new agent or changing its tools or memory. The support agent you already have stays the same — what changes is how it communicates with the user.

---

## 🌱 Getting Started

1. Locate the endpoint or function that currently invokes your support agent with a traditional request/response pattern.
2. Check your `CONTEXT-company.md` to confirm which agent you're connecting and what events you already defined in Part 1 — reuse that naming convention, don't reinvent it.
3. Review how your agent exposes streaming (LangGraph's `messages`, `values`, `updates`, or `custom` modes) before deciding which one you need to transmit tokens.
4. Create a working branch for this part.

---

## 💻 What You Need to Do

**Backend (`services/`)**

- [ ] Implement a WebSocket endpoint that accepts a persistent connection per chat session
- [ ] Stream the agent's response token by token over that connection, using whichever LangGraph streaming mode fits
- [ ] Implement receiving an interrupt message from the client: on arrival, it must pause the ongoing generation (using `interrupt()` and the checkpointing you already know) and accept new input to resume the flow
- [ ] Decouple the agent's event production from the WebSocket connections consuming it using a pub/sub pattern — an external backplane like Redis isn't required for this deliverable, but the producer/consumer pattern itself is evaluated

⚠️ **IMPORTANT:** reuse the same event names and payload conventions you defined in Part 1 wherever they apply (for example, if you need to identify the session or related ticket). Don't invent a parallel schema.

**Frontend (`uis/`)**

- [ ] Connect the existing chat interface via WebSocket instead of a single request/response call
- [ ] Render the agent's response as tokens arrive (a live typing effect, not swapping in the full message at the end)
- [ ] Add an interrupt control (for example, being able to send a new message while the agent is still responding) that fires the interrupt signal to the backend
- [ ] Implement reconnection if the WebSocket connection drops, with the same backoff discipline you used in Part 1

**Testing (`tests/`)**

- [ ] Unit test(s) verifying the WebSocket's event contract (token event, interrupt event, completion event)
- [ ] Test, or documented manual verification, that an interrupt sent mid-response genuinely stops the original generation and the agent responds to the new input

---

## 🤔 Design Questions

Before considering your implementation done, think through and document your answers to these questions in your PR:

- Why does this feature need WebSockets instead of what you built in Part 1? What specifically about the requirement forces a bidirectional channel?
- If more than one client is subscribed to the same chat session (for example, a supervisor watching the conversation live), how do you make sure they all get the same events without duplicating calls to the agent?
- What happens to the work the agent had already generated when an interrupt arrives? Is it discarded, saved, or partially reused in the next turn? What did you choose, and why?

---

## ✅ What We Will Evaluate

- [ ] The chat interface shows response tokens as they're generated, not the full response all at once
- [ ] Sending an interrupt mid-response measurably stops the original generation, and the agent's next response reflects the new input
- [ ] The WebSocket connection reconnects after a drop without losing the conversation thread
- [ ] Events between the agent, the pub/sub layer, and the WebSocket clients are named and structured, not a single generic message type
- [ ] Field and entity names match what's defined in your company's CONTEXT.md and stay consistent with what you used in Part 1

---

## 📦 How to Submit

1. Commit and push your work to your fork of the monorepo, inside this project's folder (`parte-2-realtime-ws/`).
2. Open a Pull Request against your own main branch, independent from Part 1's.
3. Include your answers to the Design Questions in the PR description.
4. Request review from your tech lead.

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Learn more about our [programs](https://4geeksacademy.com/us/coding-bootcamps) in [Full-Stack Software Development](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Data Science & Machine Learning](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering).
