---
title: "How projects are structured"
description: "Learn to read any project in the course: what each README section means (your challenge, how to start, what you need to do, what we will evaluate, how to submit) and how to use them with your coding agent in the Ask → Plan → Agent phases."
author: "@ehiber"
tags: ["AI Engineering", "Projects", "Coding Agents", "Getting Started"]
---

# How projects are structured

<!-- hide -->

_Estas instrucciones también están disponibles en [español](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/lessons/how-projects-are-structured/how-projects-are-structured.es.md)._

<!-- endhide -->

You open your first project and find a long README: a challenge, a list of steps, another list of tasks with checkboxes, a list of things that will be evaluated, and submission instructions. It is easy to feel that everything weighs the same and that you have to understand all of it before writing a single line. Or the opposite: paste the whole README into the coding agent and hope something comes out.

Neither works. Each README section has a **different purpose** and deserves a **different level of attention**. This lesson teaches you to read them that way, so you put your energy where the learning is: **understanding the problem and building a solution**.

## What you will achieve

- Recognize the five sections every project has and know what each one is for.
- Tell apart what you need to **think through** (the challenge and the evaluation) from what you just need to **follow** (how to start and how to submit).
- Use each section at the right moment of your work with your coding agent: **Ask → Plan → Agent**.

## The core idea: a project is a trip

Think of every project as a road trip. There is a starting point, a destination, a suggested route, and a place where you park the car at the end. But the most important part is knowing **why** you are traveling and **where** you want to arrive.

```mermaid
flowchart LR
  start["🌱 How to start<br/>(starting point)"]
  challenge["🎯 Your challenge<br/>(why you travel)"]
  todo["💻 What you need to do<br/>(suggested route)"]
  eval["✅ What we will evaluate<br/>(the destination)"]
  submit["📦 How to submit<br/>(park the car)"]
  start --> challenge
  challenge --> todo
  todo --> eval
  eval --> submit
```

In the README, **Your challenge** appears before **How to start**, because first you need to know what the project is about. In practice you read both almost at the same time: you set up the environment while you understand the problem.

## The five sections, one by one

### 🎯 Your challenge: understand the problem and start from here

This is the most important section of the project. It tells you **what problem exists, for whom, and why it matters**. Sometimes it comes as a story (an artist friend needs a website), sometimes as a ticket or a brief from your tech lead, and it almost always includes constraints: things you *cannot* do, or rules your solution must respect.

Many challenges also include **📚 Complementary Knowledge** blocks. They explain the concept you need to solve the problem (a state machine, what an ORM is, the N+1 problem…). They are not optional reading: they are the minimum theory you need to understand what you are going to build.

How to read it:

- Read it **slowly and more than once**. Underline the verbs ("must", "cannot", "always", "never"): that is where the rules are.
- Try to explain the problem in your own words in two or three sentences. If you cannot, you have not understood it yet.
- Write down what you do not understand. Those doubts are your first questions for your agent or your mentor.

> 💡 If you only spend quality time on one section, make it this one. A coding agent can write code for you, but it cannot understand the problem for you.

### 🌱 How to start: follow the steps

This section tells you which repository to open, whether to fork it or use a template, whether to open it in Codespaces, which dependencies to install, and which file to read first.

You **do not interpret this section, you follow it**. It is written so you can get going without having to make decisions. If a step fails or you do not understand it, do not get stuck looking for the "perfect" way to start: **ask** your mentor, your classmates, or your agent, and keep moving.

> ⚠️ Getting stuck on "how do I start" is one of the most common ways to lose an entire day. The start is already solved for you: use it.

### 💻 What you need to do: a route, not the only one

This is a task list, often with checkboxes, file names, endpoints, or specific functions. It looks like the most "real" part of the project, but take it **with a grain of salt**.

Think of it as the route Google Maps suggests: a good reference and usually the most direct path, but **not the only possible one**. Also, most of these tasks will be carried out by your **coding agent**, not by you typing line by line.

How to use it:

