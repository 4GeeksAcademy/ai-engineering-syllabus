---
name: classroom-example-brief
description: >-
  Drafts bilingual instructor-only example briefs under .learn/example/ (README.md +
  README.es.md): a shorter parallel scenario with the same stack and learning goals as
  the real project but a different domain, so teachers can build a live reference demo
  without implementing the full student deliverable. Use when the user asks for a class
  example, enunciado de ejemplo, instructor brief, .learn/example, or a teaching
  walkthrough that mirrors a syllabus project.
---

# Classroom example brief (`.learn/example/`)

## Purpose

Produce **instructor-facing** enunciados that let a teacher implement a **small, coherent reference solution** in class. The example must:

- Teach the **same technical concepts, patterns, and stack** as the official project.
- Use a **different domain and narrative** than the student README (no clone of the real use case).
- Stay **much shorter** than the official project (target **60–120 minutes** of live work, including discussion).
- **Not** replace `.learn/solution/` or the canonical student rubric — it is a **pedagogical parallel**, not the official reference implementation.

Official student instructions stay in the project root `README.md` / `README.es.md`. Do **not** rewrite those files when applying this skill unless the user explicitly asks.

## When to use

- Creating or refreshing `.learn/example/README.md` and `.learn/example/README.es.md` for a project under `content/projects/<slug>/`.
- The user wants a **classroom-safe** scenario: students still read the real README; the teacher demos the “toy” version first.

## Output location and files

| Path                          | Language | Audience                         |
| ----------------------------- | -------- | -------------------------------- |
| `.learn/example/README.md`    | English  | Instructors (and EN-first staff) |
| `.learn/example/README.es.md` | Spanish  | Instructors (ES-first staff)     |

Create `.learn/example/` if missing. **Do not** add `.learn/solution` content or modify `learn.json` unless the user asks.

### Cross-link line (recommended)

After the opening instructor note, add a single line so both files discover each other:

- In `README.es.md`: `_These instructions are also available in [English](./README.md)._`
- In `README.md`: `_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._`

(Keep accents/spelling consistent with the syllabus README translation rule.)

## Workflow

1. **Read the official briefs**  
   Read `README.md` and `README.es.md` at the project root. Extract: stack, mandatory integrations, data shapes, API/UI expectations, evaluation dimensions, and constraints (e.g. CONTEXT files, monorepo paths).

2. **Extract the teaching spine**  
   List **3–7 non-negotiable technical ideas** (e.g. Pydantic validation + TinyDB + seed idempotency + filtered `GET`; or Next.js App Router + `useSearchParams`; or agent tool loop). The example must exercise **the same spine**, not every bullet of the full rubric.

3. **Pick a substitute domain**  
   Choose a concrete, boring-friendly domain (library, gym, bakery, parking, recipes, plant swap, etc.) that **does not** reuse the original product story. Avoid trademarked brands and culturally loaded scenarios unless the project requires them.

4. **Shrink scope deliberately**  
   Drop or simplify secondary requirements (e.g. fewer endpoints, fewer views, smaller grid, no email provider in class — mock instead) while **preserving the spine**. State what was simplified in a short “Scope note” subsection.

5. **Write both languages**  
   Write `README.md` and `README.es.md` as **full translations** of each other (same sections, same checklists, same tables). Do not ship English-only.

6. **Add closure for class**  
   End with **2–3 discussion questions** in the correct language for each file (same questions, translated).

## Required structure (template)

Use this shape; adapt headings minimally if the project is non-code (e.g. milestone doc).

```markdown
# [Example title] — [one-line stack or theme] (Class Example)

> **For instructors:** … (1–2 sentences: not the student project; live demo scope; same concepts as `<project slug>`.)

_[Cross-link line EN/ES]_

---

## The challenge

[Short problem statement in plain language.]

### Scope note

[What was simplified vs the real project — explicit.]

---

## What to build

### [Model / UI / Agent loop — as appropriate]

- [ ] …

### [Core feature 2]

- [ ] …

### [Core feature 3]

- [ ] …

(Optional: small table of fields, endpoints, or routes.)

---

## Verify together

- [ ] …

---

## Discussion questions

1. …
2. …
3. …
```

## Style rules

- **No** `<!-- hide -->` blocks, badges, or 4Geeks footer — this is internal curriculum material.
- Prefer **checklists** (`- [ ]`), **tables**, and **small code blocks** (sample JSON, tiny dataset, enum values) over long prose.
- Keep the example **one screenful of reading** where possible; teachers expand verbally.
- Use vocabulary consistent with the official README (same endpoint naming style, same framework terms).

## Quality checklist (before finishing)

- [ ] Same **stack** and **central patterns** as the real project; simplifications are explicit.
- [ ] **Different domain** from the official student scenario.
- [ ] **Bilingual** pair present and aligned.
- [ ] **Does not** copy-paste large chunks of the student README or duplicate the full evaluation section.
- [ ] **Actionable** in one session; avoid hidden dependencies (or call them out).
- [ ] **Discussion questions** included at the bottom of both files.

## Anti-patterns

- Reusing the **same business story** as the student project with minor renames.
- Packing **every** acceptance criterion from the real rubric into the example (defeats the purpose).
- Putting the example in `README.md` at project root — keep it under **`.learn/example/`** only.
- English-only output when the syllabus expects **EN + ES**.

## Coordination with other skills

- **`project-solution-file`**: Canonical student reference stays in `.learn/solution/` and `learn.json`. The classroom example may mention expected behaviors but must not pretend to be the official solution package.
- **`readme-project-orchestrator`**: Applies when **scaffolding a whole project** from READMEs; this skill only adds **instructor example briefs**, not full project generation.

## Reference

For narrative tone and level of detail, compare existing pairs under `content/projects/*/.learn/example/`.
