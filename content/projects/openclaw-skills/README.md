# My Agent, My Way: Teaching Your Personal Assistant New Skills

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 The Challenge

The plumbing is done. Your OpenClaw agent is installed, your Composio connection is active — Google Docs, Google Calendar, Gmail, Google Drive, Google Tasks, GitHub, and more are all reachable — and Telegram lets you talk to it from your phone. You built this for yourself.

But right now the agent is generic. Every time you want it to do something useful, you're typing the same long instructions from scratch. It doesn't know your patterns, your style, or what "useful" even means to you specifically.

Two things will fix that. First, you'll fill in the five configuration files that define who your agent is and who it's working for — they're mostly empty right now. Second, you'll implement at least two custom skills that eliminate the most repetitive tasks in your week.

---

### The five files that make your agent yours

Inside the `.openclaw` directory you'll find five Markdown files. Together they are the agent's complete internal briefing. Right now they're mostly blank — that's the work.

| File          | What it controls                                                                                                                                 |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `IDENTITY.md` | The agent's name and symbol. What it calls itself.                                                                                               |
| `SOUL.md`     | Personality and working style. Whether it asks questions or figures things out first. How direct it is. What it values.                          |
| `AGENTS.md`   | Behavioral rules and hard limits. What the agent must never do regardless of instructions.                                                       |
| `USER.md`     | Everything about you: your name, your job, your current projects, your context. This is what the agent reads to understand who it's working for. |
| `TOOLS.md`    | Which connected services the agent may use, when to use each one, and conventions (default calendars, folders, labels, preferred channels).      |

These files aren't decoration. When you ask your agent to draft an email or plan your week, it reads these files first. A well-written `USER.md` and `SOUL.md` are the difference between an output you'd actually use and one you'd rewrite from scratch.

Fill them in as if you were briefing a real assistant on their first day. Be specific. A `SOUL.md` that says "be helpful" is useless. One that says "have opinions, be resourceful before asking, and push back when something doesn't make sense" actually shapes behavior.

---

### What tools your agent can use

Through Composio, your agent can reach any of these services:

- **Google Docs** — create, update, and read documents
- **Google Calendar** — create events, check your schedule, find free slots
- **Gmail** — read, draft, and send emails
- **Google Drive** — list, search, and organize files
- **Google Tasks** — create and manage task lists
- **GitHub** — read repos, issues, commits, and pull requests
- **Telegram** — send messages to yourself or a channel

Skills can use one or several of these together. The more connections you combine, the more powerful the result.

---

### Skill ideas — pick yours or design your own

Read through these and ask yourself: _which one would I actually trigger more than once?_ That's the one to build. You can also come up with something completely different — these are starting points.

**Skills that create new content:**

- **Daily learning log** — you tell the agent what you learned today (a few bullet points), and it formats and appends a structured entry to a Google Doc you keep as a personal knowledge journal.
- **Week plan** — given a list of goals and commitments, the agent writes a prioritized weekly plan, saves it as a new Google Doc, and creates the key events in Google Calendar.
- **Meeting notes** — you paste rough notes from a meeting; the agent formats them as decisions, action items, and open questions, then saves the result to Drive.

**Skills that sharpen existing behaviors:**

- **Smarter calendar events** — instead of asking the agent to "create an event", this skill lets you describe it in plain language ("study session Thursday afternoon, two hours, with a reminder") and handles all the details automatically.
- **Gmail drafts in your voice** — instead of asking the agent to "write an email", this skill already knows your writing style, your usual sign-off, and the kind of emails you send — the output needs minimal editing.
- **GitHub daily digest** — the agent reads your open issues and recent commits and sends you a short briefing via Telegram every time you trigger the skill.

**Skills that wire tools together:**

- **Task → Calendar** — you add tasks to Google Tasks; this skill reads the list and automatically creates time blocks in Google Calendar for any task that doesn't have one yet.
- **Inbox triage** — the agent reads your unread Gmail, identifies anything that needs action, and creates a Google Task for each one with a short description of what to do.

---

### Design before you build

