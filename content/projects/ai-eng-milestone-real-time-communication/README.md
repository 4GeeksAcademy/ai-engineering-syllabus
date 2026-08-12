# Milestone — Real-Time Systems: WebSocket Chat Streaming (Part 2 of 2)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/communication)** before writing any code — it defines which agent you're connecting, the chat session fields, and the WebSocket event contract for this part. Part 1 SSE / RFP notification details live under [`10-realtime/notification/`](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/notification), not in this CONTEXT.

---

## 🎯 The Challenge

> 📌 You're building on **your copy** of the **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** for the company you were assigned at the start of the course — not a new repository.

In Part 1 you solved half the problem: the backend tells the frontend when something happens, without anyone having to ask. But that notification only flows one way. Your company's support agent works the same way today: the user sends a message, waits, and gets the full response all at once. If the agent is heading down the wrong path, the user has no way to say so until it finishes responding.

The support team filed an **RFI**: they want to know why the chat doesn't feel like a real conversation. Your tech lead turned it into a **ticket** for your squad:

> **Context:** the support agent already exists and works — you won't touch its internal logic or its tools.
> **What I need you to build:** the agent's response arriving token by token in real time, and the user being able to interrupt it mid-response and redirect it, without waiting for it to finish.
> **Acceptance criteria:** the channel must be bidirectional (the client also sends data, not just receives), tokens must stream as they're generated, and an interruption must genuinely **abort** the ongoing generation — not just ignore the response once it arrives.

Some requirements are left implicit, and you'll need to identify them carefully: SSE (what you used in Part 1) is no longer enough because the client needs to talk back while the server keeps sending data; token streaming and abort handling need to coexist on the same channel without stepping on each other; and the connection must recover if it drops, just like in Part 1, but now in both directions — reattaching to the same chat thread.

**Out of scope for this part:** you're not building a new agent or changing its tools or memory. The support agent you already have stays the same — what changes is how it communicates with the user.

---

## 🌱 How to Start the Project

Keep working on the fork of your company's monorepo that you've been using since Milestone (and Part 1 of this milestone). If for some reason you don't have your fork yet, create it now from the [base monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Create a new branch from your main branch: `feature/websocket-chat`.
2. Locate the endpoint or function that currently invokes your support agent with a traditional request/response pattern — extend that path; do not create a parallel app or a delivery folder.
3. Check your `CONTEXT-company.md` (under `10-realtime/communication/`) to confirm which agent you're connecting and the chat session / event names for this part — reuse naming _discipline_ from Part 1, not Part 1's RFP/SSE schemas.
4. Review how your agent exposes streaming (LangGraph's `messages`, `values`, `updates`, or `custom` modes) before deciding which one you need to transmit tokens.
5. Implement under the existing layout: WebSocket in `services/`, chat UI in `uis/`, tests in `tests/`.

If you need a refresher on how to set up a project, check out [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 What You Need to Do

**Backend (`services/`)**

- [ ] Implement a WebSocket endpoint that accepts a persistent connection per chat session
- [ ] Require `session_id` (and/or LangGraph `thread_id`) in the handshake / URL so the socket is bound to an existing conversation thread
- [ ] Stream the agent's response token by token over that connection, using whichever LangGraph streaming mode fits
- [ ] On client interrupt: **abort the running stream** so no further `token_chunk` events are produced for that generation (cancel the task / stop the model stream). Do **not** treat LangGraph `interrupt()` HITL as a substitute for stream abort — use `interrupt()` only if you also need a separate graph-level pause
- [ ] After abort: mark the partial assistant message as `interrupted` (keep tokens already shown), accept new user input, and start a **new** assistant turn — do not delete or overwrite the interrupted message in place
- [ ] Decouple the agent's event production from the WebSocket connections consuming it using a pub/sub pattern — an external backplane like Redis isn't required for this deliverable, but the producer/consumer pattern itself is evaluated

⚠️ **IMPORTANT:** chat field names and entities must match your Part 2 CONTEXT. A generic implementation that ignores the context will not be accepted. Do not mix Part 1 RFP notification payloads into this WebSocket contract.

**Frontend (`uis/`)**

- [ ] Connect the existing chat interface via WebSocket instead of a single request/response call
- [ ] Render the agent's response as tokens arrive (a live typing effect, not swapping in the full message at the end)
- [ ] Add an interrupt control (for example, being able to send a new message while the agent is still responding) that fires the abort signal to the backend; keep the partial message visible and marked interrupted; show the redirected reply as a new message
- [ ] Implement reconnection with progressive backoff: on reconnect, send the same `session_id` / `thread_id` and **rehydrate** the conversation from checkpoint and/or message history before accepting new tokens — "without losing the thread" means restore context, not only reopen a socket

**Testing (`tests/`)**

- [ ] Unit test(s) verifying the WebSocket's event contract (`token_chunk`, interrupt / `generation_interrupted`, `generation_completed`)
- [ ] Test, or documented manual verification, that an interrupt mid-response stops further tokens from the original generation, leaves the partial message marked interrupted, and that the next reply is a new turn reflecting `new_input`
- [ ] Test, or documented manual verification, that reconnect with the same `session_id` restores the conversation thread (history / checkpoint), not an empty chat

---

## 🤔 Design Questions

Before considering your implementation done, think through and document your answers to these questions in your PR:

- Why does this feature need WebSockets instead of what you built in Part 1? What specifically about the requirement forces a bidirectional channel?
- If more than one client is subscribed to the same chat session (for example, a supervisor watching the conversation live), how do you make sure they all get the same events without duplicating calls to the agent?
- How did you separate **stream abort** (stop tokens) from LangGraph HITL `interrupt()` (graph pause), if you used the latter at all? What happens to the partial assistant message and the next turn?

---

## ✅ What We Will Evaluate

- [ ] The chat interface shows response tokens as they're generated, not the full response all at once
- [ ] The WebSocket is bound to an existing conversation via `session_id` and/or LangGraph `thread_id` in the handshake or URL
- [ ] Sending an interrupt mid-response measurably aborts the original generation (no further tokens), keeps the partial message marked `interrupted`, and the agent's next response is a new turn that reflects the new input
- [ ] The WebSocket reconnects after a drop with the same `session_id` / `thread_id` and rehydrates from checkpoint or history — conversation thread is not lost
- [ ] Agent event production is decoupled from WebSocket consumers via a pub/sub (or equivalent producer/consumer) pattern; events are named and structured, not a single generic message type
- [ ] Field and entity names match what's defined in your company's Part 2 CONTEXT.md

---

## 📦 How to Submit This Project

This is Part 2 of 2 of Milestone. Submit it with its own Pull Request against your main branch — independent from Part 1.

1. Commit and push your `feature/websocket-chat` branch (code lives in `services/`, `uis/`, and `tests/` — do **not** create a separate delivery folder)
2. Open a Pull Request describing what you implemented and how to test token streaming and interrupt
3. Include your answers to the Design Questions in the PR description
4. Request a review from your tech lead

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Learn more about our [programs](https://4geeksacademy.com/us/coding-bootcamps) in [Full-Stack Software Development](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Data Science & Machine Learning](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering).
