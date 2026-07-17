# Milestone 9 — Agentic Workflow Generation (Part 3 of 3): Approval & Document Completion

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/09-agentic-workflows)** before writing a single line of code — it contains your company's department approval hierarchy and the final document format.

---

## 🎯 The Challenge

> 📌 You're building on top of **your own copy** of the **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** for the company you picked at the start of the course — not a brand-new repository.

In Part 2 each department already generates and self-evaluates its section of the pricing proposal within the same ticket opened in Part 1. What's missing is the most delicate part: a human from each department has to sign off before the final document goes out to the client.

> **Ticket — Human approval and document completion**
>
> > **Context:** We already generate and self-evaluate every section of the proposal, but nobody is going to sign a pricing proposal without a human from each department giving the green light. This is the last piece of the flow we started in Part 1 — and it needs to feel like one continuous experience, not three projects taped together.
> >
> > **What I need you to build:**
> >
> > - Before a department's section is considered approved, the flow must go through a real human approval point — an actual human-in-the-loop, not just one more automatic evaluator.
> > - The flow must pause right before that irreversible action, persist its state with a checkpointer, and be able to resume exactly where it left off once the approval comes in — not restart from scratch.
> > - That pause should only affect the branch for the department that's waiting on approval; the other departments whose sections are already ready should be able to keep moving in parallel, not get blocked by each other.
> > - Define an iteration limit and an explicit arbitration node for disagreements between departments — don't let the agents sort it out on their own.
> > - Once every department has given its sign-off, the final document should generate itself, consolidating the approved sections.
> > - I want to be able to see, for any run, which agent did what and in what order, because when something breaks in production we won't have time to guess.
> >
> > Once you're done, run the complete flow end to end — from uploading the RFP in Part 1 to generating the final document here — and check that it feels like a single process: no weird state jumps, no messages that don't match up between parts, no steps that break in the handoff from one part to the next.
> >
> > **Acceptance criteria:** An RFP can travel through all three parts end to end, pause for human approval per department without blocking the others, and finish with a final document generated automatically, with full traceability of every step.
> >
> > — Your tech lead

### 📚 Complementary Knowledge: when to interrupt and when to use a guardrail

Not every control needs to pause the flow for a human. Guardrails (automated schema, type, or business validations) should resolve the clear-cut cases on their own; save interruptions (`interrupt`) for decisions that genuinely require human judgment, like approving a pricing proposal before it goes to a client. And when you do interrupt, keep it scoped: the interruption should only pause the branch of the graph that depends on that approval (that department's section and whatever depends on it), not the entire flow — one department waiting on their manager's sign-off shouldn't stall the others that are already ready to move forward.

### 🗺️ Visual reference: approval tickets & ultimate document synthesis

Once department assignment tickets from Part 2 are **fully approved**, an **ultimate document synthesizer** compiles the final agreed-upon document and delivers it to Sales — parallel department branches approve independently, then converge:

![Approval and document completion: department assignment tickets with approval status converge into ultimate document synthesizer, producing the final agreed-upon document for the Sales team](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-agentic-workflows-produce/.learn/approval-document-completion.jpg)

---

## 🌱 How to Start the Project

Continue on your Milestone 9 branch in your company's monorepo fork, picking up from where you submitted Part 2. If you don't have your fork yet, create it from the [base monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Create the `feature/milestone-9-part-3-approval-completion` branch from your Part 2 branch.
2. Set up the checkpointer that fits your environment (SQLite or Postgres — avoid the in-memory checkpointer outside of local development).
3. Install any new dependencies with `uv add`.
4. Review your `CONTEXT-company.md` to learn your company's department approval hierarchy.

---

## 💻 What You Need to Do

**Human approval per department**

- [ ] Implement an interruption point (`interrupt`) before a department's section is considered approved
- [ ] The interruption must pause only the branch of the graph corresponding to that department, without blocking the departments that are already done
- [ ] Persist the flow's state with a checkpointer before each interruption, so execution is resumable
- [ ] Implement `resume` as an explicit entry point into the graph — not as a restart of the entire flow
- [ ] Validate the human response on resume (approve, reject, or request changes) before letting it back into the graph
- [ ] Extend the ticket interface built in Part 1 (`uis/backoffice`) so each department can log its approval or rejection

**Guardrails and flow control**

- [ ] Define a maximum iteration limit on any remaining loop between departments
- [ ] Implement an explicit arbitration node to resolve disagreements between departments, instead of letting the agents settle it themselves
- [ ] Log the agent, input, output, and timestamp in the state for every node execution (traceability)

**Document completion**

- [ ] Once every department has given approval, generate the final document by consolidating the approved sections
- [ ] Update the ticket to its final status (for example: `done`) and make the generated document accessible

**End-to-end review**

- [ ] Run at least one test RFP through all three complete parts (intake → generation → approval and completion) and confirm that ticket states, messages, and data stay consistent from start to finish
- [ ] Fix any jump, inconsistent message, or data loss in the transition between parts

⚠️ **IMPORTANT:** The department approval hierarchy and the final document format must match what's specified in your `CONTEXT-company.md`. A generic implementation that ignores the context will not be accepted.

**Testing**

- [ ] Include unit tests in `tests/pipelines/` covering: successful interruption and resume, iteration limit reached, and arbitration on disagreement

---

## 🧭 Design Questions

- What happens if a department rejects its section after the interruption? Does the flow go back to the Part 2 generator, or does it require a new run?
- How do you namespace your `thread_id` so concurrent runs from different RFPs don't corrupt each other's checkpoint?
- What's the minimum information a human needs to see at the approval point to decide with confidence, without having to reread the entire document?
- If two interdependent departments return contradictory results, who arbitrates, and by what rule?

---

## ✅ What We Will Evaluate

- [ ] The flow correctly pauses before each department's approval and persists its state
- [ ] The pause only affects the corresponding department's branch — other departments can keep moving without getting blocked
- [ ] Execution resumes exactly from the interruption point, without restarting the entire flow
- [ ] An iteration limit is applied and verifiable in the code, not just mentioned
- [ ] An explicit arbitration node exists for disagreements between departments
- [ ] Every node execution is logged with agent, input, output, and timestamp
- [ ] The final document is generated automatically only once every department has given approval
- [ ] The ticket reflects the final status of the process and provides access to the generated document
- [ ] A test RFP can be traced end to end (Part 1 through Part 3) with no state jumps or visible inconsistencies between parts
- [ ] Unit tests exist for interruption/resume, the iteration limit, and arbitration

---

## 📦 How to Submit

This is Part 3 of 3 of Milestone 9. Submit it with its own Pull Request.

1. Commit and push your `feature/milestone-9-part-3-approval-completion` branch
2. Open a Pull Request describing what you implemented and how to test it
3. Include a complete example in the PR description: the input RFP, simulated approval from each department, and the generated final document
4. Request a review from your tech lead

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Find out more about our [Full-Stack Software Developer](https://4geeksacademy.com/us/coding-bootcamps/coding-full-time), [Data Science & Machine Learning](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering) programs.
