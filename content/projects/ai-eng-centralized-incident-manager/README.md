# Centralized Incident Manager

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start:** Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/centralized-incident-manager)** before writing any code — it defines the field names, valid categories, branch locations, and expected seed values your implementation must use.

---

## 🎯 Your challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

The CSV file analyser you built in the previous project proved that the validation and metrics logic works. But the support team no longer wants to export files for analysis: they want to log incidents directly from the browser, in real time, from anywhere in the company.

Your tech lead has decided to take the next step: integrate a centralised incident manager into the platform that has been under construction since Milestone 5. Anyone in the company — whether at an operational branch, at headquarters, or managing a customer-reported issue — will be able to log it through a form, query it, and track it from the same panel.

> **Note from your tech lead:** _"We have the historical data in the CSV from the previous project. We're going to load it as seed incidents of customer origin so we have real data from day one. After that, the form is the only entry point — no more manual files. And this has to work correctly even if the API is slow, even if the server returns a 500, even if the user leaves a field blank. I want to see error messages that users understand, not stack traces."_

### What makes an incident manager professional-grade?

An incident manager is not just a form connected to a database. In a real environment, each incident has a **lifecycle** (open → in progress → resolved → discarded) and an **origin** that defines its context: a customer complaint is not the same as an internal failure detected by a branch. The system must record who reported what, from where, when, and what state it is in — and must be able to aggregate that into useful metrics for leadership.

### Complementary knowledge: improving an incident manager with embeddings

An application like this one — structured forms, filters, and aggregated metrics — works well with exact field values. **Embeddings** add a semantic layer on top: they turn each incident's `title` and `description` into a dense vector that captures meaning, not just keywords.

With that representation stored in a vector database (or an extension that supports similarity search), you can evolve the same system in several directions without changing the core CRUD model:

- **Find similar incidents** — when someone registers a new report, surface past cases with comparable descriptions so support can reuse resolutions or spot recurring issues.
- **Smarter search** — queries like "payment failed at checkout" can match incidents phrased differently ("card declined during purchase"), which keyword filters alone often miss.
- **Duplicate and cluster detection** — group spikes of related reports across branches or origins before they flood the summary dashboard.
- **Assisted triage** — suggest category or priority from the text of the description by comparing it to embeddings of historical incidents already labeled by your team.

You do not need to implement any of this in the current delivery. The point is to see how the incident manager you are building today is a solid foundation: once descriptions live in the database, embeddings are a natural next step when the product needs search and intelligence beyond exact filters.

---

## 🌱 How to Start the Project

1. Work in [**ai-engineering-company-project-monorepo**](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo). If you haven't set it up yet, fork it and open it in **GitHub Codespaces** or clone it locally.
2. Read your **CONTEXT-company.md** before writing a single line of code. It defines the incident data structure, your company's branches, valid categories, and expected seed values.
3. This project extends the work from Milestone 5: reuse the existing database, API structure, and frontend architecture.

---

## 💻 What You Need to Do

### Data Model

- [ ] Define the `Incident` model with the following fields:
  - `id` — unique identifier, generated automatically.
  - `title` — brief incident title (required).
  - `description` — detailed description (required).
  - `category` — category as defined in your CONTEXT.
  - `status` — lifecycle state: `open`, `in_progress`, `resolved`, `discarded`.
  - `origin` — source of the report: `customer`, `branch`, `internal`.
  - `branch` — branch that manages or reports the incident (required for all origins; use `central` when not specific to any branch).
  - `created_at` — creation timestamp, generated automatically.
  - `updated_at` — last modification timestamp, updated automatically.
- [ ] Apply the necessary integrity constraints: required fields, allowed values for `status`, `origin`, and `category`.

### Historical Data Seed (`/scripts`)

- [ ] Create the `seed_incidents.py` script that reads the CSV file from the previous project and loads all its rows into the database, assigning `origin: "customer"` to every record.
- [ ] The script must apply the **CSV → model transformations** specified in your CONTEXT (status map, category map, `description` → `title`, `date` → `created_at`, location → `branch`) before insert — the analyzer CSV schema is not identical to this manager's model.
- [ ] The script must reuse the existing validation logic — extract the shared functions to `packages/shared/` if you haven't already: invalid CSV records are not inserted and are reported to the console at the end of execution.
- [ ] The script is idempotent: running it twice does not duplicate records (check against an identifying field from the CSV before inserting).

### Backend (`/services`)

**Management endpoints:**

