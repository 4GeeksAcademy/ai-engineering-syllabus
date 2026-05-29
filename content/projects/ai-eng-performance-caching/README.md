# Performance Optimisation: Caching

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/caching-optimization/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

Your company's platform is growing. What once handled a handful of requests per day is now under real load — more users, more API calls, more complex UI interactions. The tech lead has flagged a recurring pattern in the telemetry: some endpoints are being hit dozens of times per minute with identical queries, and some components are re-rendering far more than they need to.

The mandate is clear: before the next feature sprint, the team must profile the existing application, identify the highest-value caching opportunities, and implement them. This is not about caching everything — it's about making deliberate, justified decisions about what to cache, where to cache it, and for how long.

You will work directly on your transversal project monorepo. The output is not just working code: it's a structured technical report that explains your reasoning. Engineering decisions without documentation are just guesses — the team needs to understand why each choice was made.

### 🧠 Complementary knowledge

**When is caching the right call?**
Not every piece of data deserves a cache. Before implementing anything, evaluate two axes:

- **Computation cost vs. storage cost**: is recalculating or re-fetching this data more expensive than storing a copy of it? If a query takes 400ms and runs 200 times a minute, caching is almost certainly justified. If it takes 2ms and the data changes every 10 seconds, it probably isn't.
- **Data freshness vs. performance**: cached data is, by definition, potentially stale. A product listing can tolerate a 60-second TTL. A bank balance cannot. Every caching decision is a tradeoff between speed and consistency — document it explicitly.

**Frontend caching scope**
On the frontend, two techniques apply directly:

- **Lazy Loading**: deferring the load of components or data until they are actually needed. This reduces the initial bundle size and time-to-interactive. Useful for heavy components that appear below the fold or only in certain flows.
- **`useMemo`**: memoizing expensive computed values inside a component so they are only recalculated when their dependencies change. Only apply it when profiling shows the computation is genuinely expensive — premature memoization adds complexity without benefit.

**Backend caching levels**
On the FastAPI backend, the most practical approach at this stage is **in-process cache** (a dictionary or simple cache decorator in memory) or an **external cache** like Redis. The key question per endpoint is: _does this response depend on data that changes frequently, and does it involve meaningful computation?_ Endpoints that aggregate across many rows, call external services, or run heavy filtering are the best candidates.

**TTL discipline**
Every cached value must have an expiry. No TTL means stale data lives forever. Choose TTLs based on how often the underlying data changes — not on convenience.

**How to spot candidates with evidence (not gut feel)**
Before you cache anything, you need data. On the backend, the fastest way to see which endpoints deserve attention is to measure every request's duration.

#### 1. Timing middleware (zero dependencies)

Add this to your `main.py`:

```python
import time
import logging
from fastapi import Request

logger = logging.getLogger("api.timing")

@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration = (time.perf_counter() - start) * 1000  # ms

    logger.info(
        f"{request.method} {request.url.path} → {response.status_code} | {duration:.1f}ms"
    )
    return response
```

You immediately get one log line per request:

```text
GET /users → 200 | 312.4ms
POST /orders → 201 | 48.2ms
GET /products → 200 | 891.7ms  ← 🐢
```

**What to look for in the logs?**

| Signal in the log                                  | Question it answers                                     | Cache candidate?                  |
| -------------------------------------------------- | ------------------------------------------------------- | --------------------------------- |
| Consistently high latency (>100–200 ms)            | How expensive is the operation? (**cost** axis)         | Yes, if it repeats                |
| Same route many times in a short window            | How often is it called? (**frequency** axis)            | Yes, if the response is identical |
| Same path + same status + similar timings on reads | How stable is the underlying data? (**stability** axis) | Yes, with an appropriate TTL      |

An endpoint that is slow **and** hit in bursts with the same parameters (e.g. `GET /products?category=electronics`) is a strong candidate. A `POST` that writes data or a `GET` whose response varies per user is not — unless you scope the cache key to that user.

**Layer on real traffic:**

1. Use your frontend or repeat the same requests (same URL, same query params).
2. Rank the logs: paths with the most lines and highest `ms` go at the top of your candidate list.
3. Cross-check with the report checklist: document in `CACHING_REPORT.md` the measured time _before_ caching and the estimated benefit _after_.

**😉 Realistic load in the database:**

