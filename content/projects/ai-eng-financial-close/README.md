# Agentic Engineering – Monthly Financial Close

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: read your **[company BRIEFING](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/financial-close)** before writing any code. It defines the close's data sources, the budget, the deviation thresholds, the breakdown leadership expects, and who reviews the report before it's distributed.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)**, not on a new repository.

Company leadership reaches out with a frustration that repeats every month. Closing figures arrive late, assembled by hand from exports of different systems and spreadsheets. When they finally arrive, the numbers don't always reconcile with each other, and explaining why an area deviated from budget requires calling a meeting.

> _"I want each month's close in my inbox in the first few days of the following month, without anyone spending a weekend putting it together. I want to see how we're doing against budget, where we've deviated, and a reasonable explanation of why. But I won't accept a single figure that can't be traced back to its source. If a data point is missing, I'd rather the report say so than have someone fill it in by eye. And before the report reaches the leadership team, a trusted person has to review it."_
>
> — Company Leadership

The brief leaves four requirements implicit, and they define the project:

1. **Every figure is traceable.** Any number in the report must trace back to the record, document, or row it comes from.
2. **The model doesn't do the math.** Sums, percentages, deviations, and currency conversions are computed with deterministic code. The model decides what to calculate, interprets the results, and writes, but it doesn't do the arithmetic.
3. **What's missing is declared.** A period with incomplete data produces a report that says what's missing, not a report that looks complete.
4. **A person approves before distribution.** The agent prepares the report; distribution only happens after a human review.

### Complementary knowledge: what the model does and what the code does

Language models are good at interpreting, summarizing, and writing, but they aren't reliable at arithmetic: they can get a sum wrong convincingly, and in a financial report a convincing error is worse than an obvious one. The right pattern is an **agent with tools**: code calculates deterministically and verifiably, and the agent decides which calculations to request, reads the results, identifies which deviations matter, and writes the explanation. That way, the same period with the same data always produces the same figures, and every figure has a test behind it. The agent's explanations, on the other hand, are data-based hypotheses, and the report must present them as such.

---

## 🌱 How to Start the Project

1. `pull` the latest changes from your fork of the monorepo.
2. Read your company briefing in full before touching any code.
3. Create a new branch: `feature/financial-close`.
4. Review the test data sources the briefing specifies and their structure before designing the ingestion.
5. Design the closing report's structure before coding the agent: its sections, breakdown, and indicators.
6. Define the list of calculation tools the agent will need.

---

## 💻 What You Need to Do

**Data ingestion**

- [ ] Implement ingestion of the close's data sources specified in the briefing
- [ ] Normalize the data to a common format, always keeping a reference to its source
- [ ] Flag any incomplete or inconsistent record as uncertain instead of treating it as valid

**Deterministic calculation tools**

- [ ] Implement the calculations the close needs as code tools: totals, actual versus budget, absolute and percentage deviation, and currency conversion if the briefing requires it
- [ ] Cover every tool with automated tests
- [ ] Ensure that running the close twice on the same period and the same data produces exactly the same figures

**Closing agent**

- [ ] Implement a single agent that uses the calculation tools to analyze the period
- [ ] Identify the deviations that exceed the threshold defined in the briefing
- [ ] For each relevant deviation, write a data-based explanation, presented as a hypothesis and citing the figures that support it
- [ ] Generate the closing report with the structure and breakdown defined in the briefing
- [ ] Explicitly state in the report any data that is missing or flagged as uncertain

**Traceability**

- [ ] Link every figure in the report to the source records that produce it
- [ ] Allow the reviewer to look up, from the report, the source of any figure

**Review and distribution**

- [ ] Run the close as a background task, scheduled for the date defined in the briefing
- [ ] Send the report to the reviewer defined in the briefing before any distribution
- [ ] Allow the report to be approved or rejected with comments; a rejection produces a new version that takes those comments into account
- [ ] Distribute the report only after approval, and only to the recipients defined in the briefing

**Security and logging**

- [ ] The agent operates with its own identity and read-only access to financial data
- [ ] Log every agent action, identifying it as an action by an automated process
- [ ] Identify in the briefing which data is sensitive, and demonstrate that it never appears in logs, stored prompts, or outgoing messages

⚠️ **IMPORTANT:** the data sources, thresholds, report structure, reviewer, and recipients must match exactly what's specified in your company briefing. A generic implementation that ignores that context will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] Every figure in the report traces back to its source records
- [ ] Calculations are done with deterministic code tools covered by tests
- [ ] Running the close twice on the same data produces exactly the same figures
- [ ] Deviations above the threshold are detected, and each one has an explanation presented as a hypothesis and supported by data
- [ ] A period with incomplete data produces a report that states what's missing
- [ ] The report isn't distributed without the reviewer's approval, and a rejection with comments produces a new version
- [ ] Agent actions are logged as actions by an automated process
- [ ] Sensitive data doesn't appear in logs, stored prompts, or outgoing messages

---

## 📦 How to Submit

Open a Pull Request from your `feature/financial-close` branch to `main` on your fork. In the PR description, include the report structure, the list of calculation tools, a sample closing report with its traceability, and a sample report generated with incomplete data. Request sign-off from leadership before merging.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