- [ ] `POST /api/incidents` — creates a new incident. Validates all required fields and returns `400` with a descriptive message if any are missing or contain an invalid value.
- [ ] `GET /api/incidents` — returns the list of incidents. Accepts optional filter parameters: `status`, `origin`, `branch`, `category`.
- [ ] `GET /api/incidents/{id}` — returns the detail of a single incident. Returns `404` if it does not exist.
- [ ] `PATCH /api/incidents/{id}/status` — updates only the status of an incident. Validates that the transition is consistent with the lifecycle: from `open` you can advance to `in_progress` or `discarded`; from `in_progress` you can advance to `resolved` or `discarded`; `resolved` and `discarded` are final states.
- [ ] `GET /api/incidents/summary` — returns aggregated metrics: total by status, total by category, total by origin, and total by branch.

**Error handling in the backend:**

- [ ] Every unhandled exception returns `500` with a generic message — never the full stack trace.
- [ ] Validation errors return `400` with a JSON object that identifies the problematic field and describes the error in plain language.
- [ ] Read endpoints do not fail on an empty database: they return an empty list or zero metrics.

### Frontend (`/uis`)

**Registration form:**

- [ ] Create an incident registration page accessible from the application menu.
- [ ] The form includes all model fields. The `branch` field is always visible and required, with every branch option from your CONTEXT (including `central`, displayed as the label your CONTEXT specifies).
- [ ] When `origin` is `branch`, the `branch` field is visually highlighted to remind the user they are reporting from a specific location.
- [ ] On submit, the form shows a loading indicator while the request is in progress — the submit button is disabled during that time.
- [ ] If the API returns an error, the form shows a user-friendly message — never the raw server error text. If the error identifies a specific field, the message appears next to that field.
- [ ] After a successful submission, the form clears and displays a clear confirmation.

**Incident list panel:**

- [ ] Create a listing page showing all registered incidents, with filters by `status`, `origin`, and `branch`.
- [ ] Show a loading indicator while data is being fetched.
- [ ] If the request fails, show an error message with a retry option — the page does not go blank or break.
- [ ] If there are no incidents to show (empty list or no results for the applied filters), display an informative message — never an empty table without context.
- [ ] Each incident allows updating its status directly from the list. If the update fails, the visual state reverts to the previous value and the user is notified.

**Summary panel:**

- [ ] Display the aggregated metrics from the `/summary` endpoint: totals by status, category, origin, and branch.
- [ ] If data takes time to load or the request fails, the panel shows the corresponding state without breaking the rest of the page.

⚠️ **IMPORTANT:** Field names, categories, branch locations, and values in your implementation must match exactly what is specified in your CONTEXT.md. A generic implementation that ignores your company's context will not be accepted.

---

## ✅ What We Will Evaluate

### Model and seed

- [ ] The model includes all required fields with their integrity constraints.
- [ ] The seed script correctly loads historical incidents assigning `origin: "customer"`.
- [ ] The seed script applies the CSV → model transformations defined in your CONTEXT (status, category, title, dates, and branch mapping) before insert.
- [ ] Invalid CSV records are not inserted and are reported to the console.
- [ ] The script is idempotent: running it twice does not duplicate data.
- [ ] After seeding, `/api/incidents/summary` totals by **model** `status` and `category` match the transformed expected values in your CONTEXT (same valid-record set as the incidents-file-analyzer project).

### Backend

- [ ] All endpoints respond with the correct HTTP codes for both happy path and error cases.
- [ ] Validation errors identify the problematic field in the JSON response.
- [ ] No endpoint exposes a stack trace to the client.
- [ ] Invalid status transitions are rejected with `400`.
- [ ] The `/summary` endpoint returns correct metrics even when there are no incidents.

### Frontend

- [ ] The form validates required fields on the client before submitting.
- [ ] Loading states are visible and the submit button is disabled during the request.
- [ ] API errors are shown in plain language to the user, never as technical text.
- [ ] The list correctly handles all three possible states: loading, empty, with data.
- [ ] Status updates in the list revert visually if the request fails.
- [ ] The summary panel does not break the page if its request fails.

### Cross-cutting

- [ ] The validation logic from the previous project is extracted into `packages/shared/` and reused by both the script and the API, without duplication.
- [ ] Code is organised according to the monorepo folder structure (`scripts/`, `services/`, `uis/`, `packages/shared/`).

---

## 📦 How to Submit This Project

The project must be organised in the monorepo as follows:

```text
scripts/
  seed_incidents.py             ← historical CSV load script

packages/
  shared/                       ← validation logic shared between script and API

services/
  <api-service-name>/           ← backend with management and summary endpoints

uis/
  <ui-name>/                    ← registration, list, and summary interface
```

1. Push your branch with the structure above and open a Pull Request to the original repository.
2. Make sure the PR includes:
   - A screenshot of the form with a visible validation error.
   - A screenshot of the incident list panel with data loaded.
   - A screenshot of the summary panel with metrics.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
