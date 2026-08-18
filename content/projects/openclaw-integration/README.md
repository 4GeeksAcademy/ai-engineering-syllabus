# My 4Geeks Assistant — Teaching OpenClaw to Track Your Progress

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/openclaw-4geeks-assistant/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

<!-- endhide -->

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

---

## 🎯 Your challenge

After spending meaningful time in the course, you've come to a realization: OpenClaw is useful, but it's generic. It doesn't know anything about your course, your projects, your deadlines, or how you're actually doing. Every time you want to check your progress, you leave the agent and go look it up somewhere else — which defeats the purpose of having a personal assistant at all.

You've decided to fix that. OpenClaw should know your 4Geeks course status the same way it knows anything else you've taught it: through a skill. Specifically, it should be able to connect to your 4Geeks account using your student token and answer questions like _"What do I still have pending?"_ or _"How far along am I in the course?"_ directly from the conversation.

The way you'll build this is the same way professionals approach any agent-API integration: through conversation. You'll ask OpenClaw to help you design and create each skill, one at a time, describing what you want in plain language and letting the agent guide the implementation. No writing skills from scratch in isolation — you teach your agent what it needs to do, and it helps you make that happen.

> #### How to approach the build
>
> - Start the process by telling OpenClaw exactly what you want: _"I want to give you the ability to connect to my 4Geeks account using my student token, without me having to write any code. What do we need to do?"_
> - Let that conversation define the first skill to build. Each new question you want answered reveals the next skill.
> - Keep each skill focused on **one specific API action** — never bundle unrelated capabilities together.

The result won't just be a working integration. It will be an agent that actually knows where you stand, and that gets more useful over time as you teach it new things.

---

## 🌱 How to Start the Project

This project does not require forking a template repo. All work happens inside your OpenClaw configuration.

1. Make sure your OpenClaw instance is running and accessible.
2. Open a conversation with your agent.
3. Have your 4Geeks student token ready — you can find it in your [4Geeks account settings](https://4geeks.com).
4. Document every skill you create and every conversation that led to it in a file called `SKILL_LOG.md` — this is your deliverable.

> ⚠️ **IMPORTANT:** Your student token is a credential. Store it using OpenClaw's secure configuration mechanism — never paste it directly into a skill file or commit it to a repository.

**Student API (BreatheCode)**  
Use the endpoint map while designing skills: [Student API calls (English)](./STUDENT_API_CALLS_REFERENCE.md) · [Llamadas API (español)](./STUDENT_API_CALLS_REFERENCE.es.md).

---

## 💻 What You Need to Do

### Setup

- [ ] Confirm your OpenClaw instance is running and you can hold a conversation with it.
- [ ] Retrieve your 4Geeks student token and store it securely in your OpenClaw configuration (not hardcoded in any skill).

### Discovery conversation

- [ ] Start a conversation with OpenClaw asking it to help you connect to the 4Geeks API using your student token, without writing any code yourself.
- [ ] Document the conversation: what did OpenClaw suggest? What information did it ask for? Save a summary in `SKILL_LOG.md`.

### Core skills (minimum required)

Build each of these through conversation with OpenClaw. For each one, document: the natural language request you made, the skill OpenClaw helped you create, and a test showing it works.

- [ ] **Skill 1 — Authenticate**: OpenClaw can verify that the token is valid and the session is active.
- [ ] **Skill 2 — Get my projects**: OpenClaw can retrieve your assigned projects with their current status (pending, submitted, graded).
- [ ] **Skill 3 — Get pending work**: OpenClaw can tell you specifically what you still have to complete.
- [ ] **Skill 4 — Get my progress summary**: OpenClaw can give you an overview of how far along you are in the course.

### Extended skills (at least 2 additional)

- [ ] Identify at least 2 more things you'd want your agent to know or do from your 4Geeks account.
- [ ] Build those skills using the same conversational approach.
- [ ] Document them in `SKILL_LOG.md` following the same format.

### Skill log

- [ ] `SKILL_LOG.md` exists and documents every skill built, including:
  - The natural language prompt you used to start the conversation
  - A brief description of what the skill does and which API endpoint(s) it calls
  - A test result showing the skill works correctly

> ⚠️ **IMPORTANT:** No skill should handle more than one API concern. If a skill is doing two unrelated things, split it.

---

## ✅ What We Will Evaluate

- [ ] At least 4 core skills are implemented and functional (authenticate, get projects, get pending work, get progress summary).
- [ ] At least 2 additional skills built based on self-identified needs.
- [ ] Each skill maps to one specific API action or a tightly related set — no overly broad skills.
- [ ] The student token is stored securely and never hardcoded in any skill file or repository.
- [ ] Skills were built through conversational interaction with OpenClaw, not designed entirely outside the agent.
- [ ] `SKILL_LOG.md` documents every skill with the initiating prompt, a description of what it does, and a test result.
- [ ] Skills work correctly — OpenClaw returns accurate information from the 4Geeks API.

> Note: The quality of your `SKILL_LOG.md` is as important as the skills themselves. It demonstrates your ability to translate a real-world need into an agent capability.

---

## 📦 How to Submit

Push your `SKILL_LOG.md` to your personal GitHub repository for this project. Share the repository URL with your instructor following their submission instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/openclaw-4geeks-assistant/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
