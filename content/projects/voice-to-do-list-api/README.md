# Voice Command API — Talk to Your Task List

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

A small productivity startup has built a voice-first interface that lets users manage their to-do lists entirely by speaking. The frontend is already done — it runs in the browser, captures the user's voice through the microphone, and transcribes it to text using the Web Speech API. Your job is to build the backend that makes that interface actually do something.

The frontend sends every transcription to a single entry-point endpoint: `POST /instruction`. From there, your API must figure out what the user asked for, route the request to the right internal endpoint, and return a response the frontend can display.

The team's tech lead left you the following note before going on vacation:

> #### Backend spec — Voice Command API
>
> **Entry point**
>
> - `POST /instruction` — receives a plain-text transcription and calls the Groq API to extract intent and parameters. Must return a JSON that identifies which endpoint to call and with what arguments. The frontend will use this response to make the follow-up request.
>
> **Task endpoints (in-memory storage only — no database)**
>
> - `GET /tasks` — returns the full list of tasks
> - `POST /tasks` — creates a new task (requires `title`, optional `done` field, defaults to `false`)
> - `PUT /tasks/<int:task_id>` — replaces a task entirely
> - `PATCH /tasks/<int:task_id>` — marks a task as done or updates the title
> - `DELETE /tasks/<int:task_id>` — deletes a task by ID
>
> **Storage**
> Use a module-level list as your data store. Each task is a dict with `id`, `title`, and `done`. No database, no file system.
>
> **Groq integration**
> Use the Groq API (model: `llama3-8b-8192` or similar) from your `/instruction` endpoint. The system prompt must instruct the LLM to respond **only** with a JSON object in this exact format:
>
> ```json
> {
>   "endpoint": "/tasks",
>   "method": "POST",
>   "params": { "title": "Buy groceries" }
> }
> ```
>
> The LLM must never return free text — only that JSON. Your prompt engineering is what makes this work.

The startup's PM wants to see the full voice-to-action flow working end to end: a user says "add buy groceries to my list", and the task appears. That's your goal.

---

## 🌱 How to Start the Project

This project includes a ready-to-use frontend template. Fork the repository and open it in your preferred environment:

```
https://github.com/4GeeksAcademy/voice-command-api
```

**Option A — GitHub Codespaces (recommended):**

1. Open the repo and click **Code → Codespaces → Create codespace on main**
2. Wait for the environment to load

**Option B — Local clone:**

```bash
git clone https://github.com/4GeeksAcademy/voice-command-api
cd voice-command-api
```

The repository contains:

- `/frontend` — the pre-built voice interface (do not modify)
- `/src` — your FastAPI backend goes here

Create your own GitHub repository, push your code there, and update the remote URL:

```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO
```

For additional setup guidance: [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 What You Need to Do

### Setup

- [ ] Create a virtual environment and install FastAPI, Uvicorn, and the Groq Python SDK
- [ ] Store your Groq API key in a `.env` file — never commit it to the repository
- [ ] Configure CORS so the frontend can communicate with your API

### In-memory storage

- [ ] Declare a module-level list called `tasks` to serve as your data store
- [ ] Each task must have `id` (integer), `title` (string), and `done` (boolean, default `false`)

### Task endpoints

- [ ] `GET /tasks` — returns all tasks as a JSON array
- [ ] `POST /tasks` — creates a task from the request body and appends it to the list; returns the created task with its assigned ID
- [ ] `PUT /tasks/<task_id>` — replaces the full task object for the given ID
- [ ] `PATCH /tasks/<task_id>` — partially updates a task (title and/or done status)
- [ ] `DELETE /tasks/<task_id>` — removes the task with the given ID; returns a confirmation message

### Instruction endpoint

- [ ] `POST /instruction` — receives a JSON body with a `transcription` field (plain text)
- [ ] Calls the Groq API with an appropriate system prompt that forces the LLM to respond only with a structured JSON object indicating `endpoint`, `method`, and `params`
- [ ] Returns that JSON directly to the frontend

### End-to-end wiring

- [ ] Using the response from `/instruction`, the frontend calls the correct task endpoint automatically — verify this works for at least: create, list, update, and delete actions spoken aloud

⚠️ **IMPORTANT:** Do not use a database. All data must live in a Python list in memory. The list resets every time the server restarts — that is expected behavior for this project.

⚠️ **IMPORTANT:** The `/instruction` endpoint must not contain hardcoded intent-matching logic (no `if "add" in text`). All routing decisions must come from the LLM response.

---

## ✅ What We Will Evaluate

- [ ] All five task endpoints (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) are implemented and return appropriate HTTP status codes
- [ ] Each endpoint returns a properly serialized JSON response
- [ ] The `POST /instruction` endpoint calls the Groq API and returns the structured routing JSON
- [ ] The system prompt is well-crafted: the LLM consistently returns valid JSON in the required format across different voice inputs
- [ ] CORS is configured so the provided frontend can communicate with the API without errors
- [ ] The `.env` file is listed in `.gitignore` and the API key is never exposed in the code
- [ ] The in-memory list is correctly managed: IDs are unique and items are properly added, updated, and removed

> **Note:** The frontend is provided and will not be evaluated. You are not expected to modify it.

---

## 📦 How to Submit

Push your repository to GitHub and share the link following your instructor's submission instructions. Make sure the repository is public and that the `README.md` is present at the root.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
