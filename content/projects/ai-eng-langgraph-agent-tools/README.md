# Support Agent with LangGraph — Part 2 of 2: Tools Outside the RAG

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

This is **Part 2 of 2** and depends directly on Part 1: you need the compiled LangGraph graph, with tracing and evals working, before continuing here.

Today your agent only knows one thing: search the RAG knowledge base. But support doesn't run on documentation alone — it runs on data that changes constantly. Your tech lead's **brief** is direct:

> **From:** Tech Lead
> **To:** Agent Team
>
> The RAG you migrated in Part 1 answers questions about procedures and policies well, but when a support agent asks "what's the status of ticket 482?", the agent makes up an answer because it has no way to check that — that information doesn't live in the knowledge base, it lives in the **incident manager** we already built.
>
> I need you to give the agent a tool to query the incident system in real time. As a stretch goal, if you have time, a second tool to query the **inventory manager** also resolves frequent support questions ("do we have stock of X?").
>
> **Acceptance criteria:** the agent must decide on its own when a question requires the RAG and when it requires an external tool — without the user having to specify it.

Two requirements are implied in that brief and are easy to miss: (1) the tools must read from the services you **already built** in earlier projects (the incident manager and, if you built it, the inventory manager) — no simulated data or parallel dataset invented; and (2) if a tool fails or the service doesn't respond, the graph needs an explicit recovery path, not an error that breaks the whole run.

### Complementary knowledge: why this isn't "another RAG"

It's tempting to solve this by indexing tickets into the same vector store as the RAG. Don't: tickets change status in real time, and the RAG is meant for relatively stable knowledge (policies, procedures). A **tool** that calls the incident manager's endpoint directly always gives you the current value; an indexed copy of a ticket goes stale the moment someone changes its status. This is the difference between "knowledge" (RAG) and "live operational data" (tool call).

---

## 🌱 How to Start

1. Confirm your **incident manager** service (`GET /api/incidents`, `GET /api/incidents/{id}`) is running locally — it's the one you built in an earlier monorepo project. If you also built the **inventory manager** (`GET /inventory/products`), have it available too for the stretch goal.
2. Start from the Part 1 branch (compiled graph, with tracing and evals).
3. You don't need any new dependencies beyond whatever you already use to make HTTP calls from your backend.

---

## 💻 What You Need to Do

### Required tool: support ticket lookup

- [ ] Define a **typed contract** for the tool's input/output (e.g., input: `ticket_id` or search filters; output: status, category, source, dates — the same fields your incident API exposes).
- [ ] Implement the tool so it calls your existing incident manager service (`GET /api/incidents` or `GET /api/incidents/{id}`) — never simulated or hardcoded data.
- [ ] Add a **node** to the graph for this tool and a **conditional edge** that decides when the agent should use it instead of (or in addition to) the RAG.
- [ ] Define an explicit **timeout** for the call — if the incident service doesn't respond in time, the graph must not hang.
- [ ] Define a **fallback path**: if the tool fails or the ticket doesn't exist, the agent gives an honest answer ("I couldn't confirm that ticket's status right now"), never a made-up status.

### Stretch tool (optional): inventory lookup

- [ ] If your company has an inventory manager already built, define the same kind of typed contract to query stock by product (`GET /inventory/products`).
- [ ] Apply the same rules: timeout, fallback on failure, no simulated data.

### Agent routing

- [ ] The agent must automatically decide, from the user's question, whether it needs the RAG, a tool, or both — without the user explicitly specifying which source to use.
- [ ] No tool does more than one thing: if you find yourself making a single tool "look up tickets or inventory depending on the case," split it into two separate tools.

### Tracing and evaluation (extended from Part 1)

- [ ] Each run's trace must clearly show whether the RAG, a tool, or both were used, and in what order.
- [ ] Add at least 2 new evals that verify routing: one question that must be resolved with a tool (not the RAG), and one question that must be resolved with the RAG (not a tool). An optional third eval can verify fallback behavior when the incident service is unavailable.

⚠️ **IMPORTANT:** Tools must read from the real services you already built (incidents, and inventory if applicable). An implementation that simulates that data instead of calling your own backend will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] The ticket tool has a typed input/output contract and queries the real incident manager service.
- [ ] There is an explicit timeout on the tool call.
- [ ] There is a verifiable fallback path when the tool fails or the resource doesn't exist — no made-up answers.
- [ ] The agent routes correctly between the RAG and tool(s) based on the question's content, without explicit user instruction.
- [ ] Each tool has a single responsibility (no tool combines tickets and inventory).
- [ ] Each run's trace makes it possible to tell which source(s) were used and in what order.
- [ ] There are at least 2 new evals verifying correct routing between RAG and tool.
- [ ] (Stretch) The inventory tool, if implemented, follows the same contract, timeout, and fallback rules.

---

## 📦 How to Submit This Project

This is **Part 2 of 2**. It is submitted via its own Pull Request, separate from Part 1's — it may start from that branch, but it is reviewed independently.

```text
services/
  <agent-service>/               ← new node(s) and tool(s) added to the Part 1 graph

tests/
  pipelines/                     ← routing and fallback evals
```

1. Push your branch with the structure above and open a Pull Request to the original repository with the `part-2-external-tools` label.
2. Make sure your PR includes:
   - The trace of a run where the agent used the ticket tool.
   - The trace of a run where the agent used the RAG (to show correct routing).
   - The output of running the new evals.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
