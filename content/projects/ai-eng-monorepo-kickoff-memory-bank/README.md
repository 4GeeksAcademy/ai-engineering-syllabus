# Monorepo Kickoff – Memory Bank and Project Context

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

![build by developers](https://img.shields.io/badge/build_by-Developers-blue)
![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: read your **[company BRIEFING and its documents folder](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts)** (`<company>-BRIEFING.md` and `<company>/`) before opening the agent — it is the source of the vision, departments, stakeholders, and business constraints for your implementation.

<!-- endhide -->

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

Your company has just opened its digital unit, and the monorepo is, on purpose, almost empty: folders with an assigned responsibility, no stack chosen, and a `CONTEXT.md` at the root that is still a placeholder. Before anyone writes the first feature, your CTO has opened a ticket with a clear goal: any coding agent working in this repository must understand **what** is being built, **for whom**, and **under which rules**, without anyone having to explain it again in every session.

The raw material already exists: the company BRIEFING and the documents from its departments. But a memory bank is not a copy of those documents. Dumping them whole into the context fills the agent with tokens without deciding anything. That does not mean everything must be summarized: some documents are valuable on their own — a process described step by step, a policy with its deadlines and exceptions — and processing them would only lose detail. Those documents are added as reference documentation in the monorepo's `docs/` folder, and the context points to them instead of rewriting them. **Deciding what gets synthesized and what is kept whole is your responsibility as a developer**; when in doubt, check with your team or your CTO, as you would in any company. For everything else, the work consists of **talking with the agent** about that material — in conversational or planning mode, not in agent mode — so it asks you about whatever is unclear, so you make the decisions, and so what ends up written is a curated synthesis: vision, users, acceptance criteria, and a definition of done. **Every memory bank file must cite the source document it comes from or link to the `docs/` document it relies on**, so anyone can verify it.

There is a second trap: filling gaps. Today there is no stack, no build commands, and no coding conventions. An agent without that information does not stop: it invents. That is why whatever is not yet decided **is written down as pending, along with the event that will force it to be defined**, instead of being completed with assumptions. And the final test is not that the files exist, but that **a new agent session, with no history, can find its way by reading only the repository**.

> **From:** your CTO
> **Subject:** ticket — base context for the monorepo before the first feature
>
> Before we open the first product PRD, I want the repository to have its own memory. I don't want a dump of the BRIEFING; I want what you and the agent distilled from it after discussing it. If a department document describes a process that can't be summarized without losing information, move it to `docs/` as is and reference it from the context. That decision is yours; if you're unsure, ask before inventing.
>
> On the stack, let's be clear: **no technology has been decided today, and you are not going to decide one in this ticket.** The stack document starts empty and grows with the project: every time a new technology comes in, it gets recorded there. What I do want from today is the entry policy. Only official sources verified by a person, well-known and maintained libraries, exact pinned versions — no `latest` and no open ranges — and APIs in their current version as checked in the official documentation, not in whatever the agent remembers from its training.
>
> There are other pieces every serious project needs that we can't fill in yet: architectural boundaries and patterns, coding conventions and style guide, build, test, and execution commands, anti-patterns and explicit taboos, and environment and access rules. I want them to exist from now on as reserved slots. Whatever can already be stated — for example, what each monorepo folder is responsible for, or which business constraints are non-negotiable — gets written. Whatever can't is marked as pending. Nobody invents them to make the document look complete.
>
> The acceptance criteria are the ones in the checklist. I give sign-off on the Pull Request, after I open a clean agent session myself and ask it questions about the company. If I have to explain anything to it, the ticket comes back.

### Complementary knowledge: anatomy of a project context

A **memory bank** is a set of documents versioned in the repository that persist project knowledge beyond the current chat. Its usual pieces are: **vision and acceptance criteria** (what problem the product solves, user stories, and a definition of done, in a format that can become issues or a PRD), **tech stack**, **architectural boundaries**, **coding conventions**, **commands**, **taboos**, and **environment and access rules**, plus a record of the **current status**.

The memory bank does not replace documentation: **memory** summarizes what the agent needs to get oriented and make decisions; **documentation** in `docs/` keeps the full detail of processes, policies, or procedures. Memory links to documentation so the agent reads it only when the task requires it.

The `CONTEXT.md` file at the root of the monorepo is the context entry point and the index of every document the agent needs to work: those in `memory-bank/` and those in `docs/`. It is short, contains only the essentials and, for each document, states when to read it, so the agent loads only what it needs for each task. Several small, focused files cost fewer tokens and produce less ambiguity than a single document with everything inside.

> 🔀 **PR approved → merge into `main`.** All later work in the monorepo will start from this context.

---

## 🌱 How to Start the Project

1. Work on your fork of the company monorepo. Create the branch `feature/memory-bank`.
2. Open your company BRIEFING and the documents in its folder. Read them yourself before giving them to the agent.
3. Follow the think → talk → implement pattern: discuss the material with the agent in conversational or planning mode, and switch to agent mode only once you know what is going to be written.
4. Make a separate commit for each relevant document or decision. The history is part of the delivery.

---

## 💻 What You Need to Do

### Discovery conversation

- [ ] Ask the agent to read your company BRIEFING and documents and to ask you about anything ambiguous or missing, before proposing any content.
- [ ] Answer, decide, and keep the agent's questions that changed what ended up written in the memory bank.
- [ ] Review every agent proposal against the source documents before accepting it.
- [ ] Classify each source document: it is synthesized into the memory bank or added whole to `docs/` as reference documentation. Check with your team or your CTO when the decision is not clear.

### Memory bank

- [ ] Create the `memory-bank/` folder with one file per concern, not a single document.
- [ ] Write the **product vision**: what problem the company's digital platform solves, for whom, and what is out of scope.
- [ ] Write at least five **user stories** covering at least three different departments, each with its stakeholder and verifiable acceptance criteria, and worded so it can be turned directly into a GitHub issue.
- [ ] Set a **definition of done** shared across the project.
- [ ] Create the **tech stack** document with no technology recorded, containing the CTO's entry policy (verified sources, well-known libraries, exact versions, current APIs) and a record template for each future technology: name, exact version, official source, verification date, and reason for the choice.
- [ ] Create the documents for **architectural boundaries and patterns**, **coding conventions and style**, **build, test, and execution commands**, **anti-patterns and explicit taboos**, and **environment and access rules**. In each one, write what can already be stated and mark the rest as pending, indicating which event will force it to be defined.
- [ ] Create a **current status** document that reflects where the project stands when the ticket is closed.
- [ ] State in each document the source its content comes from (company document, monorepo README, or decision made during the conversation).
- [ ] Add to `docs/` the documents you decided to keep whole, organized by topic, and link them from the memory bank file that needs them, stating when the agent should consult them.

⚠️ **IMPORTANT:** The vision, stakeholders, departments, and business constraints must match the BRIEFING of your assigned company. A generic memory bank that would work equally well for any company, or one that dumps the source documents without having decided what is synthesized and what is referenced from `docs/`, will not be accepted.

### Context entry point

- [ ] Replace the `CONTEXT.md` placeholder at the root of the monorepo. Do not paste the BRIEFING into it: it must be brief, with a description of the company in a few lines.
- [ ] Turn `CONTEXT.md` into the index of every document the agent needs: each file in `memory-bank/` and each document in `docs/`, with one line stating when it should be read.
- [ ] Include in `CONTEXT.md` the instruction to update the index and the memory bank whenever a technology comes in, documentation is added, an architecture decision is made, or the project status changes.

### Verification

- [ ] Open a new agent session with no history, tell it to start from `CONTEXT.md`, and ask it at least three questions about the company, its users, and the stack. Check that it answers from the repository and does not invent.
- [ ] In that same session, ask it to propose a library for any future need and check that it applies the stack policy (exact version and official source) instead of simply adding it.
- [ ] Fix the memory bank wherever the clean session failed and test again.

---

## ✅ What We Will Evaluate

- [ ] `CONTEXT.md` is no longer the placeholder, does not reproduce the BRIEFING, and links to each file in `memory-bank/` and `docs/`, stating when to read it.
- [ ] `memory-bank/` contains separate files for vision and acceptance criteria, stack, architecture, conventions, commands, taboos, environment and access, and current status.
- [ ] The vision and user stories reflect the assigned company and cite their source document.
- [ ] There are at least five user stories from at least three departments, each with a stakeholder and verifiable acceptance criteria.
- [ ] An explicit definition of done exists.
- [ ] The stack document records no technology and contains the entry policy and the record template with exact version and official source.
- [ ] Documents without available information mark what is pending and its trigger; they contain no invented commands, libraries, or conventions.
- [ ] The architectural boundaries capture the responsibility of each monorepo folder.
- [ ] No file in `memory-bank/` is a verbatim copy of the company documents; documents kept whole are in `docs/` and are linked from the memory bank.
- [ ] The Pull Request documents the clean-session test: questions, answers, and corrections applied.
- [ ] The commit history separates documents and decisions; there is no single commit containing all the work.

---

## 📦 How to Submit

Push your `feature/memory-bank` branch to your fork of the monorepo and open a Pull Request against the main branch.

In the Pull Request description, include:

- Three questions the agent asked you during the conversation and what they changed in the memory bank.
- The questions from the clean-session test, a summary of its answers, and what you fixed afterwards.
- Which documents you synthesized and which you added to `docs/`, with the reason for each decision and the questions you raised when you were unsure.
- The list of items left as pending and the event that will unlock each one.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
