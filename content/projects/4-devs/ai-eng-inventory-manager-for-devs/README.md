# Operations Backoffice – Inventory Manager

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/4-devs/inventory-manager-for-devs)** before writing a single spec — it defines the units of measure, categories, lots, and reorder points concrete to your implementation.

---

## 🎯 The Challenge

> 📌 You're building on **your copy** of the company **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** you selected at the start of the course — not a new repository.

You already left the repository prepared with project rules and a memory bank. Now your CTO brings the first real business requirement: an inventory manager. Unlike the previous exercise, here it isn't enough for the agent to understand the project — it needs instructions that leave no room for interpretation at the points where a wrong interpretation is expensive.

Inventory has a property that makes it different from almost any other CRUD: an item's available stock **isn't data, it's a calculation**. It's derived from the sum of its movements — inbound, outbound, adjustments — and it is never edited directly. This is exactly the kind of rule a coding agent silently violates without explicit instructions: it will generate an editable `stock` field because that's the pattern it has seen a thousand times, and the result will look correct until someone makes a manual adjustment and the number stops matching the history. By the time anyone notices, there's already functionality built on top of the mistake.

A loose prompt — "build me an inventory CRUD" — doesn't carry that rule inside it. A well-written spec does. That's the bet of this project: when it's the agent who writes the code, the highest-value artifact you produce is no longer the code — it's the specification that governs it.

You're going to work with **Spec Driven Development (SDD)**: instead of giving the agent step-by-step orders, you're going to produce three layers — **spec** (the what: behavior, contracts, invariants), **plan** (the how: architectural decisions), and **tasks** (the order: atomic, verifiable units) — and let implementation stick to those layers. The loop is: `specify → plan → tasks → implement → verify`.

There's a common trap in this exercise: writing vibe coding with extra steps — a one-line spec, jumping straight to asking the agent to implement, and calling that Spec Driven Development because a file is involved. A spec isn't a long prompt. It's a contract that someone else — a teammate, an agent, you in three weeks — can read and verify without asking you anything.

The opposite trap is writing 20 pages of spec for a CRUD. Spec formality should be proportional to the size of the change, the risk, and the number of people affected — not every requirement needs the same level of ceremony. The three layers you're building here are justified because the stock invariant justifies them; don't repeat that level of detail for every trivial field in an item's form.

> **From:** your CTO
> **Subject:** first business requirement — inventory
>
> > Before the agent writes a single line of code for this module, I want to see the spec. Not the code — the spec. That's the artifact I'm going to review and approve, and only after approval do we move to implementation.
> >
> > The requirement, in one sentence: the operations team needs to register inventory items, log their inbound, outbound, and adjustment movements, and know at all times what's below the reorder point. Entity names, units of measure, and domain values come from your CONTEXT, not from your imagination.
> >
> > There's one thing that's not negotiable, and I want it as an explicit acceptance criterion, not a side note: an item's stock is calculated from its movements. There is no endpoint, no form field, and no operation that edits stock directly. If your spec doesn't say that with that level of clarity, the agent is going to get it wrong, and it won't be its fault.
> >
> > Write the acceptance criteria in EARS format — I want verifiable sentences, not descriptions. Break the work into tasks small enough that each one can be verified independently; the bigger the unit you hand the agent, the more it diverges from what you asked for.
> >
> > Once spec, plan, and tasks are approved, here's what happens next: I'm going to send you a requirement change mid-stream, like always happens. When it lands, the spec gets edited first and the affected tasks get regenerated from there — never the other way around. If I find you patching code without having touched the spec first, that part gets discarded and redone.
> >
> > Every task needs to stay connected to the acceptance criterion it verifies and the commit that implements it. I want to be able to go from a requirement to its test and from a test to its commit without having to ask you anything.
>
> — Handoff to the operations team as soon as the verification suite is green.

### Supplementary knowledge: EARS and the three layers

**EARS (Easy Approach to Requirements Syntax)** is a structured way to write acceptance criteria so they stop being ambiguous. The most common templates:

- **Ubiquitous**: "The system shall [behavior]." — always holds, no condition.
- **Event-driven**: "When [event], the system shall [behavior]."
- **State-driven**: "While [state], the system shall [behavior]."
- **Unwanted behavior**: "If [unwanted condition], then the system shall [behavior]."
- **Optional**: "Where [optional feature], the system shall [behavior]."

The **three layers** of a spec don't belong in a single document: mixing them is a recognized anti-pattern. The _spec_ describes behavior, contracts, and invariants — the what. The _plan_ translates that into architectural decisions — the how. The _tasks_ break the plan down into atomic units, independently testable — the order. When a requirement changes, the spec gets edited, and only the affected tasks get regenerated from there — you never patch the code first and adjust the spec afterward to match.

