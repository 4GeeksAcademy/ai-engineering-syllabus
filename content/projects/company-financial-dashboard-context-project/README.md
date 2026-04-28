# Building context from an existing project - Financial dashboard

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

---

## 🎯 The Challenge

Your team receives a repository that already contains a frontend and backend implementation, but the handover is incomplete: there is very little product documentation, almost no explicit coding standards, and no reliable project memory artifact for future contributors.

Instead of rebuilding the application, your mission is to use AI as a technical collaborator to understand the repository, define engineering rules, and document operational memory so the project can be maintained safely. You are expected to work from evidence found in the codebase, not assumptions about product behavior.

The tech lead has defined a delivery sequence that must be followed exactly:

> **Required workflow**
>
> 1. Fork the repository `https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project` and prepare your local environment.
> 2. Ask your AI assistant for a project summary and validate that summary against the real repository structure and code.
> 3. Read the generated AI content and verify that it is aligned with your own understanding of the repository.
> 4. Commit each major step in a separate commit (no bundled mega-commit for the whole project).
> 5. Identify good and bad engineering practices in the codebase and turn them into explicit project rules.
> 6. Document those rules inside `.agents/rules` and iterate until the rules are applicable to the project's real workflow.
> 7. Generate a `memory-bank` folder with at least: product description, tech stack, and current project status.

Your output should read like professional repository stewardship, not like generic notes written without code inspection.

---

## 🌱 How to Start the Project

1. Fork this repository into your own GitHub account:
   - `https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project`
2. Clone your fork locally (or open it in GitHub Codespaces).

3. Validate the available services:
   - Frontend: `http://localhost:5173`
   - Backend: `http://localhost:8000`
   - API docs: `http://localhost:8000/docs`

If you need a refresher on setup and delivery basics, check [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 What You Need to Do

### Phase 1 — Understand the handover

- [ ] Fork and clone the project repository.
- [ ] Inspect the repository structure and identify key folders, services, and entry points.
- [ ] Ask your AI assistant for a summary of the project.
- [ ] Read the generated summary and verify that it matches what you understood from the real codebase.
- [ ] Validate and correct the AI summary with direct evidence from the codebase.
- [ ] Create a dedicated commit for this phase.

### Phase 2 — Analyze engineering practices

- [ ] Review the codebase and identify at least 5 good practices and 5 bad or risky practices.
- [ ] Group findings by category (architecture, naming, testing, documentation, DX, etc.).
- [ ] Define a proposed rule set that addresses detected risks and preserves useful patterns.
- [ ] Create a dedicated commit for this phase.

### Phase 3 — Implement repository rules

- [ ] Create the `.agents/rules` directory if it does not exist.
- [ ] Add rule files that reflect your proposed standards (clear naming, scope, and rationale).
- [ ] Validate each rule by testing if it can actually guide real tasks in this repository.
- [ ] Refine rules that are ambiguous, too generic, or disconnected from real project workflows.
- [ ] Create a dedicated commit for this phase.

### Phase 4 — Build project memory

- [ ] Create a `memory-bank` folder at repository root.
- [ ] Add a product overview document based on verifiable repository evidence.
- [ ] Add a tech stack document (frontend, backend, infra/tooling, and key dependencies).
- [ ] Add a current status document (implemented features, known gaps, and next priorities).
- [ ] Create a dedicated commit for this phase.

⚠️ **IMPORTANT:** Do not center your delivery on explaining the app in depth. Center it on repository understanding quality, practical governance rules, and maintainability artifacts.

⚠️ **IMPORTANT:** Every listed phase must have its own commit. If your history has one large commit for multiple phases, the project is incomplete.

---

## ✅ What We Will Evaluate

- [ ] The repository was correctly forked and worked locally with Docker.
- [ ] The AI-generated summary exists and was validated/corrected against real code evidence.
- [ ] Commit history reflects separate commits per phase.
- [ ] Good and bad practices were identified with concrete examples.
- [ ] Proposed rules are documented inside `.agents/rules` and are actionable.
- [ ] Rule validation demonstrates real applicability to this project workflow.
- [ ] `memory-bank` exists and includes product description, tech stack, and current status.
- [ ] Documentation quality is specific, structured, and tied to repository reality.

> Note: Visual redesign, feature expansion, and major refactors are not required for this project unless they are strictly necessary to validate a rule.

---

## 📦 How to Submit

Push your fork to GitHub and share:

1. Repository URL.
2. Commit history showing one commit per phase.
3. `.agents/rules` files.
4. `memory-bank` folder.

Follow any additional submission instructions from your instructor.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
