# Operations Backoffice – Incident Manager

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

![build by developers](https://img.shields.io/badge/build_by-Developers-blue)
![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/incident-manager-for-devs)** before writing a single line of code — it defines the intake channels, incident types, severity levels, and responsible areas for your implementation.

---

## 🎯 The Challenge

> 📌 You're building on **your copy** of the company **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** you selected at the start of the course — not a new repository.

Your company's backoffice doesn't exist as a product yet: it exists as structure. The monorepo already ships folders, naming conventions, dependency management, linter configuration, and a separation of concerns that someone decided before you arrived. None of those decisions are documented anywhere. They live in the code and nowhere else.

Your CTO has opened a ticket for the first real development on top of that foundation: the backoffice's **centralized incident manager**. Right now, operational incidents arrive through different channels, get logged wherever each team happens to keep notes, and get lost between email threads and one-off messages. Nobody knows how many are open right now or who owns each one. The piece itself is deliberately scoped, and that's the point — the business deliverable matters, but the ticket's real objective is bigger: leave the repository in a state where any coding agent that joins later works **inside** the project's rules instead of inventing its own.

That's the real problem. An agent without curated context doesn't sit idle — it fills the gaps. It picks whichever dependency manager it prefers, names files however it prefers, and produces plausible code that doesn't fit the rest of the repository. The more code it generates on that wrong foundation, the more expensive it is to walk back. That's why the first job isn't writing the feature — it's **reading the existing codebase and turning what it already decides into explicit rules**.

There's a common trap in this exercise: asking the agent for a project summary and taking it at face value. An agent's summary of a repository it hasn't fully explored is a hypothesis, not a fact. **You'll need to check that summary against the actual structure and code, and record where it got it wrong** — those discrepancies are the best signal for what needs to be written down.

The second trap is writing a purely technical context. A memory bank that explains the stack but never explains what the company does, who uses the backoffice, or what a critical incident actually means in this specific operation, produces correct code that solves the wrong problem. A critical incident doesn't mean the same thing at every company, and the agent can't infer that from the code. **Product and business context is part of the deliverable, not decoration.**

> **From:** your CTO
> **Subject:** first backoffice development — incidents
>
> > Before we start adding features, I need the repository to stop depending on the memory of whoever set it up.
> >
> > Split the brief into two parts. First: go through the codebase, understand the conventions that are already in place, and write them down as project rules. Don't change them because you don't like them — if you think one is wrong, log it as a proposal and we'll discuss it; overwriting a team convention out of personal preference is the fastest way to break a shared monorepo.
> >
> > Second: build the incident manager. Operations stakeholders need to log an incident regardless of which channel it came in through, classify it, assign it to a responsible area, and know what state it's in. Types, severities, and channels come from your CONTEXT, not from your imagination.
> >
> > One thing that's not negotiable: when an incident changes state or owner, I need to be able to reconstruct afterward who moved it and when. If that isn't recorded, the manager isn't worth having.
> >
> > Acceptance criteria are the ones on the checklist. I sign off on the Pull Request myself, and I'll be reading the commit history: if I see one single commit with everything bundled in, I'm sending it back unreviewed.
>
> — Handoff to the operations team as soon as the feature is verified.

### Supplementary knowledge: what a memory bank is

A **memory bank** is a set of documents versioned in the repository itself that persist project knowledge beyond the current conversation with the agent. It solves a concrete problem: every new session starts from zero, and re-explaining the product in every prompt is expensive in tokens and fragile in results.

A useful memory bank covers, at minimum, three layers: **product context** (what the company is, who it serves, what problem this area solves), **technical stack** (what's set up and what you're working with), and **current state** (what's done, what's in progress, what decisions are closed). It's curated, concrete content: if it rambles or repeats what the agent can already read from the code, it costs tokens without adding signal.

**Rules** are different from the memory bank: memory describes the project, rules constrain how you work on it.

---

## 🌱 How to Start the Project

1. Work on your copy of the company monorepo. Create the `feature/incident-manager` branch.
2. Spin up the environment following what the repository itself documents. If something isn't documented and you have to figure it out, that finding is material for your rules.
3. Make a separate commit for each relevant step of the checklist. The history is part of the deliverable.
4. Use the right agent mode for each phase: exploration and summarization in conversational mode, rule and plan definition before touching code, implementation once the plan is closed.

---

## 💻 What You Need to Do

### Codebase Reconnaissance

- [ ] Explore the monorepo structure and ask the agent for a project summary.
- [ ] Check that summary against the actual structure and code.
- [ ] Document the discrepancies found between the agent's summary and the repository's reality.
- [ ] Identify at least three conventions already established in the code (naming, folder organization, dependency management, style, separation of concerns).
- [ ] Identify at least one practice you consider improvable and log it as a proposal, without applying it unilaterally.

### Project Rules

- [ ] Create the `.agents/rules` directory with the rules derived from the codebase.
- [ ] Split rules by scope: one rule per concern, not a single document with everything in it.
- [ ] Define how each rule applies (always active, attached by file pattern, requested by the agent, or manually invoked) and justify it.
- [ ] Write rules in verifiable terms: what is done, what isn't done, which file pattern it applies to. Avoid ambiguous phrasing.
- [ ] Iterate the rules against the real workflow: if a rule doesn't change the agent's behavior, it's either unnecessary or badly written.

### Memory Bank

- [ ] Create the `memory-bank/` directory with, at minimum: product and business context, technical stack, and current project state.
- [ ] Product context must explain the company, who uses the backoffice, and what an incident means in this operation — not just the architecture.
- [ ] Include an implementation plan for the incident manager, built with the agent before writing code.
- [ ] Keep the memory bank up to date when you close the development: the current state at the end of the project can't be the same as at the start.

⚠️ **IMPORTANT:** product context, entity names, and domain values must match what's specified in your CONTEXT.md. A generic memory bank that would work equally well for any company will not be accepted.

### Incident Manager in the Backoffice

- [ ] Implement creation, editing, listing, and lookup of incidents, with the fields defined in your CONTEXT.
- [ ] Every incident must record its intake channel, type, and severity level, drawn from your CONTEXT's catalogues.
- [ ] Implement assignment of an incident to a responsible area from those defined in your CONTEXT.
- [ ] Implement the incident's state lifecycle, from opening through closure.
- [ ] Every state change and every ownership change must be recorded with its timestamp and author, queryable from the incident's detail view.
- [ ] Add filtering of the listing by state, severity, and responsible area.
- [ ] Provide a view that shows, at a glance, the volume of open incidents by severity.
- [ ] Respect the stack and conventions already shipped in the monorepo. Don't introduce new libraries, dependency managers, or patterns without a rule that justifies it.

⚠️ **IMPORTANT:** field names, entity identifiers, and domain values in your implementation must match what's specified in your CONTEXT.md. A generic implementation that ignores the context will not be accepted.

### Verification

- [ ] Verify the manager's behavior: logging, classification, assignment, full state traversal, and traceability of changes.
- [ ] Review the agent-generated code before committing. Blind trust in its proactivity is an anti-pattern, not a shortcut.
- [ ] Record in the Pull Request which rules prevented a deviation during development.

---

## ✅ What We'll Evaluate

- [ ] The `.agents/rules` directory exists and contains at least three rules derived from the preexisting codebase, not from personal preference.
- [ ] Each rule explicitly declares its application mode and scope.
- [ ] Rules are written in verifiable, unambiguous terms.
- [ ] The `memory-bank/` directory contains product and business context, technical stack, and current project state.
- [ ] Product context reflects the assigned company and its real operation, not a generic description.
- [ ] A versioned implementation plan exists, and the delivered development matches it.
- [ ] A record exists of the discrepancies between the agent's initial summary and the actual code.
- [ ] The manager allows logging an incident with channel, type, and severity, and assigning it to a responsible area.
- [ ] The incident traverses a full state lifecycle through to closure.
- [ ] State and ownership changes are queryable with timestamp and author from the incident's detail view.
- [ ] The listing supports filtering by state, severity, and responsible area.
- [ ] A view exists showing the volume of open incidents by severity.
- [ ] Channel, type, severity, and area catalogues match those in the assigned company's CONTEXT.
- [ ] No dependencies or patterns outside the monorepo's conventions have been introduced.
- [ ] Commit history separates the development steps; there is no single commit bundling all the work.

---

## 📦 How to Deliver

Push your `feature/incident-manager` branch to your copy of the monorepo and open a Pull Request against the main branch.

In the Pull Request description, include:

- The discrepancies found between the agent's initial summary and the actual repository.
- The rules you defined and which code evidence each one comes from.
- The improvement proposal you logged without applying, if any.

---

This and many other projects are built by students as part of 4Geeks Academy's [Coding Bootcamps](https://4geeksacademy.com/). Find out more about our [courses](https://4geeksacademy.com/us/coding-bootcamps) in [Full-Stack Software Development](https://4geeksacademy.com/us/coding-bootcamps/full-stack-developer), [Data Science & Machine Learning](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning), [Cybersecurity](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity), and [AI Engineering](https://4geeksacademy.com/us/coding-bootcamps/ai-engineering).
