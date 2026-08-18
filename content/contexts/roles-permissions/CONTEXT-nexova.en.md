# CONTEXT — Roles and Permissions · Nexova

_Estas instrucciones también están disponibles en [español](./CONTEXT-nexova.es.md)._

> **Project:** Platform – Roles and Permissions  
> **Repository path:** `content/contexts/roles-permissions/CONTEXT-nexova.en.md`

---

## Your company

You are part of Nexova's AI Engineering team. Nexova is an HR consulting and talent firm (~120 people) in Valencia and Miami. CTO **Sergio Molina** opened this ticket after Legal flagged that every authenticated user currently has the same access — a recruiter must not see another practice's pipeline notes.

Use this file as the source of truth for **role names**, **departments**, **capability rules**, and **seed users**. A generic RBAC that ignores these values will not be accepted.

---

## Roles (capability axis)

Roles answer _"what can this person do?"_ — not which data they see. Persist them as their own entity. Do **not** collapse this into `is_admin`.

| `code`       | Display name | Rank | Capabilities                                                                                                                                                                                                                   |
| ------------ | ------------ | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `employee`   | Employee     | 1    | Create and read records in **own department**. Cannot approve, delete, or manage users/roles/departments.                                                                                                                      |
| `supervisor` | Supervisor   | 2    | Everything an Employee can do, plus update/approve records in **own department**. Cannot delete, cannot manage users/roles/departments, cannot see other departments.                                                          |
| `admin`      | Admin        | 3    | Everything a Supervisor can do, plus delete records, manage users, and administer roles and departments. **Cross-department visibility is an Admin capability** — it does not mean the Admin lost their department assignment. |

Rank is strictly hierarchical: `employee` < `supervisor` < `admin`. Changing a user's department must not change this rank.

---

## Departments (data-scope axis)

Departments answer _"what information concerns this person?"_ They grant **no** extra actions. Persist them as their own entity, independent from role.

| `code`               | Display name                   | Director / owner | Data that belongs to this department                                    |
| -------------------- | ------------------------------ | ---------------- | ----------------------------------------------------------------------- |
| `talent_selection`   | Talent Selection Operations    | Javier Almeida   | Search process notes, screening reports                                 |
| `corporate_training` | Corporate Training             | Elena Vargas     | Catalogue/enrolment notes, delivery reports                             |
| `customer_support`   | Customer Support Outsourcing   | Roberto Díaz     | SLA/incident notes, agent-ops reports                                   |
| `sales`              | Sales and Business Development | Megan Clarke     | Pipeline notes, proposal reports                                        |
| `marketing`          | Marketing and Communications   | Carmen Ruiz      | Campaign notes, content reports                                         |
| `human_resources`    | Human Resources (Internal)     | Patricia Solís   | Internal HR notes, onboarding reports                                   |
| `technology`         | Technology and Infrastructure  | Sergio Molina    | Platform config notes (still department-scoped for Employee/Supervisor) |

A Talent Selection Supervisor and a Sales Supervisor have **identical Supervisor capabilities**. They must not see each other's departmental records.

---

## Independence rule

- `User.role_id` and `User.department_id` are separate foreign keys (or equivalent). Neither is derived from the other.
- `PATCH` (or equivalent) that changes only the role must leave the department untouched.
- `PATCH` that changes only the department must leave the role untouched.
- Admin users still **belong** to a department (`technology` in the seed). Cross-department read/write is a **role** privilege, not a missing department.

---

## Resource access matrix

Apply **role first**, then **department**. Insufficient role → **403** with an explicit body. Never return `200` with empty/silenced data to hide a missing capability.

Direct `GET` of another department's record by id → **403** (Employee/Supervisor). List endpoints for department-scoped collections may return only the caller's department — that is scoping, not a silent denial.

