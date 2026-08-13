# Milestone — Agentic RFP Workflow: Response Generation (Part 2 of 3)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/09-agentic-workflows)** before writing a single line of code — it contains the concrete guidelines your evaluator agents must validate against.

---

## 🎯 Your challenge

> 📌 You're building on top of **your own copy** of the **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** for the company you picked at the start of the course — not a brand-new repository.

In Part 1 you already have a flow that classifies each RFP and opens a ticket for it, making it clear to Sales what's needed from each department. Now Sales wants to go one step further: turn that analysis directly into a first draft of the pricing proposal, automatically reviewed before a human ever sees it.

> **Ticket — RFP response generation and evaluation**
>
> > **Context:** Part 1 tells us what needs to be answered in each RFP, but putting together the draft of the pricing proposal is still manual and slow. I need the system to generate a first draft per department and have that draft self-evaluate before it reaches a human.
> >
> > **What I need you to build:**
> >
> > - A generator agent per department that receives the metadata and summary produced in Part 1, and drafts the corresponding section of the pricing proposal.
> > - Several evaluator agents running in parallel over each generated section: readability (again, `py-readability-metrics` works for this), relevance to what the RFP is asking for, and compliance with our company guidelines.
> > - If a section fails evaluation, it should go back to the corresponding generator with concrete feedback on what to fix — it shouldn't get stuck, and the ticket shouldn't be discarded entirely.
> > - An iteration limit on that generator-evaluator loop, so it doesn't repeat indefinitely if a generator can't pass evaluation. If a section hits that limit without passing, keep the last draft and its evaluation result, mark it `needs_human_review`, and still include it in the Part 3 handoff — never discard the whole ticket.
> > - _Optional:_ if you already have the semantic knowledge base set up, give the generator access to it — drafting with our real policies and tone instead of improvising them makes it much more likely to pass the compliance check on the first try. Not required for this part, but use it if you have it.
> >
> > **Acceptance criteria:** The handoff to Part 3 must include, for every department, both the generated content and a structured evaluation result (see schema below). Sections that exhausted the iteration limit ship with `needs_human_review` — they are not dropped.
> >
> > — Your tech lead

### 📚 Complementary Knowledge: guideline compliance

When the ticket asks an evaluator to check "compliance with company guidelines," it doesn't mean a free-form style judgment: your `CONTEXT-company.md` includes a concrete list of rules (tone, data that can't be missing, figures that must appear) that the evaluator must check the generated content against — not the agent's subjective opinion. If your company already has a semantic knowledge base, it's a good place for the generator to look up real policies, reference pricing, or brand language before drafting — it cuts down on how often the evaluator bounces a section for inventing something that doesn't match what the company actually says. This is a suggested improvement, not a requirement of this part.

**Ticket statuses for this part** (same ticket row as Part 1 — match CONTEXT names). Full lifecycle is in CONTEXT; **here you only need:**

| Status               | Role              | When                                                                        |
| -------------------- | ----------------- | --------------------------------------------------------------------------- |
| `intake_complete`    | Entry from Part 1 | Start here via Part 1 routing handoff — do not rewrite this status          |
| `drafting`           | Part 2 sets       | Generators writing proposal sections                                        |
| `under_evaluation`   | Part 2 sets       | Parallel evaluators / generator-evaluator loop                              |
| `needs_human_review` | Part 2 sets       | Iteration limit exhausted; last draft + EvaluationResult hand off to Part 3 |

Do **not** invent Part 3 statuses (`waiting_for_approval`, `done`) in this part.

### 🗺️ Visual reference: departmental mapping & deliverable finalization

This stretch of the workflow takes the **defined workstream structure** from Part 1, maps tasks to departments via an **assignment orchestrator**, runs department-scoped generation in parallel, then a **synthesizer** consolidates outputs into department-specific assignment tickets ready for evaluation / approval:

![Departmental mapping and deliverable finalization: assignment orchestrator maps workstreams to Sales, Legal & Compliance, and Operations & Delivery, then synthesizer produces department assignment tickets](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-agentic-workflows-evaluate/.learn/departmental-mapping-deliverable-finalization.jpg)

---

## 🌱 How to Start the Project

Continue on the same Milestone working branch in your monorepo fork (or create `feature/rfp-response-generation` from the branch where you submitted Part 1). If you don't have your fork yet, create it from the [base monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Build on top of the classification and routing flow you built in Part 1 — don't rewrite it from scratch.
2. **Consume Part 1's routing handoff** — Part 2 must start from tickets that Part 1 marked ready (status `intake_complete` plus the queue flag / DB field / handoff contract you defined). Input = `ticket_id` + synthesizer payload (`key_aspects` / workstream structure). Do **not** re-parse the PDF or invent a parallel summary path that ignores that contract.
3. Install any new dependencies with `uv add`.
4. Review your `CONTEXT-company.md` again: it contains the concrete guidelines your evaluator agents must validate against.

