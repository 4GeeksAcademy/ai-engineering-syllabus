# Milestone 9 — Agentic Workflow Generation (Part 2 of 3): RFP Response Generation

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/09-agentic-workflows)** before writing a single line of code — it contains the concrete guidelines your evaluator agents must validate against.

---

## 🎯 The Challenge

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
> > - An iteration limit on that generator-evaluator loop, so it doesn't repeat indefinitely if a generator can't pass evaluation.
> > - _Optional:_ if you already have the semantic knowledge base set up, give the generator access to it — drafting with our real policies and tone instead of improvising them makes it much more likely to pass the compliance check on the first try. Not required for this part, but use it if you have it.
> >
> > **Acceptance criteria:** The handoff to Part 3 must include, for every department, both the generated content and the result of its evaluation.
> >
> > — Your tech lead

### 📚 Complementary Knowledge: guideline compliance

When the ticket asks an evaluator to check "compliance with company guidelines," it doesn't mean a free-form style judgment: your `CONTEXT-company.md` includes a concrete list of rules (tone, data that can't be missing, figures that must appear) that the evaluator must check the generated content against — not the agent's subjective opinion. If your company already has a semantic knowledge base, it's a good place for the generator to look up real policies, reference pricing, or brand language before drafting — it cuts down on how often the evaluator bounces a section for inventing something that doesn't match what the company actually says. This is a suggested improvement, not a requirement of this part.

### 🗺️ Visual reference: departmental mapping & deliverable finalization

This stretch of the workflow takes the **defined workstream structure** from Part 1, maps tasks to departments via an **assignment orchestrator**, runs department-scoped generation in parallel, then a **synthesizer** consolidates outputs into department-specific assignment tickets ready for evaluation / approval:

![Departmental mapping and deliverable finalization: assignment orchestrator maps workstreams to Sales, Legal & Compliance, and Operations & Delivery, then synthesizer produces department assignment tickets](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-agentic-workflows-evaluate/.learn/departmental-mapping-deliverable-finalization.jpg)

---

## 🌱 How to Start the Project

Continue on the same Milestone 9 working branch in your monorepo fork (or create `feature/milestone-9-part-2-rfp-response` from the branch where you submitted Part 1). If you don't have your fork yet, create it from the [base monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Build on top of the classification and routing flow you built in Part 1 — don't rewrite it from scratch.
2. Install any new dependencies with `uv add`.
3. Review your `CONTEXT-company.md` again: it contains the concrete guidelines your evaluator agents must validate against.

---

## 💻 What You Need to Do

**Per-department generation**

- [ ] Implement a generator agent per department that receives the relevant summary produced in Part 1
- [ ] The generator agent must produce content specific to its department's section of the pricing proposal

> 💡 _Optional:_ if your company already has a semantic knowledge base, you can give the generator access to it so it drafts with real policies and brand language. This isn't a requirement of this part and isn't graded as one — it's an improvement that can reduce how often a section bounces back during evaluation.

**Parallel evaluation**

- [ ] Implement multiple evaluator agents that run in parallel over each generated section
- [ ] At least one evaluator must check readability (suggested: `py-readability-metrics`)
- [ ] At least one evaluator must check relevance (that the content actually answers what the RFP asks for)
- [ ] At least one evaluator must check compliance with the guidelines defined in your `CONTEXT-company.md`

**Generator-evaluator loop**

- [ ] If a section fails evaluation, the flow must return it to the corresponding generator agent along with the reasons for failure
- [ ] Define and enforce an iteration limit to prevent the generator-evaluator loop from repeating indefinitely

**Ticket status**

- [ ] Update the ticket created in Part 1 to reflect generation and evaluation progress (for example: `drafting`, `under_evaluation`)

⚠️ **IMPORTANT:** The company guidelines you evaluate generated content against, and the expected format of each section, must match what's specified in your `CONTEXT-company.md`. A generic implementation that ignores the context will not be accepted.

**Testing**

- [ ] Include unit tests in `tests/pipelines/` for at least one generator agent and one evaluator agent, including the case where evaluation fails

---

## 🧭 Design Questions

- What state information does each evaluator agent actually need? Are you passing it only the section it should review, or the entire document?
- How do you prevent two parallel evaluators from conflicting when writing their results to the shared state?
- What happens if a generator agent hits the iteration limit without passing evaluation? What does the ticket show Sales in that case?
- Is the feedback the generator receives after a failure specific enough to fix the real problem, or is it generic?

---

## ✅ What We Will Evaluate

- [ ] Each department has its own generator agent, clearly separated from the others
- [ ] Evaluators run in parallel and don't block execution across other departments
- [ ] The system correctly applies the generator-evaluator loop, including the iteration limit
- [ ] The ticket accurately reflects generation and evaluation progress in real time
- [ ] The evaluation criteria (readability, relevance, guidelines) are implemented in a verifiable way, not as unstructured free text
- [ ] Unit tests exist covering both the success case and the evaluation-failure case
- [ ] The implementation uses the guidelines and formats defined in your company's `CONTEXT-company.md`

---

## 📦 How to Submit

This is Part 2 of 3 of Milestone 9. Submit it with its own Pull Request — don't wait until Part 3 is ready.

1. Commit and push your `feature/milestone-9-part-2-rfp-response` branch
2. Open a Pull Request describing what you implemented and how to test it
3. Include an example of a generated section in the PR description: one that passes evaluation and one that fails
4. Request a review from your tech lead

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Find out more about our [Full-Stack Software Developer](https://4geeksacademy.com/us/coding-bootcamps/coding-full-time), [Data Science & Machine Learning](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering) programs.
