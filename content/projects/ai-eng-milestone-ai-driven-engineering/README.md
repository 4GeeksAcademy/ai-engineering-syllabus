# Milestone — AI-driven Engineering

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

<!-- endhide -->

**Before you start**: read your company briefing in [`00-general-contexts`](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts) and copy it into `CONTEXT.md` at the root of your monorepo before writing any code — that is where your company's identity, constraints, and roadmap live.

---

## 🎯 Your challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

This is where your company project begins. You have a template repository and a company scenario — but no coherent system yet. Everything you build from here — interfaces, APIs, agents, automations — will live in this same space. Before adding features, you need the infrastructure that keeps that code coherent, maintainable, and AI-ready.

Your tech lead has had a ticket sitting on the board for two weeks:

> **Subject: Monorepo AI Setup — we need this done this week**
>
> Hi,
>
> I've reviewed the state of the repo and we're starting without any supporting structure. If I drop an agent on this right now it's going to make mistakes that will cost us triple the time to fix.
>
> I need the repository to have clear, persistent context before we keep adding features: what the company is, what we're building, what the project rules are. That goes into the memory bank. The agent has to read it before touching anything — and it has to include both business context and technical context, not just one of the two.
>
> I also want an `AGENTS.md` that defines how any agent operates in this repo — what workflow it has to follow before making a commit. No agents writing code without going through the delivery process.
>
> For more specific rules we'll use the `.agents/` folder. Think about what conventions the agent needs to know to not break what we already have, and document them there with the correct scope.
>
> Finally, I want us to formalise at least one skill that captures a recurring task in our workflow — something the agent can execute consistently and that we can reuse as the project grows. It needs explicit acceptance criteria: if it can't be verified, it doesn't count.
>
> For the application layer, follow the monorepo template structure: the public website under `./uis/website` and the internal applications under `./uis/backoffice` with its own layout and entry view so we have something visible from day one. Any backend services belong under `/services`.
>
> When you're done, open a PR and let me know.
>
> — [Your tech lead]

### 💡 Memory bank, rules, and skills: what they are and why they matter

A **memory bank** is a set of Markdown files that the coding agent reads before each session. It is not static documentation — it is the active context of the project: business description, architectural decisions made, active constraints, and the current state of development. Without it, every agent session starts from scratch and repeats the same mistakes. That's why the memory bank must be updated every time the project evolves: new decisions, architecture changes, completed features, problems encountered. A memory bank that isn't kept up to date stops being useful within days. **Never forget this!**

The expected structure for agent configuration in the monorepo is the following:

```text
./.agents
└─ /rules
   └─ <rule-name>.md
└─ /skills
   └─ /<skill>
      └─ SKILL.md
./memory-bank
└─ <context>.md
```

> ⚠️ **Attention:** Do not confuse `.agents/` with the `/agents` and `/skills` folders you will see in the monorepo. `.agents/` is the configuration directory for coding agents (Cursor, Windsurf, Claude Code…) — this is where the rules and skills that teach the agent how to work in this repository go. The `/agents` and `/skills` folders are for the agents and integrations you will build for the company in later modules. They are different things: one configures how your development tool works, the other is product code.

Before creating any new folder, review the `README.md` inside each folder of the monorepo — the template repository includes instructions on what should go in each space. Following them will prevent duplication and keep a structure the agent can navigate without ambiguity.

**Development rules** (`AGENTS.md` and `.agents/rules/`) are the protocol the agent follows automatically: what to read at the start, what steps are mandatory before each commit, which conventions to respect, and when to stop and ask. They act as the team agreement that ensures the agent doesn't make decisions on its own where it shouldn't.

An **agent skill** is a structured, reusable instruction: more concrete than a generic rule, with defined inputs, expected output, and verifiable acceptance criteria. A good skill has a single objective and can be tested independently.

---

## 🌱 How to Start the Project

