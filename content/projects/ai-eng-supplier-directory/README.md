# Supplier Directory — Lightweight Storage API

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

<!-- endhide -->

**Before you start:** Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** before writing any code — it defines the exact supplier fields, valid categories, allowed statuses, and the initial data your seeder must load.

---

## 🎯 Your challenge

You already have FastAPI endpoints working and know how to structure an API. Your company's platform keeps growing — and with it, the need to eliminate the failure points that slow the team down. One of the most visible: critical business data still lives in spreadsheets that each person keeps on their own machine, updates independently, and shares by email. The result is always the same — out-of-sync versions, decisions made from different data, and time wasted trying to figure out which file is the right one. It is time to replace that with a database with a single source of truth, accessible to everyone through the API — no SQL yet, but with real structure from day one.

Your company's procurement team currently manages its supplier directory in a spreadsheet. Key information — what each supplier provides, which country they operate in, their current rate, and whether they are active or suspended — is updated manually, inconsistently, and with no traceability. When the price of an ingredient or component rises, the team finds out late. When a new supplier needs to be added, nobody knows where to register them officially.

Your tech lead has decided to build a supplier management API using **FastAPI + TinyDB + Pydantic**. The choice of TinyDB is deliberate: you do not always need a large-scale database to solve a problem well. A lightweight solution that demands minimal resources and can be deployed immediately can be exactly the right tool for the job. The solution must start with real data from the very first run — not an empty database — and must reject any input that does not match the defined structure.

> ### 📋 What is a seeder?
>
> A seeder is a script that loads initial data into the database before the application starts being used. It is a standard backend development practice: it allows the system to start from a known, realistic state, useful for both testing and demonstrations. In this project, the seeder will import the existing supplier directory that currently lives in a spreadsheet — exactly what happens when a company migrates from Excel to an in-house tool.

> **Note from your tech lead:**
>
> > _"I need the directory operational by Thursday. Use TinyDB — we'll migrate to Postgres once we have the ORM ready. The seeder must load all suppliers from the CONTEXT on startup; I don't want to see an empty database in the demo. Pydantic validates everything that comes in: if a supplier has no country or its status is not one of the two allowed values, the API rejects it with a 422 before it ever touches the database. Two search endpoints are non-negotiable: filter by country and filter by product category. And when a rate is updated, I want the timestamp of the change recorded — the team will need that for audits."_

---

## 🌱 How to Start the Project

1. Work in the [**ai-engineering-company-project-monorepo**](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo). If you have not set it up yet, fork it, then open your fork in **GitHub Codespaces** or clone it locally:

   ```text
   https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo
   ```

2. Read your **CONTEXT-company.md** file before writing any code. It defines the supplier model fields, valid categories, allowed statuses, and the data the seeder must load.

3. Work inside the `/services/api` (backend) and `/uis/application` (frontend) folders of the monorepo.

There is no starter code. The project starts from scratch.

---

## 💻 What You Need to Do

### Data model

- [ ] Define the Pydantic `Supplier` model with the required fields from your CONTEXT: name, country, product categories, rate, last rate update date, and status.
- [ ] The `status` field must accept only the values defined in your CONTEXT (active / suspended or their equivalents). Use an `Enum` or a field validator to reject any other value.
- [ ] The rate must be a positive number. Pydantic must reject zero or negative values before the data reaches TinyDB.
- [ ] Create separate input and response models where necessary (for example: the `updated_at` field is generated by the system, not sent by the client).

### Seeder

- [ ] Create a `seed.py` script that loads the initial suppliers defined in your CONTEXT into TinyDB.
- [ ] The seeder must be executable with `pipenv run seed` without modifying the code.
- [ ] If the database already has data, the seeder must not create duplicates — check before inserting.
- [ ] Confirm in the console how many records were inserted when it finishes.

### Endpoints