With only a handful of rows, almost every endpoint looks fast — timing logs will not show where caching actually helps. Before you trust the middleware output, **grow the dataset** on the tables your heaviest reads touch (catalog, orders, users with relations, etc.).

- Ask your **coding agent** to generate a **seeder** (script in your stack: Alembic, Prisma seed, Django management command, etc.) or a **SQL script** that inserts many records, then review and run it locally.
- Prioritise **data quality**, not just row count: varied names, categories, dates, prices, and valid foreign keys so filters, joins, sorts, and aggregations behave like production — not five hundred identical `"test"` rows.
- Re-run the timing middleware after seeding. In `CACHING_REPORT.md`, note approximate row counts before vs. after and how latency on your chosen endpoints changed.

**On the frontend:**

- **React DevTools → Profiler**: components that re-render without real prop changes are candidates for `useMemo` or state splitting.
- **Lazy Loading**: routes or modals not needed on first paint but heavy in the bundle (Network tab: large JS fetched only when entering that view).

> ⚠️ Do not cache everything that looks slow: measure first, then prioritise cases where cost × frequency × stability justify the freshness/performance tradeoff.

---

## 🌱 How to Start the Project

This project is built on top of your existing transversal project monorepo. You do not fork a new repository.

1. Open your monorepo in Codespaces or clone it locally.
2. Create a new branch: `git checkout -b feature/caching-optimisation`
3. Make sure both the frontend and backend run correctly before making any changes.

---

## 💻 What You Need to Do

### Frontend Analysis and Optimisation

- [ ] Audit your Next.js application and identify at least **two components or routes** that are good candidates for Lazy Loading. Document your reasoning: why is deferring this component's load justified?
- [ ] Implement Lazy Loading for those components using `next/dynamic` or `React.lazy`.
- [ ] Audit your components for expensive computed values. Identify at least **one `useMemo` opportunity** where the computation is non-trivial and the dependency array is well-defined.
- [ ] Implement the `useMemo` optimisation. Do not apply it to trivial calculations.

### Backend Analysis and Optimisation

- [ ] List all endpoints in your FastAPI application. For each one, assess: (a) how expensive is the operation? (b) how frequently is it called? (c) how often does the underlying data change?
- [ ] Identify at least **two endpoints** that meet the cost + frequency + stability criteria for caching.
- [ ] Implement caching for those endpoints. You may use an in-memory dictionary with TTL logic, `functools.lru_cache` where applicable, or a Redis-based cache if your stack supports it.
- [ ] Implement cache invalidation: if the underlying data changes (e.g., a write operation), the relevant cached values must be cleared or marked stale.

> ⚠️ **IMPORTANT:** Do not cache endpoints that return personalised, session-specific, or sensitive data without scoping the cache key to the authenticated user. A shared cache key for private data is a data leak, not a performance gain.

### Technical Report

- [ ] Write a `CACHING_REPORT.md` (or equivalent) in your monorepo with the following sections:
  - **Frontend decisions**: which components were lazy-loaded and why; which values were memoized and what the measured or estimated benefit is.
  - **Backend decisions**: for each cached endpoint, document the operation cost, call frequency estimate, TTL chosen, and invalidation strategy.
  - **Tradeoffs acknowledged**: at least one explicit discussion of a data freshness tradeoff — where you chose a specific TTL and why that level of potential staleness is acceptable for this use case.
  - **What was not cached and why**: identify at least one endpoint or component you considered but decided against caching, with justification.

---

## ✅ What We Will Evaluate

- [ ] At least two components or routes implement Lazy Loading with documented justification.
- [ ] At least one `useMemo` is applied to a non-trivial computed value with a correct dependency array.
- [ ] At least two backend endpoints are cached with TTL-based expiry.
- [ ] Cache invalidation is implemented: cached values are cleared when the underlying data changes.
- [ ] No private or session-specific data is stored in a shared cache key.
- [ ] `CACHING_REPORT.md` is present and addresses all required sections.
- [ ] Decisions in the report are specific and justified — not generic ("we cached this because it's slow").
- [ ] At least one tradeoff (freshness vs. performance) is explicitly discussed.

> Note: The evaluation focuses on decision quality and implementation correctness, not on the number of endpoints or components cached. Fewer well-justified decisions are preferred over many unjustified ones.

---

## 📦 How to Submit

Push your branch to GitHub and open a Pull Request to `main` in your transversal project repository. Share the PR link according to your instructor's instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/caching-optimization/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
