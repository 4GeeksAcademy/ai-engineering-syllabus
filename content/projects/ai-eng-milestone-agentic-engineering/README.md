# Milestone 8 — Agent Memory and Self-Improvement

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/08-agent-engineering/memory)** — it defines what information must never enter your agent's memory, and what kinds of facts are actually worth remembering at your company.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

Your agent already knows the company (RAG), calls tools through the MCP Server, and stays inside its security guardrail. The problem is that every conversation starts from zero: it doesn't remember that a similar escalation was resolved yesterday, or that a user already corrected a piece of data last week. Your tech lead opened a **ticket** after two different clients had to repeat the same correction three times in the same week.

It's not a coincidence that this project comes right after the guardrails sprint, and not before. Without guardrails, a manipulation attempt damages a single conversation; with persistent memory but no prior protection, that same attempt could get written into the memory store and repeat itself in every future conversation — the error stops being a one-off and becomes cumulative. That's why the agent was hardened against manipulation in the previous sprint first, and only now does it gain the ability to remember and self-improve.

### 🧠 Complementary Knowledge: Memory Architectures

An agent's memory isn't a single component — it's organized by temporal scope. The context window is enough when the task fits in a single session. Episodic memory (Redis, key-value, prompt caching) lets the agent remember past interactions and personalize. A VectorDB retrieves semantically similar information across large corpora. Knowledge graphs matter when explicit relationships (dependency, hierarchy) are the actual retrieval requirement — something cosine similarity can't capture. Fine-tuning (parametric memory) is the last resort: expensive, slow to update, and it doesn't let you selectively "forget." No self-improving memory architecture works without a cleanup and consolidation cycle — without curation, raw accumulation degrades retrieval quality over time.

> **From: Tech Lead — Ticket #MEM-092**
>
> The agent already knows the company, uses the MCP Server's tools, and stays inside its guardrail. But every conversation starts from zero: it doesn't remember that we resolved a similar escalation yesterday, or that someone already corrected a piece of data last week. I need the agent to learn from interaction, without that meaning it starts making things up or piling junk into its memory forever.
>
> You don't need a new graph or a multi-agent architecture for this — it's the same agent as always, with one extra self-evaluation step:
>
> 1. When the agent detects, within its own response, something worth remembering, it proposes it to the user in the same conversation ("want me to remember this for next time?") instead of writing it straight to memory.
> 2. That decision — yes, no, or an edit — can't be a fuzzy interpretation of the next message. It has to be explicitly classified against the pending proposal and logged: what was proposed, what the user decided, and when. If the decision can't be determined with reasonable confidence, the proposal is discarded by default — approval is never assumed from silence or ambiguity.
> 3. Only what's approved and logged gets consolidated into the persistent store; what's rejected is discarded, but the record that it was proposed and rejected stays.
>
> I won't accept a memory that grows without limit, that self-edits without the user knowing, or a memory write with no trace of who authorized it.

---

## 🌱 How to Start the Project

1. If you already have your fork of the company's monorepo, create a new branch from your latest progress (previous milestone or day).
2. If for some reason you don't have a fork yet (for example, you joined late or lost it), fork the [reference monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) before continuing.

```bash
git checkout -b w23-d67-agent-memory
```

3. Keep building on the same LangGraph agent that already exposes the MCP Server and applies guardrails — this project doesn't replace that base, it extends it.
4. Install any new dependency with `uv add` (never `pip install` or `pipenv`).

---

## 💻 What You Need to Do

### Memory Architecture Selection

- [ ] Choose a persistent memory backend (e.g. Redis, a key-value store, a VectorDB, or a combination) and document in writing why it fits what your agent needs to remember at your company.
- [ ] Implement an explicit read/write memory interface — the agent must not accumulate state by simply appending everything to the system prompt.

⚠️ **IMPORTANT:** Which facts are memorable and which are strictly forbidden to store must match exactly what's specified in your CONTEXT-company.md. A generic implementation that ignores those restrictions will not be accepted.

### Self-Evaluation and Memory Proposal

