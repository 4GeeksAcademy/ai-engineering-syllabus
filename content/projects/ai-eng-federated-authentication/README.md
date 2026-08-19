# Platform – Federated Authentication

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: read your **[COMPANY-BRIEF.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts)** and your **[CONTEXT-federated-auth.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/federated-authentication)** before writing any code — that's where your company's chosen identity provider and specific security rules live.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** — not on a new repository.

The support team has filed several **tickets** from users asking to sign in with their Google or Microsoft account instead of remembering yet another password. Your CTO is on board with the idea, but sets a security condition that isn't negotiable.

> _"I want federated login, but with one strict rule: federated sign-in can **only be used to access an account that already exists and that the user themselves explicitly linked from their profile**. I don't want anyone to be able to create a new account just by showing up with a Google login — that opens the door for anyone with access to an external email to create an identity inside our system without going through any control of ours. Linking is a deliberate act by the user, done from inside the application, not a side effect of logging in."_
>
> — CTO

Read this carefully, because it changes the flow you were probably picturing:

1. **Federated login does not create accounts.** If someone tries to sign in with an external provider and that provider isn't linked to any existing account, the system must reject it — never automatically create a new account as a result of that attempt.
2. **Linking happens in exactly one place: the profile of an already-authenticated user.** A user who signed in through the traditional method decides, from their account settings, to associate an external provider. From that point on, that provider can be used for future sign-ins.
3. **Unlinking must be just as accessible as linking**, and must never leave the user with no way to access their account.

### Complementary knowledge: why this is a security decision, not a convenience one

Letting federated login create accounts automatically seems simpler, but it hands over the decision of "who can enter my system" to an external provider you don't control. If the flow allows account creation just by showing up with a valid email, someone could register with an email that isn't verifiably theirs for your business, or impersonate a corporate email pattern if there's no explicit validation behind it. Requiring linking to happen from an already-authenticated session guarantees there's always a human with an identity your system has already verified making that decision — the external provider is never, by itself, the door in.

---

## 🌱 How to Start the Project

1. `pull` the latest changes from your fork of the monorepo.
2. Read `COMPANY-BRIEF.md` and `CONTEXT-federated-auth.md` in full before touching any code.
3. Create a new branch: `feature/federated-auth`.
4. Review the current authentication flow and existing user model before deciding how the link will be stored.
5. Diagram the two flows separately first — linking and federated login — because they share a provider but not their logic.

---

## 💻 What You Need to Do

**Data model**

- [ ] Model the relationship between a user and their linked external providers, allowing zero, one, or multiple providers per user
- [ ] Store only the necessary identifiers from the external provider — never credentials or long-lived tokens left unencrypted

**Linking flow (from the profile)**

- [ ] Implement linking of an external provider accessible only from the profile of an already-authenticated user
- [ ] Verify that the external provider being linked isn't already linked to a different account
- [ ] Confirm to the user, within the interface, that linking completed and which provider was associated
- [ ] Implement unlinking from the same place, with a warning if it's the user's only available access method

**Federated login flow**

- [ ] Implement sign-in with the external provider only for accounts that already have that provider linked
- [ ] Explicitly reject the login attempt when the external provider isn't linked to any account — with no new account created as a side effect
- [ ] Log every linking, unlinking, and rejected federated login attempt in the audit system

**Security**

- [ ] Implement the OAuth flow with `state` and `redirect_uri` validation to prevent session fixation attacks
- [ ] Ensure the session created after a successful federated login has the same expiration and revocation behavior as a traditional session

⚠️ **IMPORTANT:** the required identity provider(s) and any additional security rules for your company must match exactly what's specified in your `CONTEXT-federated-auth.md`. A generic implementation that ignores that context will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] A federated login attempt with an unlinked provider is explicitly rejected and does not create a new account, verified with a test
- [ ] Linking an external provider is only accessible from the profile of an already-authenticated session, never from the login screen
- [ ] An external provider cannot be linked to two different accounts at the same time
- [ ] Unlinking works and warns the user if it would leave them without an alternative access method
- [ ] Every linking, unlinking, and rejected federated login event is logged in an auditable way
- [ ] The OAuth flow implements `state` and `redirect_uri` validation

---

## 📦 How to Submit

Open a Pull Request from your `feature/federated-auth` branch to `main` on your fork. In the PR description, include a diagram or description of the two flows (linking and login) and evidence that a login attempt with an unlinked provider is rejected. Request sign-off from your CTO before merging.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
