# Frontend Performance Audit

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/frontend-performance-audit/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

Your company's corporate site and backoffice are live. The team is proud of the features — but the CTO just dropped a message in the dev channel: the team should look for performance improvements — both to support better SEO on the corporate site and to make sure the backoffice performs well for the people using it daily. Before the next milestone, you need to audit both frontends, identify what's dragging down performance, apply the necessary fixes, and document everything with the rigour you'd expect in a professional codebase.

This is not about making things pretty. It's about making them fast, measurable, and maintainable.

A good performance audit follows a clear loop: **measure → analyse → fix → measure again**. You'll run Lighthouse before touching a single line of code, then review the codebase to identify what can be improved — including components or logic that appear more than once and should be extracted into reusable units. You'll install a set of agent skills specifically designed to guide the correction of web vitals issues, apply the fixes they recommend, and close the loop with a second Lighthouse run to validate your work.

> Your CTO has left the following note in the team's task tracker:
>
> #### Performance audit — both frontends
>
> - Run Lighthouse on the corporate site and on the backoffice. Record the initial scores (Performance, Accessibility, Best Practices, SEO).
> - Review the codebase. Identify components or logic that are duplicated across files and could be refactored into a shared component or custom hook.
> - In case you need it, you can install one of the following agent skills to guide the correction process:
>   - [core-web-vitals](https://www.skills.sh/addyosmani/web-quality-skills/core-web-vitals)
>   - [performance](https://www.skills.sh/addyosmani/web-quality-skills/performance)
>   - [web-perf (Cloudflare)](https://www.skills.sh/cloudflare/skills/web-perf)
> - Apply the corrections the skills identify as needed.
> - Deliverables:
>   - An `AUDIT.md` file with the analysis: initial scores, issues identified, root cause for each.
>   - A `REPORT.md` file with the improvements applied and their measured impact on the original scores.
>   - Screenshots of Lighthouse before and after changes, committed to the repo.

The goal is not a perfect 100. The goal is a documented, evidence-based improvement cycle — the same one you'll repeat throughout your career every time you ship a frontend.

---

### What makes a useful Lighthouse audit?

Lighthouse analyses **one page at a time** — it doesn't crawl your whole application. A single run on the homepage tells you nothing about how a dashboard view with heavy data loads performs. When auditing an application with multiple views, run Lighthouse on the pages that matter most: those with the most visual complexity, the most components rendered at once, or the highest user traffic. For the corporate site that is usually the home and any content-heavy page; for the backoffice it is typically the main dashboard or any view with tables, charts, or real-time data.

Lighthouse gives you four top-level scores: **Performance**, **Accessibility**, **Best Practices**, and **SEO**. For a production frontend, the benchmarks that matter most are:

- **Performance ≥ 90** — Anything below 50 is considered poor and will affect real users on mobile networks.
- **LCP (Largest Contentful Paint) < 2.5s** — How fast the main content appears.
- **CLS (Cumulative Layout Shift) < 0.1** — Unexpected layout movement as the page loads.
- **FID / INP (Interaction to Next Paint) < 200ms** — Responsiveness to user input.
- **TTFB (Time to First Byte)** — How fast the server starts sending the HTML response.

A full Lighthouse report can feel overwhelming the first few times you open it — dozens of audits, opportunities, and diagnostics on a single screen. **Do not try to fix everything at once.** A practical way to work through it:

1. **Start with the main indicators** — the four scores plus Core Web Vitals and server timing signals such as **TTFB**, **LCP**, **CLS**, and **INP**. These tell you _where_ the pain is (network, render, layout, interactivity) before you dive into every sub-audit.
2. **Use your AI agent as a tutor** — paste or describe one metric at a time and ask what it measures, what “good” looks like, and which fixes usually move it. Go step by step: understand the indicator, then the recommended actions for _your_ stack (Next.js, images, fonts, hydration, etc.).
3. **Fix one issue per commit** — pick the highest-impact KPI, apply a targeted change, commit with a clear message, re-run Lighthouse on the same URL, and record the delta. Repeat until the main KPIs are in a healthy range.
4. **Then tackle complementary issues** — accessibility hints, best-practices warnings, SEO opportunities, and lower-priority audits matter, but they come _after_ the metrics that directly affect real users on slow devices.

Common root causes students overlook: unoptimised images, render-blocking resources, layout shifts caused by missing `width`/`height` attributes on images, fonts loaded without `display: swap`, and component hydration issues in Next.js.

---

## 🌱 How to Start the Project

This project does not use a new starter template. You work inside your existing company monorepo.

1. Open your monorepo in Codespaces or clone it locally.
2. Make sure both your corporate site and backoffice are running (`npm run dev` or the equivalent command in each app).
3. Open Chrome or Brave — Lighthouse is available natively in the DevTools (Lighthouse tab).
4. Take your first screenshots before making any changes.

---

## 💻 What You Need to Do

### Measurement

- [ ] Run Lighthouse on the corporate site in both **desktop and mobile** modes — at minimum on the home page, plus any other view you consider complex enough to audit. Record all four scores per page and per mode.
- [ ] Run Lighthouse on the backoffice — at minimum on the main dashboard or the most element-heavy view. Record all four scores per page.
- [ ] Take screenshots of both Lighthouse reports and commit them to a `/audit/before/` folder in the repo.

### Code analysis

- [ ] Review both frontends and identify at least two cases where a component or logic block is repeated and could be extracted into a shared component or a Custom Hook.
- [ ] Document each case in `AUDIT.md`: where it appears, why it qualifies as a refactor candidate, and what the shared abstraction would look like.

### Agent skill installation

- [ ] In case you need it, install one or more of the agent skills listed by the CTO:
  - `https://www.skills.sh/addyosmani/web-quality-skills/core-web-vitals`
  - `https://www.skills.sh/addyosmani/web-quality-skills/performance`
  - `https://www.skills.sh/cloudflare/skills/web-perf`
- [ ] Run the agent on both frontends and record what corrections it identifies.

### Corrections

- [ ] Prioritise main KPIs (TTFB, LCP, CLS, INP, Performance score) before lower-priority Lighthouse audits; use your agent to interpret one indicator at a time.
- [ ] Apply fixes incrementally — **one issue per commit**, re-run Lighthouse on the same URL after each change to confirm impact.
- [ ] Apply the corrections the agent skills identify as required fixes (not suggestions).
- [ ] Apply the refactors you identified during the code analysis — extract at least one reusable component or Custom Hook.

### Measurement — second round

- [ ] Re-run Lighthouse on both frontends after corrections.
- [ ] Take new screenshots and commit them to `/audit/after/`.

### Deliverables

- [ ] Write `AUDIT.md` containing: initial Lighthouse scores, issues identified with a root-cause explanation for each, and the refactor analysis.
- [ ] Write `REPORT.md` containing: a description of each correction applied, the before/after score comparison, and your assessment of what had the biggest impact.
- [ ] Commit both markdown files and all screenshots to the repo.

⚠️ **IMPORTANT:** Do not restructure the architecture of either frontend to pass this audit. Apply targeted corrections. The goal is improvement, not a rewrite.

---

## ✅ What We Will Evaluate

- [ ] Lighthouse was run on both frontends before and after, with screenshots committed to the repo.
- [ ] `AUDIT.md` identifies concrete issues with root-cause reasoning — not just a list of what Lighthouse flagged.
- [ ] At least one reusable component or Custom Hook was extracted and integrated into the codebase.
- [ ] `REPORT.md` shows a measurable improvement in at least one Lighthouse score per frontend.
- [ ] If agent skills were installed, there is evidence of their use in the correction process.
- [ ] Applied corrections target real causes (image optimisation, layout shift, hydration issues) rather than superficial changes that inflate scores without addressing the underlying problem.
- [ ] Code quality is maintained after refactoring — no broken features, no regressions.

> Note: Achieving a score of 100 is not an evaluation criterion. Evidence-based improvement and quality of analysis are.

---

## 📦 How to Submit

Push your changes to your company monorepo on GitHub and share the repository URL according to your instructor's instructions. Make sure `AUDIT.md`, `REPORT.md`, and the `/audit/` folder with all screenshots are included in the final commit.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/frontend-performance-audit/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