| Resource                                                   | Minimum role                                                                                    | Department-scoped?                    | Notes                                                              |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------ |
| `GET /auth/me`                                             | authenticated                                                                                   | no                                    | Returns role **and** department                                    |
| `GET/POST /users` (create/list)                            | `admin`                                                                                         | no                                    | User administration                                                |
| `PATCH /users/{id}/assignment`                             | `admin`                                                                                         | no                                    | Change `role_id` and/or `department_id` independently              |
| `GET/POST /roles`, `GET/PUT /roles/{id}`                   | `admin`                                                                                         | no                                    | Role administration                                                |
| `GET/POST /departments`, `GET/PUT /departments/{id}`       | `admin`                                                                                         | no                                    | Department administration                                          |
| Existing write endpoints that mutate business data         | `supervisor` (update/approve), `admin` (delete)                                                 | yes, when the record has a department | Map your current inventory/supplier/incident routes onto this rule |
| `GET/POST /internal-reports` (canonical scoped collection) | `employee` (read/create own dept), `supervisor` (update own dept), `admin` (all depts + delete) | **yes**                               | Required even if other modules are incomplete                      |

### Canonical department-scoped collection: `internal-reports`

If your monorepo does not yet have a clean department-scoped entity, implement this one. If you already have incidents/inventory/suppliers, **also** tag those records with `department_id` and enforce the same rule.

| Field           | Type            | Rules       |
| --------------- | --------------- | ----------- |
| `id`            | string/uuid     | primary key |
| `department_id` | FK → Department | required    |
| `title`         | string          | required    |
| `body`          | string          | required    |
| `created_by`    | FK → User       | required    |
| `created_at`    | datetime        | system      |

---

## Seed data

Seed **exactly** these roles, departments, and users (plus any extra you need for local demo). Passwords may be a shared dev hash; emails must match.

### Roles

```python
ROLES_SEED = [
    {"code": "employee", "name": "Employee", "rank": 1},
    {"code": "supervisor", "name": "Supervisor", "rank": 2},
    {"code": "admin", "name": "Admin", "rank": 3},
]
```

### Departments

```python
DEPARTMENTS_SEED = [
    {"code": "talent_selection", "name": "Talent Selection Operations"},
    {"code": "corporate_training", "name": "Corporate Training"},
    {"code": "customer_support", "name": "Customer Support Outsourcing"},
    {"code": "sales", "name": "Sales and Business Development"},
    {"code": "marketing", "name": "Marketing and Communications"},
    {"code": "human_resources", "name": "Human Resources (Internal)"},
    {"code": "technology", "name": "Technology and Infrastructure"},
]
```

### Users (role and department set independently)

```python
USERS_SEED = [
    {
        "email": "javier.talent@nexova.example",
        "role": "supervisor",
        "department": "talent_selection",
        "name": "Javier Almeida",
    },
    {
        "email": "megan.sales@nexova.example",
        "role": "supervisor",
        "department": "sales",
        "name": "Megan Clarke",
    },
    {
        "email": "elena.training@nexova.example",
        "role": "employee",
        "department": "corporate_training",
        "name": "Elena Vargas",
    },
    {
        "email": "patricia.hr@nexova.example",
        "role": "employee",
        "department": "human_resources",
        "name": "Patricia Solís",
    },
    {
        "email": "sergio.admin@nexova.example",
        "role": "admin",
        "department": "technology",
        "name": "Sergio Molina",
    },
]
```

Javier and Megan are the **same-role / different-department** pair used in evaluation.

### Internal reports (minimum)

Seed at least one report in `talent_selection` and one in `sales` so the pair above can be tested.

```python
INTERNAL_REPORTS_SEED = [
    {
        "department": "talent_selection",
        "title": "Search #441 — screening bottleneck",
        "body": "48 CVs pending consultant review. No candidate PII in this note.",
    },
    {
        "department": "sales",
        "title": "HubSpot hygiene — stale opportunities",
        "body": "12 opportunities with no activity in 14 days. Follow-up sequence proposed.",
    },
]
```

---

## Frontend / backoffice

- Hide or disable create/approve/delete actions the current role cannot perform.
- Lists of departmental data show **only** the authenticated user's department (Admin sees all).
- Admin-only view: list/create/edit **roles** and **departments**, and assign them to users **independently**. Employee and Supervisor who open that route (or call the API) get **403**.

---

## Tests Legal will ask for

1. Employee calling a Supervisor-only update → **403**.
2. Supervisor calling Admin-only `GET /roles` or user assignment → **403**.
3. Javier (`supervisor` + `talent_selection`) `GET` Megan's sales report by id → **403**.
4. Changing Megan's department to `marketing` does **not** change her role; changing Javier's role to `employee` does **not** change his department.
5. Permission checks live in one dependency/middleware — not copied into every route body.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
