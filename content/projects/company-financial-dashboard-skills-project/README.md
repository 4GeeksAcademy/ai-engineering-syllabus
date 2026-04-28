# Enhacing development with agent skills - Financial dashboard

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

The financial dashboard you shipped recently is working. The data loads, the charts render, the layout holds up. Your tech lead reviewed the pull request and left a comment:

> _"Good work. Before we merge, I want you to raise the bar on two fronts: accessibility and deployment best practices. I'm sharing two skills you can load directly into your coding agent — they'll guide it to make the right improvements without you having to remember every rule from scratch. Once you've applied them, explore the skills ecosystem and see what else is worth adding. Then document what you learned."_

This is how professional teams scale quality: not by memorizing every checklist, but by building reusable knowledge that can be loaded into any agent and applied consistently across any codebase.

### What is an agent skill?

An agent skill is a structured, self-contained instruction set that tells a coding agent _how_ to perform a specific task — what to look for, what patterns to apply, what to avoid, and how to verify the result. Skills are composable: you can combine several small, focused skills to get a compound improvement without writing one massive prompt.

The ecosystem at [skills.sh](https://skills.sh) hosts community-maintained skills ready to load. But the key insight is this: **a skill is only as good as how clearly it defines its objective, inputs, outputs, and acceptance criteria.** You will experience that first-hand today.

> Your tech lead has shared the following instructions:
>
> #### Accessibility (`accessibility`)
>
> Apply the `accessibility` skill to the dashboard. The goal is to ensure people using assistive technologies — screen readers, keyboard navigation, high-contrast modes — can use the product without friction. The skill will guide the agent to audit and fix the most common issues: missing `aria-label` attributes, poor focus management, missing `alt` text, and low-contrast interactive elements.
>
> #### Vercel + React Best Practices (`vercel-react-best-practices`)
>
> Apply the `vercel-react-best-practices` skill. This covers deployment-ready patterns: correct use of `next/image`, `next/font`, avoiding layout shift, proper metadata per page, and avoiding anti-patterns that hurt Lighthouse scores on Vercel deployments.
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

You will leave this session with an improved codebase _and_ a documented skill of your own — a transferable artifact you can take to any future project.

---

## 🌱 How to Start the Project

You will continue working on the **same repository** you used in the previous session. Do not fork a new repo.

1. Open your existing financial dashboard repository (your fork of [**ai-eng-financial-dashboard-context-project**](https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project)) in GitHub Codespaces or clone it locally.
2. Make sure your memory bank (`memory-bank/`) and context rules (`.cursor/rules/` or equivalent) from the previous session are committed and up to date.
3. Pull the latest changes if you are working in a team: `git pull origin main`.
4. Create a new branch for today's work: `git checkout -b feature/agent-skills`.

If you need a refresher on project setup: [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 What You Need to Do

### 1. Discover and load the provided skills

- [ ] Run `npx skills find accessibility` and review what the skill covers before applying it.
- [ ] Run `npx skills find vercel-react-best-practices` and review it.
- [ ] Load both skills into your coding agent and read through what they instruct the agent to do.

### 2. Apply the `accessibility` skill

- [ ] Use the agent with the `accessibility` skill loaded to audit the dashboard.
- [ ] Fix all `aria-label` and `role` issues flagged by the agent.
- [ ] Ensure every interactive element (buttons, links, inputs) is reachable via keyboard (`Tab` / `Enter` / `Space`).
- [ ] Add or correct `alt` text on all images and icons.
- [ ] Verify there are no color contrast issues on text and interactive elements.

### 3. Apply the `vercel-react-best-practices` skill

- [ ] Replace any standard `<img>` tags with `next/image` where appropriate.
- [ ] Ensure all pages have correct `<title>` and `<meta description>` via Next.js metadata API.
- [ ] Remove any anti-patterns flagged by the skill (e.g. layout-shift-causing styles, unoptimized font imports).
- [ ] Verify the build passes locally: `npm run build`.

### 4. Explore the ecosystem

- [ ] Run `npx skills find <topic>` for at least two topics relevant to this project (e.g. `performance`, `seo`, `forms`, `typescript`).
- [ ] Apply at least one additional skill you consider valuable for the dashboard. Justify your choice in a comment or in the memory bank.

### 5. Write your own skill

- [ ] Identify something specific to this financial dashboard that is not covered by existing skills — a pattern, a constraint, a naming convention, a data-formatting rule.
- [ ] Write a skill file for it following the structure learned in class: clear objective, defined inputs, expected output, acceptance criteria.
- [ ] Save it in the `.skills/` folder of the project and load it into the agent to verify it produces the expected guidance.

### 6. Update the memory bank

- [ ] Update `memory-bank/progress.md` (or equivalent) to reflect the skills applied, changes made, and the skill you authored.

⚠️ **IMPORTANT:** Do not rewrite the entire dashboard from scratch. The goal is _targeted improvement_ using skills — not a full rebuild. Every change must be traceable to a specific skill instruction.

---

## ✅ What We Will Evaluate

- [ ] Both `accessibility` and `vercel-react-best-practices` skills were correctly loaded and applied — improvements are visible and traceable to the skill's instructions.
- [ ] Accessibility issues are resolved: keyboard navigation works, `aria-*` attributes are correctly set, `alt` text is present, contrast passes basic checks.
- [ ] Build passes (`npm run build`) with no new warnings introduced.
- [ ] At least one additional skill was discovered via `npx skills find` and applied with a written justification.
- [ ] A custom skill file exists in `.skills/`, is well-structured (objective, inputs, outputs, acceptance criteria), and contains meaningful, project-specific guidance — not generic filler.
- [ ] Memory bank reflects the session's work accurately.
- [ ] Changes are committed on a feature branch with clear, descriptive commit messages — one skill application per commit is ideal.

> **Note:** The quality of the custom skill will be evaluated on its clarity and specificity, not on its length. A short, precise skill beats a long, vague one.

---

## 📦 How to Submit

Push your feature branch to GitHub and open a pull request against `main`. Share the pull request URL with your instructor.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
