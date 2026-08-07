# Secure Practices for AI Integration in Systems

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/cybersecurity-analysis)** before writing any code — it defines the applicable regulatory framework, company data, and the specific constraints for your implementation.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

You've already built agents that classify, respond to, and escalate requests; given them memory; connected them to external tools through MCP; and exposed real-time updates to the dashboard. All of that works — but nobody has verified yet whether it's safe to run in production. Your compliance lead has opened a **ticket** requesting a formal audit before the system keeps growing.

The **brief** is direct: this isn't just about "it works," it's about proving that every component touching a language model — endpoints, agents, third-party integrations — follows security-by-design principles and can hold up against a recognized reference framework. Your tech lead was just as specific in the **handoff**: the deliverable isn't only a report, it's also the remediation of at least the most critical gaps that report identifies.

> **From:** Compliance Lead
> **To:** AI Engineering Team
>
> **Context:** Our AI systems have grown fast — agents, RAG, MCP, workflows with human approval — but we've never done a formal, system-wide security review. Before we keep scaling, we need to know where we stand.
>
> **What I need:** An inventory of all of the company's AI systems, a report structured around the NIST checklist (Govern, Identify, Protect, Detect, Respond, Recover) with a prioritized improvement roadmap, and implementation of the most urgent protections — especially against prompt injection and secrets handling.
>
> **Acceptance criteria:** The report covers all six NIST functions with at least one concrete action per function; the AI systems inventory is complete with an assigned owner per component; the implemented protections can be demonstrated with a reproducible test case.

### 📎 Complementary Knowledge: the NIST Framework

NIST organizes cybersecurity management into six functions: **Govern** (policy and accountability), **Identify** (inventory and risk assessment), **Protect** (preventive controls), **Detect** (monitoring and alerts), **Respond** (incident plan), and **Recover** (service restoration). You don't need to implement all six at enterprise scale — you need to map your current system against each function and prioritize what's missing. It's the same logic as a quality checklist, applied to security.

---

## 🌱 How to Start the Project

1. `git pull` your monorepo fork and create a new branch for this work: `git switch -c feature/nist-security-practices`.
2. Read your `CONTEXT-company.md` to identify the regulatory framework that applies to your company and the AI systems you've already built in prior milestones.
3. Review `.env.example` and confirm how credentials and API keys are currently managed.
4. Before touching any code, sketch or list (in your own report's README) every point where a language model receives external input — from a user, from a document in your semantic knowledge base, or from an MCP tool.

---

## 💻 What You Need to Do

**Inventory and governance**

- [ ] Document a complete inventory of the company's AI systems built so far (agents, RAG, MCP, workflows), with an assigned owner per component.
- [ ] For each component, identify who is responsible for the control when the model or tool is provided by a third party.

⚠️ **IMPORTANT:** The applicable regulatory framework (which regulation governs, what notification deadlines apply, which data is restricted) depends on your CONTEXT.md. A generic report that ignores your company's context will not be accepted.

**Security by design (backend and agents)**

- [ ] Verify and fix credential handling: no API key or secret should be hardcoded in the code; everything must come from environment variables or a vault.
- [ ] Implement explicit validation and sanitization of any user input before it reaches the model.
- [ ] Clearly separate system instructions from user content in your prompts, so user content can never override the instructions.
- [ ] If any agent reads external content (documents from your knowledge base, results from MCP tools), document and mitigate the risk of indirect prompt injection.
- [ ] If any component generates code, SQL, or tool calls, add a validation layer for that output before it's executed.
- [ ] Implement rate limiting on at least one endpoint that triggers model calls, to prevent uncontrolled cost loops.
- [ ] Add logging and traceability of what action each agent took and why, for at least one existing agentic flow.
- [ ] Confirm that irreversible actions (deleting data, sending communications, approving processes) require explicit human confirmation.

⚠️ **IMPORTANT:** Your company's specific values — what counts as an irreversible action, which data is sensitive, what response SLA applies to an incident — are defined in your CONTEXT.md.

**NIST report**

- [ ] Write the report covering all six NIST functions (Govern, Identify, Protect, Detect, Respond, Recover), with at least one concrete, prioritized action per function.
- [ ] For each identified gap you didn't fix in this cycle, document the risk and the proposed mitigation.

---

## ✅ What We Will Evaluate

- [ ] The AI systems inventory lists every component built so far, with an assigned owner.
- [ ] No API keys or credentials are hardcoded anywhere in the code; all come from environment variables or a vault.
- [ ] There is at least one reproducible test case demonstrating a prompt injection attempt being blocked or neutralized.
- [ ] At least one endpoint that invokes a model has verifiable rate limiting implemented.
- [ ] There is verifiable logging of at least one agent's decisions and actions.
- [ ] Identified irreversible actions require human confirmation before executing.
- [ ] The NIST report covers all six functions with at least one concrete action per function.
- [ ] The report explicitly references your CONTEXT.md's regulatory framework, not generic regulation.

---

## 📦 How to Submit

1. Commit and push your branch.
2. Open a Pull Request to your own fork of the monorepo, including the NIST report as a markdown file inside your delivery folder.
3. In the PR description, link the prompt injection test case and briefly explain which gaps remain open and why.
4. Request review from your tech lead before final sign-off.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
