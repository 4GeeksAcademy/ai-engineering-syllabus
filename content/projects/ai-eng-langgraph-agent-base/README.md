# Support Agent with LangGraph — Part 1 of 2: Migration and Agent Flow

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

In Milestone 7 you built the four functions of your RAG system (`setup`, `embed`, `retrieve`, `query`) and exposed them through a FastAPI endpoint. It works, but it's a black box: it takes in a question and returns an answer, without anyone — including you — being able to see what decisions it made along the way.

Your tech lead opened a **ticket** with a clear requirement: before adding any new capability to the agent (Part 2 of this same project), the reasoning flow has to become explicit as a graph, with state, nodes, and transitions that can be traced and evaluated independently.

> **Tech lead's note:** _"I don't want you to rewrite the RAG logic from scratch — the `retrieve` and `embed` you already have work fine. What I want is that same behavior living inside a LangGraph graph, with single-responsibility nodes, and every run traced. If I can't see why the agent answered what it answered, I can't trust it in production."_

Three things are implied in that ticket and are easy to miss: (1) the graph must be compiled before any execution, so structural errors are caught at build time rather than in production; (2) the state passed between nodes must be minimal and explicit, not the full conversation history; and (3) every run must produce a queryable trace, not just a final answer.

### Complementary knowledge: from naive loop to graph

A "naive" agent is simply a Python `while` loop: call the model, if it requests a tool run it, feed the result back, repeat. That works for prototypes, but it doesn't scale: there's no way to pause, resume, trace a specific step, or test a node in isolation.

LangGraph formalizes that same loop as a state machine: each step is a **node**, each decision about where to go next is an **edge**, and the compiled set is the **graph**. This is what lets you, in Part 2, add a new tool without touching the rest of the flow: you just add a node and a conditional edge that decides when to use it.

---

## 🌱 How to Start

1. Keep working on your existing fork of the [**monorepo**](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo). If for some reason you don't have one yet, fork it and open it in **GitHub Codespaces** or clone it locally.
2. Install the dependency with `uv add langgraph` (never use `pip install` or `pipenv`).
3. Locate your Milestone 7 code: your `setup`, `embed`, `retrieve`, and `query` functions in `data/pipelines/`, and the endpoint that exposes them in `services/`.

---

## 💻 What You Need to Do

### Agent graph (`services/`)

- [ ] Define the graph's **state**: the minimum information a node needs to decide the next step (user question, retrieval result, partial answer). Don't include the full conversation history without justifying why you need it.
- [ ] Model at least these **nodes**: one that receives the question, one that runs `retrieve` against your knowledge base (reusing the code from `data/pipelines/`, not duplicating it), and one that generates the final answer with `query`.
- [ ] Define the **edges** between nodes based on explicit output conditions, not as a hardcoded fixed sequence.
- [ ] **Compile the graph** before any execution — compilation must fail clearly if there's a structural error (an unconnected node, a mistyped state, etc.).
- [ ] Implement **checkpointing** at every meaningful state transition, so a run can be inspected or resumed.

### Tracing and evaluation

- [ ] Instrument the graph so that **every run produces a trace**: which nodes ran, in what order, and what each one produced. You can use a tracing tool (e.g., LangSmith) or your own structured log if you don't have access to one — what matters is that the trace is queryable after the run, not just printed to the console.
- [ ] Write at least 3 **evals**: test cases with an input question and a verifiable criterion about the answer or the trace (for example: "for this question, the `retrieve` node must run before `query`"). Evals run against the trace, not against a live execution every time.
- [ ] Evals must live in `tests/pipelines/` and be runnable with a single command.

### Endpoint (`services/`)

- [ ] Expose the compiled graph through an endpoint (e.g., `POST /agent/query`) that replaces or coexists with the Milestone 7 endpoint. The endpoint must not contain its own business logic — it only invokes the graph.
- [ ] If the graph fails at any node, the endpoint responds with a clear error message, never a raw stack trace.

⚠️ **IMPORTANT:** The agent's behavior (which documents it retrieves, what it answers) must remain correct according to your Milestone 7 knowledge base. Migrating to LangGraph is not an excuse for answers to stop being grounded in your company's data.

---

## ✅ What We Will Evaluate

- [ ] The graph's state is minimal and explicit — it doesn't carry full history without justification.
- [ ] There are single-responsibility nodes for receiving the question, retrieval, and answer generation.
- [ ] Edges are defined by output conditions, not hardcoded as a fixed sequence.
- [ ] The graph is explicitly compiled before execution and fails with a clear error on a structural problem.
- [ ] There is verifiable checkpointing on at least one state transition.
- [ ] Every run produces a queryable trace, not just a final answer.
- [ ] There are at least 3 runnable evals in `tests/pipelines/`, with verifiable criteria on the trace or the answer.
- [ ] The endpoint invokes the graph without duplicating business logic and handles errors without exposing internal details.
- [ ] The Milestone 7 `retrieve`/`embed`/`query` functions are reused from `data/pipelines/`, not rewritten from scratch.

---

## 📦 How to Submit This Project

This is **Part 1 of 2**. It is submitted via its own Pull Request, independent from Part 2's (which may build on this branch, but is reviewed separately).

```text
data/
  pipelines/                    ← Milestone 7 RAG functions, reused without duplication

services/
  <agent-service>/               ← LangGraph graph, nodes, endpoint

tests/
  pipelines/                     ← agent evals
```

1. Push your branch with the structure above and open a Pull Request to the original repository with the `part-1-langgraph` label.
2. Make sure your PR includes:
   - A screenshot or export of the trace from at least one full run.
   - The output of running the evals (console or file).

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
