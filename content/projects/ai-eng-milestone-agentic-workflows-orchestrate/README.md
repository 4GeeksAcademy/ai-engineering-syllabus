# Milestone 9 — Agentic Workflow Generation (Part 1 of 3): RFP Intake & Routing

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/09-agentic-workflows)** before writing a single line of code — it defines the departments, the RFP format, and the guidelines specific to your company for this part of the milestone.

---

## 🎯 The Challenge

> 📌 You're building on top of **your own copy** of the **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** for the company you picked at the start of the course — not a brand-new repository.

You already built an agent capable of using tools, remembering context across interactions, and orchestrating itself securely through an MCP server. Now your company needs several agents to work together to solve a real business problem.

The Sales team receives dozens of RFPs (_Requests for Proposal_) in PDF every week from clients asking for a pricing proposal, and it's struggling to hit deadlines because every request needs input from several different departments — and nobody can tell, just by reading the document, who needs to be asked what. Your tech lead assigns you the following ticket: build the first stretch of an agentic workflow that receives these RFPs, determines whether they really are RFPs, and splits the work across the right agents.

> **Ticket — Agentic workflow for RFP intake and routing**
>
> > **Context:** Sales is missing deadlines because nobody knows, when an RFP comes in, which departments to involve or what each one needs. We need to automate that first analysis before we even touch generating the proposal itself (that's the next part).
> >
> > **What I need you to build:**
> >
> > - A ticket-mode interface where the team can upload the RFP (it always arrives as a PDF) and see its status in real time: analyzing, waiting for approval, done...
> > - PDF RFPs are heavy and will get expensive in tokens if we hand them to the agents as-is. I'd suggest converting them to Markdown as soon as they come in — something like Microsoft's **MarkItDown** does this well — before any agent processes them.
> > - A first classifier agent that decides whether the document is a legitimate RFP; if it isn't, the flow should stop there, without moving on to the rest of the pipeline.
> > - For each valid RFP, extract metadata and readability metrics that let us anticipate how long processing will take (`py-readability-metrics` could work for this).
> > - The rest of the flow needs to split the analysis by department using the orchestrator-worker-synthesizer pattern we covered in class — I don't want a single agent trying to do it all.
> >
> > **Acceptance criteria:** Sales should be able to look at the result of a processed RFP and know, without reading the original document, what's needed from each department and who to ask.
> >
> > — Your tech lead

### 📚 Complementary Knowledge: PDFs, readability, and "ticket mode"

Real-world RFPs arrive as PDFs, a format dense in markup and visual noise that burns far more tokens than necessary when fed directly to an LLM. Converting them to Markdown with a tool like **MarkItDown** before processing cuts that cost and gives your agents cleaner text to work with. Once the text is in Markdown, `py-readability-metrics` computes indexes like Flesch-Kincaid or Gunning Fog; use it to estimate how expensive each RFP will be to process, not as a note on literary quality. "Ticket mode" simply means every uploaded RFP becomes an entity with a lifecycle — states like `analyzing`, `waiting_for_approval`, or `done` — that the frontend can query and refresh, just like a support ticket.

### 🗺️ Visual reference: initial analysis & workstream isolation

This part of the workflow starts with rapid triage (is this an RFP / complex enough?), then an **orchestrator** decomposes the primary document into parallel workstreams (sections / departments), workers process them independently, and a **synthesizer** consolidates everything into a defined workstream structure with meta-info:

![Initial analysis and workstream isolation: triage router, RFP filter, orchestrator-worker decomposition into parallel sections, then synthesizer into defined workstream structure](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-agentic-workflows-orchestrate/.learn/rfp-intake-workstream-isolation.jpg)

---

## 🌱 How to Start the Project

Keep working on the fork of your company's monorepo that you've been using since Milestone 1. If for some reason you don't have your fork yet, create it now from the [base monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Create a new branch from your main branch: `feature/milestone-9-part-1-rfp-intake`.
2. Install any new dependencies with `uv add` (for example, `uv add markitdown` and `uv add py-readability-metrics`) — never with `pip install` or `pipenv`.
3. If you need to build or extend an interface, do it on top of `uis/backoffice` — don't create a new app.
4. Place your agent logic in `services/`, following the same pattern you used in Milestone 8.
5. Read your `CONTEXT-company.md` before defining the departments or the sample RFP format.

---

## 💻 What You Need to Do

**Intake interface (ticket mode)**

- [ ] Implement an interface in `uis/backoffice` where PDF RFP documents can be uploaded, creating a ticket for each one
- [ ] The ticket must show its current status (for example: `analyzing`, `waiting_for_approval`, `done`) and update as the flow progresses

**Document ingestion and conversion**

- [ ] Convert each RFP from PDF to Markdown before handing it to the agents (suggested: `MarkItDown` from Microsoft) to reduce token usage
- [ ] Extract metadata from the converted document (e.g., client, date, departments mentioned)
- [ ] Compute readability metrics that let you anticipate processing time (suggested: `py-readability-metrics`)

**Classifier agent**

- [ ] Implement a first agent that reads the (already converted) document and determines whether it's a valid RFP
- [ ] If the document isn't an RFP, the flow must stop and leave the ticket in an explicit discarded state (don't fail silently)

**Department orchestration**

- [ ] Implement the orchestrator-worker-synthesizer pattern: the orchestrator breaks the RFP down into per-department subtasks
- [ ] Each worker agent extracts the key aspects relevant to its department
- [ ] A synthesizer agent consolidates the results into a summary that tells Sales what to ask each department for

**Routing**

- [ ] Implement the routing of the classified document toward the rest of the agentic flow

⚠️ **IMPORTANT:** The department names, the RFP format, and the classification criteria must match what's specified in your `CONTEXT-company.md`. A generic implementation that ignores the context will not be accepted.

**Testing**

- [ ] Include unit tests in `tests/pipelines/` for the classifier agent and at least one worker agent

---

## 🧭 Design Questions

- What happens if an RFP mentions a department that doesn't exist in your `CONTEXT-company.md`? How does your classifier agent handle it?
- What does each worker agent actually need from the shared state? Are you passing it the whole document, or only what's relevant to its department?
- How do you decide that a document "isn't an RFP"? What criterion do you use, and what happens if the agent gets it wrong?
- What happens if two worker agents return contradictory information about the same section of the RFP?

---

## ✅ What We Will Evaluate

- [ ] The ticket accurately reflects the flow's real status at every moment (analyzing, waiting for approval, done, discarded)
- [ ] The classifier agent correctly rejects documents that aren't RFPs, without stopping the rest of the system
- [ ] Metadata and readability metrics are computed and stored for every processed document
- [ ] The orchestrator-worker-synthesizer pattern is implemented with clearly separated agents (not a single monolithic agent)
- [ ] The final result identifies, per department, the key aspects and who to approach — verifiable against a real test case
- [ ] Unit tests exist for the classifier agent and at least one worker agent
- [ ] The implementation uses the departments and RFP format defined in your company's `CONTEXT-company.md`

---

## 📦 How to Submit

This is Part 1 of 3 of Milestone 9. Submit it with its own Pull Request against your main branch — don't wait until Parts 2 and 3 are ready.

1. Commit and push your `feature/milestone-9-part-1-rfp-intake` branch
2. Open a Pull Request describing what you implemented and how to test it
3. Include a sample test RFP and the output your flow produces in the PR description
4. Request a review from your tech lead

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Find out more about our [Full-Stack Software Developer](https://4geeksacademy.com/us/coding-bootcamps/coding-full-time), [Data Science & Machine Learning](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering) programs.
