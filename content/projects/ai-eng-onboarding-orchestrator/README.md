# Agentic Engineering – Onboarding Agent

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: read your **[company BRIEFING](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/onboarding-orchestrator)** before writing any code. It defines the stages of corporate onboarding, the content every new hire must learn, the documents and access to be handled, and who approves each stage.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)**, not on a new repository.

The People team reaches out with a problem that repeats with every new hire to the corporate team. The person arrives, receives a long document, a list of links, and a couple of meetings, and from there they figure things out on their own. Nobody knows for sure whether they understand how the company operates, what's expected of their role, or what the internal guidelines are — and the paperwork (documents, system access, signatures) gets lost between emails.

> _"I want every new hire to walk the same path, at their own pace, without me having to chase them. I want them to learn about the company, how we operate, what's expected of their role, and how we work here — and not move on to the next stage until they've shown they understood the previous one. If they have questions, those should be answered from our official documentation, not with made-up answers. And some stages can only be closed by their direct manager. That's not a decision for the machine."_
>
> — Head of People

The brief leaves four requirements implicit, and they define the architecture:

1. **The process takes days or weeks, not minutes.** The agent has to persist its state and resume exactly where it left off, even if the service restarts between one stage and the next.
2. **Moving forward requires proving understanding.** Every content stage ends with a check. Having "opened the document" is not the same as having understood it.
3. **Answers come from official material, or they don't come at all.** If a question isn't covered by the company's documentation, the agent says so and routes it to a person. It never fills the gap with a guess.
4. **Some decisions don't belong to the agent.** The direct manager's approvals are real stopping points in the flow: the agent pauses, waits, and only continues when a person with the right permission decides.

### Complementary knowledge: why one stateful agent, and not several

It's tempting to split onboarding across several specialized agents (one for content, one for paperwork, one for questions). But onboarding is a **sequential, long-running process with a single thread of responsibility**: at any given moment there's exactly one next thing to do for that person, and the hard part isn't reasoning in parallel — it's not losing state. A single agent with an explicit stage graph, a persistence mechanism (checkpointer), and a lookup tool over the official documentation solves that in a way that is simpler, easier to debug, and cheaper than coordinating several agents. Choosing the simplest architecture that solves the problem is an engineering decision you must be able to defend.

---

## 🌱 How to Start the Project

1. `pull` the latest changes from your fork of the monorepo.
2. Read your company briefing in full before touching any code.
3. Create a new branch: `feature/onboarding-orchestrator`.
4. Draw the process as a state graph before coding: stages, entry and exit conditions for each, comprehension checks, human approval points, and deadlines.
5. Gather and organize the official onboarding material the briefing describes. It will be the agent's single source of truth.
6. Decide which tools the agent needs and which it must **not** have. Start with the shortest possible list.

---

## 💻 What You Need to Do

**Flow design**

- [ ] Model your company's corporate onboarding as an explicit graph of stages, with a verifiable exit condition for each one
- [ ] Include, at minimum, stages covering the company, its operations, the role's functions, ways of working, and internal guidelines
- [ ] Include the administrative stages the briefing specifies (documents, system access, signatures)
- [ ] Mark the points in the graph that require human approval and who can grant it
- [ ] Define the expected deadline for each stage according to the briefing

**Content and comprehension checks**

- [ ] Index the official onboarding material so the agent can query it
- [ ] Present each stage's content adapted to the new hire's role
- [ ] Close each content stage with a comprehension check; if it isn't passed, the agent reinforces the content and repeats the check
- [ ] Answer the person's questions using only the official material, citing the source
- [ ] When a question isn't covered by the material, the agent explicitly acknowledges it and routes it to a person on the team

**Agent and state**

- [ ] Implement the orchestrator as a single agent using an agent framework (e.g., LangGraph)
- [ ] Persist each onboarding's state with a checkpointer, so the process survives a service restart
- [ ] Allow several onboardings to progress in parallel, each with its own isolated state
- [ ] Run the agent outside the request-response cycle, as a background task

**Human approvals**

- [ ] Implement approval points as real interruptions of the flow: the agent stops and doesn't proceed until it receives the decision
- [ ] Verify that the approver has the right role and department to approve
- [ ] Handle rejection: the flow must know what to do if an approval is denied

**Follow-up and escalation**

- [ ] Send reminders to the new hire when a pending stage approaches its deadline
- [ ] Escalate to their direct manager when a stage goes past its deadline
- [ ] Build a view for the People team: which onboardings are active, which stage each one is at, and which are blocked
- [ ] Give the new hire a view of their own progress and what they still have left

**Security and traceability**

- [ ] The agent operates with its own identity and narrower permissions than any person on the team
- [ ] Log every agent action, identifying it as an action by an automated process, not a person
- [ ] Identify in the briefing which data about the new hire is sensitive, and demonstrate that it never appears in logs, stored prompts, or outgoing messages

⚠️ **IMPORTANT:** the stages, content, documents, approvers, and deadlines must match exactly what's specified in your company briefing. A generic flow that ignores that context will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] The process is modeled as an explicit graph covering the company, operations, role functions, ways of working, guidelines, and administrative steps
- [ ] A test demonstrates that if the service restarts mid-onboarding, the agent resumes exactly at the stage it was in
- [ ] No content stage is marked as complete without passing its comprehension check
- [ ] Answers to questions cite the official material, and a question outside that material is acknowledged and routed instead of answered with an invented response
- [ ] The agent doesn't move past an approval point without a human decision, and only accepts one from someone with the right permission
- [ ] An overdue stage triggers escalation to the direct manager
- [ ] Agent actions are logged as actions by an automated process
- [ ] The new hire's sensitive data doesn't appear in logs, stored prompts, or outgoing messages
- [ ] The choice of a single-agent architecture is justified in writing

---

## 📦 How to Submit

Open a Pull Request from your `feature/onboarding-orchestrator` branch to `main` on your fork. In the PR description, include the stage graph diagram, the justification for the single-agent architecture, evidence of the resume-after-restart test, and an example of a question outside the official material that was correctly routed. Request sign-off from the People team before merging.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
