# Branch Queue — Tagged Service Queue Manager

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/branch-queue/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your challenge

Banco Meridional has modernized its branches — clients now take a numbered ticket at the entrance and sit down to wait. Each ticket is tagged with a service type: **deposits**, **withdrawals**, or **account management**. The branch has dedicated agents for each service type, and they operate independently: the deposits agent calls their next client regardless of what the withdrawals agent is doing.

The operations manager has noticed a problem with the current paper-based system: if the deposits agent finishes with a client and the only people waiting are there for withdrawals, the deposits agent sits idle even though there might be a deposits client who arrived earlier but is buried in the general list. The branch needs a system where each agent can instantly call their next client without scanning the entire waiting room.

The IT team has been asked to build a terminal-based queue manager to model this system before it gets integrated into the branch's touchscreen kiosks.

> The operations manager's requirements document reads:
>
> #### Ticket issuance
>
> - A client takes a ticket specifying a **service type**: `deposit`, `withdrawal`, or `account_management`.
> - The ticket must record the client's name, the service type, and the arrival timestamp.
> - Tickets are numbered sequentially from 1 upward (global counter, across all services).
>
> #### Agent operations
>
> - Each agent is assigned to exactly one service type.
> - When an agent is free, they call the **next client in their service queue** — the one who has been waiting longest for that service type.
> - An agent cannot call a client from a different service queue.
>
> #### System operations required
>
> - Issue ticket: register a new client in the appropriate service queue.
> - Call next: given a service type, dequeue and return the next client waiting for it.
> - Peek next: show who is next for a given service type without removing them.
> - List all waiting: display all clients currently waiting, grouped by service type, in the order they will be attended within each group.
> - Global stats: report the current count of waiting clients per service type and overall.

Think carefully about how to structure the queues internally. A single ordered list of all clients would require scanning the entire list every time an agent calls their next client — which gets slow as the branch fills up. There is a simpler structure that makes each agent's `call next` operation instant, regardless of how many people are waiting for other services. What is it?

---

## 🌱 How to Start the Project

This project does not require a starter repository — you will build it from scratch.

1. Create a new GitHub repository called `branch-queue`.
2. Clone it locally or open it in a GitHub Codespace.
3. Create a `branch_queue.py` file as your entry point.
4. Review the [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project) guide if needed.

---

## 💻 What You Need to Do

### Data model

- [ ] Define a `Ticket` class (or dataclass) with at minimum: `number` (int, global sequential), `client_name`, `service_type` (string: `"deposit"`, `"withdrawal"`, `"account_management"`), and `issued_at` (timestamp).
- [ ] Define a `BranchQueue` class that manages one internal queue per service type and a global ticket counter.

### Core queue operations

- [ ] `issue_ticket(client_name, service_type)` — create and enqueue a ticket in the correct service queue; return the issued ticket.
- [ ] `call_next(service_type)` — dequeue and return the next client for that service type; raise a meaningful error if no clients are waiting for it.
- [ ] `peek_next(service_type)` — return the next client for a service type without removing them.
- [ ] `list_waiting()` — return a dictionary with each service type as a key and its ordered list of waiting tickets as the value.
- [ ] `stats()` — return a dictionary with the count per service type and a `"total"` key.

### CLI interaction

- [ ] Build a simple text menu (loop) that lets a user:
  - Issue a new ticket (prompt for client name and service type).
  - Call the next client for a given service type.
  - View the full waiting list grouped by service.
  - See queue stats.
  - Exit.

### Correctness and edge cases

- [ ] Ticket numbers must be globally sequential — two clients cannot share a number even if they are in different service queues.
- [ ] Clients in the same service queue must be called in strict arrival order.
- [ ] `call_next()` or `peek_next()` on an empty service queue must not crash the program.
- [ ] An invalid service type must be rejected at ticket issuance with a clear message.

### Design notes (no code required — include as comments or a `DESIGN.md`)

- [ ] Explain why a separate queue per service type makes `call_next` more efficient than a single shared queue.
- [ ] Describe what would happen if two agents of the same service type called `call_next` at the same moment. What state mutation must happen first to ensure the same client is not called twice?

⚠️ **IMPORTANT:** Use only Python's standard library (`collections.deque`, `datetime`). No external packages.

---

## ✅ What We Will Evaluate

- [ ] `BranchQueue` maintains one internal queue per service type.
- [ ] Ticket numbers are globally sequential across all service types.
- [ ] Within each service queue, FIFO order is strictly preserved.
- [ ] All five operations (`issue_ticket`, `call_next`, `peek_next`, `list_waiting`, `stats`) are implemented and work correctly.
- [ ] Edge cases handled: empty queue does not crash; invalid service type is rejected with a message.
- [ ] Code is organized in classes with clear responsibilities.
- [ ] Design note explains why the per-service structure is more efficient than a single shared list.
- [ ] Design note addresses the concurrent `call_next` scenario and identifies the correct mutation order.
- [ ] CLI loop is functional and does not crash on invalid input.

> Note: persistence, authentication, or agent assignment are not required and will not be evaluated.

---

## 📦 How to Submit

Push your repository to GitHub and share the link according to your instructor's instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/branch-queue/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
