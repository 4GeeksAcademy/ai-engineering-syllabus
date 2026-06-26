# In-Class Example: Print Shop Job Queue — Priority Queue (Class Example)

> **For instructors:** Parallel classroom scenario for `triage-queue`. Same spine (priority queue with FIFO within level, five core operations, CLI menu, stdlib-only data structures, design discussion on concurrency), different domain. Students still follow the full hospital brief in the project root `README.md`.

_These instructions are also available in [Spanish](./README.es.md)._

---

## The challenge

A neighborhood print shop still tracks orders on a paper pad. Rush wedding programs jump ahead of standard flyers, but two clerks updating the pad at once erase each other's notes. Your live demo models a **terminal queue manager** — no UI — that can later plug into a real app.

> **From the shop manager's spec:**
>
> - Each job gets a **priority level** (1 = rush, 2 = same-day, 3 = standard).
> - Record customer name, arrival time, and priority level.
> - Level 1 always before 2, level 2 always before 3; **FIFO within the same level**.
> - Operations: enqueue, dequeue, peek, list queue, stats.

### Scope note

Scoped for **one live session (~60–90 min)**. Same patterns as the student project, but:

- Domain is a **print shop**, not a hospital.
- Single file `print_queue.py` — no starter repo.
- `DESIGN.md` is **verbal in class**; students write it for the real project.
- Full five-option CLI menu is homework if time runs short; live demo needs at least add / call next / view queue.

---

## What to build

### Data model

- [ ] `Job` dataclass: `customer_name`, `priority_level` (int 1–3), `arrived_at` (`datetime`).
- [ ] `PrintQueue` class owning the internal priority structure.

### Core queue operations

- [ ] `enqueue(job)` — insert respecting priority + arrival order.
- [ ] `dequeue()` — remove and return next job; meaningful error if empty.
- [ ] `peek()` — next job without removing.
- [ ] `list_queue()` — all waiting jobs in attention order.
- [ ] `stats()` — `dict` counts per priority level.

| Method       | Expected behavior                                           |
| ------------ | ----------------------------------------------------------- |
| `enqueue`    | Rush job lands ahead of waiting same-day and standard jobs  |
| `dequeue`    | Always pops from lowest non-empty level (1 → 2 → 3)         |
| `peek`       | Same target as `dequeue` but no mutation                    |
| `list_queue` | `[all level-1 jobs FIFO] + [level-2 FIFO] + [level-3 FIFO]` |
| `stats`      | e.g. `{1: 0, 2: 2, 3: 1}`                                   |

### CLI (minimum for live demo)

- [ ] Text menu loop:
  - Add job (name + priority).
  - Call next job (`dequeue`).
  - View queue (`list_queue`).
  - _(Homework if needed: stats + exit polish)_

### Correctness (demo in front of class)

- [ ] Rush job arriving while same-day and standard jobs wait → goes to front.
- [ ] Two same-day jobs → strict arrival order.
- [ ] Empty `dequeue()` / `peek()` → caught in CLI, no crash.

⚠️ **Stdlib only:** `collections.deque`, `heapq`, `datetime`.

---

## Verify together

- [ ] Add standard job, then rush job → rush prints first on "call next".
- [ ] Add two same-day jobs 30 seconds apart → first added called first.
- [ ] `list_queue` order matches expected attention order after mixed inserts.
- [ ] `stats()` counts match visible queue.
- [ ] `dequeue()` on empty queue prints friendly message, program continues.
- [ ] Invalid priority (e.g. `4`) rejected without crash.

---

## Discussion questions

1. Why is a single `deque` insufficient for this spec? What breaks if you only append and pop from one end?
2. Three separate `deque` instances (one per level) vs one `heapq` with `(priority, counter, job)` tuples — what trade-offs matter for enqueue/dequeue complexity and code clarity?
3. If two clerks share one queue object, what mutation order on `dequeue` + `enqueue` prevents the same job from being processed twice?
