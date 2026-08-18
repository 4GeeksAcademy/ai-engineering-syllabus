---
name: module-guidelines-generator
description: Generates debate-first pedagogical guidelines (lineamientos) per module/day, **content-first**: theory topics from the syllabus CSV drive every section; the day’s project is referenced only **generically** (never named) as the application/deliverable hook. Produces two bilingual texts per skill: (1) students — short motivating header (3–5 lines, plain text) + 1–2 preview questions ("before class"); (2) professors — compact hybrid debate kit delivered as plain Markdown (copy-paste ready with headings/lists intact), with concise Summary (ends with class checkpoint), Debate pacing, opening/closing, and 5 dimension subsections (Learn/Reflect/Be aware of/Do/Avoid) with compact representative aspects + 1–2 Socratic, engineering-reasoning reflexive questions per dimension (built to develop critical thinking via trade-offs, failure modes, evidence, and second-order effects), optional bridge, facilitator probes (Reflect/Avoid only), and Participation criteria. **MANDATORY:** run `syllabus-context-reader` (`parse_syllabus.py` on the planning CSV) before generating — never invent or assume day content. Use when asked to "generate guidelines for module X", "generate lineamientos", "generate guidelines", "student guidelines", "mentor guidelines", "class debate", "reflective questions", or "w8 d22". Trigger on "lineamientos", "teaching guide", "debate", "guidelines".
---

# 4Geeks Academy — Module Guidelines Generator

This skill generates **two bilingual guideline texts per skill/module**: one for **students** (short motivating header) and one for **professors** (outcome-focused teaching guide). Both are always delivered in **Spanish and English**. All outputs must be returned in **Markdown**.

## Content-first principle (mandatory)

Guidelines are **about the class content** — what students learn and discuss that day. The project provides the application context (**GC-1**); it does **not** replace or overshadow the theory plan.

| Priority                 | Source                                                                        | Role in guidelines                                                                                           |
| ------------------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **1 — Primary**          | `content` **before** `---` (theory topics from CSV)                           | Drives summary, must-discuss, Learn/Reflect/Be aware of/Do/Avoid aspects, preview questions, opening/closing |
| **2 — Framework**        | `how_to_think`, `best_practices`, `patterns`, `anti_patterns`, `limitaciones` | Shapes dimensions and facilitator probes                                                                     |
| **3 — Application hook** | `content` **after** `---` (project definition)                                | Application context only (**GC-1**: generic references, never named); not the main debate narrative          |

**Agent rule:** never generate guidelines without running `parse_syllabus.py` for the target week/day. Extract theory topics from parser output; **do not** write project-led guidelines that skip or underweight syllabus theory bullets.

**Bad (project-led):** debate centers on “Voice Agent” wiring while ignoring Pydantic validation, HTTP methods, or API docs listed in theory.

**Good (content-led):** debate centers on CRUD endpoints, Pydantic contracts, and API documentation; the day’s project is where students apply those concepts.

## Global constraints

These rules apply to **all generated output**. Inline references use the label (e.g. **GC-1**); do not restate the full constraint — just apply it.

- **GC-1 — Project-agnostic output:** never print the specific project name, title, or unique features. Refer to it generically: “your project”, “the day’s project”, “the deliverable”, “what you build today”. `project_name` is internal context only. `project_focus` aligns the _kind_ of application — never names it. Guidelines must stay valid if the project is swapped.

- **GC-2 — No temporal references in output:** never cite week/day codes (`w7 d21`, “day 21”, “semana 8”) in student or professor text. Use topic/skill labels in natural language.

- **GC-3 — Engineering reasoning in every question:** every reflective question and facilitator probe must exercise ≥1 lens from the **Question design rubric** (trade-offs, constraints/assumptions, failure modes, evidence-over-intuition, second-order effects, alternatives/reversibility). Forbid recall/definition questions and yes/no without “why”.

- **GC-4 — Bilingual parity & natural Spanish:** both languages convey the same meaning. Spanish must read as native classroom Spanish — adapt phrasing/idioms, never literal translation. Spanish mentor headings in Spanish (see heading mapping table).

