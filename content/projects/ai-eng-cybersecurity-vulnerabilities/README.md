# Web Vulnerability Audit and Remediation (OWASP Top 10)

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/cybersecurity-analysis)** before writing any code — it reminds you which applications and services are part of your monorepo and which OWASP categories matter most for your agentic system.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

The company's applications — frontend, backend, and the agentic system — have never gone through a formal web security audit. They run on default configuration in several places: direct root access, open ports nobody remembers the reason for, and no systematic review of the most common vulnerabilities any internet-connected application is exposed to.

A security **ticket** has come in: before any of the company's applications receive more real traffic, they need to pass an audit based on the **OWASP Top 10**. Your tech lead's **brief** is clear: listing the findings isn't enough — every critical vulnerability identified must be fixed and verifiable before **sign-off**.

> **From:** Tech Lead
> **To:** Engineering Squad
>
> **Context:** Our applications have never passed a formal web security audit. We have APIs, frontends, and an agentic system running on default configuration in several places.
>
> **What I need:** Basic server hardening (SSH access, non-root user, folder permissions, firewall) and a complete audit against the OWASP Top 10, with critical vulnerabilities fixed — including the ones specific to your agentic system.
>
> **Acceptance criteria:** The server doesn't allow direct root login; a firewall exposes only the necessary ports; every OWASP Top 10 category was explicitly evaluated against your application, with a finding (applies / doesn't apply) and evidence; every vulnerability marked critical is fixed and demonstrated.

---

## 🌱 How to Start the Project

1. `git pull` your monorepo fork and create a new branch for this work: `git switch -c feature/owasp-top10-audit`.
2. Review how you currently access your server: are you using the root user for everything? which ports are exposed?
3. Get familiar with the 10 OWASP Top 10 categories before auditing — don't guess at them while reviewing code.
4. Before fixing anything, document the current state: it's your baseline for demonstrating improvement.

---

## 💻 What You Need to Do

**Server hardening**

- [ ] Create a dedicated (non-root) access user for day-to-day operational tasks.
- [ ] Restrict or disable direct SSH root login.
- [ ] Define explicit folder permissions to separate code, logs, and sensitive configuration files.
- [ ] Configure a firewall that only allows the ports strictly necessary for your application to work.

**OWASP Top 10 audit**

- [ ] Evaluate each of the 10 OWASP Top 10 categories against your backend, your frontend, and your agentic system separately.
- [ ] For each category, document whether it applies or not to your system, with concrete evidence (endpoint, file, line of code) backing your conclusion.
- [ ] Pay special attention to the categories that interact with your agentic system: broken access control (can a user invoke a tool they shouldn't?), cryptographic failures (how are your API keys stored?), and security misconfiguration (does your agent run with more permissions than it needs?).

**Remediation**

- [ ] Fix every vulnerability your audit marked as critical.
- [ ] For each fix, leave reproducible evidence (a test, a scan screenshot, or a command demonstrating the before/after).

⚠️ **IMPORTANT:** Check your `CONTEXT-company.md` to confirm which applications and services in your monorepo should be included in the audit's scope.

---

## ✅ What We Will Evaluate

- [ ] The server doesn't allow direct SSH root login.
- [ ] A dedicated non-root user exists for operational tasks, with explicit folder permissions.
- [ ] The firewall exposes only the strictly necessary ports; everything else is closed.
- [ ] All 10 OWASP Top 10 categories were explicitly evaluated, with a finding and evidence per category.
- [ ] The agentic system was audited as its own component, not assumed "already secure" because it's covered by the backend.
- [ ] Every vulnerability marked critical is fixed, with reproducible before/after evidence.

---

## 📦 How to Submit

1. Commit and push your branch.
2. Open a Pull Request to your own fork of the monorepo, including the OWASP Top 10 audit report as a markdown file inside your delivery folder.
3. In the PR description, link evidence for at least two critical fixes.
4. Request review from your tech lead before final sign-off.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
