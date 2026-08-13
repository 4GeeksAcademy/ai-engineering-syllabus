# Milestone — Agentic RFP Workflow: Intake & Routing (Part 1 of 3)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/09-agentic-workflows)** before writing a single line of code — it defines the departments, the RFP format, persistence rules, and the guidelines specific to your company for this part of the milestone.

---

## 🎯 Your challenge

> 📌 You're building on top of **your own copy** of the **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** for the company you picked at the start of the course — not a brand-new repository.

You already built an agent capable of using tools, remembering context across interactions, and orchestrating itself securely through an MCP server. Now your company needs several agents to work together to solve a real business problem.

The Sales team receives dozens of RFPs (_Requests for Proposal_) in PDF every week from clients asking for a pricing proposal, and it's struggling to hit deadlines because every request needs input from several different departments — and nobody can tell, just by reading the document, who needs to be asked what. Your tech lead assigns you the following ticket: build the first stretch of an agentic workflow that receives these RFPs, determines whether they really are RFPs, and splits the work across the right agents.

> **Ticket — Agentic workflow for RFP intake and routing**
>
> > **Context:** Sales is missing deadlines because nobody knows, when an RFP comes in, which departments to involve or what each one needs. We need to automate that first analysis before we even touch generating the proposal itself (that's the next part).
> >
> > **What I need you to build:**
> >
> > - A ticket-mode interface where the team uploads the RFP (always PDF) and sees status in real time. Upload goes through the **existing** company backend — **no new API service**. Store the PDF under `data/raw/` as part of the intake process.
> > - Persist the ticket, RFP metadata, and per-department key aspects in **PostgreSQL (Supabase)** — same DB stack you already use for inventory — not TinyDB and not JSON-only files as the source of truth.
> > - Put the LangGraph (or equivalent) pipeline under `data/pipelines/` (e.g. `data/pipelines/rfp_intake/`). Routers in `services/` only trigger and query; they do not own the agent graph. Standalone CLI helpers belong in `scripts/`.
> > - PDF RFPs are heavy on tokens. Convert to Markdown as soon as they arrive — **MarkItDown** (or an equivalent PDF→Markdown step you document) — before any agent reads them.
> > - A classifier agent that decides whether the document is a legitimate RFP; if it isn't, stop the flow and mark the ticket `discarded`.
> > - For each valid RFP, extract metadata and readability metrics (`py-readability-metrics` works) so Sales can anticipate processing cost.
> > - Split analysis by department with orchestrator-worker-synthesizer — not one agent doing everything. Use a **dedicated `rfp_intake` graph**; do not bolt RFP nodes onto the CX / knowledge-agent graph.
> >
> > **Acceptance criteria:** Sales should be able to look at the result of a processed RFP and know, without reading the original document, what's needed from each department and who to ask.
> >
> > — Your tech lead

### 📚 Complementary Knowledge: PDFs, readability, tickets, and async intake

Real-world RFPs arrive as PDFs. Converting them to Markdown before the LLM cuts token cost and noise. Use `py-readability-metrics` on the Markdown to estimate processing cost (Flesch-Kincaid, Gunning Fog, etc.), not as a literary grade.

**Ticket mode** means each upload becomes a row with a lifecycle the UI can poll. Same ticket continues in later parts — full vocabulary lives in CONTEXT. **This part only uses:**

| Status            | When                                                            |
| ----------------- | --------------------------------------------------------------- |
| `analyzing`       | Upload accepted; conversion + agents running                    |
| `discarded`       | Classifier rejected the document                                |
| `intake_complete` | Synthesizer finished; Sales can read per-department key aspects |

PDF→Markdown + classifier + parallel workers can take minutes. **`POST` upload must not run the full pipeline synchronously**: create the ticket (`analyzing`), store the PDF under `data/raw/`, return quickly (e.g. `202` + `ticket_id`), run the pipeline in the background, and let the UI poll `GET` ticket status.

### 🗺️ Visual reference: initial analysis & workstream isolation

This part of the workflow starts with rapid triage (is this an RFP / complex enough?), then an **orchestrator** decomposes the primary document into parallel workstreams (sections / departments), workers process them independently, and a **synthesizer** consolidates everything into a defined workstream structure with meta-info:

![Initial analysis and workstream isolation: triage router, RFP filter, orchestrator-worker decomposition into parallel sections, then synthesizer into defined workstream structure](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-agentic-workflows-orchestrate/.learn/rfp-intake-workstream-isolation.jpg)

---

## 🌱 How to Start the Project

Keep working on the fork of your company's monorepo that you've been using since Milestone. If for some reason you don't have your fork yet, create it now from the [base monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Create a new branch from your main branch: `feature/rfp-intake`.
2. Install any new dependencies with `uv add` (for example, `uv add markitdown` and `uv add py-readability-metrics`) — never with `pip install` or `pipenv`.
3. Extend `uis/backoffice` for the upload UI — don't create a new frontend app.
4. Add HTTP routes on the **existing** backend under `services/` (same process / same API). Implement the agent pipeline in `data/pipelines/` (e.g. `data/pipelines/rfp_intake/`). Put one-off CLI runners in `scripts/` if needed.
5. Read your `CONTEXT-company.md` before defining departments, schema, or test RFPs. Use the sample PDFs under `rfp-requests/<company>/` in the CONTEXT folder — upload them through the UI to verify the flow.

---

## 💻 What You Need to Do

**Monorepo layout (non-negotiable)**

- [ ] **No new API service** — extend the existing backend in `services/`; routers call into `data/pipelines/`
- [ ] Implement the RFP intake graph/pipeline under `data/pipelines/` (dedicated `rfp_intake`, not mixed into the CX agent graph)
- [ ] Standalone scripts (manual reprocess, smoke runs) live in `scripts/`, not as a second HTTP API
- [ ] Persist **Ticket**, **RFP metadata**, and **DepartmentSection.key_aspects** in **PostgreSQL (Supabase)** via SQLModel (or your existing DB layer) — TinyDB is not acceptable for this data

**Intake interface (ticket mode)**

- [ ] Implement an interface in `uis/backoffice` where PDF RFPs can be uploaded, creating one ticket per upload
- [ ] On upload, store the PDF under `data/raw/` (runtime artifact of the process) and set ticket status to `analyzing`
- [ ] Upload endpoint returns quickly; pipeline runs asynchronously; UI polls/refreshes status (`analyzing` → `intake_complete` or `discarded`)

**Document ingestion and conversion**

- [ ] Convert each RFP from PDF to Markdown **before** any agent reads it (required: MarkItDown or a documented equivalent)
- [ ] Extract metadata from the converted document (fields required by your CONTEXT)
- [ ] Compute readability metrics that anticipate processing cost (suggested: `py-readability-metrics`)
- [ ] Store metadata and metrics in PostgreSQL with the ticket

**Classifier agent**

- [ ] Implement a first agent that reads the converted Markdown and determines whether it's a valid RFP
- [ ] If it isn't, stop the flow and set the ticket to `discarded` (don't fail silently)

