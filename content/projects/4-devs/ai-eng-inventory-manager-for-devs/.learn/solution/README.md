# Operations Backoffice – Inventory Manager — Reference Solution

## Purpose

Spec Driven Development on the company monorepo: **spec → plan → tasks → implement → verify**, then absorb a mid-stream requirement change by editing the spec first.

Domain catalogues (units, categories, locations/lots, reorder rules) come from `content/contexts/4-devs/inventory-manager-for-devs/`. Generic inventory that ignores CONTEXT fails review.

Builds on existing `.agents/rules` and `memory-bank/` — specs must not restate them; they extend them.

## Expected layout

```text
specs/inventory-manager/
  spec.md      # what: behavior, contracts, invariants (EARS + IDs)
  plan.md      # how: architecture decisions only
  tasks.md     # order: atomic tasks, each linked to a criterion ID
# plus implementation in monorepo services/uis following existing conventions
```

Branch: `feature/inventory-manager`. One commit per implemented task (reference task id). One mega-commit = reject.

## Required coverage (from README)

### Spec layer (`spec.md`)

- Behavior, contracts, invariants — no architecture dump, no task list.
- Acceptance criteria in **EARS**, each with unique id (e.g. `INV-001`).
- Explicit criterion: **stock is derived from movements; never edited directly**.
- Unwanted behavior criteria: movement that would leave stock negative; movement on nonexistent item or lot.

### Plan layer (`plan.md`)

- Data model, where stock calculation lives, movement recording approach.
- Justifies non-obvious decisions; does not restate EARS criteria.

### Tasks layer (`tasks.md`)

- Atomic, independently verifiable tasks.
- Each task references the criterion id it implements.
- No task bundles unrelated criteria.

### Implementation

- Item CRUD with CONTEXT fields.
- Movements: inbound, outbound, adjustment — each with reason + timestamp.
- Available stock = calculation from movements (no direct stock write path).
- Reorder point per item; backoffice visibly flags below-reorder items.
- Respect monorepo stack/conventions.

### Verification

- Test suite maps to acceptance criteria (including stock invariant + unwanted behaviors).
- Traceability: `requirement (INV-xxx) → test → commit (task id)`.

### Requirement change

- Edit `spec.md` first → update `plan.md` if needed → regenerate **only** affected tasks.
- PR documents which spec sections changed and which tasks were regenerated.
- Evidence of code-first patches without spec update = fail that part.

## Indicative EARS examples (not copy-paste for students)

```text
INV-010 (Ubiquitous): The system shall compute an item's available stock solely from the sum of its recorded movements.
INV-020 (Unwanted): If an outbound movement would leave available stock negative, then the system shall reject the movement and leave stock unchanged.
INV-030 (Event-driven): When available stock falls below the item's reorder_point, the system shall mark the item as below reorder in listing and detail views.
```

Exact ids/wording are student-owned; presence of invariant + unwanted cases is non-negotiable.

## Reviewer checklist

- [ ] Three separate files under `specs/inventory-manager/` — layers not mixed
- [ ] EARS criteria with unique ids; stock invariant explicit + tested
- [ ] Unwanted: negative stock, missing item/lot — criteria + tests
- [ ] Tasks ↔ criterion ids; commits ↔ task ids
- [ ] Items + inbound/outbound/adjustment; CONTEXT domain values
- [ ] Below-reorder visible in backoffice
- [ ] Requirement change: spec-first, partial task regen documented in PR
- [ ] Commit history split by tasks
