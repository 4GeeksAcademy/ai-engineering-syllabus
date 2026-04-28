# Talk to the Machine — Building a Chat Interface with a Real AI API

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-coding-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your Challenge

A small digital consultancy has been hired by a client who wants to explore AI-powered interfaces for internal use. Before committing to a full product, the team lead has asked you to build a **proof-of-concept chat interface** that communicates with a real language model through an external API.

The goal is not just to get the model to respond — it's to make the conversation data **visible and measurable**. The client wants to understand what's happening under the hood: how many tokens they're consuming, how costs accumulate over a session, and what the model's overall performance looks like. This kind of observability is something any serious AI integration needs from day one.

You'll be using [Groq](https://groq.com/), a platform that provides ultra-fast inference for open-source LLMs and returns rich metadata with every response. Your job is to build a **React/Next.js frontend** that integrates with the Groq API — managing async data flow, UI state, and session persistence correctly.

> Your team lead has shared the following brief:
>
> #### What we need
>
> - A chat UI where the user can type messages and receive AI responses
> - An account on [Groq](https://console.groq.com/) with an API Key stored as an environment variable
> - Use the **Llama 3 model by Meta** available on Groq's free tier
> - Each Groq response includes a `usage` object — track and display token consumption (prompt tokens, completion tokens, cumulative totals) across the full session
> - At least one additional metric from the response must appear in the UI: model name, response time, or tokens per second are all valid choices
> - The conversation history must survive a page refresh — the user shouldn't lose their session just because they accidentally reloaded the tab

The team lead also mentioned this is a proof of concept, so the interface doesn't need to be pixel-perfect — but the data must be accurate and always up to date.

### A note on authenticating with an external API

When you call an external API as a registered user of that service, you establish your identity using a **Bearer Token** — a credential you obtained when you signed up, sent in the `Authorization` header of every request:

```text
Authorization: Bearer YOUR_API_KEY_HERE
```

Think of it as the session pass that grants you access. Without it, the API server doesn't know who you are and will reject your request with a `401 Unauthorized` response. For this project, your Bearer Token is the Groq API Key you'll generate in your account. It opens the session between your app and the Groq API — and it should always be stored in a `.env` file, never written directly in your code or committed to GitHub.

---

## 🌱 How to Start the Project

This project starts from scratch — you'll generate the initial UI using [v0.dev](https://v0.dev/), Vercel's AI-powered component generator.

1. Go to [https://v0.dev](https://v0.dev) and describe the interface you need — for example: _"a chat interface with a message history panel and a token usage stats sidebar"_
2. Create your own public GitHub repository. Open it in **GitHub Codespaces** or clone it locally.
3. Export or copy the generated React/Next component code from V0 and paste it into your project

> 💡 v0 will give you a starting point — not a finished product. You'll need to wire up the API calls, state management, and persistence yourself. That's the actual work.

---

## 💻 What You Need to Do

### Account and Setup

- [ ] Create a free account at [https://console.groq.com/](https://console.groq.com/)
- [ ] Generate an API Key and store it in a `.env` file (e.g. `NEXT_PUBLIC_GROQ_API_KEY`)
- [ ] Confirm the key works by making a test `fetch` call to `https://api.groq.com/openai/v1/chat/completions` with the Bearer token in the `Authorization` header

### Chat Interface

- [ ] Generate the initial UI layout using v0.dev and export it into your Next.js project
- [ ] Build a message input field and send button that trigger the API call
- [ ] Display the full conversation history — user messages and AI responses visually differentiated
- [ ] Use `useState` to manage the list of messages and the current input value
- [ ] Each time the user sends a message, append it to the state and send the **full conversation history** (all previous turns) to the Groq API — use the Llama 3 model by Meta available on Groq

⚠️ **IMPORTANT:** The API must be called using `fetch` — no third-party SDK or wrapper library. You must set the `Authorization: Bearer <your_key>` and `Content-Type: application/json` headers manually on every request.

### Promises and Async Flow

- [ ] Handle the `fetch` call using `async/await`
- [ ] While the API is processing, show a loading indicator or a "thinking…" state in the UI — use `useState` to track it
- [ ] If the API returns an error (non-2xx status), catch it and display a clear, human-readable message to the user instead of crashing

### Token Usage and Metrics Panel

- [ ] After each response, read the `usage` object from the Groq API response
- [ ] Accumulate and display the running total of **prompt tokens sent** for the entire session
- [ ] Accumulate and display the running total of **completion tokens received** for the entire session
- [ ] Display the **combined total tokens** consumed so far in the session
- [ ] Display at least one additional metric from the Groq response: model name, response time, or tokens per second

### Session Persistence

- [ ] Use `useEffect` to load the conversation history from `localStorage` when the component mounts
- [ ] Save the conversation history to `localStorage` after every new message so the session survives a page refresh
- [ ] Include a "Clear conversation" button that resets the message state and wipes `localStorage`

---

## ✅ What We Will Evaluate

- [ ] The Groq API is called correctly using `fetch` with `Authorization: Bearer` and `Content-Type: application/json` headers on every request
- [ ] The full conversation history is sent on every API call (stateless communication handled correctly client-side)
- [ ] The Promise is handled with `async/await` and a loading state is shown while waiting for the response
- [ ] API errors are caught and shown to the user as readable messages — no raw crashes or silent failures
- [ ] `useState` manages messages, loading state, and metrics correctly
- [ ] `useEffect` is used to load and sync conversation data from `localStorage`
- [ ] Token data from the `usage` object is accumulated and displayed correctly across the full session
- [ ] The conversation persists after a page refresh and can be manually cleared
- [ ] At least one additional metric beyond token counts is visible in the UI

> **Note:** Visual design is not evaluated. A functional, readable layout is enough.

---

## 📦 How to Submit

Push your project to your GitHub repository and share the link following your instructor's delivery instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
