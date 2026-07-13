# Company's Telemetry – Technical Report

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: You need the `telemetry_events` table in Supabase with at least 20 rows of real events generated from the backoffice, including at least one technical event (error, failed login, etc.) in addition to business ones. Without real data there is nothing to analyse.

This project produces a **technical report**, not a business report. Business-decision metrics (sales, conversion, revenue) are built later, in the Data Pipelines milestone, with tools dedicated to that kind of analysis.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

The data is there. The `telemetry_events` table has real events with `timestamp`, `event_type`, and `tags`. But raw data is not the answer — it is the raw material. Today you transform it, but not into a business report: into a **technical report**. An operational radar for the engineering team itself — how healthy the system is, how fast it responds, where things fail, which events occur most frequently and why.

The deliverable is a Python analysis pipeline and an endpoint that serves the result: operational metrics calculated from the stored events, served as JSON, ready to be consumed by any technical dashboard or internal monitoring tool.

> Your tech lead sent you this message:
>
> > "We have data. Now I need technical visibility into the system.
> >
> > Write the analysis pipeline. For each relevant operational dimension, one Python function that loads the relevant events, transforms them with Pandas, and returns a serialisable result. Then a `GET /telemetry/report` endpoint that serves them together.
> >
> > Two non-negotiable rules: first, don't calculate anything inside the endpoint on every request — the pipeline goes separately and the endpoint calls it, with cache. Second, convert timestamps to `datetime` before any grouping — if you don't, you'll get incorrect groups with no visible error, and you'll spend hours finding the bug.
> >
> > One important clarification: this is **not** the report for the CEO. No conversion rates, no revenue — we're going to build that with the data pipelines later. Today I want to know how healthy the system is: event volume, error rate, latency, which event types dominate. Metrics with a real temporal dimension, not a global number with no context."

---

### 📚 Complementary Knowledge — The Formula for Any Report

The data stored in `telemetry_events` answers the question "what happened?". Operational questions are different: "how many error events happened per day this week?" or "what event type is most frequent?". Answering them requires transformation — always in the same order:

```
load (SQL) → refine (Pandas) → convert types → group → aggregate → serve
```

### Where each filter belongs

| Criterion                                          | Layer                | How                                                                                                                                                 |
| --------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `timestamp` range (`start_date` / `end_date`)      | **SQL**              | `WHERE timestamp >= :start AND timestamp < :end` — bounds are **inclusive start, exclusive end** in UTC                                             |
| `event_type` (one or many)                         | **SQL**              | `WHERE event_type = '...'` or `WHERE event_type IN (...)` — ratio metrics need every relevant type loaded in one query                             |
| `tags` dimensions (warehouse, endpoint, etc.)      | **Pandas**           | Extract from `tags`, drop rows where the dimension is null, then `groupby` — segment **all** values, do not pre-filter to a single value           |
| Derived flags (`is_error`, rates)                  | **Pandas**           | Build columns after load, then `.agg()`                                                                                                            |
| Optional `tags` predicates (e.g. `endpoint = X`)   | **Pandas** (default) | Filter the DataFrame after extracting the field; SQL `tags->>'...'` push-down is optional optimisation, not required                                |

**Load (SQL)** — fetch only rows the metric needs. Never load the entire `telemetry_events` table into memory.

**Refine (Pandas)** — after load: extract `tags` fields, drop rows with null dimensions, apply any extra row-level filters the metric requires. This is **not** a substitute for SQL `event_type` / `timestamp` filtering.

**Date window ownership** — the endpoint computes the default period (last 7 days when query params are omitted) and passes `start_date` / `end_date` into every metric function. Metric functions apply that window **once in SQL**; do not re-apply a separate "last 7 days" filter in Pandas.

**Convert types** — timestamps arrive as strings. Doing `groupby()` on strings that look like dates produces incorrect groups without raising any error. Always convert before grouping:

```python
df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
df['date'] = df['timestamp'].dt.date
```

**Group** with `groupby()` by the dimension that answers the question: by day, by `event_type`, by the value of a property inside `tags`.

**Aggregate** with `.count()`, `.sum()`, or `.mean()`. The mental formula is always:

```
METRIC = AGGREGATION(column) grouped by DIMENSION
```

**Serve** the result as a list of dicts with `.reset_index().to_dict(orient='records')` — directly serialisable to JSON.

**What not to do:** calculate the report inside the endpoint on every request. If the data does not change every second, the calculation goes in a separate function called once, with the result cached.

---

## 🌱 How to Start the Project

1. Open your fork of the monorepo and locate `services/` (FastAPI backend).
2. Check `telemetry_events` in Supabase and confirm you have at least 20 rows with a variety of `event_type` values — if not, generate activity in the backoffice first (including at least one technical event).
3. Review your event catalogue (`telemetry-plan.md`) — today you work with the **technical/operational** dimensions of that catalogue, not the business ones.
4. Follow the order: analysis functions → report endpoint → cache.

---

## 💻 What You Need to Do

### Phase 1 — Analysis Pipeline with Pandas