- [ ] After each relevant interaction, the agent must self-evaluate whether there's something new or corrected worth remembering, using an explicit criterion (not simply "always").
- [ ] The simplest way to solve this is to ask the model for **structured output in a single call**: the response the user sees, plus a `memory_proposal` field (if applicable, what would be added/changed and why). You don't need a second model call, a separate agent, or a multi-agent architecture — it's the same agent with one additional output field.
- [ ] The agent must be able to dismiss most interactions as "nothing to remember" — document at least 3 examples of interactions that should NOT generate a proposal.
- [ ] When there is something memorable, the agent **proposes it to the user within its own response** (for example, as a question at the end) — it never writes directly to memory at this step.

### User Confirmation and Auditable Log

- [ ] When there's a pending memory proposal, the user's next message must first be evaluated against that proposal: does it approve, reject, or edit it? Reuse the same kind of intent classification you already implemented for sensitive responses in the guardrails sprint — not a plain `"yes" in message`.
- [ ] There can only be **one pending proposal at a time**: if one is already unresolved, the agent must not launch a second one until the first is closed.
- [ ] If the user changes topic without clearly responding yes or no, the proposal is discarded by default — approval is never assumed from silence or ambiguity.
- [ ] Every decision (proposal, outcome, originating message, timestamp) is logged in an auditable way, regardless of whether the proposal was approved or rejected.
- [ ] After resolving the pending proposal (in the same turn or a later one), the conversation continues normally — including cases where the user answers the proposal and asks another question in the same message.

### Consolidation and Cleanup

- [ ] Implement a consolidation mechanism that keeps memory from growing without control (e.g., summarizing, deduplicating, or discarding low-relevance entries).
- [ ] Document the expiration or cleanup policy you applied and why you chose it.

### Evidence

- [ ] Document at least two complete cycles of the flow: one where a memory update is approved and reflected in a future interaction, and one where it's rejected and memory stays unchanged.

---

## 🎨 Design Decisions

As part of the challenge, your implementation must resolve — without being told explicitly in a checklist — the following decisions:

- What kind(s) of memory (episodic, semantic/vector, knowledge graph) does your company actually need, and why did you rule out the other options?
- What information should never enter the agent's memory, no matter who asks for it? Check your CONTEXT — some companies have non-negotiable restrictions here.
- How does the agent decide what to forget, and what happens to a pending proposal if the user never responds?
- How do you prevent a malicious user from "poisoning" the agent's memory with false information presented as a legitimate correction?
- Why doesn't this require a multi-agent architecture to solve self-evaluation and the memory proposal? Justify your answer with what you implemented.

---

## ✅ What We Will Evaluate

- [ ] The chosen memory architecture is justified in writing and matches what the agent actually needs to remember.
- [ ] There's an explicit read/write memory interface (not implicit memory via the system prompt).
- [ ] The agent correctly distinguishes memorable interactions from non-memorable ones, with at least 3 documented examples of each type.
- [ ] The memory proposal is communicated within the same conversation, not through a separate channel or process.
- [ ] No memory update is written without an explicit, correctly classified user decision (not a naive text match).
- [ ] Only one proposal is pending at a time, and silence or ambiguity resolves as rejection by default, not approval.
- [ ] Every proposal and its outcome are logged in an auditable way, regardless of whether it was approved or rejected.
- [ ] There's a documented, functional consolidation/cleanup mechanism.
- [ ] At least two complete evidence cycles are delivered (one approved, one rejected).
- [ ] The design decisions explicitly address the restrictions in your CONTEXT-company.md, especially what must never be remembered.

---

## 📦 How to Submit

Follow the standard Pull Request flow against your own fork of the monorepo:

- [ ] Open a PR from `w23-d67-agent-memory` to your main branch.
- [ ] Include in the PR description the justification for your memory architecture and the answers to the design decisions.
- [ ] Attach or describe the evidence for both complete cycles (approved and rejected).

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Find out more about our [programs](https://4geeksacademy.com/us/coding-bootcamps) in [Full-Stack Software Development](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering).
