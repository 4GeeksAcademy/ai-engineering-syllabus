# Platform – Roles and Permissions

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: read your **[COMPANY-BRIEF.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts)** and your **[CONTEXT-roles-permissions.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/roles-permissions)** before writing any code — that's where your company's roles, departments, and concrete access rules live.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** — not on a new repository.

Your CTO opens a high-priority **ticket**: the system currently treats every authenticated user as if they had the same level of access. That worked while the team was small and everyone trusted everyone — but it's no longer sustainable, and Legal has flagged it as a risk before the company keeps growing.

The **brief** is clear on a point that's easy to blur, so read it carefully: you're being asked for **two distinct mechanisms that work together, not one**.

> _"I need two separate things, and I don't want you to collapse them into a single permissions table. First, a person's **role**: what they can do, what they can see, and what responsibility they carry inside the system — Employee, Supervisor, and Admin, at minimum. Second, the **department** they belong to: that doesn't grant or remove action permissions, but it does determine which specific information concerns them. An Operations Supervisor and a Finance Supervisor have exactly the same capabilities as Supervisors — but they shouldn't see the same data."_
>
> — CTO

Three requirements are left implicit in that brief and **you need to catch them by reading carefully**:

1. Role and department are **independent axes**. Changing someone's department must not change what their role allows them to do; changing their role must not automatically change which departmental information they see.
2. The system needs **at least three roles** with a clear, verifiable capability hierarchy — a single `is_admin` boolean isn't enough.
3. Access rules must be enforced **in the backend**, not just hidden behind buttons in the frontend. A user without permission who calls the endpoint directly must receive an explicit rejection, not a silent response with empty data.

### Complementary knowledge: role vs. department

It's easy to confuse these two concepts because both "restrict" something — but they restrict different things. **Role** answers _"what can this person do in the system?"_ — it's about capabilities and responsibility (create, approve, delete, manage users). **Department** answers _"what information concerns this person?"_ — it's about data scope (see their area's reports, not everyone's). A correct design evaluates both axes on every access decision: first whether the role allows the action, then whether the department allows visibility into that specific data.

---

## 🌱 How to Start the Project

1. `pull` the latest changes from your fork of the monorepo.
2. Read `COMPANY-BRIEF.md` and `CONTEXT-roles-permissions.md` in full before touching any code.
3. Create a new branch: `feature/roles-permissions`.
4. Map every existing endpoint in your system and classify it by the minimum role required to use it.
5. Design the data model for roles, departments, and their relationship to the user before writing your first migration.

---

## 💻 What You Need to Do

**Data model**

- [ ] Define at least three roles with an explicit, documented capability hierarchy (e.g., Employee, Supervisor, Admin)
- [ ] Define department as an entity independent from role
- [ ] Model the user–role–department relationship so a user can change department without losing their role, and vice versa

**Backend**

- [ ] Implement a centralized permission-checking mechanism (middleware or dependency), not repeated validations endpoint by endpoint
- [ ] Apply the role restriction to every endpoint according to the capability it exposes
- [ ] Apply the department restriction to every endpoint that returns department-scoped data
- [ ] Return an explicit rejection code (403) when the role isn't sufficient — never a response with empty or silenced data
- [ ] Write automated tests demonstrating that a user with the wrong role and department cannot access a restricted resource

**Frontend / backoffice**

- [ ] Hide or disable interface actions the user's role doesn't allow
- [ ] Show only the departmental data that corresponds to the authenticated user
- [ ] Implement a roles and departments administration view accessible only to the Admin role

⚠️ **IMPORTANT:** the exact role names, existing departments, and rules for which information concerns each department must match exactly what's specified in your `CONTEXT-roles-permissions.md`. A generic implementation that ignores that context will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] At least three roles exist with differentiated, test-verifiable capabilities
- [ ] Role and department behave as independent axes: changing one does not alter the other
- [ ] Every sensitive endpoint explicitly rejects (403) a user without the required role, verified with a direct API call, not just from the interface
- [ ] A user with the same role but a different department cannot access data outside their departmental scope
- [ ] Permission checking is centralized, not duplicated per endpoint
- [ ] A roles and departments administration view exists, restricted to the Admin role

---

## 📦 How to Submit

Open a Pull Request from your `feature/roles-permissions` branch to `main` on your fork. In the PR description, include the roles-and-capabilities table you defined, plus evidence (screenshot or test log) that a sensitive endpoint rejects a user without permission. Request sign-off from your CTO before merging.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
