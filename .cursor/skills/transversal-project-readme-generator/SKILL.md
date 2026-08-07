---
name: transversal-project-readme-generator
description: >-
  Generates the universal project statement (README.md + README.es.md) for a
  single milestone of a 4Geeks Academy transversal project. The README is written
  in generic "your company" framing — no sector, no company name — so it applies
  equally to every student regardless of their assigned scenario. Use when a
  milestone needs a new README from scratch, or when an existing README needs to
  be rewritten. Trigger on "write the README for milestone N", "create the
  project statement for hito X", or "rewrite the milestone README". Do NOT use
  for CONTEXT files — use transversal-project-context-generator instead.
---

# 4Geeks Academy — Transversal README Generator

Generates `README.md` + `README.es.md` for one milestone of a transversal project. The output is a universal project statement: technically precise, professionally framed, and written with no reference to any specific company or sector. Every student receives the same README regardless of which company scenario they have been assigned.

---

## Step 1 — Collect Required Inputs

Confirm all inputs before generating. If any are missing, ask for all of them at once — never in multiple rounds.

| Input                | Description                                                               | Default                                                                    |
| -------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `milestone_number`   | The milestone number (e.g., `6`)                                          | — Must ask —                                                               |
| `milestone_topic`    | Core skill(s) this milestone teaches (e.g., `Telemetry & Data Pipelines`) | — Must ask —                                                               |
| `milestone_position` | Position in the course: `early`, `mid`, or `late`                         | — Must ask —                                                               |
| `prior_milestones`   | What students have already built in previous milestones                   | — Must ask —                                                               |
| `tech_stack`         | Technologies required (e.g., `FastAPI + PostgreSQL + Next.js`)            | — Must ask —                                                               |
| `template_repo`      | Starter repo URL students will fork                                       | `https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo` |
| `authors`            | GitHub username(s) for the metadata block                                 | — Must ask —                                                               |

---

## Step 2 — Authoring Rules

### Voice and framing

Write in second person, direct professional tone. The company is always "your company". Stakeholders are always generic: "your tech lead", "your CTO", "your manager". Never name a sector, industry, company, or technology that is not part of the required stack.

**Do:** `Your company has been running on gut feeling for too long.`
**Don't:** `Nexova Solutions needs a pipeline.` / `The logistics company requires tracking.`

### In-company communication register

The challenge narrative and the CTO/manager brief must use the vocabulary that reflects how work is actually requested and communicated inside a company. This is deliberate: it exposes students to professional register before they enter the workforce.

**Preferred terms — use them naturally, not all at once:**

| Term                                    | When to use it                                                                                                                                                |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RFI** (Request for Information)       | A department is evaluating options and asks the tech team to clarify feasibility, scope, or technology choices before committing.                             |
| **RFP** (Request for Proposal)          | A stakeholder asks the tech team to propose a solution to a defined problem, including approach, timeline, and trade-offs.                                    |
| **RFQ** (Request for Quotation)         | The business needs an effort estimate or cost breakdown before approving work.                                                                                |
| **Brief**                               | A short, informal document a stakeholder sends to initiate a request — common for product or design work. Use when the request is exploratory or early-stage. |
| **PRD** (Product Requirements Document) | A formal document defining what to build. Use when describing the artifact the student must produce or reference.                                             |
| **Ticket / Issue**                      | A tracked unit of work in an issue tracker. Use when describing tasks scoped to implementation.                                                               |
| **Stakeholder**                         | Anyone outside the tech team who has an interest in the outcome: business owner, analyst, ops manager.                                                        |
| **Acceptance criteria**                 | The specific, testable conditions a deliverable must meet to be considered done. Use in evaluation sections.                                                  |
| **Handoff**                             | The moment the tech team delivers a result to a stakeholder or to the next stage of a process.                                                                |
| **Sign-off**                            | Formal approval from a stakeholder. Use to frame what it means to "complete" the milestone.                                                                   |

**Do:** `The operations team filed an RFI asking whether the current data pipeline can support real-time alerts. Your tech lead has forwarded it to your squad.`
**Do:** `Your manager shared a brief from the analytics department: they need a dashboard before the quarterly review.`
**Don't:** `You need to build a dashboard.` (too flat — no professional context)

Place at least one of these terms in the CTO/manager brief blockquote and at least one in the opening paragraph of the challenge narrative.

### The CONTEXT anchor — mandatory

The README must reference `CONTEXT-company.md` (link to <https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts>) in exactly two places:

1. **In the hidden metadata block** — a note before the student starts.
2. **In the task checklist** — a `⚠️ IMPORTANT` warning that a generic implementation ignoring the context will not be accepted.
   This is the mechanism that enforces contextualization. Without it, students treat the README as a standalone assignment and ignore their scenario.

### Embed requirements in prose

The challenge narrative must contain at least two or three requirements that the student has to extract by reading carefully — not everything goes in checklists. This mirrors how real briefs work.

### Company monorepo reminder — mandatory

At the very beginning of the **🎯 The Challenge** section (before the narrative opens), insert a short callout block reminding students that this project belongs to the company they were assigned at the start of the course and must be worked on in their own fork of the company monorepo.

Use this exact callout (adapt the language to match the document language):

**English:**

```markdown
> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.
```

**Spanish:**

```markdown
> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.
```

This callout must appear as the **first element inside the 🎯 The Challenge section**, before any narrative text or blockquote.

