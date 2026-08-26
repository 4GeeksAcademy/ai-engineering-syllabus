# Building context from an existing project - Financial dashboard

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones estan [disponibles en español](./README.es.md)._

<!-- endhide -->

---

## 🎯 Your challenge

Your team inherits a repository that already has a frontend and a backend. The handover is incomplete: almost no product docs, no explicit coding standards, and no project memory for the next person (or the next coding agent) who opens the repo.

You do **not** need prior knowledge of the stack. In AI Engineering you often join unfamiliar codebases. The coding agent is your primary investigator. You drive it: ask what the app does, how pieces connect, how to run it, and what unfamiliar files are for. Every answer must be checked against real files — reject guesses and hallucinations.

Your mission is not to rebuild the product. Your mission is to leave the repo **agent-ready**: validated understanding, actionable rules the agent will follow later, and a `memory-bank` grounded in evidence.

### How you work (every phase)

1. Ask the coding agent first.
2. Demand file/path evidence for important claims.
3. Reject invented ports, frameworks, or APIs.
4. Commit agent-produced artifacts only after you verified them.
5. Keep a short verification trail (wrong claim → correction) in the commit message, PR notes, or a small `verification.md`.

### What not to do

- Do not invent best practices from memory or taste — derive them from the codebase with the agent.
- Do not paste this README as the only prompt and ship whatever comes back unchecked.
- Do not center the delivery on a long product essay. Center it on verified context, rules that steer real tasks, and maintainable memory.

> **Required workflow**
>
> 1. Fork `https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project` and open it in your coding agent.
> 2. Ask the agent how to run the project and which services exist. Start only what the repo evidence supports (Docker Compose, scripts, READMEs, config). Confirm URLs and ports from that evidence — do not assume fixed localhost ports.
> 3. Ask for a project summary. Mark each major claim: ✅ verified in code / ❌ wrong / ❓ unverified. Correct wrong claims with the agent.
> 4. One commit per major phase (no mega-commit for the whole project).
> 5. Ask the agent what conventions already exist and what risks would hurt future agent edits. Turn those findings into proposed rules — each rule must map to at least one concrete repo fact.
> 6. Have the agent draft rule files under `.agents/rules`. Test them: give the agent a small real task and check whether the rules actually steer the work. Iterate until they do.
> 7. Have the agent draft a `memory-bank` covering at least product description, tech stack, and current status. Verify before committing.

Delivery should read like professional repository stewardship driven by agent collaboration — not generic notes without code inspection.

---

## 🌱 How to Start the Project

1. Fork this repository into your own GitHub account:
   - `https://github.com/4GeeksAcademy/ai-eng-financial-dashboard-context-project`
2. Clone your fork locally (or open it in GitHub Codespaces).
3. Open the project in your coding agent and ask it how to bring services up and how to confirm they are healthy. Follow repo evidence (compose files, Dockerfiles, package scripts, docs).

If you need a refresher on setup and delivery basics, check [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

> **Tip:** You may hit environment errors (permissions, mounts, missing tools). Paste the exact error into the agent and ask for a step-by-step fix grounded in this repo.

---

## 💻 What You Need to Do

### Phase 1 — Understand the handover (with the agent)

- [ ] Fork and clone the project repository.
- [ ] Ask the agent to map structure, services, and entry points — then spot-check key paths yourself.
- [ ] Ask for a project summary (what it does, how pieces connect, how to run it).
- [ ] Verify the summary against the real codebase; mark ✅ / ❌ / ❓ and correct mismatches with the agent.
- [ ] Record a short verification trail (commit message, PR notes, or `verification.md`).
- [ ] Create a dedicated commit for this phase.

### Phase 2 — Derive engineering findings (with the agent)

- [ ] Ask the agent to surface useful conventions and risky patterns that would affect future contributors or agents.
- [ ] Keep only findings tied to concrete files, folders, or behaviors — drop vague statements.
- [ ] Group surviving findings by category (architecture, naming, testing, documentation, DX, etc.).
- [ ] Turn findings into a proposed rule set: each rule cites at least one repo fact.
- [ ] Create a dedicated commit for this phase (analysis / proposed rules notes are fine here).

### Phase 3 — Implement and test repository rules

- [ ] Create `.agents/rules` if it does not exist.
- [ ] Have the agent draft rule files (clear naming, scope, rationale, and project-specific guidance).
- [ ] Validate each rule with a small real task in this repo (docs change, commit hygiene, frontend tweak, backend route change — whatever fits). Refine with the agent until guidance is actionable.
- [ ] Create a dedicated commit for this phase.

### Phase 4 — Build project memory

- [ ] Create a `memory-bank` folder at repository root (filenames may follow agent/repo convention).
- [ ] Ensure it covers, at minimum:
  - Product overview grounded in verifiable evidence
  - Tech stack (languages, frameworks, infra/tooling, key dependencies)
  - Current status (what works, known gaps, next priorities)
- [ ] Reject unsupported product claims or invented roadmaps.
- [ ] Create a dedicated commit for this phase.

⚠️ **IMPORTANT:** Every listed phase must have its own commit. One large commit for multiple phases = incomplete.

---

## ✅ What We Will Evaluate

- [ ] Repo forked and runnable using the setup the agent discovered from project evidence.
- [ ] AI-generated summary exists and was verified/corrected against real code (verification trail present).
- [ ] Commit history shows separate commits per phase.
- [ ] Engineering findings cite concrete evidence; proposed rules map to those findings.
- [ ] `.agents/rules` contains actionable, project-specific rules (not generic slogans).
- [ ] Rule validation shows they steer a real task in this repository.
- [ ] `memory-bank` covers product, stack, and current status, tied to repository reality.
- [ ] Artifacts look like agent-assisted stewardship you verified — not unchecked paste or personal preference lists.

> Note: Visual redesign, feature expansion, and major refactors are not required unless strictly needed to validate a rule.

---

## 📦 How to Submit

Push your fork to GitHub and share:

1. Repository URL.
2. Commit history showing one commit per phase.
3. `.agents/rules` files.
4. `memory-bank` folder.
5. Verification trail (in commits, PR notes, or `verification.md`).

Follow any additional submission instructions from your instructor.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