- **GC-5 — No future content:** do not teach or reference content from days after the target day. `prior_skills` calibrates tone/prerequisites only.

---

### Chat delivery format (mandatory)

In the agent chat, **Students** and **Mentors** are delivered as copyable blocks (rendered Markdown in chat is not suitable for copying).

**Block titles (outside the fence):**

- Put a **visible heading before each copy block** so the user can identify what they are copying.
- Use these exact headings:
  - `### Students — English`
  - `### Students — Español`
  - `### Mentors — English`
  - `### Mentors — Español`
- Headings stay **outside** the code fence — never inside the copyable content.

**Students — plain text:**

- After each Students heading, open a ` ```text ` fence containing **only** the student guideline text to copy (3–5 lines).
- No bullet lists or Markdown headings inside; natural Spanish (not literal).

**Mentors — plain Markdown:**

**Mentor instructions must be delivered as plain Markdown**, ready to paste into CMS, Notion, Google Docs, or any platform **preserving formatting** (headings, lists, bold).

- Deliver the **Mentors** section inside a ` ```markdown ` fence containing **only** the teaching kit to copy — summary, debate pacing, dimensions, closing (e.g. starts with the summary paragraph or `### Debate pacing`).
- The fence must contain guideline content only: no block titles, no agent commentary, no copy instructions.
- Use only standard Markdown syntax: `#`–`####`, `-` lists / numbered lists, `**bold**` where applicable.
- The professor should be able to select **Mentors → English** or **Mentors → Spanish** and paste directly with visible formatting.
- **In agent chat (Cursor):** mandatory to deliver **four blocks** (or two if the user requests only one language/audience), each with its heading **before** the fence:
  - `### Students — English` → ` ```text ` …
  - `### Students — Español` → ` ```text ` …
  - `### Mentors — English` → ` ```markdown ` …
  - `### Mentors — Español` → ` ```markdown ` …
- Do not repeat Students or Mentors as rendered chat text only.
- Do not use disk files unless the user explicitly requests it.

**Example (agent chat layout):**

````markdown
#### Students — English

```text
You will learn...
```

#### Students — Español

```text
Aprenderás...
```

#### Mentors — English

```markdown
Students cover theory on...
**Class checkpoint:** ...
```

#### Mentors — Español

```markdown
Los estudiantes cubren teoría sobre...
**Checkpoint de la clase:** ...
```
````

---

## Source of Truth: Syllabus (via `syllabus-context-reader`)

**MANDATORY — before generating any output**, load syllabus context using the **`syllabus-context-reader`** skill:

- Skill path: `course-outline-generator/skills/syllabus-context-reader/SKILL.md`
- Follow its workflow end-to-end (run `scripts/parse_syllabus.py`; do **not** read the planning by hand).
- Cross-ref: use the parser workflow exactly as defined there (see its `scripts/parse_syllabus.py` extraction + `--include-prior` guidance). Do not re-implement JSON extraction inside this skill.

**Do NOT** use these as primary sources:

- `course-outline-generator/ai-engineering/syllabus.md`
- <https://raw.githubusercontent.com/4GeeksAcademy/course-outline-generator/refs/heads/main/ai-engineering/syllabus.md>

**Official source:** CSVs under `**/syllabus/` (canonical: `ai-engineering-syllabus/docs/syllabus/`). `syllabus.md` is a derived export only — if it disagrees with the CSV, the CSV wins.

The parser auto-discovers those CSVs. **If more than one and the user did not name the program/file → ask which one** (see `syllabus-context-reader`). Do not hardcode a CSV path.

### Required parser invocation

1. Resolve CSV: `--list-csvs` (or follow skill §2). Multiple + unspecified → **ask user**.
2. If week/day unknown, run `--list` or `--search`.
3. Always extract the target day with **`--include-prior`**:

```bash
python3 course-outline-generator/skills/syllabus-context-reader/scripts/parse_syllabus.py \
  --week <week> \
  --day <day> \
  --include-prior
# if several CSVs: add --csv "<path or unique name substring>"
```

