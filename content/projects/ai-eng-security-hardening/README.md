# Platform – Security Hardening

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** — not on a new repository.

Before any new public-facing surface goes live, your CTO requires a security audit of what already exists. It comes to you as a blocking-priority **ticket**: nothing new gets deployed until this is resolved.

> *"I'm not going to authorize exposing more public surface until we know what vulnerabilities exist in what we've already built. I want you to audit the application the way an external attacker would, document what you find, fix it, and give me evidence that it was broken and now isn't. A checklist ticked off from memory doesn't work for me — I want real findings."*
>
> — CTO

Three requirements from the brief are worth clarifying before you start:

1. **The audit is guided, not a tool you run and walk away from.** You need to understand why each finding is a problem, not just paste a scanner's output.
2. **"Fixed" means demonstrated, not assumed.** Every vulnerability you report needs proof it existed and proof it no longer does.
3. **The scope is your own application**, not third-party infrastructure or external services you don't control.

### Complementary knowledge: the OWASP Top 10 as a starting point, not a ceiling

The OWASP Top 10 is a list of the most common, highest-impact vulnerability categories in web applications — things like broken access control, cryptographic failures, injection, security misconfiguration, or components with known vulnerabilities. It's a good starting point because it's the list any technical reviewer expects you to know, but it isn't exhaustive: an application can pass all ten categories and still have problems specific to its own business logic (for example, an endpoint that exposes more data than it should, even with authentication correctly implemented). The goal of this project is to think like an attacker about your specific application, not just check off a generic list.

---

## 🌱 How to Start the Project

1. `pull` the latest changes from your fork of the monorepo.
2. Create a new branch: `feature/security-hardening`.
3. Inventory the endpoints and flows in your application that represent the highest risk (authentication, payments if they exist, sensitive data, destructive actions).
4. Before fixing anything, document the current state — you'll need the "before" to prove the "after."

---

## 💻 What You Need to Do

**Guided audit**

- [ ] Review your application against each category of the current OWASP Top 10, documenting what applies and what doesn't for your specific system
- [ ] Identify at least three real vulnerabilities in your own application, with reproducible evidence for each (request, payload, or concrete steps)
- [ ] Document the impact of each vulnerability found: what an attacker could do if they exploited it

**Rate limiting**

- [ ] Implement rate limits on the most sensitive endpoints (login, password recovery, critical write endpoints)
- [ ] Verify the limit responds with an appropriate status code (429) and doesn't simply fail ambiguously

**Secrets management**

- [ ] Audit that no secret (API keys, credentials, tokens) is hardcoded in the source code or commit history
- [ ] Implement or verify a secret rotation mechanism, and document the procedure to rotate one without causing a service interruption

**Fix and verify**

- [ ] Fix every vulnerability found in the audit
- [ ] For each one, document "before" (vulnerable) and "after" (fixed) evidence — screenshot, log, or automated test

---

## ✅ What We Will Evaluate

- [ ] There's an audit report with at least three real vulnerabilities found in the actual application, not generic or copied ones
- [ ] Every reported vulnerability has reproducible evidence that it existed and evidence that it was fixed
- [ ] The identified sensitive endpoints have functional rate limiting, verified with a test that triggers the limit
- [ ] No secrets are exposed in the source code or commit history
- [ ] There's clear documentation of the secret rotation procedure

---

## 📦 How to Submit

Open a Pull Request from your `feature/security-hardening` branch to `main` on your fork. In the PR description, include the full audit report (findings, before/after evidence, and fixes applied). Request sign-off from your CTO before merging — this project isn't approved without reproducible evidence.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