---

### Prior milestone continuity

If this is not milestone 1, open with one sentence acknowledging what was built before and how this milestone extends it. Do not re-explain prior work.

> You've already built the API and the authentication layer. Now your company needs to understand what's happening inside that system in real time.

### Complementary knowledge

If the milestone requires operational context not covered in lessons (e.g., what makes a good dashboard, what an SLA is), add a brief focused subsection inside the challenge. Keep it under 150 words. Label it clearly.

### Git branching standard (mandatory)

How to Start must include a create-branch step. Same English branch/PR strings in both READMEs.

- Create: `git switch -c <type>/<kebab-capability>` — never `git checkout -b`
- Types: `feature` \| `fix` \| `chore` \| `docs` \| `refactor` \| `perf` \| `test`
- Name = functionality shipped, not curriculum metadata (`milestone-N`, `hito-N`, `part-N`, `wNNdNN` banned)
- PR title (if any): `<type>: <short capability>` — no `[WxxDyy]`
- PR label (if any): functionality English label, not part/parte codes

✅ `feature/rfp-intake` · ❌ `feature/milestone-9-part-1-rfp-intake`

---

## Step 3 — Structure

Follow this structure exactly, in this order:

```markdown
1. Milestone Title (e.g., "Milestone — Telemetry & Data Pipelines")
2. Hidden metadata block
3. --- separator
4. The Challenge (🎯)
   └── Company monorepo callout (mandatory — first element)
   └── [optional] complementary knowledge subsection
   └── CTO/manager brief in nested blockquotes
5. How to Start the Project (🌱)
6. What You Need to Do (💻) — checklist
7. What We Will Evaluate (✅) — checklist
8. How to Submit (📦)
9. --- separator + Footer
```

### Milestone Title (length — mandatory)

- H1 title in **both** languages must be **≤ 80 characters** (count every character, including spaces, em dash, and any `(Part X of Y)` / `(Parte X de Y)` suffix).
- Prefer short, capability-focused wording. Put Part refs at the **end** of the title.
- If the title also lands in `learn.json` (`title.en` / `title.es` / `title.us`), apply the same ≤80 limit there.
- Before delivering, count characters on each language title and shorten if over the limit.

### Hidden metadata block template

```markdown
<!-- hide -->

By [@username](https://github.com/username) and [other contributors](https://github.com/4GeeksAcademy/repo-name/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** before writing any code — it defines the specific company data, field names, KPIs, and constraints for your implementation.
```

### CONTEXT warning for the task checklist

Place this after any checklist group whose implementation depends on context data:

```markdown
⚠️ **IMPORTANT:** Field names, entity IDs, and domain-specific values in your implementation must match what is specified in your CONTEXT.md. A generic implementation that ignores the context will not be accepted.
```

### Checklist format

Use `- [ ]` for every item in both checklists. Group task items by layer (backend, frontend, data, testing). Evaluation criteria must be observable and measurable — not vague qualities.

✅ `The pipeline has three identifiable stages implemented as separate functions`
❌ `Good code quality`

### Footer templates

**README.md:**

```markdown
---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@username](https://github.com/username) and [other contributors](https://github.com/4GeeksAcademy/repo-name/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
```

**README.es.md:**

```markdown
---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
```

---

## Step 4 — Bilingual Output

READMEs are delivered in two stages:

**Stage 1 — Primary document (working language):** Generate the primary language version first and deliver it for review. Do not generate the translation until the primary document has been explicitly approved. The primary language is the working language of the course — typically Spanish, unless the user specifies otherwise.

**Stage 2 — Translation (after approval):** Once the primary document is approved, generate the translation. The translation must be a faithful, consistent rendering — same structure, same section order, same wording intent. Do not add, remove, or reword requirements between versions.

Each file must link to its counterpart, written in the language of the target document — so a reader who does not understand the current document can still find the translation:

- In `README.md` (English): `_Estas instrucciones están [disponibles en español](./README.es.md)._`
- In `README.es.md` (Spanish): `_These instructions are [available in English](./README.md)._`

---

## Quality Self-Check Before Delivering

- [ ] Company monorepo callout present as the first element inside the 🎯 The Challenge section (both language versions)
- [ ] No sector name, company name, or industry reference anywhere in the README
- [ ] At least one in-company communication term (RFI, RFP, brief, PRD, ticket, stakeholder, acceptance criteria, handoff, or sign-off) appears in both the challenge narrative opening and the CTO/manager brief
- [ ] CONTEXT anchor present in both the metadata block and the task checklist
- [ ] At least two or three requirements embedded in the challenge narrative (not only in checklists)
- [ ] Prior milestone continuity sentence present (if not milestone 1)
- [ ] Complementary knowledge subsection present if the milestone requires context not in lessons
- [ ] All checklist items use `- [ ]` format
- [ ] Milestone title ≤ 80 characters in both languages (H1 and any synced `learn.json` title)
- [ ] Evaluation criteria are observable and measurable
- [ ] Primary language document generated and delivered for review before translation begins
- [ ] Translation generated only after explicit approval of the primary document
- [ ] Translation is structurally identical to the approved primary — same requirements, same checklist items, same order
- [ ] Both README.md and README.es.md link to each other (once both exist)
- [ ] Footer present in both files with correct language variant
- [ ] Branch/PR follow Git branching standard (`git switch -c`, functionality names, shared English)
