# Give Your Agent a Memory

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/openclaw-memory/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your challenge

You have been using Openclaw for a few weeks now, building skills and wiring up integrations. It has been useful — but every time you start a new session, it forgets everything. It doesn't know your name, your ongoing projects, your preferences, or what you were working on yesterday.

You need to fix that.

Your task is to identify a **real personal need** — something you genuinely want your agent to remember or track across sessions — and then implement the right type of memory for it. Not every need requires the same solution: storing your preferred coding style is different from logging a daily work journal, which is different from letting the agent remember facts about your ongoing projects.

Before you write a single line of configuration, you should be able to answer: *What does my agent need to remember, and why is this memory type the right fit for this specific case?*

> Your agent's memory architecture should satisfy the following requirements:
>
> #### Persistent context
>
> - A `Memory.md` file that defines who you are: your name, role, working preferences, and any rules the agent must always follow.
>
> #### Episodic notes
>
> - At least one entry inside the `/memory` folder — a structured daily note or log that captures something that happened in your work session (a task completed, a decision made, a resource found).
>
> #### Smarter retrieval
>
> - QMD configured as the memory search method, replacing the default `memory_search`. Your configuration must include keyword search, semantic similarity, and reranking enabled.
>
> #### Justified architecture decision
>
> - A short written note (inside `Memory.md` or as a separate `MEMORY_DESIGN.md`) explaining why you chose this architecture for your personal use case, and what a more advanced alternative (like `mem0`) would give you that this setup does not.

Pick a scenario that is genuinely yours. Don't invent a fake use case — think about what you actually do. Here are some examples to spark ideas:

- **Course progress tracker:** The agent knows which module you are on, how many projects are pending, and which ones are done — so it can open each session by telling you whether you are on track or falling behind.
- **Daily decision log:** The agent remembers the technical decisions you made this week (why you chose one library over another, what you tried that didn't work) so you don't repeat the same research twice.
- **Reference manager:** The agent recalls links, docs, and resources you have shared with it, and can surface the relevant ones when you ask about a topic.
- **Side project context:** The agent holds the current state of a personal project — what is built, what is broken, what the next step is — without you having to re-explain it every session.

A real need produces a better implementation.

---

## 🌱 How to Start the Project

This project is built on top of your existing Openclaw setup from previous lessons. You do not need to fork a new repo — work directly in your Openclaw configuration directory.

1. Open your Openclaw workspace in your local environment or Codespace.
2. If you need a fresh start or want to review the base setup, refer to the repository you created in Week 2 Day 6.
3. Create a new branch for this project: `git switch -c feature/memory-setup`
4. Need a reminder on how to structure a coding project? [Read the guide](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 What You Need to Do

### Memory design

- [ ] Write a `MEMORY_DESIGN.md` file (or a dedicated section at the top of `Memory.md`) that:
  - [ ] Describes your personal use case in one paragraph (what you want the agent to remember and why)
  - [ ] Justifies the memory type(s) chosen for it
  - [ ] Briefly explains what `mem0` offers and why you chose to use it or not for this case

### Memory.md — persistent context

- [ ] Create or update `Memory.md` with at minimum:
  - [ ] Your name and a brief description of your working context (role, current projects)
  - [ ] At least 3 behavioral rules for the agent (e.g., preferred language, response style, things to always or never do)
  - [ ] One section of project-specific context relevant to your use case

### /memory folder — episodic notes

- [ ] Create at least 2 entries in the `/memory` folder following a consistent naming convention (e.g., `YYYY-MM-DD-topic.md`)
- [ ] Each entry must have a structured format: date, context, key facts or decisions, and any follow-up actions

### QMD configuration

- [ ] Install and configure QMD as the memory search method in Openclaw
- [ ] Verify that the three retrieval modes are active: keyword search, semantic similarity, and reranking
- [ ] Run at least one manual test query against your memory folder and document the result in your `MEMORY_DESIGN.md`

### Verification

- [ ] Start a new Openclaw session and confirm the agent correctly recalls at least two pieces of information from `Memory.md`
- [ ] Ask the agent a question that should trigger a `/memory` folder search and verify the retrieval works

⚠️ **IMPORTANT:** Do not use `mem0` as your primary memory solution in this project unless you can clearly justify why the simpler architecture is insufficient for your use case. The goal is to match the right tool to the problem — not to use the most complex option available.

---

## ✅ What We Will Evaluate

- [ ] `Memory.md` is present and contains structured, meaningful personal context (not placeholder text)
- [ ] At least 2 episodic entries exist in `/memory` with a consistent format and real content
- [ ] QMD is correctly configured and replaces the default memory search
- [ ] A manual retrieval test is documented with the query used and the result obtained
- [ ] `MEMORY_DESIGN.md` (or equivalent section) explains the use case and justifies the architecture choice with clear reasoning
- [ ] The agent correctly recalls context from `Memory.md` in a new session (demonstrated by screenshot or log)
- [ ] Branch name follows the `feature/memory-setup` convention

> Note: The quality of `mem0` integration is not evaluated. The justification for whether or not to use it is what matters.

---

## 📦 How to Submit

Push your `feature/memory-setup` branch to your GitHub repository and share the link following your instructor's instructions. Include a screenshot or a short terminal log showing the agent recalling memory in a fresh session.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/openclaw-memory/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
