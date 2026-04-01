# AI Agent Rental Platform — Admin Panel Prototype

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en Español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

A startup called **AgentHub** is building a SaaS platform where companies can rent AI agents — pre-configured intelligent assistants that can be equipped with different skills (capabilities such as browsing the web, reading documents, or managing calendars) and deployed for specific business tasks.

The founding team has a working backend and a rough idea of what their internal admin panel should look like, but no one on the team has time to build it. They've brought you in as a freelance frontend developer. Your first deliverable is a **fully designed HTML prototype** of the admin panel — something the team can review, validate, and hand off to backend developers later.

Before writing a single line of HTML, you'll need to produce a **specification document** — a structured description of what you're going to build, written in enough detail that an AI coding agent (or another developer) could implement it from scratch without asking questions. This is the core practice of **Spec-Driven Development (SDD)**: you define the what and the rules before you start building. The spec isn't a formality — it's your contract with the codebase.

The product team has shared the following brief:

> #### Admin Panel Requirements — AgentHub
>
> The panel must include the following six sections, accessible from a persistent sidebar navigation. A toggle in the top bar must allow switching the entire interface between light and dark mode using Tailwind's `dark:` utilities.
>
> **1. Dashboard**
> At a glance, the admin must be able to see: total revenue generated (this month), total discount and coupon losses, number of active agents across all clients, and number of agents currently flagged as failing. Each of these should be a visible metric card. Below the cards, include a placeholder area for a weekly activity chart.
>
> **2. User Management**
> A table listing all registered users (name, email, plan, status). Each row must have an action dropdown — a small menu triggered by a `⋮` button — with at least two options: "View detail" and "Delete". Choosing "View detail" opens a modal overlay showing the full user record. The modal must close via a button and by clicking the backdrop.
>
> **3. Agent Management**
> A listing of all agents registered in the platform, showing agent name, owner, current status (active / inactive / failing), and a collapsed skill list. Each agent's associated skills are hidden by default; clicking an expand control reveals the full list with a smooth transition. Each agent also has an action dropdown with options to "Configure" — which opens a modal showing the agent's system prompt — and "Delete".
>
> **4. Skills**
> A section dedicated to the catalog of available skills — the capabilities that can be attached to agents. Each skill has a name, a short description, and an indicator of how many agents currently have it enabled. Include a brief in-panel explanation of what a "skill" means in this platform context. Skills also have an action dropdown with "View detail" and "Delete".
>
> **5. Agent Contracts**
> A table showing all active and past rental contracts. Each row must show the client, the rented agent, the contracted skills, contract dates, and the total amount paid. Each row has an action dropdown. Choosing "View detail" opens a modal with the full contract breakdown, including the itemized list of contracted skills and their individual prices.
>
> **6. Error Log**
> A log of execution errors from agents — showing timestamp, agent name, error type, and a short description. Errors must be visually categorized by type or severity using color-coded badges. Each entry has an action dropdown with "View detail" (opens a modal with the full error trace) and "Mark as resolved".

The panel should feel professional and immediately usable as a reference for future development. All data must be hardcoded — the team is not expecting API connections or a backend at this stage.

**Your job is to write the specification first, commit it to the repository, and then build the prototype against it.**

---

## 🌱 How to Start the Project