---

## 💻 What You Need to Do

**Consume Part 1 routing**

- [ ] Part 2 entry reads Part 1's routing handoff (`ticket_id` + synthesizer / `key_aspects` payload, via the queue flag, DB field, or documented contract from Part 1) — generators must not re-ingest the raw PDF as their primary input

**Per-department generation**

- [ ] Implement a generator agent per department that receives the relevant summary produced in Part 1 (from that handoff)
- [ ] The generator agent must produce content specific to its department's section of the pricing proposal

> 💡 _Optional:_ if your company already has a semantic knowledge base, you can give the generator access to it so it drafts with real policies and brand language. This isn't a requirement of this part and isn't graded as one — it's an improvement that can reduce how often a section bounces back during evaluation.

**Parallel evaluation**

- [ ] Implement multiple evaluator agents that run in parallel over each generated section
- [ ] At least one evaluator must check readability (suggested: `py-readability-metrics`)
- [ ] At least one evaluator must check relevance (that the content actually answers what the RFP asks for)
- [ ] At least one evaluator must check compliance with the guidelines defined in your `CONTEXT-company.md`
- [ ] Persist each section's evaluation as a structured `EvaluationResult` (field names may vary slightly; shape must be equivalent):

```text
EvaluationResult:
  section_id / department_id
  readability: { pass, score, details }
  relevance: { pass, missing_aspects[] }
  compliance: { pass, rule_ids[], violations[] }
  overall_pass: bool
  feedback_for_generator: string   # concrete and actionable
```

**Generator-evaluator loop**

- [ ] If a section fails evaluation, the flow must return it to the corresponding generator agent along with `feedback_for_generator` from the `EvaluationResult`
- [ ] Define and enforce an iteration limit to prevent the generator-evaluator loop from repeating indefinitely
- [ ] When the limit is hit without a pass: keep the last draft + its `EvaluationResult`, set the section (and ticket if needed) to `needs_human_review`, and still include it in the Part 3 handoff — do not discard the ticket

**Ticket status**

- [ ] Update the ticket created in Part 1 (from `intake_complete`) to reflect generation and evaluation progress (`drafting`, `under_evaluation`, `needs_human_review`). Persist drafts and `evaluation_results` in PostgreSQL. Still no new API: extend the existing backend and the pipeline under `data/pipelines/`.

⚠️ **IMPORTANT:** The company guidelines you evaluate generated content against, and the expected format of each section, must match what's specified in your `CONTEXT-company.md`. A generic implementation that ignores the context will not be accepted.

**Testing**

- [ ] Include unit tests in `tests/pipelines/` for at least one generator agent and one evaluator agent, including a case where evaluation fails
- [ ] Add one compliance-failure case tied to a rule from your `CONTEXT-company.md` (e.g. a draft that promises something the guidelines forbid → `compliance.pass == false`). Keep it small: one fixture, one assertion on fail — no full loop required for this case

---

## 🧭 Design Questions

- What state information does each evaluator agent actually need? Are you passing it only the section it should review, or the entire document?
- How do you prevent two parallel evaluators from conflicting when writing their results to the shared state?
- When a section hits `needs_human_review` after exhausting iterations, how do you surface that to Sales so they know which draft is provisional?
- Is the feedback the generator receives after a failure specific enough to fix the real problem, or is it generic?

---

## ✅ What We Will Evaluate

- [ ] Each department has its own generator agent, clearly separated from the others
- [ ] Part 2 consumes Part 1's routing handoff (`ticket_id` + synthesizer / `key_aspects` payload) — does not re-parse the PDF as the primary generator input
- [ ] Evaluators run in parallel and don't block execution across other departments
- [ ] The system correctly applies the generator-evaluator loop, including the iteration limit and `needs_human_review` handoff when exhausted
- [ ] The ticket accurately reflects generation and evaluation progress in real time
- [ ] Evaluation output follows the `EvaluationResult` shape (structured readability / relevance / compliance — not unstructured free text)
- [ ] Drafts and `evaluation_results` are persisted in PostgreSQL; still one backend API under `services/` (no second HTTP service)
- [ ] Unit tests cover success, a generic evaluation-failure case, and one CONTEXT-anchored compliance failure
- [ ] The implementation uses the guidelines and formats defined in your company's `CONTEXT-company.md`

---

## 📦 How to Submit

This is Part 2 of 3 of Milestone. Submit it with its own Pull Request — don't wait until Part 3 is ready.

1. Commit and push your `feature/rfp-response-generation` branch
2. Open a Pull Request describing what you implemented and how to test it
3. Include an example of a generated section in the PR description: one that passes evaluation and one that fails
4. Request a review from your tech lead

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Find out more about our [Full-Stack Software Developer](https://4geeksacademy.com/us/coding-bootcamps/coding-full-time), [Data Science & Machine Learning](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering) programs.