- Use it to understand **which pieces** the solution will have and how they relate to each other.
- Give it to the agent as **context** during the planning phase, not as an order to execute blindly.
- If the agent proposes a different path that also reaches the destination (see the next section), that is fine, as long as **you can explain why** it works.

### ✅ What we will evaluate: the destination

This list is **the destination of the trip**. It is what your submission is reviewed against, so it is your personal checklist before you submit.

How to use it:

- Read it **at the beginning**, right after the challenge. Knowing where you are going changes how you plan.
- While you work, compare every step forward with this list: does this get me closer to any item?
- Before submitting, go through it item by item and verify your project **meets** each one. "I think so" is not enough: open it, run it, check it.

> 💡 A good exercise is to ask the agent, in Ask mode, to review your project against this list and tell you what is missing. But the final call on whether each item is met is yours.

### 📦 How to submit: follow the steps

Like **How to start**, this section is a set of steps you follow without much questioning: commit and push, open a Pull Request, make sure `.env` is not uploaded, add a screenshot, submit the URL on the platform…

You can always ask when you need to, but do not turn submission into a new problem. It is the finish line.

### Where to put your energy

| Section | What it is | How to treat it |
| --- | --- | --- |
| 🎯 Your challenge | The problem | **Think it through** |
| 🌱 How to start | The starting point | Follow the steps |
| 💻 What you need to do | A suggested route | Use it as a reference |
| ✅ What we will evaluate | The destination | **Check your work against it** |
| 📦 How to submit | The finish line | Follow the steps |

How to start and how to submit are the **beginning and the end**. What sits in between (understanding the problem and building the solution) is where you actually learn.

## Working the project with your agent: Ask → Plan → Agent

During the course you work with a coding agent in three phases. Each README section fits into one of them:

```mermaid
flowchart LR
  ask["Ask<br/>Understand"]
  plan["Plan<br/>Design the route"]
  agent["Agent<br/>Build"]
  check["Check against<br/>✅ What we will evaluate"]
  ask --> plan
  plan --> agent
  agent --> check
  check -->|something missing| plan
```

1. **Ask (understand).** Here you work with **🎯 Your challenge** and **✅ What we will evaluate**. Ask the agent about whatever you do not understand: concepts, constraints, new terms. No code is written yet. The goal is for *you* to understand the problem.
2. **Plan (design the route).** Now **💻 What you need to do** comes in. Ask the agent for a plan that solves the challenge and meets the evaluation, using the task list as a reference. Read the plan, question it, and adjust it. If you do not understand a step in the plan, go back to Ask.
3. **Agent (build).** With the plan approved, let the agent implement it. Your job is to review what it does, run it, and check that it makes sense.
4. **Check.** Compare the result with **✅ What we will evaluate**. If something is missing, plan that part again.

**🌱 How to start** happens before this cycle and **📦 How to submit** happens after it. They do not need a plan: they are the entry and exit steps.

## A practical way to read any project

When you open a new project, try this order:

1. Read **🎯 Your challenge** in full, including the complementary knowledge blocks.
2. Read **✅ What we will evaluate** so you know where you need to arrive.
3. Follow **🌱 How to start** until your environment is ready.
4. Skim **💻 What you need to do** to get an idea of the pieces.
5. Work with your agent through **Ask → Plan → Agent**.
6. Check your work against **✅ What we will evaluate**.
7. Follow **📦 How to submit**.

## Checklist before starting any project

- [ ] I read **🎯 Your challenge** in full and can explain the problem in my own words.
- [ ] I read the **📚 Complementary Knowledge** blocks.
- [ ] I read **✅ What we will evaluate** and know what the destination is.
- [ ] I followed **🌱 How to start** and my environment works (or I already asked about what did not).
- [ ] I started with the agent in **Ask**, not directly in **Agent**.

## Conclusion

Projects are not task lists to tick off: they are **problems to solve**. The README structure is designed to take the unimportant work off your plate (how to start and how to submit are already solved) so you can focus on what matters: **understanding the challenge, knowing the destination, and building a solution with your agent** that you can explain.

Start by following the steps. Understand the problem. Plan the route. Build. Check that you arrived. Submit.