**Department orchestration**

- [ ] Implement orchestrator-worker-synthesizer: orchestrator decomposes into per-department subtasks
- [ ] Each worker receives **metadata + department-relevant extracts** (not inventing volumes/figures absent from the RFP); store `key_aspects` per department in PostgreSQL
- [ ] Synthesizer consolidates into a Sales-facing summary (what to ask whom)
- [ ] On success, set ticket status to `intake_complete` and leave a clear handoff for Part 2

**Routing**

- [ ] Implement routing of the classified document toward the rest of the agentic flow (queue flag, DB field, or documented handoff contract — no second API). The handoff **must** carry `ticket_id` + synthesizer payload (`key_aspects` / workstream structure) so Part 2 can start without re-parsing the PDF.

⚠️ **IMPORTANT:** Department names, RFP format, and classification criteria must match your `CONTEXT-company.md`. A generic implementation that ignores the context will not be accepted.

**Testing**

- [ ] Include unit tests in `tests/pipelines/` for the classifier agent and at least one worker agent
- [ ] Verify against the CONTEXT sample PDFs (formal accept, informal accept, invalid reject) by uploading them through the UI

---

## 🧭 Design Questions

- What happens if an RFP mentions a department that doesn't exist in your `CONTEXT-company.md`? How does your classifier/orchestrator handle it?
- What does each worker actually need from shared state? Are you passing the whole document, or only what's relevant — and what do you do when a required figure is missing?
- How do you decide that a document "isn't an RFP"? What happens on a false negative?
- What happens if two workers return contradictory information about the same section?
- Where does async work run (background task, worker process, Prefect) — and how does the ticket stay truthful if the job crashes mid-pipeline?

---

## ✅ What We Will Evaluate

- [ ] Same backend API only; pipeline code under `data/pipelines/`; no second HTTP service
- [ ] Ticket, RFP metadata, and key aspects persisted in PostgreSQL (Supabase)
- [ ] Uploaded PDFs land under `data/raw/` as part of intake; UI drives upload
- [ ] Ticket status reflects reality: `analyzing` → `intake_complete` or `discarded` (Part 1); not `waiting_for_approval`
- [ ] Upload is async (quick response + background pipeline + pollable status)
- [ ] Classifier rejects non-RFPs without stopping other tickets
- [ ] Metadata and readability metrics stored per processed document
- [ ] Orchestrator-worker-synthesizer as separate agents on a dedicated `rfp_intake` graph
- [ ] Routing handoff carries `ticket_id` + synthesizer / `key_aspects` payload for Part 2 (queue flag, DB field, or documented contract)
- [ ] Final result lists per-department key aspects + contacts — verifiable against CONTEXT sample PDFs
- [ ] Unit tests for classifier and at least one worker
- [ ] Implementation matches departments and RFP format in `CONTEXT-company.md`

---

## 📦 How to Submit

This is Part 1 of 3 of Milestone. Submit it with its own Pull Request against your main branch — don't wait until Parts 2 and 3 are ready.

1. Commit and push your `feature/rfp-intake` branch
2. Open a Pull Request describing what you implemented and how to test it
3. Include a sample test RFP (from CONTEXT `rfp-requests/`) and the output your flow produces in the PR description
4. Request a review from your tech lead

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Find out more about our [Full-Stack Software Developer](https://4geeksacademy.com/us/coding-bootcamps/coding-full-time), [Data Science & Machine Learning](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering) programs.
