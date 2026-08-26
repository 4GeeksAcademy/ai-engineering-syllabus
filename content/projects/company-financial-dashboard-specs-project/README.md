# Applying Spec Driven Development - Financial dashboard

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your challenge

You continue on the **same inherited financial dashboard** from the context project. The client's finance team has feedback on three new capabilities. Before anyone builds a component, your tech lead stops the team:

> **"We spec first. Then we build."**

A well-written specification defines what the user sees, what data each component needs, and what rules govern every field. If the spec is clear, any developer — or coding agent — can implement it without asking you questions.

**Stack-agnostic means your prior knowledge, not the project's stack.** This repo has a predefined frontend and backend. You do **not** need to already know TypeScript interfaces, OpenAPI, or every API field name. Your coding agent explores `/docs` and existing frontend patterns; you drive it, verify every type and rule against live API evidence, and reject guesses.

### How you work (every phase)

1. Ask the agent to explore `/docs` and relevant existing frontend code before drafting specs.
2. For each feature, give the PM outcome as a prompt — let the agent propose types, components, and edge cases.
3. Mark API claims ✅ verified in `/docs` / ❌ wrong / ❓ unverified; correct with the agent.
4. Commit spec artifacts only after verification — separate commits for types, components, and data contract are ideal.
5. Do **not** implement React components or API calls in this project.

> Your product manager shared the following feature requests:
>
> ---
>
> #### Feature 1 — Date range filter on the home dashboard
>
> The finance team wants to focus on specific periods without seeing all historical data at once. Add two date inputs to the top of the home dashboard — a start date and an end date — that filter all the data currently displayed on the page. Dates are sent to the API in `YYYY-MM-DD` format. Both inputs are optional; when empty, the dashboard shows all available data. The available date range (earliest and latest dates in the dataset) must be shown near the inputs as a reference so the user knows what range is valid.
>
> Relevant endpoint: `GET /api/metrics/facets` (to retrieve the available date range) and the filters extension on the existing metrics endpoint.
>
> ---
>
> #### Feature 2 — Anomaly alerts table on the home dashboard
>
> Below the existing charts, add a table that highlights periods where spending spiked unexpectedly. The table has four columns: period, recorded outcome, rolling average of the previous 3 periods, and the percentage increase. The spike threshold is configurable by the user via a numeric input (a ratio between `0.01` and `1.0`, defaulting to `0.3`). If no anomalies are detected for the current threshold, the table must show an explicit empty state message — not just disappear. The table must also respect the date range set in Feature 1 if active.
>
> Relevant endpoint: `GET /api/metrics/alerts?threshold=<ratio>`
>
> ---
>
> #### Feature 3 — B2B vs B2C comparison view
>
> Create a new page in the dashboard for comparing revenue performance between the two business lines: B2B and B2C. The view has two sections side by side. Each section shows a table with the top 5 income categories for that business line, displaying category name, total income, and percentage of the group total. Below both sections, a single chart compares the total income of B2B against B2C visually. The user can filter the comparison by a date range (same `YYYY-MM-DD` format). The available categories for each group must come from the facets endpoint.
>
> Relevant endpoints: `GET /api/metrics/categories/top?operation_type=income&limit=5` and `GET /api/metrics/facets`

Your specifications must be precise enough that a coding agent can build each feature from them alone — because every field name, parameter, and edge case was verified against `/docs`, not invented.

---

## 🌱 How to Start the Project

Continue on the **same repository** from the context project. Do not fork a new repo.

1. Open your financial dashboard fork ([**ai-eng-financial-dashboard-context-project**](https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project)) in your coding agent.
2. Confirm `memory-bank/` and `.agents/rules` from prior work are committed and current.
3. Create a branch: `git switch -c feature/frontend-specs`.
4. Create `frontend/specs/` — all specification files go here.
5. Ask the agent to start the backend and open `/docs`; explore endpoints for the three features before writing any spec.