### Map JSON output → guideline inputs

From `current` in the parser JSON:

| Parser field     | Use in guidelines as                                                                                                                                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `skill`          | Skill name, scope, `skill_name`                                                                                                                                                                                                                                    |
| `content`        | **Split on `---`:** (1) **before** → `theory_topics`, `main_concepts`, `key_actions` — **primary** source for all debate dimensions; (2) **after** → `project_focus` (application hook, **GC-1**). Never let the project section override missing theory coverage. |
| `how_to_think`   | Thinking development → **Learn**, **Reflect**                                                                                                                                                                                                                      |
| `best_practices` | **Be aware of**, evaluation priorities                                                                                                                                                                                                                             |
| `patterns`       | **Do**, patterns to reinforce                                                                                                                                                                                                                                      |
| `anti_patterns`  | **Avoid** (required; do not omit)                                                                                                                                                                                                                                  |
| `limitaciones`   | **Be aware of**, constraints in class and project                                                                                                                                                                                                                  |
| `week` + `day`   | Position in course (e.g. Week 8 — Day 22)                                                                                                                                                                                                                          |

From `prior_skills`: calibrate tone and prerequisites only (**GC-5**). Default parser mode is **smart** (prior milestones + last 15 regular lessons). If you need the full course history, re-run with `--prior-full`. Check `prior_skills_meta.total_prior` vs `returned`.

Do not invent learning objectives or concepts absent from the parser output. If a framework field is `null` or empty, infer only from `content` and `skill`; avoid advanced assumptions.

---

## When to Use This Skill

Use when:

1. Adding or documenting a new skill or module in the syllabus.
2. Creating "lineamientos" or content briefs for theory + practice per skill.
3. Preparing student-facing and professor-facing instructions for a module.
4. A user asks for "guidelines", "lineamientos", "cabecera de módulo", or "guía docente por resultados esperados".

**Do NOT use this skill to:**

- Generate project READMEs (use `module-project-readme-generator` or `transversal-project-readme-generator`).
- Generate CONTEXT files (use `transversal-project-context-generator`).

---

## Required Inputs

Confirm you have (or ask for) the following. If any are missing, ask for **all missing items at once**.

| Input           | Description                                                                                                                                            | Required                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| `skill_name`    | Name of the skill or module                                                                                                                            | Required                     |
| `skill_type`    | Category: `web-fundamentals`, `styling-ui`, `programming-logic`, `milestone`                                                                           | Optional — helps tailor tone |
| `theory_topics` | Core theory topics covered in class (extracted from `content`, before the `---` separator) — **primary input**; must be parsed from CSV before writing | Required                     |
| `main_concepts` | 3–5 core concepts this skill teaches                                                                                                                   | Required                     |
| `key_actions`   | 2–4 things the student should be able to do by the end                                                                                                 | Required                     |
| `project_name`  | Name of the module project(s) — **internal context only** (**GC-1**)                                                                                   | Optional                     |
| `project_focus` | What the project emphasizes — internal use, aligns theory with deliverable generically (**GC-1**)                                                      | Optional but recommended     |

If the parser output already provides these values, extract them from `current` (theory topics and project details both live in `content`); ask the user only for items still missing after the CSV extraction.

---

## Output: Two Bilingual Texts per Skill

Always produce **two distinct texts** for the same skill. Both must be **bilingual (Spanish and English)** regardless of any language preference.

---

### 1. Student Guidelines (Lineamientos para estudiantes)

**Purpose:** A short, motivating class opener in natural language that tells students **what theory content they will cover**, what they should be able to do by the end applied in the day’s project (**GC-1**), and includes 1–2 preview questions grounded in **syllabus theory topics**.

**Rules:**

