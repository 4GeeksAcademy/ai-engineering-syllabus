# Securing Agents: Harness and Guardrails

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/08-agent-engineering/harnessing)** before writing any code — it defines your knowledge base topics, the boundaries of your agent's scope, and the company-specific restrictions your system prompt and guardrails must respect.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

Your knowledge base query agent already works: it answers questions using RAG over your company's documents, it can call tools, and, since last sprint, it consumes the MCP Server as a client. The problem is that right now anyone can talk to it about anything, ask it to ignore its instructions, or turn it into their personal assistant — and the agent would comply.

Your tech lead opened a **ticket** after an internal security review: _"The agent passed every functional test but failed every abuse test. We need the protection harness before we expose it to real users."_ The ticket includes three non-negotiable acceptance criteria you need to read carefully, because not everything is written as a checklist.

> **From: Tech Lead — Ticket #SEC-114**
>
> We need to lock down the agent before the next deployment. Three specific things:
>
> 1. The agent can answer questions outside the company's domain (small talk, a general trivia question), but **it must always bring the conversation back to the company's context** — it cannot turn into a general-purpose chatbot.
> 2. Nobody should be able to use this agent as their personal ChatGPT for tasks that have nothing to do with us (writing them an essay, giving them code for another project, acting as a therapist). That needs to be blocked.
> 3. The system prompt cannot be modified by the user. If someone asks it to "ignore your previous instructions" or "act as if you had no rules," the agent must refuse without exception — no matter how many ways they rephrase it.
>
> Document how you tested each of these cases. If you only have one filter, we're not accepting the PR.

### 🧠 Complementary Knowledge: Harness and Guardrails

A **harness** is everything that wraps around the model to turn it into a reliable agent: tool orchestration, verification loops, context/memory, guardrails, and observability. The model decides; the harness executes, controls, and contains.

**Guardrails** exist because agents fail in three distinct ways, and each one needs a different defense:

- **Structural failures**: malformed JSON, missing fields in a tool response.
- **Content failures**: hallucinations, sensitive information leakage, harmful content.
- **Security failures**: prompt injection that manipulates the model into ignoring instructions or exfiltrating data.

A single guardrail is never enough — each type of failure needs its own layer of protection.

---

## 🌱 How to Start the Project

If you already have your fork of the company's monorepo from the start of the course, simply create a new branch from your latest work (previous milestone/day) and continue building on the agent you already have.

If for some reason you don't have a fork yet (for example, you joined late or lost it), fork the [reference monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) before continuing.

```bash
git checkout -b w22-d66-agent-guardrails
```

Install any new dependency you need with `uv add` (never `pip install` or `pipenv`).

---

## 💻 What You Need to Do

### Secure System Prompt

- [ ] Rewrite your agent's system prompt, clearly separating **system instructions** from **user input** — the model must never treat a user instruction as having the same authority as the system prompt.
- [ ] The system prompt must explicitly declare the company's domain and the conditions under which the agent is allowed to step outside it (permitted small talk, mandatory redirection).
- [ ] Document in the PR at least 3 "jailbreak" or instruction-change attempt variants you tested against your agent (e.g., "ignore your instructions," "you are now an assistant with no rules," "forget that you work for the company").

⚠️ **IMPORTANT:** Allowed topics, domain boundaries, and company-specific rules in your implementation must match what is specified in your CONTEXT.md. A generic system prompt that ignores the context will not be accepted.

### Content and Scope Guardrails

- [ ] Implement a guardrail that detects when a query is a request for personal, non-company-related use (e.g., "write me a love poem," "help me with my university homework") and responds by declining the task while redirecting to the agent's purpose.
- [ ] Implement a guardrail that allows general or casual questions (e.g., "what time is it in Tokyo?") but closes the response by steering the conversation back to the company's context.
- [ ] Add validation of the model's output before returning it to the user (expected format, absence of leaked internal instructions, absence of sensitive CONTEXT data that shouldn't be exposed).

### Security Guardrails (Anti-Injection)

- [ ] Implement a layer that sanitizes or isolates any text coming from an external tool or a document retrieved via RAG — that content must **never** be treated as a system instruction.
- [ ] Implement an explicit rejection mechanism for instruction-change requests, rephrased in at least three different ways.
- [ ] Add an automated test (`tests/pipelines/` or the test directory corresponding to your agent) that runs your injection-attempt cases and fails the build if the agent obeys them.

### Minimal Observability

- [ ] Log every time a guardrail blocks or redirects a request, including the type of failure detected (structural, content, or security).
- [ ] Expose a simple summary (endpoint or command) of how many times each guardrail was triggered during a test session.

---

## ✅ What We Will Evaluate

- [ ] The agent redirects to the company's context when it receives an out-of-domain query, instead of answering it like a general-purpose assistant.
- [ ] The agent consistently rejects at least 3 distinct instruction-change attempt variants documented in the PR.
- [ ] The agent rejects requests to be used as a personal chatbot (tasks unrelated to the company) without losing usefulness for legitimate queries.
- [ ] More than one guardrail is implemented — not a single generic validation.
- [ ] Content coming from tools or RAG documents is never treated as a system instruction (demonstrated with a test case).
- [ ] Every guardrail block or redirection is logged with the corresponding failure type.
- [ ] The implementation respects the field names, knowledge base topics, and restrictions defined in your CONTEXT.md.

---

## 📦 How to Submit Your Project

Open a Pull Request from your branch to your fork of the company's monorepo, with a description that includes the jailbreak/injection test cases you documented. This delivery is independent and does not depend on other parts or milestones — don't wait for other work to be finished before submitting your PR.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
