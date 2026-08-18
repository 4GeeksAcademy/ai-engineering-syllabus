# CONTEXT — Roles and Permissions · HealthCore

_Estas instrucciones también están disponibles en [español](./CONTEXT-healthcore.es.md)._

> **Project:** Platform – Roles and Permissions  
> **Repository path:** `content/contexts/roles-permissions/CONTEXT-healthcore.en.md`

---

## Your company

You are part of **HealthCore Digital**. HealthCore is an outpatient clinic network with **12 clinics** in the US and UK (~200 people). CTO **James Osei** opened this ticket after **Claire Whitfield** (Compliance) flagged that every authenticated user currently has the same access — unacceptable under HIPAA / UK GDPR.

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

| `code`                | Display name                   | Director / owner | Data that belongs to this department                                                    |
| --------------------- | ------------------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `clinical_operations` | Clinical Operations            | Dr. Marcus Reid  | Clinic operational notes, documentation-time notes, cross-location clinical ops reports |
| `patient_experience`  | Patient Experience and Access  | Priya Nair       | Booking/no-show notes, reminder-campaign notes, access reports                          |
| `revenue_cycle`       | Revenue Cycle and Billing      | Tom Callahan     | Claims/denial notes, collection reports, billing operational notes                      |
| `compliance`          | Compliance and Data Governance | Claire Whitfield | HIPAA/GDPR audit notes, access-review reports                                           |
| `people_workforce`    | People and Workforce           | Diane Foster     | Hiring/onboarding notes, CME-tracking notes                                             |
| `technology`          | Technology                     | James Osei       | Platform config notes (still department-scoped for Employee/Supervisor)                 |

A Clinical Operations Supervisor and a Revenue Cycle Supervisor have **identical Supervisor capabilities**. They must not see each other's departmental records.

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

Do **not** put clinical PHI in seed reports. Operational notes only.

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
    {"code": "clinical_operations", "name": "Clinical Operations"},
    {"code": "patient_experience", "name": "Patient Experience and Access"},
    {"code": "revenue_cycle", "name": "Revenue Cycle and Billing"},
    {"code": "compliance", "name": "Compliance and Data Governance"},
    {"code": "people_workforce", "name": "People and Workforce"},
    {"code": "technology", "name": "Technology"},
]
```

### Users (role and department set independently)

```python
USERS_SEED = [
    {
        "email": "marcus.clinical@healthcore.example",
        "role": "supervisor",
        "department": "clinical_operations",
        "name": "Dr. Marcus Reid",
    },
    {
        "email": "tom.billing@healthcore.example",
        "role": "supervisor",
        "department": "revenue_cycle",
        "name": "Tom Callahan",
    },
    {
        "email": "priya.access@healthcore.example",
        "role": "employee",
        "department": "patient_experience",
        "name": "Priya Nair",
    },
    {
        "email": "claire.compliance@healthcore.example",
        "role": "employee",
        "department": "compliance",
        "name": "Claire Whitfield",
    },
    {
        "email": "james.admin@healthcore.example",
        "role": "admin",
        "department": "technology",
        "name": "James Osei",
    },
]
```

Marcus and Tom are the **same-role / different-department** pair used in evaluation.

### Internal reports (minimum)

Seed at least one report in `clinical_operations` and one in `revenue_cycle` so the pair above can be tested.

```python
INTERNAL_REPORTS_SEED = [
    {
        "department": "clinical_operations",
        "title": "Austin North — documentation time spike",
        "body": "Average documentation minutes per encounter up 12% week over week. No patient identifiers.",
    },
    {
        "department": "revenue_cycle",
        "title": "US denial rate — coding mismatch cluster",
        "body": "14% denial rate driven by three CPT mismatch patterns. No member IDs in this note.",
    },
]
```

---

## Frontend / backoffice

- Hide or disable create/approve/delete actions the current role cannot perform.
- Lists of departmental data show **only** the authenticated user's department (Admin sees all).
- Admin-only view: list/create/edit **roles** and **departments**, and assign them to users **independently**. Employee and Supervisor who open that route (or call the API) get **403**.

---

## Tests Compliance will ask for

1. Employee calling a Supervisor-only update → **403**.
2. Supervisor calling Admin-only `GET /roles` or user assignment → **403**.
3. Marcus (`supervisor` + `clinical_operations`) `GET` Tom's revenue-cycle report by id → **403**.
4. Changing Tom's department to `compliance` does **not** change his role; changing Marcus's role to `employee` does **not** change his department.
5. Permission checks live in one dependency/middleware — not copied into every route body.

---

_Internal document — 4Geeks Academy · AI Engineering Track_