1. Fork the template repository: [https://github.com/4GeeksAcademy/html-hello](https://github.com/4GeeksAcademy/html-hello)
2. Create your own GitHub repository and update the remote URL to point to it.
3. Open the project in GitHub Codespaces or clone it locally.
4. Read the full brief carefully before writing the specification.
5. Need help getting started? [Follow these instructions](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 What You Need to Do

### Write the specification first

- [ ] Create a file called `SPECS.md` at the root of the repository.
- [ ] In `SPECS.md`, write a structured specification that includes:
  - [ ] A short product description (what AgentHub is and who the admin user is).
  - [ ] The tech stack and constraints (HTML, Tailwind via CDN, vanilla JS only, no frameworks, no backend).
  - [ ] **At least 3 specifications per section** — each describing a concrete visual or interactive requirement for that view. A good spec entry names a component, describes its contents, and defines its behavior. For example, for the Dashboard: _(1) four metric cards in a responsive 2×2 grid, each with an icon, a label, and a hardcoded value; (2) cards use distinct accent colors per metric type and include a subtle shadow; (3) below the cards, a full-width placeholder div with a dashed border and a centered label represents the weekly activity chart._ Apply this level of detail to all six sections.
  - [ ] A component inventory: a list of the reusable UI components shared across sections (sidebar, metric card, action dropdown, modal, badge, collapsible skill list, dark mode toggle).
  - [ ] Acceptance criteria: a numbered list of verifiable conditions that must be true for the prototype to be considered complete — include at least one criterion per interactive behavior (dropdown, modal, collapsible, dark mode).
- [ ] Commit `SPECS.md` to the repository **before** starting any HTML work.

> ⚠️ **IMPORTANT:** The specification must be committed before the first HTML file. Use a separate Git commit for the spec — the Git history will be checked. An AI coding agent should be able to read your `SPECS.md` and build the panel from it without asking any questions. That is your quality bar.

### Build the prototype

- [ ] Build the admin panel as a single `index.html` file (or multiple linked HTML files, one per section).
- [ ] Use **Tailwind CSS via CDN** for all styling — no custom CSS files, no inline `style` attributes.
- [ ] Implement a persistent **sidebar** with navigation links to all six sections and an active state indicator on the current section.

**Dashboard**

- [ ] Four metric cards (total revenue, discount losses, active agents, failing agents), each with an icon, a label, and a hardcoded value.
- [ ] A full-width placeholder area below the cards representing a weekly activity chart.

**User Management**

- [ ] A table with at least 5 hardcoded user rows showing name, email, plan, and status badge.
- [ ] Each row has a `⋮` action dropdown with "View detail" and "Delete".
- [ ] "View detail" opens a modal with the full user record. The modal closes via a close button and by clicking the backdrop.

**Agent Management**

- [ ] A listing with at least 4 agents, each showing name, owner, status badge, and a collapsed skill list.
- [ ] Clicking the expand control reveals the agent's associated skills with a smooth transition; clicking again collapses them.
- [ ] Each agent has a `⋮` action dropdown with "Configure" and "Delete". "Configure" opens a modal with the agent's system prompt in an editable `<textarea>`.

**Skills**

- [ ] A catalog of at least 4 skills, each showing name, description, and the number of agents that have it enabled.
- [ ] A brief in-panel explanation of what a "skill" is in the AgentHub context.
- [ ] Each skill has a `⋮` action dropdown with "View detail" and "Delete".

**Agent Contracts**

- [ ] A table with at least 4 contracts showing client, agent, contracted skills, start/end dates, and amount paid.
- [ ] Each row has a `⋮` action dropdown. "View detail" opens a modal with the full contract breakdown, including itemized skills and their individual prices.

**Error Log**

- [ ] At least 6 hardcoded error entries showing timestamp, agent name, color-coded error type badge, and short description.
- [ ] Each entry has a `⋮` action dropdown with "View detail" and "Mark as resolved".

**Global interactions**

- [ ] A dark/light mode toggle in the top bar switches the entire panel between color schemes using Tailwind's `dark:` utilities. The chosen mode is preserved while navigating between sections.
- [ ] All action dropdowns close when clicking outside their menu area.
- [ ] All modals close when clicking the backdrop.

> ⚠️ **IMPORTANT:** All interactivity must be implemented with **vanilla JavaScript** only — no frameworks (React, Vue, etc.), no jQuery, no build tools. Tailwind must be loaded via CDN only.

---

## ✅ What We Will Evaluate

- [ ] `SPECS.md` was committed before any HTML file (verified via Git history).
- [ ] The spec contains at least 3 concrete specifications per section, a component inventory, and a numbered acceptance criteria list.
- [ ] All six panel sections are present and accessible from the sidebar.
- [ ] Tailwind utility classes are used consistently throughout — no inline styles, no external CSS files.
- [ ] All list rows have a working `⋮` action dropdown that opens, closes on click, and closes on outside click.
- [ ] "View detail" opens a modal in at least four different sections.
- [ ] Modals close via the close button and via backdrop click.
- [ ] Agent skill lists are collapsed by default and expand/collapse on click with a visible transition.
- [ ] The dark/light mode toggle switches the full panel and the state is maintained between sections.
- [ ] Hardcoded data is consistent across sections (the same agent name appears in Agent Management, Contracts, and Error Log).
- [ ] HTML uses semantic tags correctly — `section`, `table`, `nav`, `header`, `main`, and similar.
- [ ] The layout is usable on both desktop and tablet viewports.

> Note: Form submission, live search, and real page navigation are not evaluated. The interactive behaviors above — dropdowns, modals, collapsibles, dark mode — are required and will be tested manually.

---

## 📦 How to Submit

Push your repository to GitHub and share the link according to your instructor's instructions. Make sure the repository is public and that both `SPECS.md` and the HTML files are committed and visible.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
