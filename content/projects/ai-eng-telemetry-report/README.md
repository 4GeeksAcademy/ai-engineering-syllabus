# Company's Telemetry – Report

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: You need the `telemetry_events` table in Supabase with at least 20 rows of real events generated from the backoffice. Without real data there is nothing to analyse — generate activity in the inventory module before continuing.

Re-read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/telemetry-report)** alongside `docs/telemetry/telemetry-plan.md` — each metric must answer one of the three KPIs defined there for your assigned company, not a generic inventory dashboard.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

The data is there. The `telemetry_events` table has real events with `timestamp`, `event_type`, and `tags`. But raw data is not the answer — it is the raw material. Today you transform it.

The deliverable is a Python analysis pipeline and an endpoint that serves the result: the metrics for the KPIs you defined in Phase 1, calculated from the stored events, served as JSON, and ready to be consumed by any dashboard or reporting tool.

> Your tech lead sent you this message:
>
> > "We have data. Now I need answers.
> >
> > Write the analysis pipeline. For each KPI in the plan, one Python function that loads the relevant events, transforms them with Pandas, and returns a serialisable result. Then a `GET /telemetry/report` endpoint that serves them together.
> >
> > Two non-negotiable rules: first, don't calculate anything inside the endpoint on every request — the pipeline goes separately and the endpoint calls it, with cache. Second, convert timestamps to `datetime` before any grouping — if you don't, you'll get incorrect groups with no visible error, and you'll spend hours finding the bug.
> >
> > I want real metrics with a temporal dimension. A global number with no grouping context is not a metric — it's a count."

---

### 📚 Complementary Knowledge — The Formula for Any Report

The data stored in `telemetry_events` answers the question "what happened?". Business questions are different: "how many orders failed per day this week?" or "what event type is most frequent?". Answering them requires transformation — always in the same order:

```
load (SQL) → refine (Pandas) → convert types → group → aggregate → serve
```

### Where each filter belongs

| Criterion                                          | Layer                | How                                                                                                                                                 |
| -------------------------------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `timestamp` range (`start_date` / `end_date`)      | **SQL**              | `WHERE timestamp >= :start AND timestamp < :end` — bounds are **inclusive start, exclusive end** in UTC                                             |
| `event_type` (one or many)                         | **SQL**              | `WHERE event_type = '...'` or `WHERE event_type IN (...)` — ratio metrics need every type in the denominator loaded in one query                    |
| `tags` dimensions (`warehouse`, `office`, etc.)    | **Pandas**           | Extract from `tags`, drop rows where the dimension is null, then `groupby` — segment **all** values, do not pre-filter to a single warehouse/clinic |
| Derived flags (`is_failure`, rates)                | **Pandas**           | Build columns after load, then `.agg()`                                                                                                             |
| Optional `tags` predicates (e.g. `reason = waste`) | **Pandas** (default) | Filter the DataFrame after extracting the field; SQL `tags->>'...'` push-down is optional optimisation, not required                                |

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

`df.groupby('date')['id'].count()` — events per day. Without a grouping dimension you only have a global number; with one you have actionable context.

**Serve** the result as a list of dicts with `.reset_index().to_dict(orient='records')` — directly serialisable to JSON.

**What not to do:** calculate the report inside the endpoint on every request. If the data does not change every second, the calculation goes in a separate function called once, with the result cached.

---

## 🌱 How to Start the Project

1. Open your fork of the monorepo and locate `services/` (FastAPI backend).
2. Check `telemetry_events` in Supabase and confirm you have at least 20 rows with a variety of `event_type` values — if not, generate activity in the backoffice first.
3. Review your `CONTEXT-company.md` and `docs/telemetry/telemetry-plan.md` — the KPIs from your company context are exactly the metrics you will calculate today.
4. Follow the order: analysis functions → report endpoint → cache.

---

## 💻 What You Need to Do

### Phase 1 — Analysis Pipeline with Pandas

- [ ] Create `services/telemetry/analysis.py` with at least **two metric functions**, each encapsulating the calculation of one KPI from your plan. Each function must:
  - Receive `start_date` and `end_date` parameters (computed by the endpoint — inclusive start, exclusive end, UTC)
  - Load from Supabase only the events relevant to that metric: filter `event_type` (single value or `IN (...)` for ratio metrics) and `timestamp` range **in the SQL query**, not in Python
  - Refine in Pandas after load: extract `tags` dimensions, drop null dimension rows, apply any metric-specific row filters
  - Load the result into a Pandas DataFrame
  - Convert `timestamp` to `datetime` with `pd.to_datetime(..., utc=True)` before any grouping operation
  - Group with `groupby()` by the appropriate temporal dimension and aggregate with `.count()`, `.sum()`, or `.mean()`
  - Return the result as a list of dicts serialisable to JSON with `.reset_index().to_dict(orient='records')`
- [ ] Each function must be **independent and side-effect free** — calling it twice with the same parameters must produce the same result.
- [ ] Do not use loops to calculate metrics — only Pandas operations (`.groupby()`, `.agg()`, `.count()`, `.sum()`, `.mean()`).

⚠️ **IMPORTANT:** Metric names and business questions must map to KPIs grounded in `CONTEXT-company.md` via your Phase 1 plan. A generic "events per day" count without your company's grouping dimensions will not be accepted.

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
        "metric_name_1": [...],
        "metric_name_2": [...]
      }
    }
    ```
- [ ] The endpoint **must not run the pipeline on every request** — implement a simple in-memory cache with a 60-second TTL. If the same `start_date`/`end_date` combination is requested within the TTL, return the cached result without recalculating.

### 🔵 Additional Activity — Authentication Metric

- [ ] If you instrumented the authentication flow in D47, add a third metric function that calculates the **daily login failure rate**: `user_login_failed` divided by total login attempts (`user_login_failed` + `user_login_succeeded`) per day. Load both event types with `event_type IN (...)` in SQL, then compute the ratio in Pandas. Include it in the endpoint under the key `auth_failure_rate`.

---

## ✅ What We Will Evaluate

- [ ] The file `services/telemetry/analysis.py` exists and contains at least two independent metric functions
- [ ] Each function follows the formula `load (SQL) → refine (Pandas) → convert types → group → aggregate` in that order
- [ ] Timestamps are converted to `datetime` with `utc=True` before any temporal `groupby()`
- [ ] No loops are used to calculate metrics — only Pandas operations
- [ ] Each function returns a list of dicts serialisable to JSON
- [ ] The `GET /telemetry/report` endpoint accepts optional `start_date` and `end_date` and defaults to 7 days
- [ ] The endpoint returns JSON with the structure `{ "period": {...}, "metrics": {...} }`
- [ ] The endpoint has an in-memory cache with a 60-second TTL — it does not recalculate on every request
- [ ] Each metric answers a KPI from the student's `telemetry-plan.md`, justified with data from `CONTEXT-company.md`
- [ ] The returned metrics have a grouping dimension — they are not global numbers without context

---

## 📦 How to Submit

1. Make sure the changes are in your fork: `analysis.py` in `services/telemetry/` and `GET /telemetry/report` endpoint in `services/`.
2. Create a Pull Request against the main branch of the monorepo with the title: `[W17D49] Telemetry Report`.
3. In the PR description, include:
   - The name of the two metrics implemented and the business question each one answers
   - A sample of the JSON returned by `GET /telemetry/report` with real data
   - Whether you implemented the authentication metric

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
