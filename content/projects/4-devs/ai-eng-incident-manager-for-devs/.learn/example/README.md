# In-Class Example: Café Ops Incident Board

> **Instructor note:** Classroom example for _Operations Backoffice – Centralized Incident Manager_. Same core ideas (recon → rules → memory-bank → lifecycle + history) on a tiny café domain. Scoped for a 1–2 hour live session. Do NOT share with students before they attempt the main project.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The scenario

### Scope note

Live-session scope only. Same patterns as the official student project; secondary CONTEXT catalogues and monorepo depth are reduced. Students still follow the full brief in the project root `README.md`.

A small café chain runs three locations. Shift leads report equipment and staffing issues by WhatsApp or phone; nothing is centralized. The ops lead wants a tiny backoffice board: log an incident, assign an area, move status, and see who changed what.

The repo is a stub monorepo with folders and naming already decided but undocumented.

---

## Phase 1 — Reconnaissance (15 min)

- [ ] Ask the agent for a project summary.
- [ ] Open the real tree and correct at least **two** wrong claims in that summary.
- [ ] Note ≥2 conventions already visible in code (e.g. package manager, folder layout).
- [ ] Log one improvement idea **without** applying it.

---

## Phase 2 — One rule + tiny memory bank (20 min)

Create `.agents/rules/no-new-package-manager.md`:

```markdown
---
description: Do not introduce a second package manager
globs: ["**/package.json", "**/pnpm-lock.yaml", "**/package-lock.json"]
alwaysApply: false
---

# No second package manager

- Use the lockfile and manager already present in the repo.
- Do not add npm/yarn/pnpm if another is already the source of truth.
- If a change seems to require a different manager, stop and ask.
```

Create `memory-bank/` with:

- `product.md` — café ops, who uses the board, what a "critical" incident means here
- `stack.md` — whatever the stub already uses
- `status.md` — empty board → first incident feature in progress

---

## Phase 3 — Minimal incident board (40–50 min)

### Model

| Field                  | Notes                                                         |
| ---------------------- | ------------------------------------------------------------- |
| `id`                   | Auto                                                          |
| `title`, `description` | Required                                                      |
| `channel`              | `whatsapp` \| `phone_call` \| `dashboard`                     |
| `type`                 | `equipment_failure` \| `staffing_gap` \| `customer_complaint` |
| `severity`             | `critical` \| `high` \| `medium` \| `low`                     |
| `responsible_area`     | `operations` \| `people` \| `technology`                      |
| `status`               | `open` → `assigned` → `in_progress` → `resolved` → `closed`   |
| `assigned_to`          | Optional string                                               |
| history                | Status and assignee changes with `author` + timestamp         |

### Must demo

- [ ] Create + list + filter by `status` and `severity`
- [ ] Assign `responsible_area` / `assigned_to`
- [ ] Full status walk to `closed`
- [ ] Detail view shows change history
- [ ] Simple open-by-severity counts

---

## Discussion questions

1. Why record agent-summary discrepancies instead of only fixing the summary quietly?
2. When is a rule better than a memory-bank paragraph?
3. Why is "updated_at changed" not enough for ops accountability?

---

## Instructor checklist

- [ ] Students corrected the agent summary with evidence
- [ ] Rule has scope / apply mode
- [ ] Memory bank mentions product meaning of severity, not only stack
- [ ] History shows author + time for at least one status change
