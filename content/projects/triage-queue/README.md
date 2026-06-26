# Triage Queue — Priority Queue Manager

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/triage-queue/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

A public hospital's IT department has been asked to modernize its emergency unit intake process. Right now, a nurse manually writes patient names on a whiteboard and calls them out in arrival order — which creates chaos when a critical case comes in and jumps the line, or when two nurses try to update the board at the same time and one entry gets erased.

The hospital's technical lead has handed you a spec outlining what the new triage queue manager must do. The system will run in a terminal for now — no UI, just a clean Python program that correctly models and operates the queue so it can later be integrated into a larger application.

> Your technical lead's spec reads as follows:
>
> #### Patient intake
>
> - When a new patient arrives, they are assigned a **triage level** (1 = critical, 2 = urgent, 3 = standard).
> - The patient's name, arrival timestamp, and triage level must be recorded.
>
> #### Attention order
>
> - Patients with triage level 1 are always served before level 2, and level 2 before level 3.
> - Within the same triage level, patients are attended in **arrival order** (FIFO).
>
> #### Operations required
>
> - Enqueue: add a new patient.
> - Dequeue: call the next patient to be attended.
> - Peek: show who is next without removing them.
> - List queue: display all patients currently waiting, in the order they will be attended.
> - Stats: report the current count per triage level.

A simple `deque` won't be enough here — you'll need to think carefully about how to model a priority queue and what data structure best supports the required operations. Think about what happens if a level-1 patient arrives while the queue is being processed: how do you ensure they are placed correctly without re-sorting the entire queue on every insertion?

This is the kind of problem that appears constantly in production systems — scheduling jobs, routing support tickets, processing webhook events. Build it cleanly and you'll have something real to talk about in your next technical interview.

---

## 🌱 How to Start the Project

This project does not require a starter repository — you will build it from scratch.

1. Create a new GitHub repository called `triage-queue`.
2. Clone it locally or open it in a GitHub Codespace.
3. Create a `triage_queue.py` file as your entry point.
4. Review the [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project) guide if needed.

---

## 💻 What You Need to Do

### Data model

- [ ] Define a `Patient` class (or dataclass) with at minimum: `name`, `triage_level` (int, 1–3), and `arrived_at` (timestamp).
- [ ] Define a `TriageQueue` class that internally manages the priority queue logic.

### Core queue operations

- [ ] `enqueue(patient)` — add a patient; position in the queue must respect triage level and arrival order.
- [ ] `dequeue()` — remove and return the next patient to be attended; raise a meaningful error if the queue is empty.
- [ ] `peek()` — return the next patient without removing them.
- [ ] `list_queue()` — return all waiting patients in attention order as a list.
- [ ] `stats()` — return a dictionary with the count of waiting patients per triage level.

### CLI interaction

- [ ] Build a simple text menu (loop) that lets a user:
  - Add a new patient (prompt for name and triage level).
  - Call the next patient.
  - View the current queue.
  - See queue stats.
  - Exit.

### Correctness and edge cases

- [ ] A new critical (level 1) patient arriving while level-2 and level-3 patients are waiting must be placed ahead of them.
- [ ] Two patients at the same triage level must be attended in strict arrival order.
- [ ] Calling `dequeue()` or `peek()` on an empty queue must not crash the program — handle it gracefully.

### Design notes (no code required — include as comments or a `DESIGN.md`)

- [ ] Briefly explain why you chose your internal data structure over alternatives (e.g., a single `deque`, a sorted list, three separate queues).
- [ ] Describe how you would handle the case where a worker picks a patient from the queue at the same moment another worker enqueues a new critical patient. What state mutation order prevents double-processing?

⚠️ **IMPORTANT:** Use only Python's standard library (`collections.deque`, `heapq`, `datetime`). No external packages.

---

## ✅ What We Will Evaluate

- [ ] `TriageQueue` correctly models a priority queue: level 1 always before level 2, level 2 always before level 3.
- [ ] Within the same triage level, FIFO order is strictly preserved.
- [ ] All five operations (`enqueue`, `dequeue`, `peek`, `list_queue`, `stats`) are implemented and work correctly.
- [ ] Edge cases handled: empty queue dequeue/peek does not crash, duplicate triage levels are ordered by arrival.
- [ ] Code is organized in classes with clear responsibilities (no logic dumped in `main()`).
- [ ] Design note explains the data structure choice with a concrete reason.
- [ ] Design note addresses the concurrent mutation scenario, even informally.
- [ ] CLI loop is functional and does not crash on invalid input.

> Note: persistence (saving to a file or database) is not required and will not be evaluated.

---

## 📦 How to Submit

Push your repository to GitHub and share the link according to your instructor's instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/triage-queue/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
