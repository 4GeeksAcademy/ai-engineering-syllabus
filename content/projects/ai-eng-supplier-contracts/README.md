# Agentic Engineering – Supplier and Contract Management

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: read your **[company BRIEFING](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/supplier-contracts)** before writing any code. It defines the suppliers, contracts, and pricing data you'll work with, the alert thresholds, and who approves each decision.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)**, not on a new repository.

Operations leadership reaches out with a problem that costs money every quarter. Supplier price increases are discovered when the invoice arrives. Contracts are scattered across folders and emails, and nobody knows for sure when each one expires, how much notice it requires, or whether a specific increase is allowed. When it's time to renegotiate, someone spends days gathering price history, reviewing the contract, and comparing against other suppliers.

> _"I need to find out about a price increase before we pay it, not after. And when I do, I want to know right away whether the contract allows it, how much it costs us, what alternatives we have, and how much room the contract gives us to negotiate or walk away. Today that's done by two people who don't talk to each other: one looks at prices and the other looks at contracts. I want the system to connect both. But nobody talks to a supplier on behalf of the company without my approval."_
>
> — Operations Leadership

The brief leaves four requirements implicit, and they define the project:

1. **These are two specialties that need each other.** Analyzing prices and analyzing contracts require different sources, tools, and criteria. But the important questions ("is this increase allowed?", "should we renegotiate?") need both at once, so something has to coordinate them.
2. **Every figure and every clause is traceable.** Every price must trace back to its source record, and every statement about a contract to the clause and page it comes from. If the data doesn't exist, the system says so; it doesn't estimate it.
3. **The model doesn't do the math.** Price changes, financial impact, and comparisons are computed with deterministic code. The model interprets, writes, and decides what to calculate, but it doesn't do the arithmetic.
4. **The system prepares; people decide.** No communication with a supplier and no decision with financial impact is executed without human approval.

### Complementary knowledge: when a multi-agent architecture actually makes sense

A single agent with every price-analysis and contract-analysis tool piles up competing instructions and a context full of information irrelevant to each specific task, which degrades the quality of its decisions. A **supervisor + specialists** architecture solves this: each specialist has a narrow scope, its own tools, and its own context, and the supervisor decides whom to consult and combines the answers. The cost is added complexity: you need a clear contract for what each specialist receives and returns, and you need to keep the supervisor from looping through consultations. A multi-agent architecture is justified when the specialties are genuinely distinct and the important questions cut across them, as they do here. For a linear process, one agent is enough.

---

## 🌱 How to Start the Project

1. `pull` the latest changes from your fork of the monorepo.
2. Read your company briefing in full before touching any code.
3. Create a new branch: `feature/supplier-contracts`.
4. Review the test data the briefing specifies (suppliers, price history, and contracts) and its structure before designing the ingestion.
5. Draw the architecture before coding: what the supervisor does, what each specialist does, which tools each one has, and what data passes between them.
6. Write down the input and output contract for each specialist.

---

## 💻 What You Need to Do

**Data and document ingestion**

- [ ] Implement ingestion of the supplier registry and its price history, always keeping a reference to the source
- [ ] Implement ingestion of the PDF contracts and extract their key terms: expiry date, renewal or cancellation notice period, price revision conditions, exit clauses, and penalties
- [ ] Keep the source clause and page for every extracted term
- [ ] Flag any low-confidence extraction as uncertain instead of treating it as valid

**Pricing specialist**

- [ ] Maintains price history by supplier and by product or service
- [ ] Detects price increases above the threshold defined in the briefing
- [ ] Calculates the financial impact of an increase based on purchase volume
- [ ] Compares a supplier's price with other suppliers in the same category

**Contracts specialist**

- [ ] Answers what a contract allows or prevents in a specific situation, citing the clause
- [ ] Determines whether a price increase falls within what the price revision clause allows
- [ ] Generates alerts with the lead time defined in the briefing before each expiry date or notice deadline

**Supervisor**

- [ ] Receives the request, decides which specialists to consult, and combines their answers into a single response
- [ ] When an increase is detected, automatically determines whether the contract allows it and what its impact is
- [ ] Generates, on request, a renegotiation brief that combines price history, comparison with other suppliers, financial impact, and contractual leverage (notice period, exit clauses, penalties)
- [ ] Limits the number of consultations per request to avoid loops

**Calculation and traceability**

- [ ] Implement price changes, financial impact, comparisons, and currency conversions (if the briefing requires them) as deterministic code tools covered by tests
- [ ] Ensure every figure and every contractual reference in a response or brief can be traced back to its source
- [ ] When a data point or clause is missing, the system states it explicitly instead of assuming it

**Human approval and security**

- [ ] The system can draft supplier communications, but none is sent without human approval
- [ ] Apply the approval thresholds and approvers defined in the briefing
- [ ] Each agent operates with its own identity and only with its specialty's tools
- [ ] Log every action by every agent, identifying which agent performed it
- [ ] Identify in the briefing which data is sensitive, and demonstrate that it never appears in logs, stored prompts, or outgoing messages

⚠️ **IMPORTANT:** the suppliers, contracts, thresholds, alert lead times, and approvers must match exactly what's specified in your company briefing. A generic implementation that ignores that context will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] The architecture separates supervisor and specialists, with tools and input/output contracts defined for each
- [ ] An increase above the threshold is detected and evaluated against the price revision clause of the corresponding contract
- [ ] The renegotiation brief combines data from both specialists into a coherent recommendation
- [ ] Every figure traces back to its source record, and every contractual statement to its clause and page
- [ ] Calculations are done with deterministic code, verifiable with tests
- [ ] Expiry and notice alerts fire with the defined lead time
- [ ] No supplier communication is sent without human approval from the correct approver
- [ ] When a data point or clause doesn't exist, the system states it instead of inventing it
- [ ] Sensitive data doesn't appear in logs, stored prompts, or outgoing messages
- [ ] The choice of a multi-agent architecture is justified in writing

---

## 📦 How to Submit

Open a Pull Request from your `feature/supplier-contracts` branch to `main` on your fork. In the PR description, include the architecture diagram, the input and output contracts for each specialist, the justification for the multi-agent architecture, an example of an increase detected and evaluated against its contract, and a renegotiation brief with its traceability. Request sign-off from Operations leadership before merging.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
