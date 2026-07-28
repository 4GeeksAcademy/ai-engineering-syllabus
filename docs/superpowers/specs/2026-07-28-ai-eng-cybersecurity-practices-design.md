# Design: `ai-eng-cybersecurity-practices`

**Project:** `ai-engineering-syllabus/content/projects/ai-eng-cybersecurity-practices`  
**Date:** 2026-07-28  
**Status:** Approved (design dialogue); awaiting implementation plan  
**Approach:** Full pack (READMEs + learn.json + `.learn/solution` + `.learn/example` EN/ES); preview URL wired, no binary PNG

---

## Problem

Students have already shipped agents, memory, MCP, and dashboard updates on their company monorepo fork. Nothing yet proves the stack is safe for production. Need a LearnPack project that:

1. Points students at company-specific security CONTEXT under `cybersecurity-analysis`.
2. Requires a NIST-mapped audit (Govern → Recover) plus remediation of critical gaps.
3. Matches sibling project packaging (root briefs, learn.json, solution bar, Maple Street classroom example).

Source briefs already exist (Downloads `README.md` / `README.es.md`); CONTEXT folder already exists with four companies (Nexova, HealthCore, Brasaland, TrackFlow).

---

## Goals

1. Scaffold `ai-eng-cybersecurity-practices` under `content/projects/`.
2. Root READMEs use CONTEXT link:  
   `https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/cybersecurity-analysis`
3. Ship `learn.json` aligned with monorepo-template siblings.
4. Ship `.learn/solution/README.md` as CONTEXT-aware grading bar (not a filled company solution).
5. Ship `.learn/example/README.md` + `README.es.md` as Maple Street Library security-audit parallel.
6. No `preview.png` binary in this pass; `learn.json` still references the conventional preview URL.

### Non-goals

- Generating real `preview.png` artwork.
- Per-company example scenarios (one Maple Street example only).
- Assigning a BreatheCode `asset_id` (unknown; omit or leave unset until registry).
- Implementing student monorepo remediations inside this syllabus repo.
- Editing existing `content/contexts/cybersecurity-analysis/*` files.

---

## Packaging approach (chosen)

**Approach 1 — Mirror `ai-eng-agent-harness` / `ai-eng-mcp-company-tools` full pack**

| File | Role |
| --- | --- |
| `README.md` / `README.es.md` | Student brief from Downloads; CONTEXT URL → `cybersecurity-analysis` |
| `learn.json` | Metadata, monorepo `template_url`, draft status, sharing links |
| `.learn/solution/README.md` | Staff grading bar: inventory, controls, NIST, common mistakes |
| `.learn/example/README.md` + `.es.md` | Maple Street classroom parallel (smaller scope, same spine) |

Rejected: generate preview PNG now; company-specific classroom examples.

---

## Layout

```
content/projects/ai-eng-cybersecurity-practices/
  README.md
  README.es.md
  learn.json
  .learn/
    solution/README.md
    example/README.md
    example/README.es.md
```

---

## Root READMEs

- Content: provided EN/ES briefs (Secure Practices / Prácticas Seguras).
- Only required content change vs Downloads: CONTEXT link target becomes  
  `.../tree/main/content/contexts/cybersecurity-analysis`  
  (not the generic `.../contexts` root).
- Keep monorepo fork framing, NIST ticket narrative, inventory + security-by-design + NIST report checklists, evaluation, submit via PR.

---

## `learn.json`

| Field | Value |
| --- | --- |
| `slug` | `ai-eng-cybersecurity-practices` |
| `title.en` | Secure Practices for AI Integration in Systems |
| `title.es` | Prácticas Seguras en la Integración de IA en Sistemas |
| `description` | Inventory + NIST six-function report + remediate critical gaps (prompt injection, secrets, rate limiting, agent logging, HITL irreversible actions) |
| `template_url` | `https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo` |
| `status` | `draft` |
| `difficulty` | `intermediate` |
| `duration` | `2` |
| `coverImage` | `ai-coding.svg` |
| `technologies` | python, security, nist, agents, prompt-injection, rate-limiting, observability |
| `translations` | `["es", "en"]` |
| `projectType` | `project` |
| `gitpod` | `true` |
| `solution` / `preview` / `sharing` | Same URL pattern as siblings under this slug |
| `telemetry.batch` | Omit `asset_id` until assigned (do not invent) |

---

## `.learn/solution` — grading bar

Indicative quality bar for the student’s company monorepo fork. Values must come from assigned `CONTEXT-*.md` under `content/contexts/cybersecurity-analysis/`.

Must verify:

1. AI systems inventory complete; owner per component (CONTEXT inventory section).
2. No hardcoded secrets; env/vault only.
3. ≥1 reproducible prompt-injection test that blocks/neutralizes (CONTEXT suggested cases).
4. Rate limiting on ≥1 model-calling endpoint, verifiable.
5. Logging of decisions/actions on ≥1 agentic flow.
6. Irreversible actions require explicit human confirmation (CONTEXT irreversible list).
7. NIST report covers Govern, Identify, Protect, Detect, Respond, Recover — ≥1 concrete prioritized action each; cites CONTEXT regulatory framework (not generic).
8. Unfixed gaps documented with risk + proposed mitigation.

Include: recommended monorepo layout (indicative), PR evidence checklist, common-mistakes table (generic NIST, missing CONTEXT regs, injection test that never fails build, secrets in code).

---

## `.learn/example` — Maple Street (EN + ES)

Instructor classroom parallel. Same spine as graded project; different domain.

| Graded project | Class example |
| --- | --- |
| Company monorepo + CONTEXT-company.md | Maple Street Library desk agent only |
| Full AI inventory + full NIST report | Short inventory + 6-row NIST checklist |
| Company prompt-injection + HITL from CONTEXT | 2 injection cases + 1 irreversible (waive fine) needs human confirm |
| Prod rate limit + agent logs | In-memory rate limit + print / tiny CLI logs |

Teaching spine:

1. Inventory of AI touchpoints (user, FAQ/RAG, tools).
2. Secrets via env.
3. Input validation + system/user separation.
4. Untrusted FAQ/RAG isolation (poisoned `[SYSTEM]` chunk).
5. Rate limit on model-calling endpoint.
6. Agent action logging.
7. Human confirm before irreversible waive.
8. Mini NIST table with one action per function.

Students still follow root `README.md` for the graded deliverable.

---

## Testing / validation (of this scaffold)

- CONTEXT URLs resolve to existing folder with four company pairs.
- `learn.json` valid JSON; slug matches folder name.
- EN/ES example cross-link; root READMEs cross-link.
- No invented telemetry `asset_id`.
- No edits to `content/contexts/cybersecurity-analysis/`.

---

## Open follow-ups (out of scope for scaffold)

- Register BreatheCode asset and fill `telemetry.batch`.
- Add real `preview.png` when design asset available.
- Syllabus outline / CSV linkage if not already pointed at this slug.
