<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: read your **[COMPANY-BRIEF.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts)** and your **[CONTEXT-audit-log.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/audit-log)** before writing any code — that's where your company's critical events and who should be able to query them live.

---

# Platform – Audit Log

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** — not on a new repository.

Compliance (or whoever fills that role at your company) opens a **ticket** after a minor incident that nobody could fully reconstruct: someone modified sensitive data, but there was no reliable way to know who, when, or from where. Your CTO passes it to you as a priority.

> _"I need to be able to answer, without ambiguity, three questions about any sensitive action in the system: who did it, exactly what they did, and when. A normal application log that anyone with database access can edit or delete after the fact doesn't work for me — I need something that, once written, stays written. If in six months someone asks 'who changed this,' the answer has to come from the system, not from anyone's memory."_
>
> — CTO

Three requirements from the brief are easy to implement halfway if you don't read closely:

1. **Genuinely append-only.** An audit record that can be edited or deleted from the application isn't an audit record — it's just another log. Immutability must be a property of the design, not a convention the team promises to respect.
2. **The "who" isn't only the human user.** If your system has agents or automated processes acting on data, those actions must be logged too, clearly identifying that the actor was a process, not a person.
3. **Not everyone can query the full record.** Who can see which part of the audit log depends on the roles and departments you already defined at the platform level — this project builds on that foundation, it doesn't replace it.

### Complementary knowledge: what makes a record "an audit record"

A technical log (errors, latency, traces) and an audit record aren't the same thing, even though both "record things." The audit record exists to answer accountability and compliance questions — who did what to which resource — and that's why its design prioritizes three properties a technical log usually doesn't need: **immutability** (can't be altered once written), **completeness** (covers every sensitive action, not just errors), and **clear attribution** (there's always an identified actor, human or system). A common technique to reinforce immutability is hash chaining: each entry includes the hash of the previous entry, so altering a past record visibly breaks the chain.

---

## 🌱 How to Start the Project

1. `pull` the latest changes from your fork of the monorepo.
2. Read `COMPANY-BRIEF.md` and `CONTEXT-audit-log.md` in full before touching any code.
3. Create a new branch: `feature/audit-log`.
4. Inventory the sensitive actions that already exist in your system (creation, modification, deletion of critical resources, permission changes, access to restricted data).
5. Design the audit entry schema first (actor, action, resource, timestamp, origin) before deciding where each record gets triggered.

---

## 💻 What You Need to Do

**Model and storage**

- [ ] Design a dedicated append-only table or collection for the audit log, separate from the system's operational tables
- [ ] Each entry includes at minimum: actor (user or process), action performed, affected resource, timestamp, and origin (IP or process identifier)
- [ ] Implement a mechanism that makes any later alteration of an already-written entry evident (e.g., hash chaining)
- [ ] Guarantee, at the database or application level, that there's no `UPDATE` or `DELETE` path onto this table from the application

**Event capture**

- [ ] Instrument audit capture on the sensitive actions identified in your initial inventory
- [ ] Log actions executed by automated processes or agents, clearly distinguishing them from human actions
- [ ] Log relevant authentication events (successful login, failed login, permission changes) if your system already has those flows

**Viewer and querying**

- [ ] Implement a backoffice view to query the log, with filters by actor, action type, resource, and date range
- [ ] Restrict access to the viewer according to the roles and departments already defined in your platform — not every Admin should necessarily see the entire unrestricted log, depending on what your company context specifies
- [ ] Implement reasonable pagination or query limits so the viewer stays usable with real data volumes

⚠️ **IMPORTANT:** the events considered critical for your company and the rules for who can query them must match exactly what's specified in your `CONTEXT-audit-log.md`. A generic implementation that ignores that context will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] There's a test demonstrating that an audit log entry cannot be modified or deleted from the application once written
- [ ] All sensitive actions identified in the inventory are correctly logged, with actor, action, resource, and timestamp
- [ ] Actions performed by automated processes or agents are clearly differentiated from human actions
- [ ] The audit viewer allows filtering by actor, action, resource, and date, and respects role- and department-based access restrictions
- [ ] The tamper-evidence mechanism (e.g., hash chaining) works: manually altering an entry detectably breaks the chain

---

## 📦 How to Submit

Open a Pull Request from your `feature/audit-log` branch to `main` on your fork. In the PR description, include the audit entry schema you designed, the list of instrumented actions, and evidence that a manual alteration of an entry is detectable. Request sign-off from your CTO before merging.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
