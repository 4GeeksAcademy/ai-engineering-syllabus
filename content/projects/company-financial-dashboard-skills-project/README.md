# Enhancing development with agent skills - Financial dashboard

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your challenge

You continue on the **same inherited financial dashboard** from the context project. You already left it agent-ready: a verified `memory-bank`, rules under `.agents/rules`, and a working local setup you discovered with your coding agent.

The app runs. Data loads, charts render. Your tech lead reviewed your stewardship work and left a comment:

> _"Good foundation. Before we merge the next changes, raise the bar on two fronts: accessibility and deployment best practices. I'm sharing two skills you can load directly into your coding agent — they'll guide the audit and fixes without you memorizing every rule. Once applied, explore the skills ecosystem and see what else fits this repo. Then capture one internal skill the team will reuse here — commits, deployment, testing, or something specific to this dashboard. Document what you learned."_

Professional teams scale quality this way: reusable instruction packs loaded into agents, applied consistently on inherited codebases — not checklists copied from memory.

**Stack-agnostic means your prior knowledge, not the project's stack.** This dashboard has a predefined stack — you documented it in the context project `memory-bank`. The assigned skills (`accessibility`, `vercel-react-best-practices`) match that stack. You do **not** need to already know Next.js, Vercel deployment patterns, or accessibility APIs. Load the skill, let the agent apply it, and verify outcomes in the running app and build.

The agent applies the skill; you drive, verify results against repo evidence, and reject changes that do not match what the skill and codebase support.

### What is an agent skill?

An agent skill is a structured, self-contained instruction set that tells a coding agent _how_ to perform a specific task — what to look for, what patterns to apply, what to avoid, and how to verify the result. Skills are composable: combine several small, focused skills for compound improvement without one massive prompt.

The ecosystem at [skills.sh](https://skills.sh) hosts community-maintained skills ready to load. **A skill is only as good as how clearly it defines objective, inputs, outputs, and acceptance criteria.** You will experience that today — including when you author your own.

### How you work (every phase)

1. Load the skill, then let the agent audit and propose changes — do not hand-fix from this README alone.
2. Ask the agent to cite files and explain each change before accepting it.
3. Verify outcomes in the running app and with the build/test command your `memory-bank` or repo scripts document.
4. Keep changes traceable to a skill (commit message or PR notes).
5. Update `memory-bank` when the repo's quality baseline or workflow changes.

> Your tech lead has shared the following instructions:
>
> #### Accessibility (`accessibility`)
>
> Apply the `accessibility` skill to the dashboard. Goal: people using assistive technologies — screen readers, keyboard navigation, high-contrast modes — can use the product without friction. The skill guides the agent to audit and fix common issues: missing `aria-label` attributes, poor focus management, missing `alt` text, and low-contrast interactive elements.
>
> #### Vercel + React Best Practices (`vercel-react-best-practices`)
>
> Apply the `vercel-react-best-practices` skill. Covers deployment-ready patterns: correct use of `next/image`, `next/font`, avoiding layout shift, proper metadata per page, and anti-patterns that hurt Lighthouse scores on Vercel deployments.
>
> #### Exploring the ecosystem
>
> To discover what else is available without guessing names, run:
>
> ```bash
> npx skills find <topic>
> ```
>
> For example: `npx skills find forms`, `npx skills find performance`, `npx skills find seo`. Browse what comes back and decide if any skill is worth applying to this project.

You will leave with an improved codebase, at least one additional community skill applied, and **one internal project skill** your team can reload on this repo.

---

## 🌱 How to Start the Project

Continue on the **same repository** from the context project. Do not fork a new repo.

1. Open your financial dashboard fork ([**ai-eng-financial-dashboard-context-project**](https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project)) in your coding agent.
2. Confirm `memory-bank/` and `.agents/rules` from the context project are committed and current.
3. Ask the agent to confirm how to run the app and which build command validates the frontend — use repo evidence, not assumptions.
4. Pull latest if working in a team: `git pull origin main`.
5. Create a branch: `git switch -c feature/agent-skills`.

If you need a refresher: [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 What You Need to Do

### 1. Discover and load the provided skills

- [ ] Run `npx skills find accessibility` and review what the skill covers before applying it.
- [ ] Run `npx skills find vercel-react-best-practices` and review it.
- [ ] Load both skills into your coding agent and read what they instruct the agent to do.

### 2. Apply the `accessibility` skill (agent-led, you verify)

- [ ] With the skill loaded, ask the agent to audit the dashboard and propose fixes.
- [ ] Review each proposal; accept only changes you can tie to a real file and skill instruction.
- [ ] Verify outcomes: keyboard reachability on interactive elements, correct `aria-*` / `role` where needed, `alt` text on images/icons, basic contrast on text and controls.
- [ ] Commit with a message that references the `accessibility` skill.

### 3. Apply the `vercel-react-best-practices` skill (agent-led, you verify)

- [ ] With the skill loaded, ask the agent to audit deployment-oriented frontend patterns and apply fixes.
- [ ] Review proposals against the skill — e.g. `next/image` where appropriate, page metadata, layout-shift and font anti-patterns the skill flags.
- [ ] Run the frontend build command documented in this repo; confirm it passes without new unjustified warnings.
- [ ] Commit with a message that references the `vercel-react-best-practices` skill.

### 4. Explore the ecosystem

- [ ] Run `npx skills find <topic>` for at least two topics relevant to this project (e.g. `performance`, `seo`, `forms`, `typescript`, `testing`).
- [ ] Apply at least one additional skill you consider valuable. Justify the choice in the memory bank or PR notes.

### 5. Write an internal project skill

- [ ] With the agent, identify a gap **specific to this inherited repo** that community skills do not cover well — e.g. commit message conventions, deployment steps for this dashboard, testing/QA checks before merge, data-formatting rules, API usage patterns, or dashboard-specific UI conventions discovered in the codebase.
- [ ] Have the agent draft a skill file; you refine it to class structure: clear objective, defined inputs, expected output, acceptance criteria.
- [ ] Save it under `.skills/` and load it into the agent to verify it produces actionable guidance for a real task on this repo.

### 6. Update the memory bank

- [ ] Update `memory-bank/progress.md` (or equivalent) with: skills applied, verified changes, ecosystem skill chosen (and why), and the internal skill you authored.

⚠️ **IMPORTANT:** Do not rewrite the dashboard from scratch. Targeted improvement via skills — every change traceable to a skill instruction. You verify; the agent implements.

---

## ✅ What We Will Evaluate

- [ ] Both `accessibility` and `vercel-react-best-practices` skills were loaded and applied — improvements visible and traceable to skill instructions.
- [ ] Accessibility outcomes verified: keyboard navigation works, `aria-*` attributes correct where needed, `alt` text present, contrast passes basic checks.
- [ ] Frontend build passes using this repo's documented command, without new unjustified warnings.
- [ ] At least one additional skill discovered via `npx skills find` and applied with written justification.
- [ ] An internal skill exists in `.skills/`, well-structured (objective, inputs, outputs, acceptance criteria), with meaningful **project-specific** guidance — commits, deployment, testing/QA, or another repo-derived topic; not generic filler.
- [ ] Memory bank reflects the session accurately.
- [ ] Changes on `feature/agent-skills` with clear commits — one skill application per commit is ideal.
- [ ] Work reads as agent-driven improvement on an inherited codebase that you verified — not unchecked bulk edits.

> **Note:** Custom skill quality is judged on clarity and specificity, not length. A short, precise skill beats a long, vague one.

---

## 📦 How to Submit

Push your feature branch to GitHub and open a pull request against `main`. Share the pull request URL with your instructor.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