- **Content-first:** lead with theory topics from `content` (before `---`); reference the day’s project/deliverable per **GC-1** — not as the sole subject of the opener.
- **Target: 3–5 lines per language. Maximum: 5 lines total**, including preview questions (inline, not bullet lists).
- **Plain text preferred** — avoid bullet lists unless explicitly requested.
- Motivating and clear; use second person (tú/vos or usted, per course convention).
- **Forward-looking tone** — students read this **before or at the start of class**; describe what they **will do/learn that day**, not what they are doing now. **Do not** require "Today you will…" / "Hoy vas a…" every time.
  - EN: use **"You will…"** (e.g. "You will create…", "You will learn…") and/or direct imperative (**"Create…"**, **"Build…"**). Optional: "By the end you will be able to…". Avoid present for the main action (not "You create…" / "You are building…").
  - ES: use **"Vas a…"** / **"Crearás…"** / **"Aprenderás…"** and/or imperative (**"Crea…"**, **"Construye…"**). Optional: "Al final podrás…". Avoid present for the main action (not "Creas…" / "Estás construyendo…").
- Must state: what the student **will** learn (**theory topics from syllabus**) + what they **will** be able to do by the end (applied in the project, **GC-1**).
- Include **1–2 preview questions** students can reflect on before class — at least one must reference a **theory topic** from the CSV content plan. Frame at least one as a **critical-thinking prompt** (**GC-3**: a trade-off, a hidden assumption, or “what would break if…”).
- Encourage steady progress: "By the end you should feel capable of...", "Don't aim for perfection on the first try."
- Spanish must read as native classroom Spanish (not literal translation from English). Adapt phrasing and rhythm while preserving intent.

**Output structure:**

```markdown
## English

[Short student header — 3–5 lines, max 5]

---

## Spanish

[Short student text in Spanish — 3–5 lines, max 5, natural phrasing]
```

---

### 2. Professor Guidelines (Lineamientos para profesor)

**Purpose:** Debate-first teaching kit centered on **that day’s syllabus content**. Turn the 5 Thinking Framework dimensions into a reflexive discussion that builds **engineering judgment and critical thinking** — students should reason about _why_, _when_, and _at what cost_ each **theory concept** matters for excelling as an AI Engineer, with the project as proof of application. The mentor’s job is not to deliver answers but to facilitate the reasoning: surface trade-offs, challenge assumptions, and ask for evidence.

**Rules:**

- **Content-first:** summary, must-discuss, dimension aspects, and reflective questions must trace to **theory bullets** in `content` (before `---`). Reference the project per **GC-1** in the class checkpoint — do not make it the only subject of debate.
- Direct, imperative or neutral third person.
- Structured debate flow (not one dense paragraph).
- Must explicitly address the following **5 outcome dimensions** as their own `####` subsections:
  1. **Learn**
  2. **Reflect**
  3. **Be aware of**
  4. **Do**
  5. **Avoid**