If you need a reminder on branching: [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 What You Need to Do

### Phase 1 — Explore the API (with the agent)

- [ ] With the backend running, ask the agent to map the endpoints, response shapes, and query parameters for all three features using `/docs`.
- [ ] Cross-check against existing frontend fetch patterns in the repo where helpful.
- [ ] Note any mismatches between PM wording and actual API fields — resolve them in the spec, not at implementation time.
- [ ] Optional: short verification trail in commit messages or `verification.md`.

### Phase 2 — TypeScript types (agent drafts, you verify)

- [ ] Have the agent draft `frontend/specs/api-types.ts` with interfaces for API responses used by the three features:
  - `FacetsResponse` — date range reference and B2B vs B2C view
  - `AlertEntry`, `AlertsResponse` — anomaly table
  - `CategoryEntry`, `TopCategoriesResponse` — B2B vs B2C comparison table
- [ ] Have the agent draft `frontend/specs/param-types.ts` with query parameter types:
  - `DateRangeFilter` — optional start/end dates as `string` in `YYYY-MM-DD` format
  - `AlertsParams` — threshold plus date range filter
  - `TopCategoriesParams` — operation type, limit, and date range filter
- [ ] Verify every property name and type against `/docs`; strict TypeScript — no `any`, no `object`.
- [ ] Every property needs JSDoc: meaning, valid values, format where applicable.
- [ ] Commit: types verified against OpenAPI.

### Phase 3 — Component specifications (agent drafts, you verify)

- [ ] Have the agent draft `frontend/specs/components.md` for each feature:

  **Feature 1 — Date range filter**
  - Component name(s), props, layout
  - Behavior when only one date input is filled
  - How the available date range hint (from `FacetsResponse`) is displayed

  **Feature 2 — Anomaly alerts table**
  - Component name(s) and props
  - Four columns and their data types
  - Empty state when alerts array is empty
  - Behavior when threshold input is out of range

  **Feature 3 — B2B vs B2C comparison view**
  - Components for two-panel layout, top-5 table, comparison chart
  - Props for each component
  - What each panel renders when top-5 list is empty
  - What the comparison chart displays and what its two data points represent

- [ ] Align component props with types from Phase 2; resolve ambiguities the PM brief left open.
- [ ] Commit: component specs.

### Phase 4 — Data contract documentation

- [ ] Have the agent draft `frontend/specs/README.md` covering all three features:
  - Endpoint(s) each feature consumes (paths verified in `/docs`)
  - TypeScript types for each request and response
  - Valid values and constraints for every parameter
  - At least 2 edge cases per feature and what the UI must show
- [ ] Read it as if you were handing it to a fresh agent session — fix anything that would trigger follow-up questions.
- [ ] Run `npx tsc --noEmit` and fix type errors.
- [ ] Commit: data contract README.

> ⚠️ **IMPORTANT:** You are specifying the frontend layer, not implementing it. Do not build React components or wire API calls. Deliverables: TypeScript types, `components.md`, and `frontend/specs/README.md`.

---

## ✅ What We Will Evaluate

- [ ] API exploration evidence: types and endpoints traceable to `/docs`, not guessed field names.
- [ ] All response interfaces match live OpenAPI shapes, without `any`.
- [ ] `DateRangeFilter` has both fields optional, typed as `string` with `YYYY-MM-DD` JSDoc.
- [ ] `AlertsParams` and `TopCategoriesParams` extend or include `DateRangeFilter`.
- [ ] `components.md` names every component, lists props with types, specifies conditional rendering per feature.
- [ ] Anomaly table empty state explicitly specified.
- [ ] Single-date-input behavior explicitly specified.
- [ ] Both B2B vs B2C panels specify empty top-5 rendering.
- [ ] `frontend/specs/README.md` covers all three features with endpoints, types, parameters, and ≥ 2 edge cases each.
- [ ] TypeScript compiles (`npx tsc --noEmit`).
- [ ] Work on `feature/frontend-specs` with meaningful commits; specs read as agent-assisted work you verified.
- [ ] No React components, fetch calls, or backend changes.

> Note: Implementation is out of scope. A spec good enough for a coding agent to build without questions is the bar.

---

## 📦 How to Submit

Push your `feature/frontend-specs` branch to GitHub and share the repository URL with your instructor. Ensure `frontend/specs/` is present and the branch is visible.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