Read the `CONTEXT.md` at the **root of your monorepo** before doing anything else. That file must be your company briefing from [`00-general-contexts`](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts) (`CONTEXT-<company>-briefing.en.md`) — not the empty template placeholder. The memory bank you are going to build must describe the company and project from your specific scenario — not a generic fictional company.

1. Fork the template repository: [ai-engineering-company-project-monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)
2. Open your fork in **GitHub Codespaces** or clone it locally, then review the existing structure before creating new folders
3. Configure your coding agent with access to the full repository
4. Document initial setup decisions in the memory bank **before** writing any application code

---

## 💻 What You Need to Do

### Agent Infrastructure

- [ ] Create the `memory-bank/` folder at the root of the monorepo with at least the following files:
  - [ ] `projectbrief.md` — business description, project objectives, and the problem it solves
  - [ ] `techContext.md` — tech stack, architectural decisions made, and technical constraints
  - [ ] `progress.md` — current state of development and planned next steps
- [ ] Create the `AGENTS.md` file at the root of the monorepo defining:
  - [ ] Which memory bank files the agent must read at the start of each session
  - [ ] The mandatory workflow before each commit (minimum 4 ordered, explicit steps)
  - [ ] The folders and files the agent **must not modify** without explicit developer confirmation
- [ ] Create the `.agents/` folder with at least one development rule documented with its scope (always active, file-pattern based, or agent-requested)
- [ ] Implement at least one **agent skill** for a recurring workflow task, with:
  - [ ] A single, clearly defined objective
  - [ ] Documented inputs
  - [ ] Explicit and verifiable acceptance criteria

⚠️ **IMPORTANT:** The memory bank, rules, and skill must be aligned with the data, processes, and constraints in your monorepo's `CONTEXT.md` (your company briefing). A generic infrastructure — or one built against the unreplaced template placeholder — will not be accepted.

### Application Structure

- [ ] Initialise the frontend structure under `/uis` inside the monorepo following the template repository structure
- [ ] Create the public-facing project in `./uis/website`:
  - [ ] Home route (`/`) renders a corporate website aligned with your company briefing in `CONTEXT.md`
  - [ ] Content is built with reusable components and consistent styling for your company's visual identity
- [ ] Create the internal app in `./uis/backoffice`:
  - [ ] Route `/` accessible with a basic entry view (welcome screen or empty dashboard structure)
  - [ ] Its own layout, separate from the public website layout in `./uis/website`
  - [ ] At least one piece of company-relevant logic or data from `CONTEXT.md` visible in the interface — not only in the console or terminal
- [ ] Place any backend services under `/services`, following the monorepo template conventions

---

## ✅ What We Will Evaluate

- [ ] The memory bank contains both business context **and** technical context — not just one of the two
- [ ] `AGENTS.md` specifies a workflow with at least 4 ordered steps before the commit
- [ ] The `.agents/` folder contains at least one rule with an explicit scope of application
- [ ] The implemented skill has a single objective, documented inputs, and verifiable acceptance criteria
- [ ] The public interface in `./uis/website` starts without errors using the project's dev command
- [ ] The `/` route in `./uis/website` renders a complete corporate website aligned with `CONTEXT.md`
- [ ] `./uis/backoffice` exists, has its own layout, and renders without errors
- [ ] `./uis/backoffice` shows company-relevant output on screen — not only in the console
- [ ] Application code follows the monorepo folder conventions without unnecessary duplication

---

## 📦 How to Submit

1. Make sure your working branch is named `feature/agent-memory-bank`
2. Run the delivery workflow defined in your `AGENTS.md` before the final commit
3. Open a Pull Request targeting the `main` branch of your fork
4. In the PR description include:
   - Screenshot of the corporate website rendered from `./uis/website`
   - Screenshot of `./uis/backoffice` with company-relevant content visible on screen
   - Direct link to your `AGENTS.md`
5. Submit the link to your PR on the 4Geeks campus

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