- [ ] Create `services/telemetry/analysis.py` with at least **3 metric functions**, each encapsulating the calculation of a distinct operational dimension from your own event catalogue. Valid examples (adapt to what you actually captured):
  - Event volume by type and by day — which events occur, and how often?
  - Error rate — events with `level='error'` (or a failure `event_type`) over the total, grouped by day or by event type
  - Latency or response time, if your plan captured a performance metric — average or percentile per day

  Each function must:
  - Receive `start_date` and `end_date` parameters (computed by the endpoint — inclusive start, exclusive end, UTC)
  - Load from Supabase only the events relevant to that metric: filter `event_type` (single value or `IN (...)` for ratio metrics) and the `timestamp` range **in the SQL query**, not in Python
  - Refine in Pandas after load: extract `tags` dimensions, drop null dimension rows, apply any metric-specific row filters
  - Convert `timestamp` to `datetime` with `pd.to_datetime(..., utc=True)` before any grouping operation
  - Group with `groupby()` by the appropriate temporal or operational dimension and aggregate with `.count()`, `.sum()`, or `.mean()`
  - Return the result as a list of dicts serialisable to JSON with `.reset_index().to_dict(orient='records')`
- [ ] Each function must be **independent and side-effect free** — calling it twice with the same parameters must produce the same result.
- [ ] Do not use loops to calculate metrics — only Pandas operations (`.groupby()`, `.agg()`, `.count()`, `.sum()`, `.mean()`).

⚠️ **IMPORTANT:** The metrics you choose must answer **technical or operational** questions about the system's behaviour — volume, errors, latency, availability — not business questions (sales, conversion, revenue). A business report disguised as a technical report will not be accepted; that analysis belongs to the Data Pipelines milestone.

### Phase 2 — Report Endpoint

- [ ] Create the `GET /telemetry/report` endpoint in FastAPI. It must:
  - Accept optional query parameters `start_date` and `end_date` in ISO 8601 format; if not provided, default to the last 7 days (`start_date = now − 7d`, `end_date = now`, both UTC)
  - Resolve the period once and pass `start_date` / `end_date` to every metric function — functions do not apply their own default window
  - Call the metric functions from the analysis pipeline with those parameters
  - Return a JSON with the structure:
    ```json
    {
      "period": { "from": "...", "to": "..." },
      "metrics": {
        "events_per_day": [...],
        "error_rate_by_type": [...]
      }
    }
    ```
- [ ] The endpoint **must not run the pipeline on every request** — implement a simple in-memory cache with a 60-second TTL. If the same `start_date`/`end_date` combination is requested within the TTL, return the cached result without recalculating.

### 🔵 Additional Activity — Authentication Metric

- [ ] If you instrumented the authentication flow in the previous project, add a third metric function that calculates the **daily login failure rate**: `user_login_failed` divided by total login attempts (`user_login_failed` + `user_login_succeeded`) per day. Load both event types with `event_type IN (...)` in SQL, then compute the ratio in Pandas. Include it in the endpoint under the key `auth_failure_rate`.

### 🔵 Additional Activity — Simple Visual Dashboard

- [ ] Build a minimal page in `uis/backoffice/` (e.g. `/telemetry`) that fetches `GET /telemetry/report` and renders it visually — a chart or table per metric is enough (bar/line chart for `events_per_day`, `error_rate_by_type`, etc.). Use any charting library already available in the frontend, or a simple HTML table if you'd rather keep it minimal.
- [ ] The page should let you pick or display the current `period` (`from`/`to`) being shown, so it's clear what window the numbers cover.
- [ ] This dashboard is a **technical** view for the engineering team, not a business dashboard — keep it visualizing the same operational metrics from your report, nothing more.
- [ ] No need for polish here: a working, readable visualization of real data is the goal, not a design exercise.

---

## ✅ What We Will Evaluate

- [ ] The file `services/telemetry/analysis.py` exists and contains at least three independent metric functions
- [ ] Each function follows the formula `load (SQL) → refine (Pandas) → convert types → group → aggregate` in that order
- [ ] Timestamps are converted to `datetime` with `utc=True` before any temporal `groupby()`
- [ ] No loops are used to calculate metrics — only Pandas operations
- [ ] Each function returns a list of dicts serialisable to JSON
- [ ] The `GET /telemetry/report` endpoint accepts optional `start_date` and `end_date` and defaults to 7 days
- [ ] The endpoint returns JSON with the structure `{ "period": {...}, "metrics": {...} }`
- [ ] The endpoint has an in-memory cache with a 60-second TTL — it does not recalculate on every request
- [ ] Each metric answers a **technical/operational** question about the system's behaviour — not a business question
- [ ] The returned metrics have a grouping dimension — they are not global numbers without context

---

## 📦 How to Submit

1. Make sure the changes are in your fork: `analysis.py` in `services/telemetry/` and the `GET /telemetry/report` endpoint in `services/`.
2. Create a Pull Request against the main branch of the monorepo with the title: `[W17D49] Telemetry Report`.
3. In the PR description, include:
   - The name of the metrics implemented and what operational question each one answers
   - A sample of the JSON returned by `GET /telemetry/report` with real data
   - Whether you implemented the additional authentication metric and/or the simple visual dashboard

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