The spec doesn't replace the test suite — it originates it. The code remains the executable truth; the tests are the mechanism that checks that truth fulfills what the spec promised.

---

## 🌱 How to Start the Project

1. Work on your copy of the company monorepo. Create the `feature/inventory-manager` branch.
2. Before writing any spec, review the `.agents/rules` and `memory-bank/` that already exist in your repository — the spec shouldn't repeat what's already documented there, it should build on it.
3. Follow the `specify → plan → tasks → implement → verify` loop in that order. Don't start implementing before spec and plan are approved.
4. Make a separate commit for each implemented task, referencing its identifier. The history is part of the deliverable.

---

## 💻 What You Need to Do

### Phase 1 — Specify

- [ ] Create `specs/inventory-manager/spec.md` with the behavior, contracts, and invariants of the inventory manager.
- [ ] Write the acceptance criteria in EARS format, each with a unique identifier (e.g. `INV-001`).
- [ ] Explicitly include the stock invariant as an acceptance criterion: stock is derived from movements, never edited directly.
- [ ] Define unwanted behavior: what should happen when a movement would leave stock negative, or when an outbound movement is attempted on a nonexistent item or lot.

### Phase 2 — Plan

- [ ] Create `specs/inventory-manager/plan.md` with the architectural decisions needed to fulfill the spec: data model, how available stock is calculated, where that logic lives.
- [ ] Justify any decision that isn't obvious from the spec — the plan explains the how, it doesn't repeat the what.

### Phase 3 — Tasks

- [ ] Create `specs/inventory-manager/tasks.md` with atomic tasks, independently verifiable.
- [ ] Each task references the identifier of the acceptance criterion (spec) it implements.
- [ ] No task bundles more than one unrelated acceptance criterion — if a task is hard to verify in isolation, it's too big.

### Phase 4 — Implement

- [ ] Implement the tasks in the defined order, without skipping the plan or improvising new scope directly with the agent.
- [ ] Implement creation, editing, listing, and deletion of inventory items, with the fields defined in your CONTEXT.
- [ ] Implement stock movement logging: inbound, outbound, and adjustment, each with its reason and timestamp.
- [ ] An item's available stock is calculated from its movements — no operation edits it directly.
- [ ] Implement a reorder point per item and a visible signal in the backoffice when stock falls below it.
- [ ] Respect the stack and conventions already shipped in the monorepo.

### Phase 5 — Verify

- [ ] Write a test suite that verifies each acceptance criterion in the spec, including the stock invariant and the unwanted behaviors.
- [ ] Every implementation commit must stay connected to the task and the acceptance criterion it verifies.
- [ ] Review the agent-generated code before committing. Blind trust in its proactivity is an anti-pattern, not a shortcut.

### Requirement Change

- [ ] When the requirement change arrives (see delivery checklist), edit `spec.md` first, then update `plan.md` if applicable, and regenerate only the tasks in `tasks.md` affected by the change.
- [ ] Document in the Pull Request which spec sections changed and which tasks were regenerated as a result — don't rewrite the whole spec for a one-off change.

---

## ✅ What We'll Evaluate

- [ ] `spec.md`, `plan.md`, and `tasks.md` exist in `specs/inventory-manager/`, each with content proper to its layer — no mixing of behavior, architecture, and tasks into a single document.
- [ ] Acceptance criteria are written in EARS format, are verifiable, and have a unique identifier.
- [ ] The invariant "stock is derived from movements, never edited directly" is explicit as an acceptance criterion and is verified by at least one test.
- [ ] Criteria and tests exist for unwanted behavior: a movement that would leave stock negative, a movement on a nonexistent item or lot.
- [ ] Each task in `tasks.md` references the acceptance criterion it implements, and each implementation commit references its task.
- [ ] The test suite verifies the spec's acceptance criteria, not just the happy path.
- [ ] The inventory manager allows registering items and logging inbound, outbound, and adjustment movements, with the entity names and domain values from the assigned company's CONTEXT.
- [ ] The backoffice visibly flags items below the reorder point.
- [ ] The requirement change was resolved by editing the spec first and regenerating only the affected tasks — there's no evidence of code patches without an updated spec.
- [ ] Commit history separates the development tasks; there is no single commit bundling all the work.

---

## 📦 How to Deliver

Push your `feature/inventory-manager` branch to your copy of the monorepo and open a Pull Request against the main branch.

In the Pull Request description, include:

- Link to `specs/inventory-manager/spec.md`, `plan.md`, and `tasks.md`.
- The `requirement → test → commit` traceability table or list.
- Which spec sections changed as a result of the requirement change and which tasks were regenerated.

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Find out more about our [courses](https://4geeksacademy.com/us/coding-bootcamps) in [Full-Stack Software Development](https://4geeksacademy.com/us/coding-bootcamps/full-stack-developer), [Data Science & Machine Learning](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering).
