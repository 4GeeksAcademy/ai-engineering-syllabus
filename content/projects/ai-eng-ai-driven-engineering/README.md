# Milestone 4 — AI-driven Engineering

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** before writing any code — it defines the specific company data, naming conventions, KPIs, and constraints for your implementation.

---

## 🎯 The Challenge

You have three milestones behind you: the public website, the business logic in TypeScript, and the first AI-generated components. You have pieces. What you don't have yet is the system that connects them and will grow alongside them.

From this milestone on, the monorepo stops being a collection of separate projects and becomes the technical core of your company. Everything you build from here — APIs, agents, automations — will live in this same space. That's why, before adding more code, you need to build the infrastructure that will make that code coherent, maintainable, and AI-ready.

Your tech lead has had a ticket sitting on the board for two weeks:

> **Subject: Monorepo AI Setup — we need this done this week**
>
> Hi,
>
> I've reviewed the state of the repo and we're accumulating code without any supporting structure. If I drop an agent on this right now it's going to make mistakes that will cost us triple the time to fix.
>
> I need the repository to have clear, persistent context before we keep adding features: what the company is, what we're building, what the project rules are. That goes into the memory bank. The agent has to read it before touching anything — and it has to include both business context and technical context, not just one of the two.
>
> I also want an `AGENTS.md` that defines how any agent operates in this repo — what workflow it has to follow before making a commit. No agents writing code without going through the delivery process.
>
> For more specific rules we'll use the `.agents/` folder. Think about what conventions the agent needs to know to not break what we already have, and document them there with the correct scope.
>
> Finally, I want us to formalise at least one skill that captures a recurring task in our workflow — something the agent can execute consistently and that we can reuse in upcoming milestones. It needs explicit acceptance criteria: if it can't be verified, it doesn't count.
>
> As for the app, the public website needs to live in `./uis/website` as a Next.js app — not as a copy, but as an improved version with reusable components. In parallel, create `./uis/application` to host all internal company logic with its own layout and entry view, and integrate the TypeScript script from the business logic module (Milestone 2) there so we have something visible from day one. Any APIs must be created under `/services`.
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

> ⚠️ **Attention:** Do not confuse `.agents/` with the `/agents` and `/skills` folders you will see in the monorepo. `.agents/` is the configuration directory for coding agents (Cursor, Windsurf, Claude Code…) — this is where the rules and skills that teach the agent how to work in this repository go. The `/agents` and `/skills` folders are for the agents and integrations you will build for the company starting in later milestones. They are different things: one configures how your development tool works, the other is product code.

Before creating any new folder, review the `README.md` inside each folder of the monorepo — the template repository includes instructions on what should go in each space. Following them will prevent duplication and keep a structure the agent can navigate without ambiguity.

**Development rules** (`AGENTS.md` and `.agents/rules/`) are the protocol the agent follows automatically: what to read at the start, what steps are mandatory before each commit, which conventions to respect, and when to stop and ask. They act as the team agreement that ensures the agent doesn't make decisions on its own where it shouldn't.

An **agent skill** is a structured, reusable instruction: more concrete than a generic rule, with defined inputs, expected output, and verifiable acceptance criteria. A good skill has a single objective and can be tested independently.

---

## 🌱 How to Start the Project

Read your `CONTEXT-company.md` before doing anything else. The memory bank you are going to build must describe the company and project from your specific scenario — not a generic fictional company.

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

⚠️ **IMPORTANT:** The memory bank, rules, and skill must be aligned with the data, processes, and constraints defined in your `CONTEXT.md`. A generic infrastructure that ignores the company context will not be accepted.

### Next.js + TypeScript Application

- [ ] Initialise the frontend structure under `/uis` inside the monorepo following the template repository structure
- [ ] Create the public web project in `./uis/website` (Next.js + TypeScript)
- [ ] Migrate and improve the corporate website from Milestone 1 in `./uis/website` as the home route (`/`):
  - [ ] All sections from Milestone 1 present and complete
  - [ ] Implemented with reusable React components and correct TypeScript typing
  - [ ] Styles consistent with the visual identity established in Milestone 1
- [ ] Create the internal app in `./uis/application`:
  - [ ] Route `/` in `./uis/application` accessible with a basic entry view (welcome screen or empty dashboard structure)
  - [ ] Its own layout, separate from the public corporate website layout in `./uis/website`
- [ ] Integrate the TypeScript script from the business logic module (Milestone 2) inside `./uis/application`:
  - [ ] Code is imported from its original location in the monorepo — not copied
  - [ ] The output of the business logic is visible in the interface (not just in the console)

---

## ✅ What We Will Evaluate

- [ ] The memory bank contains both business context **and** technical context — not just one of the two
- [ ] `AGENTS.md` specifies a workflow with at least 4 ordered steps before the commit
- [ ] The `.agents/` folder contains at least one rule with an explicit scope of application
- [ ] The implemented skill has a single objective, documented inputs, and verifiable acceptance criteria
- [ ] The public web in `./uis/website` starts without errors with `npm run dev`
- [ ] The `/` route in `./uis/website` renders the complete corporate website with TypeScript components
- [ ] `./uis/application` exists, has its own layout, and renders without errors
- [ ] The TypeScript script (Milestone 2) is integrated in `./uis/application` and produces visible output on screen
- [ ] No business logic code is duplicated — it is imported from its original location in the monorepo

---

## 📦 How to Submit

1. Make sure your working branch is named `milestone-4`
2. Run the delivery workflow defined in your `AGENTS.md` before the final commit
3. Open a Pull Request targeting the `main` branch of your fork
4. In the PR description include:
   - Screenshot of the corporate website rendered from `./uis/website`
   - Screenshot of `./uis/application` with the TypeScript script (Milestone 2) visible on screen
   - Direct link to your `AGENTS.md`
5. Submit the link to your PR on the 4Geeks campus

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
