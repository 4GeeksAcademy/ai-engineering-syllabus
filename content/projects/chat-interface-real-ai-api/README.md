# Talk to the Machine — Building a Chat Interface with a Real AI API

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your Challenge

A small digital consultancy has been hired by a client who wants to explore AI-powered interfaces for internal use. Before committing to a full product, the team lead has asked you to build a **proof-of-concept chat interface** that communicates with a real language model through an external API.

The goal is not just to get the model to respond — it's to make the conversation data **visible and measurable**. The client wants to understand what's happening under the hood: how many tokens they're consuming, what the model's response speed looks like, and how costs accumulate over a session. This kind of visibility is something any serious AI integration needs from day one.

You'll be using [Groq](https://groq.com/), a platform that provides ultra-fast inference for open-source LLMs and returns rich metadata with every response. Your job is to build a frontend that integrates with the Groq API directly — no backend, no proxy, just a browser talking to a real AI endpoint.

> Your team lead has shared the following brief:
>
> #### What we need
>
> - A chat UI where the user can type messages and receive responses from the AI model
> - An account on [Groq](https://console.groq.com/) with an API Key configured to work in the project
> - The API must be called directly from the frontend using `fetch` — the model to use is `llama3-8b-8192`
> - Each response from Groq includes a `usage` object. The interface must use it to track and display token usage (prompt tokens, completion tokens, and cumulative totals for the entire conversation)
> - At least one additional metric from the Groq response must also be surfaced in the UI (response time, tokens per second, or model name are all valid choices)

The team lead reminded you that this is a proof of concept — the UI does not need to be complex, but the data must be accurate and update in real time after every message exchange.

---

## 🌱 How to Start the Project

Fork the boilerplate from the following repository and follow the instructions in the README:

[https://github.com/4GeeksAcademy/html-hello](https://github.com/4GeeksAcademy/html-hello)

You can work in Codespaces (recommended) or clone it locally. Either way, create your own public GitHub repository and update the remote URL so your work is pushed to your account.

> 💡 You'll be calling the Groq API from the browser. Store your API key in a way that makes it easy to configure — but be mindful: never commit secrets to a public repository. For this project, a `.env` file or a clearly named constant at the top of your script is sufficient.

---

## 💻 What You Need to Do

### Account and Setup

- [ ] Create a free account at [https://console.groq.com/](https://console.groq.com/)
- [ ] Generate an API Key from the Groq dashboard
- [ ] Confirm you can reach the Groq API endpoint (`https://api.groq.com/openai/v1/chat/completions`) with a test request using your key

### Chat Interface

- [ ] Build a chat UI with an input field and a send button
- [ ] Display the conversation history as a list of messages — user messages and AI responses visually differentiated
- [ ] Each time the user sends a message, append it to the conversation and send the **full conversation history** (all previous messages) to the Groq API
- [ ] Display the AI's response in the chat as soon as it is received
- [ ] Use the model `llama3-8b-8192` in all API calls

⚠️ **IMPORTANT:** The API must be called using `fetch` — no third-party SDK or wrapper library. This is the core skill being practiced.

### Token Usage and Metrics Panel

- [ ] After each response, read the `usage` object from the Groq API response
- [ ] Display a running total of **prompt tokens sent** across the entire session
- [ ] Display a running total of **completion tokens received** across the entire session
- [ ] Display the **combined total tokens** consumed so far
- [ ] Display at least one additional metric from the Groq response: model name, response time (`x-groq-request-time` response header or any timing you can capture), or tokens per second

> The metrics panel must update automatically after every message — the data should always reflect the full conversation to date, not just the last exchange.

---

## ✅ What We Will Evaluate

- [ ] The Groq API is called correctly using `fetch` with the right headers (`Authorization: Bearer`, `Content-Type: application/json`) and a valid request body
- [ ] The full conversation history is sent on every request (not just the latest message)
- [ ] The response is displayed in the UI without requiring a page reload
- [ ] Token data from the `usage` object is correctly read and accumulated across the session
- [ ] The metrics panel updates after every message exchange and shows correct cumulative totals
- [ ] At least one additional metric beyond token counts is displayed
- [ ] HTTP response status codes are handled — if the API returns an error, the user sees a meaningful message instead of a crash

> **Note:** Visual design is not evaluated. A functional, readable layout is enough.

---

## 📦 How to Submit

Push your project to your GitHub repository and share the link following your instructor's delivery instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
