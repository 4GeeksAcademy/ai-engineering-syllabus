# In-Class Example: Pantry Stock Board (SDD)

> **Instructor note:** Classroom example for _Operations Backoffice – Inventory Manager_. Same loop (`specify → plan → tasks → implement → verify`) on a tiny pantry domain. Scoped for a 1–2 hour live session. Do NOT share with students before they attempt the main project.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The scenario

### Scope note

Live-session scope only. Same SDD patterns as the official student project; CONTEXT catalogues and monorepo depth are reduced. Students still follow the full brief in the project root `README.md`.

A coworking kitchen tracks coffee, milk, and snacks. People used to edit a `stock` number in a spreadsheet. Ops lead wants a tiny board: register items, log movements, never touch stock directly — and flag anything below reorder.

Assume `.agents/rules` and a small `memory-bank/` already exist from a prior exercise.

---

## Phase 1 — Spec (20 min)

Create `specs/pantry/spec.md` with ≥4 EARS criteria, including:

| Id        | Intent                                 |
| --------- | -------------------------------------- |
| `PAN-001` | Stock derived from movements only      |
| `PAN-002` | Reject outbound that would go negative |
| `PAN-003` | Reject movement on unknown item        |
| `PAN-004` | Flag when stock &lt; reorder_point     |

No architecture or task list in this file.

---

## Phase 2 — Plan + tasks (15 min)

- [ ] `plan.md` — where calculation lives (e.g. service function summing movements); justify why no `stock` column is writable.
- [ ] `tasks.md` — one task per criterion id; e.g. `T-001` → `PAN-001`.

---

## Phase 3 — Implement + verify (40–50 min)

### Minimal model

| Entity   | Fields                                                                              |
| -------- | ----------------------------------------------------------------------------------- |
| Item     | `name`, `unit` (`kg`\|`unit`), `reorder_point`                                      |
| Movement | `item_id`, `kind` (`inbound`\|`outbound`\|`adjustment`), `quantity`, `reason`, `at` |

### Must demo

- [ ] Item create/list
- [ ] Log inbound then outbound; stock display matches sum
- [ ] Attempt direct stock edit path does not exist (or is rejected)
- [ ] Negative outbound rejected; stock unchanged
- [ ] Below-reorder visual signal
- [ ] At least one test per `PAN-00x`

### Mid-session change (optional 10 min)

Instructor adds: "Adjustments that set absolute stock are forbidden; only delta adjustments." Students edit `spec.md` first, regenerate affected tasks only, then code.

---

## Discussion questions

1. Why is an editable `stock` field the agent's default failure mode?
2. What belongs in `plan.md` that must **not** appear in `spec.md`?
3. Why regenerate only affected tasks after a requirement change?

---

## Instructor checklist

- [ ] Spec uses EARS + ids; invariant explicit
- [ ] Layers not mixed into one doc
- [ ] Tests map to criterion ids
- [ ] If change demo ran: evidence of spec-first edit