- [ ] `POST /suppliers` — Register a new supplier. Return the created supplier with its TinyDB-assigned ID. Reject invalid inputs with `422`.
- [ ] `GET /suppliers` — List all suppliers. Accept optional query parameters to filter by country and by product category. If no parameters are provided, return all.
- [ ] `GET /suppliers/{id}` — Return the detail of a supplier by ID. Return `404` if it does not exist.
- [ ] `PATCH /suppliers/{id}/rate` — Update a supplier's rate. Automatically record the `updated_at` timestamp at the time of the change. Do not accept rates equal to or less than zero.
- [ ] `PATCH /suppliers/{id}/status` — Activate or suspend a supplier. Accept only the two status values defined in the CONTEXT.
- [ ] `DELETE /suppliers/{id}` — Remove a supplier from the directory. Return `404` if the ID does not exist.

⚠️ **IMPORTANT:** Field names, valid categories, and allowed statuses in your implementation must match exactly what is specified in your CONTEXT.md. A generic implementation that ignores your company's context will not be accepted.

### Frontend (`/uis/application`)

- [ ] Create a supplier directory page accessible from the application menu.
- [ ] Display the full list of suppliers in a table or list with their main fields: name, country, categories, current rate, and status.
- [ ] Include filter controls by country and by category that update the list without reloading the page.
- [ ] Implement a form to register a new supplier that consumes the `POST /suppliers` endpoint. Display an error message if the API rejects the input.
- [ ] Allow updating a supplier's rate from the interface and reflect the change in the list immediately after the API responds.
- [ ] Allow changing a supplier's status (activate / suspend) from the interface with a visible control on each row or in the detail view.
- [ ] Visually distinguish active suppliers from suspended ones (for example, with a colour-coded badge or differentiated style).

---

## ✅ What We Will Evaluate

### Model and validation

- [ ] The Pydantic model reflects exactly the fields defined in the CONTEXT.
- [ ] `status` values outside the allowed set are rejected with `422` before reaching TinyDB.
- [ ] Rates with a zero or negative value are rejected with `422`.
- [ ] The `updated_at` field is generated by the system, not sent by the client.

### Seeder

- [ ] `pipenv run seed` runs without errors and loads the CONTEXT suppliers into the database.
- [ ] Running the seeder more than once does not produce duplicates.
- [ ] The number of records inserted is confirmed in the console when it finishes.

### Endpoints

- [ ] `POST /suppliers` creates a supplier and returns the complete object with ID.
- [ ] `GET /suppliers` with no parameters returns all suppliers.
- [ ] `GET /suppliers?country=X` returns only suppliers from the specified country.
- [ ] `GET /suppliers?category=Y` returns only suppliers that provide that category.
- [ ] `GET /suppliers/{id}` returns `404` for non-existent IDs.
- [ ] `PATCH /suppliers/{id}/rate` updates the rate and records the change timestamp.
- [ ] `PATCH /suppliers/{id}/status` rejects disallowed status values with `422`.
- [ ] `DELETE /suppliers/{id}` returns `404` for non-existent IDs.

### Frontend

- [ ] The supplier list loads from the API and displays the fields defined in the CONTEXT.
- [ ] The country and category filters work and update the list without reloading the page.
- [ ] The registration form validates required fields on the client side and displays the API error if the server rejects the input.
- [ ] Rate updates and status changes are reflected in the interface after the API responds.
- [ ] Active and suspended suppliers are visually distinguished.

### Cross-cutting

- [ ] TinyDB persists correctly: data is still there after restarting the server.
- [ ] HTTP errors are consistent: `404` when not found, `422` when input is invalid, `200`/`201` when the operation succeeds.
- [ ] Code is organised according to the monorepo folder structure (`services/` for the backend, `uis/application` for the frontend).

---

## 📦 How to Submit This Project

The project must be organised in the monorepo as follows:

```text
services/
  api/
    main.py           ← FastAPI application
    models.py         ← Pydantic models
    database.py       ← TinyDB initialisation
    routes/
      suppliers.py    ← supplier directory endpoints
    seed.py           ← initial data loading script
uis/
  application/
    app/
      suppliers/      ← supplier directory page
```

1. Push your branch with the structure above and open a Pull Request to the original repository.
2. Make sure the PR includes:
   - A screenshot of the `pipenv run seed` output in the terminal.
   - A screenshot of the response from at least one of the filter endpoints (by country or by category) in Swagger UI or an HTTP client.
   - A screenshot of the supplier list in the web interface with at least one filter applied.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