- Include (inside the kit):
  - **Content plan + what good looks like:** enumerate or summarize **theory topics from the syllabus** first; then how those topics connect to the day’s deliverable (**GC-1**) and what applying both well looks like.
  - **Evaluation priorities:** understanding over memorization; application over ticking checklists; meaningful intent.
  - **Class checkpoint line (#7):** the last line inside **Summary** tying debate outputs to both theory coverage and applying it in the day’s project (**GC-1**).
- Questions must be **open-ended and Socratic** (no answer keys embedded) and must demand **engineering reasoning** (**GC-3**).
- Keep it concise: **Summary ~45–60 words**; avoid long paragraphs.
- Per dimension, include aspects **inline in one compact paragraph** (no subsection title), using 1–3 short phrases/cases.
- Per dimension, include **1–2 reflective questions** (regular and milestone days).
- Under **Reflect** and **Avoid** only, add **facilitator probes (#3)** (1–2 bullets like `If they say X, ask Y`, `How could we use...`, `What if...`), grounded in `how_to_think` trade-offs and/or `anti_patterns`.
- **Milestone behavior:** when parser `current.is_milestone` is true, keep **1 question (max 2) per dimension** and emphasize demo/evaluation conversation over theory drill.
- **GC-4** applies: Spanish mentor text natural, non-literal; all section headings in Spanish (see mapping table).

| English                                | Español                              |
| -------------------------------------- | ------------------------------------ |
| A summary                              | Un resumen                           |
| **Class checkpoint:**                  | **Checkpoint de la clase:**          |
| Debate pacing                          | Ritmo del debate                     |
| Bridge within the module (if applies)  | Puente dentro del módulo (si aplica) |
| Participation criteria                 | Criterios de participación           |
| Debate                                 | Debate                               |
| Opening — professional impact          | Apertura — impacto profesional       |
| Learn                                  | Aprender                             |
| Reflect                                | Reflexionar                          |
| Be aware of                            | Tener en cuenta                      |
| Do                                     | Hacer                                |
| Avoid                                  | Evitar                               |
| **Reflective questions:**              | **Preguntas reflexivas:**            |
| Facilitator probes:                    | Sondeos del facilitador:             |
| Closing — Excellence as an AI Engineer | Cierre — Excelencia como AI Engineer |

- **Mandatory plain Markdown delivery (mentor):** the teaching kit is returned as renderable Markdown when copy-pasted; not as agent prose or code block.
- Mentor output must be **plain Markdown copy-ready**: clean headings + lists only, no meta commentary, no decorative prefixes, no escaped formatting artifacts.

#### Question design rubric (engineering critical thinking)

Every reflective question and facilitator probe must move students from _what_ to _why / when / at what cost_. Design each one to exercise at least one **engineering reasoning lens**:

- **Trade-offs:** force a defensible choice between competing goods (speed vs. reproducibility, simplicity vs. coverage, abstraction vs. control) and ask students to justify where they draw the line.
- **Constraints & assumptions:** surface what must be true for an approach to hold, and what breaks when that assumption fails.
- **Failure modes:** ask _how_ it breaks, _how you'd detect it_, and _what it costs_ in production or in a team.
- **Evidence over intuition:** require a test, metric, log, or observable signal that would prove or disprove the claim ("How would you know?").
- **Second-order effects:** ask what the decision causes downstream — for maintenance, cost, teammates, or the AI agent's behavior.
- **Alternatives & reversibility:** ask what else was considered and how hard the decision is to undo.

The goal is to **open minds to the engineering way of thinking**, not to extract a correct answer. Prefer concrete scenarios grounded in the day’s theory topics. Reject questions answerable by quoting the lesson.

**Default lens bias per dimension** — vary question shapes; do not ask every dimension as a trade-off:

| Dimension   | Primary lens                                             | Secondary lens               |
| ----------- | -------------------------------------------------------- | ---------------------------- |
| Learn       | Constraints & assumptions (what must be true; the model) | Alternatives                 |
| Reflect     | Trade-offs (competing goods, where to draw the line)     | Second-order effects         |
| Be aware of | Failure modes (risks, limits)                            | Constraints & assumptions    |
| Do          | Evidence over intuition (how you'd verify)               | Trade-offs                   |
| Avoid       | Failure modes (what breaks, who pays)                    | Alternatives & reversibility |

Use the primary lens as the default; switch to the secondary (or any lens) when it yields a sharper question or avoids repeating a shape already used that day.

**Milestone days** (`current.is_milestone` true): bias toward **Evidence over intuition** (demo proof — "how would you show it works?") and **Second-order effects** (what the decision means for the product / next milestone); de-emphasize abstract trade-off drills. Keep 1 question (max 2) per dimension.

**Good vs. bad questions** (recall → engineering rewrite — use as a contrast anchor):

| Weak (recall / yes-no)      | Rubric-grade rewrite                                                                                              | Lens                         |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| "What is a Docker image?"   | "If your image runs locally but fails in CI, what assumption broke — and how would you prove where?"              | Constraints + evidence       |
| "Is testing important?"     | "Which single test, if green, would convince you this is safe to merge — and which would convince you not?"       | Evidence                     |
| "What does `useEffect` do?" | "If this effect fires one extra time in production, who notices, what does it cost, and how would you detect it?" | Failure modes + second-order |

**Bridge — rules:**

- Include **Bridge within the module** only when today's skill **directly continues** a lesson from the **same module** (same CSV module block, e.g. between `### MODULE NAME ###` markers or equivalent section in `content`).
- **Do not** bridge across modules or hitos (e.g. do not link "Working with AI coding agents" to "Next.js APIs" unless they share the same module block).
- If there is no same-module continuity, **omit the Bridge section entirely** (do not leave an empty "if applies").
- When bridging, reference the **prior topic/skill in natural language** (**GC-2**).

**Output structure (professor — paste as-is):**

```markdown
## English

[Summary (~45–60 words, covering theory topics + generic project link + evaluation priorities)]

**Class checkpoint:** [...]

### Debate pacing

[Suggested order, must-discuss, if-time, time guide]

### Bridge within the module (if applies)

[One bullet: prior topic → today's skill. Omit this whole section if not same module. No week/day references.]

### Participation criteria

- ... (3 bullets)

### Debate

#### Opening — professional impact

1. [...]

#### Learn

[Inline aspects sentence: 1–3 compact phrases/cases, no "Representative aspects" label]
**Reflective questions:**

1. ... (1–2)

#### Reflect

[Inline aspects sentence: 1–3 compact phrases/cases, no "Representative aspects" label]
**Reflective questions:**

1. ...
   Facilitator probes:

- If they say X, ask Y

#### Be aware of

...

#### Do

...

#### Avoid

...
Facilitator probes:

- If they say X, ask Y

### Closing — Excellence as an AI Engineer

1. [...]

---

### Spanish

... (Resumen)

**Checkpoint de la clase:** [...]

### Ritmo del debate

[...]

### Puente dentro del módulo (si aplica)

[Un bullet: tema previo → skill de hoy. Omitir sección entera si no es el mismo módulo. Sin referencias a semana/día.]

### Criterios de participación

- ... (3 bullets)

### Debate

#### Apertura — impacto profesional

1. [...]

#### Aprender

[Frase de aspectos en línea]
**Preguntas reflexivas:**

1. ...

#### Reflexionar

[...]
**Preguntas reflexivas:**

1. ...
   Sondeos del facilitador:

- Si dicen X, pregunta Y

#### Tener en cuenta

...

#### Hacer

...

#### Evitar

...
Sondeos del facilitador:

- ...

### Cierre — Excelencia como AI Engineer

1. [...]
```

---

## Workflow

1. **Load syllabus context (mandatory)** — Invoke **`syllabus-context-reader`**: read `SKILL.md`, run `parse_syllabus.py` with `--week`, `--day`, and **`--include-prior`**. Resolve week/day from the user request (e.g. `w8 d22` → `--week 8 --day 22`). If ambiguous, run `--list` or `--search` first; never guess from `syllabus.md`.
2. **Map parser JSON (content-first)** — Populate inputs from `current` (see table above). **First:** parse `content` before `---` into an explicit `theory_topics` list (every `+` / `-` bullet in the CSV theory block). **Second:** extract `project_focus` from after `---` (**GC-1**). Derive `main_concepts` and `key_actions` from theory topics + `how_to_think`/`patterns`, not from project title alone. Treat `prior_skills` as prerequisites only (**GC-5**). **Stop** if parser was not run — do not generate from memory or `syllabus.md`.
3. **Internal: representative aspects per dimension** _(process-visible, result-hidden)_ — For each dimension (Learn/Reflect/Be aware of/Do/Avoid) derive **1–3 compact** aspects/cases from **theory topics first**, then render them as **one inline sentence** in final output (no subsection title):
   - Learn/Reflect: `content` (**theory topics before `---`**), `how_to_think`, `skill`
   - Be aware: `best_practices`, `limitaciones`, theory constraints in `content`
   - Do: `patterns` + **theory activities** in `content`; project application only as supporting example
   - Avoid: `anti_patterns` (**required; never omit**)
   - If a field is `null`, infer only from `content` + `skill`.
     Also run **Bridge check**: scan `prior_skills` + CSV module boundaries (`### … ###` in planning). Bridge **only** if the immediately relevant prior lesson is in the **same module** as today and sets up today's skill. Extract **topic label** from that prior `skill` (not week/day). If no same-module link, set bridge = omit.
   - **Hidden internal rule:** do not include this "Phase 2 analysis" in the final student/professor text; only carry the _selected_ aspects and resulting questions forward.
4. **Internal: debate questions kit** _(process-visible, result-hidden)_ —
   - Create **open-ended Socratic questions** from the representative aspects, each applying the **Question design rubric** (minimum one engineering reasoning lens).
   - Regular days: **1–2 questions per dimension**.
   - Milestone days (`current.is_milestone` true): target **1 question (max 2) per dimension** (keep total questions small; emphasize "what good looks like").
   - Add exactly **1 opening** career-impact question (whole class).
   - Add exactly **1 closing** question tied to how decisions show up in theory content and the day’s deliverable.
   - **Quality bar:** apply **GC-3**. Prefer concrete scenarios from **syllabus theory topics** first, then project application or anti-patterns. At least **3 of 5** dimension aspect sentences must name a theory topic from the CSV content plan.
   - **GC-4** applies.
5. **Generate student guidelines** — 3–5 lines per language, plain text, motivating, **forward-looking**. **Lead with theory topics from syllabus**; mention the project per **GC-1**. Add **1–2 preview questions** (inline, not bullet lists) grounded in content plan (**GC-3**). **GC-4** applies. In agent chat: heading `#### Students — English` / `#### Students — Español` **before** each ` ```text ` fence; fence contains only the student guideline text to copy.
6. **Generate professor guidelines (debate-first hybrid kit)** —
   - **Expected outcomes summary**: concise (**~45–60 words**), **name or summarize theory topics first**, then project link (**GC-1**) + evaluation priorities; end with **class checkpoint line** tying **content mastery** to the day’s project.
   - **Debate pacing (#1)**: order + must-discuss (**2–3 items from theory plan**) + if-time + time guide (~45–60 min debate + practice).
   - **Bridge within the module** (from Bridge check): include section only when same-module continuity exists; one bullet referencing **prior topic** (**GC-2**); never week/day codes.
   - **Participation criteria (#13)**: exactly 3 bullets.
   - **Opening**: opening career-impact question.
   - For each dimension: `####` section with **inline aspects sentence** (1-3 compact phrases/cases, no title) + **Reflective questions** (1-2). Under **Reflect** and **Avoid** add **Facilitator probes (#3)** (1-2 "If they say X, ask Y" probes; no answer keys).
   - **GC-4** applies to Spanish mentor version.
   - In agent chat: deliver with headings `#### Mentors — English` / `#### Mentors — Español` **before** each ` ```markdown ` fence; fence contains only the mentor kit to copy. Default; no disk files unless user asks.
   - For CMS paste: user copies block interior; headings, bullets, bold preserved on paste.
7. **Dedup pass (#5)** — Ensure no two questions across dimensions share the same intent. If overlap, merge, rephrase, or drop the weaker one.
8. **Deliver both texts** — Return a single Markdown block in the required output format with both languages and clear audience separation.

---

## Additional resources

- For skill-type tone examples, see [reference.md](reference.md)

## Output Format

Present the result in a single block:

```markdown
# Guidelines — [Skill]

## Students

### English

[Student guidelines in English: header (3–5 lines, max 5) + 1–2 "before class" preview questions.]

---

### Spanish

[Student guidelines in Spanish: opener (3–5 lines, max 5), natural phrasing + 1–2 "before class" preview questions.]

## Mentors

> **Delivery rule:** everything under `## Mentors` must be **plain copyable Markdown** (not wrapped in code fences). The user pastes directly into their tool and headings/lists are preserved.

### English

[Professor guidelines in English — plain Markdown only: Summary (with class checkpoint) + Debate pacing + Opening + Learn/Reflect/Be aware of/Do/Avoid (inline aspects + questions, probes in Reflect/Avoid) + Bridge within module only if same module (topic-based, no w/d) + Closing + Participation criteria. No code fence around this block.]

---

### Spanish

[Professor guidelines in Spanish — same plain copyable Markdown format; **section headings in Spanish**; natural Spanish, not literal translation.]
```

**Chat delivery (default):** four copy blocks with visible headings **before** each fence — `#### Students — English`, `#### Students — Español`, `#### Mentors — English`, `#### Mentors — Español`. Each fence contains **only** the guideline content to copy. Do not rely on rendered chat text alone. Disk files only if user requests.

If the user needs integration into a platform (e.g. CMS fields or `learn.json`), offer a compact key-value structure (`guidelines_student_es`, `guidelines_student_en`, `guidelines_professor_es`, `guidelines_professor_en`) upon request — values still in plain Markdown for professor fields.

---

## Quality Self-Check Before Delivering

- [ ] **Syllabus source**: `parse_syllabus.py` ran with `--include-prior`; guidelines not generated from memory or `syllabus.md`.
- [ ] **Content-first**: theory topics from `content` (before `---`) drive summary, must-discuss, dimensions, and preview questions.
- [ ] **GC-1 (project-agnostic)**: no project name, title, or unique feature in either text; only generic references.
- [ ] **GC-2 (no temporal refs)**: no week/day codes in output; bridge uses topic labels only.
- [ ] **GC-3 (engineering reasoning)**: every question/probe applies ≥1 rubric lens; no recall/definition or yes/no-without-why.
- [ ] **GC-4 (bilingual quality)**: both languages same meaning; Spanish natural and non-literal; Spanish headings in Spanish.
- [ ] **GC-5 (no future content)**: no content from days after the target day; tone matches `prior_skills`.
- [ ] Guidelines align with parser `current` fields.
- [ ] At least **3 of 5** dimension aspect sentences and **2 of 3** must-discuss items name concrete theory topics.
- [ ] Both texts generated (student + professor) for the same skill.
- [ ] Student text: 3–5 lines per language (max 5), plain text, forward-looking (EN: “You will…” / imperative; ES: “Vas a…” / imperative).
- [ ] Student text states what the student will learn (theory) + what they will do (applied in project).
- [ ] Student preview questions exist (1–2) inline in each language.
- [ ] Professor text: summary (~45–60 words) ending with class checkpoint, Debate pacing, Participation criteria (exactly 3 bullets).
- [ ] Professor text covers all 5 dimensions as `####` subsections: Learn, Reflect, Be aware of, Do, Avoid.
- [ ] Anti-patterns explicitly mentioned under Avoid.
- [ ] Bridge included only for same-module continuity; omitted otherwise.
- [ ] Chat delivery: 4 copy blocks with headings before fences; student in ` ```text `, mentor in ` ```markdown `.
- [ ] Facilitator probes only under Reflect and Avoid; never as full answer keys.
- [ ] Per dimension: inline aspects (1–3 phrases), reflective questions (1–2). Milestone days: 1 question (max 2) per dimension.
- [ ] No internal analysis / “Phase 2” in final text. No duplicate question intent across dimensions.
- [ ] No mixed audiences: one text for Students, one for Mentors.
- [ ] Skill name, theory topics, and main concepts reflected correctly in both texts.
- [ ] Output is valid Markdown.

---

## Manual spot-check (before committing this skill)

- Run the generator for **Week 8 Day 22**: verify `Debate pacing` exists, `Facilitator probes` appears under Reflect/Avoid, the summary ends with class checkpoint; **no Bridge** to week 7 (different module: "Working with AI coding agents" starts at w8); if bridging w8 d23 from d22, use topic labels only.
- Pick a **sparse day** from the CSV (null/empty `anti_patterns` or `limitaciones`): verify questions still exist, and Avoid/Be aware degrade gracefully without inventing concepts.
- Pick an **HITO / milestone day**: verify reduced per-dimension questions (target 1–2) and deliverable-focused Summary/opening/closing.
