---
name: transversal-project-orchestrator
description: Orchestrates the generation of all artifacts for a 4Geeks Academy transversal project milestone — the universal project statement and the company-specific briefing files. Use this skill when a user wants to generate everything for a milestone at once, or when it is unclear whether they need only the README, only the BRIEFING files, or both. Trigger on phrases like "generate milestone N", "create all the files for hito X", "set up milestone N for these companies", or any request that involves a milestone number and one or more company descriptions without specifying which artifact they want. For targeted requests ("only generate the README", "only generate the context"), this skill will detect the intent and delegate accordingly. Always use this skill as the entry point when the scope of the request is ambiguous.
---

# 4Geeks Academy — Transversal Project Generator (Orchestrator)

This skill is the single entry point for transversal project generation. It detects what needs to be produced and delegates to the appropriate specialized skill.

---

## Step 1 — Detect What Is Needed

Before asking for any inputs, determine which artifacts the request requires:

| Situation                           | What to generate            | Skills to invoke                                                                      |
| ----------------------------------- | --------------------------- | ------------------------------------------------------------------------------------- |
| No README exists for this milestone | README + all BRIEFING files | `transversal-project-readme-generator` → then `transversal-project-context-generator` |
| README exists, new company needed   | BRIEFING file(s) only       | `transversal-project-context-generator`                                               |
| README exists, needs rewrite        | README only                 | `transversal-project-readme-generator`                                                |
| Explicit "everything" request       | README + all BRIEFING files | Both skills in order                                                                  |

If the situation is ambiguous, ask one clarifying question before proceeding:

> Does a README already exist for this milestone, or does it need to be created?

Do not ask any other questions until this is resolved.

---

## Step 2 — Collect Inputs for the Detected Scope

Collect only the inputs needed for the detected scope. Never ask for inputs that belong to an artifact that will not be generated.

**If README needs to be generated**, collect:

| Input                | Description                             | Default                                                                    |
| -------------------- | --------------------------------------- | -------------------------------------------------------------------------- |
| `milestone_number`   | Milestone number (e.g., `6`)            | — Must ask —                                                               |
| `milestone_topic`    | Core skill(s) this milestone teaches    | — Must ask —                                                               |
| `milestone_position` | `early`, `mid`, or `late` in the course | — Must ask —                                                               |
| `prior_milestones`   | What students have already built        | — Must ask —                                                               |
| `tech_stack`         | Technologies required                   | — Must ask —                                                               |
| `template_repo`      | Starter repo URL                        | `https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo` |
| `authors`            | GitHub username(s)                      | — Must ask —                                                               |

**If BRIEFING files need to be generated**, collect:

| Input               | Description                                         | Default                               |
| ------------------- | --------------------------------------------------- | ------------------------------------- |
| `existing_readme`   | The milestone README — read it in full              | — Must ask if not already available — |
| `company_scenarios` | Company descriptions to generate BRIEFING files for | — Must ask —                          |
| `reference_context` | An existing BRIEFING file for parity calibration    | Optional                              |

> If both README and BRIEFING are needed, collect all inputs together in a single round before generating anything.

---

## Step 3 — Execute in Order

When both artifacts are needed, always generate the README first and the BRIEFING files second. The BRIEFING generator requires a completed README as input — it reads the README to extract the implied BRIEFING structure before writing anything.

### Generating the README

Read and follow `.cursor/skills/transversal-project-readme-generator/SKILL.md` in full before writing any README content.

### Generating the BRIEFING files

Once the README is complete (either just generated or provided as input), read and follow `.cursor/skills/transversal-project-context-generator/SKILL.md` in full before writing any BRIEFING content.

Pass the completed README as the `existing_readme` input to the context generator — even when it was just generated in the same session. The context generator must read it to extract the implied structure.

---

## Step 4 — Delivery

Deliver files in this order:

1. `README.md` (if generated)
2. `README.es.md` (if generated)
3. `<slug>-BRIEFING.en.md` / `<slug>-BRIEFING.es.md` for each company variant (if generated)

If only one type of artifact was generated, deliver only those files. Do not deliver placeholder or empty files for artifacts that were not requested.

---

## Quality Self-Check

- [ ] Scope was detected before collecting any inputs
- [ ] Only inputs relevant to the detected scope were requested
- [ ] README generator skill was read before generating the README
- [ ] Context generator skill was read before generating BRIEFING files
- [ ] When both were generated, README was completed before BRIEFING generation began
- [ ] BRIEFING generator received the completed README as input
- [ ] All files delivered in the correct order
