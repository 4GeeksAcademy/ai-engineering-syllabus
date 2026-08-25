# Operations Backoffice – Centralized Incident Manager — Reference Solution

## Purpose

Two deliverables, in order:

1. **Repository stewardship** — conventions already in the monorepo become explicit `.agents/rules` + a company-specific `memory-bank/`.
2. **Incident manager** — CRUD + lifecycle + assignment + change history, catalogues from `content/contexts/centralized-incident-manager-for-devs/`.

Not an auth project. Field names, channels, types, severities, areas, and lifecycle come from the student's `CONTEXT-company.md` — generic placeholders fail review.

## Expected layout

```text
.agents/
  rules/                    # ≥3 rules derived from preexisting codebase
memory-bank/                # product, stack, current state (+ implementation plan)
# plus monorepo apps/services as already structured — no new stack without a justified rule
```

Branch: `feature/incident-manager`. Commits split by checklist phase — one mega-commit is a reject.

## Required coverage (from README)

### Codebase reconnaissance

- Agent summary of the monorepo exists.
- Student verified that summary against real structure/code.
- Documented discrepancies (agent hypothesis vs repository reality).
- ≥3 conventions identified from code (naming, folders, deps, style, separation of concerns).
- ≥1 improvement proposal logged without applying unilaterally.

### Project rules (`.agents/rules`)

- ≥3 rule files, one concern each.
- Each rule declares application mode (always / glob / agent-requested / manual) + scope.
- Verifiable wording: what is done, what is not, which paths.
- Evidence in PR: which rule blocked a deviation during development.

### Memory bank (`memory-bank/`)

Minimum layers:

| Artifact            | Must cover                                                                                |
| ------------------- | ----------------------------------------------------------------------------------------- |
| Product / business  | Company, who uses backoffice, what an incident means in this operation (CONTEXT-grounded) |
| Tech stack          | What the monorepo already ships                                                           |
| Current state       | Done / in progress / closed decisions — updated at end ≠ start                            |
| Implementation plan | Written with the agent before coding the manager                                          |

### Incident manager

- Create, edit, list, detail — fields from CONTEXT.
- Catalogues: intake channel, type, severity, responsible area — exact CONTEXT values.
- State lifecycle through closure (and `reopened` if CONTEXT defines it).
- Every status change and every ownership / responsible-area change → timestamped, authored history, queryable from detail.
- List filters: state, severity, responsible area.
- At-a-glance view: volume of **open** incidents by severity.
- Respect monorepo stack/conventions; no new libs/managers/patterns without a justifying rule.

## Indicative history entry shape

```json
{
  "field": "status",
  "from": "open",
  "to": "assigned",
  "author": "felipe.guerrero",
  "at": "2026-03-12T14:22:00Z"
}
```

Exact schema may follow monorepo patterns; presence of timestamp + author + queryable history is non-negotiable.

## Validation notes

- CONTEXT catalogues match implementation enums (channel, type, severity, area).
- Seed / sample data satisfies CONTEXT seed rules when present.
- Empty list and zero open-by-severity counts do not 500.
- Re-run or re-seed must not invent duplicate business identities if CONTEXT requires idempotency.
- Review agent-generated code before commit.

## Reviewer checklist

- [ ] Discrepancy record exists (agent summary vs real repo)
- [ ] `.agents/rules` ≥3 codebase-derived rules with mode + scope
- [ ] `memory-bank/` has product, stack, state; product is company-specific
- [ ] Versioned implementation plan; delivery matches it
- [ ] Manager: channel/type/severity + area assignment + full lifecycle
- [ ] Change history queryable from detail (timestamp + author)
- [ ] Filters: state, severity, area; open-by-severity volume view
- [ ] Catalogues match assigned CONTEXT
- [ ] No stack/convention drift without a rule
- [ ] Commit history split by steps; PR documents rules + discrepancies + optional improvement proposal