Before writing any skill, create a `SKILLS_DESIGN.md` file at the root of your repo and answer these three questions for each skill you plan to implement:

1. **What does this skill do?** One sentence.
2. **What input does the agent need?** What do you give it, in what format — and what does it already know from the five configuration files?
3. **What does a good output look like?** Format, destination (a Doc, a Calendar event, a Telegram message…), and how you'll know it worked.

Commit this file before starting implementation. It is part of the deliverable and will be reviewed independently.

---

## 🌱 How to Start the Project

1. Keep working in the **same environment** where you already installed OpenClaw and finished the earlier syllabus projects (Composio, Telegram, Drive/Calendar, etc.): your VPS, local machine, or Codespace. This assignment extends that setup—you are not reinstalling OpenClaw from scratch.
2. Use your **existing Git repository** for that agent if you already have one. If your tree is missing paths this project expects (for example the five Markdown files under `.openclaw` and a place for custom skills), create or add them following your instructor’s brief and the official [OpenClaw](https://github.com/openclaw/openclaw) documentation—without relying on an external starter repository.
3. Open that workspace the way you already do (**GitHub Codespaces**, local clone, or SSH to your VPS).
4. Run `openclaw doctor` to confirm your existing setup — Composio connections and Telegram — is still healthy before touching anything.
5. Read the [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project) guide if needed.

---

## 💻 What You Need to Do

### Configure the five files

- [ ] Open `IDENTITY.md` and give your agent a name and a symbol that feel right.
- [ ] Write `SOUL.md` with enough specificity that the agent's personality is actually different from default — include how it handles uncertainty, whether it asks or acts first, and what kind of tone it uses with you.
- [ ] Set the hard limits in `AGENTS.md` — at minimum, one rule about privacy and one about when the agent should stop and ask rather than act.
- [ ] Fill in `USER.md` with your real context: name, current projects, tools you use, goals, anything the agent should always know about you.
- [ ] Fill in `TOOLS.md` with the services your agent can reach through Composio, when to use each one, and any defaults (which calendar, which Drive folder, how to sign off in Gmail, etc.).
- [ ] Run `openclaw doctor` after editing all five. Zero errors before moving on.

### Document your design

- [ ] Create `SKILLS_DESIGN.md` at the root of the repo with the three design questions answered for each skill.
- [ ] Commit it before writing any skill implementation.

### Implement your skills

- [ ] Implement at least two custom skills as proper OpenClaw skills — not raw terminal prompts.
- [ ] Each skill must visibly draw on the configuration in the five files — the output should feel different from what the agent would produce without your setup.
- [ ] At least one skill must produce verified output in a Composio-connected service (Google Docs, Google Calendar, Gmail, Google Tasks, Google Drive) or send a message via Telegram.
- [ ] Test each skill with a real, personal input — not a placeholder.

> ⚠️ **IMPORTANT:** All skills must work with your currently connected tools. Do not configure a new API, OAuth flow, or external service as part of this project — that is tomorrow's topic. Any skill requiring a new connection setup will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] All five configuration files (`IDENTITY.md`, `SOUL.md`, `AGENTS.md`, `USER.md`, `TOOLS.md`) contain specific, non-generic content.
- [ ] `openclaw doctor` runs without errors.
- [ ] `SKILLS_DESIGN.md` is committed before the implementation and answers all three design questions for each skill.
- [ ] At least two skills are implemented as proper OpenClaw skills.
- [ ] At least one skill produces verified output in a connected service (Docs, Calendar, Gmail, Tasks, Drive, or Telegram).
- [ ] No new external API or OAuth connection was configured as part of this project.
- [ ] The agent's outputs visibly reflect the configuration in the five files — tone, style, and context are consistent with what was written there.
- [ ] The student can explain the reasoning behind each skill: why that task, why that input, why that output format.

> Note: A well-reasoned `SKILLS_DESIGN.md` with a partially working implementation scores higher than a working skill with no design thinking documented.

---

## 📦 How to Submit

Push your repository to GitHub — including `SKILLS_DESIGN.md` — and share the link following your instructor's instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
