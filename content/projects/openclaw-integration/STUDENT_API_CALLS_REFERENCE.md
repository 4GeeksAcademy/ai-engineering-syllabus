# 📡 Student API calls reference (BreatheCode)

_Spanish version: [español](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/openclaw-integration/STUDENT_API_CALLS_REFERENCE.es.md)._

This document summarizes student-oriented endpoints for **4Geeks Academy**: HTTP method, path, parameters, and response shape. It does not include code samples or example bodies; for detailed schemas, use the linked OpenAPI at the end.

> 💡 **Start here**
> If you are automating or integrating anything, read **Authentication** and **Essential prerequisites** first. That will save you 401 errors and empty filters.

---

## 📑 Quick index

Use in-file search (**Ctrl+F** / **Cmd+F**) on the left-column keyword to jump quickly.

| Section                 | What it covers                    |
| ----------------------- | --------------------------------- |
| 🔐 Authentication       | Token and public routes           |
| 🌐 Base URL             | Where the API lives               |
| 🎯 Essential parameters | `academy_id`, `cohort_id`, slug   |
| 🎓 Admissions           | You, cohorts, syllabus            |
| ✅ Assignments          | Tasks and submissions             |
| 🏆 Certificates         | Certificates                      |
| 📊 Activity             | Your activity and cohort activity |
| 📚 Registry             | Lessons, exercises, technologies  |
| 📅 Events               | Events                            |
| 📋 Enumerations         | Statuses and types                |
| 🔗 Docs and resources   | Swagger, OpenAPI, and more        |

---

## 🔐 Authentication

Most endpoints require a token in the **Authorization** header, with the literal prefix **Token**, a space, and the token value.

The token is obtained by signing in with **POST** `/v1/auth/login` (public).

Endpoints marked as public do not require a token.

> 🚨 **Security**
> Do not share your token in public repos, screenshots, or chats. Treat it like a password: environment variables or secret managers—never hardcoded in the repository.

---

## 🌐 Base URL

In production the API is usually served from **https://breathecode.herokuapp.com**. Other environments may use a different base.

> 📝 **Environments**
> If your bootcamp uses another instance, confirm the base URL with your instructor or technical team before shipping integrations.

---

## 🎯 Essential prerequisites

Before filtering by academy or cohort, resolve:

- **academy_id** — Numeric academy id for the student. Often taken from the first item of **profile_academy** in the current-user response.
- **cohort_id** and **cohort.slug** — Numeric id and textual slug for the cohort. The active cohort is usually the one with **educational_status** **ACTIVE** in the student’s cohort list.

> 💡 **Mental shortcut**
> Think of **academy_id** as “which campus?” and **cohort_id** / **slug** as “which cohort am I in?” Many lists filter better with one or the other depending on the endpoint.

---

## 🎓 Admissions — user and cohorts

### 👤 Current user

- **GET** `/v1/admissions/user/me`
- **Path or query parameters:** none required.
- **Response:** user object with id, email, name, and profile relations; includes **profile_academy** with linked academies (each with **academy** **id**, **name**, **slug**, etc.).

### 📋 My cohorts

- **GET** `/v1/admissions/academy/cohort/me`
- **Optional query:** **academy** (academy id); **educational_status** (e.g. **ACTIVE**, **GRADUATED**, **SUSPENDED**, **DROPPED**).
- **Response:** array of cohort enrollments; each item includes **cohort** (**id**, **name**, **slug**, **schedule**, etc.), **role**, **educational_status**, **created_at**.

### 📖 Public syllabus

- **GET** `/v1/admissions/public/syllabus`
- **Authentication:** not required.
- **Response:** public syllabi.

---

## ✅ Assignments — tasks and submissions

> 📝 **Typical flow**
> List tasks → update URLs if needed → **deliver** with the **deliver** endpoint when ready for review. Exact order may depend on your syllabus rules.

### 📥 List my tasks

- **GET** `/v1/assignment/user/me/task`
- **Useful query:** **task_status** (**PENDING**, **DONE**, **APPROVED**, **REJECTED**); **task_type** (**PROJECT**, **EXERCISE**, **LESSON**); **cohort** (cohort id); **limit** and **offset** for pagination.
- **Response:** list of assigned tasks with status, type, dates, and review metadata.

### 🔍 Task detail

- **GET** `/v1/assignment/task/{task_id}`
- **Path parameter:** **task_id** (numeric).
- **Response:** full task detail (description, score, feedback, etc.).

### ✏️ Update a task

- **PUT** `/v1/assignment/task/{task_id}`
- **Path parameter:** **task_id**.
- **Body:** typically submission URLs, e.g. repo (**github_url**) and deployment (**live_url**); exact schema is in OpenAPI.

### 🚀 Deliver a task

- **POST** `/v1/assignment/task/{task_id}/deliver`
- **Path parameter:** **task_id**.
- **Response:** per Swagger contract (marks task submitted for review).

---

## 🏆 Certificates

### 📜 List certificates

- **GET** `/v1/certificate/`
- **Optional query:** **cohort** (cohort id).
- **Response:** user’s certificates (filterable by cohort).

### 🔗 Certificate by token

- **GET** `/v1/certificate/{token}`
- **Path parameter:** unique certificate **token**.
- **Authentication:** public (no user token).
- **Response:** certificate data for that token.

> 🚧 **Public links**
> The URL token identifies the certificate. Anyone with the link can view it without logging in—share only over secure channels.

---

## 📊 Activity

### 🙋 My activity

- **GET** `/v1/activity/me`
- **Optional query:** **cohort** (id or slug per your instance); **date_start** and **date_end** as dates (e.g. **YYYY-MM-DD**).
- **Response:** user learning activity (time, exercises, etc., per API model).

### 👥 Cohort activity

- **GET** `/v1/activity/cohort/{cohort_id}`
- **Path parameter:** **cohort_id** may be numeric id or cohort slug.
- **Response:** aggregated or per-member cohort activity (progress comparison).

---

## 📚 Registry — learning content

### 🔎 Search assets (lessons, exercises, projects)

- **GET** `/v1/registry/asset`
- **Useful query:** **asset_type** (**LESSON**, **EXERCISE**, **PROJECT**); **technologies** (technology slug, e.g. python, react, javascript); **difficulty** (**BEGINNER**, **EASY**, **INTERMEDIATE**, **HARD**); **like** (search text); **limit**.
- **Response:** list of assets matching filters.

> 💡 **Exploring the catalog**
> Combine **asset_type** + **technologies** to practice the stack you see in class, or raise difficulty gradually.

### 📄 Asset detail

- **GET** `/v1/registry/asset/{asset_slug}`
- **Path parameter:** **asset_slug** (human-readable resource id).
- **Response:** full asset (readme, technologies, difficulty, repository, etc.).

### ✨ My assets

- **GET** `/v1/registry/asset/me`
- **Response:** assets created or modified by the user.

### 🛠️ Technologies

- **GET** `/v1/registry/technology`
- **Optional query:** **like** (name search); **limit**.
- **Response:** catalog of technologies on the platform.

---

## 📅 Events

### 🎟️ Events

- **GET** `/v1/events/all`
- **Optional query:** **academy** (academy id); **upcoming** (boolean, e.g. future only); **limit**.
- **Response:** list of events per filters.

---

## 📋 Useful enumerations and conventions

### 🎓 Educational status (**educational_status**)

- **ACTIVE** — Currently enrolled.
- **GRADUATED** — Graduated.
- **SUSPENDED** — Suspended.
- **DROPPED** — Dropped / withdrawn.

### ✅ Task status (**task_status**)

- **PENDING** — Pending.
- **DONE** — Completed by the student.
- **APPROVED** — Approved in review.
- **REJECTED** — Rejected; corrections needed.

### 🧩 Task type (**task_type**)

- **LESSON** — Lesson.
- **EXERCISE** — Exercise.
- **PROJECT** — Project.
- **QUIZ** — Quiz.

### 📄 Pagination

Many listings support **limit** (number of results) and **offset** (offset from the start).

### 🔒 Context filtering

Data is usually limited to cohorts the user is enrolled in, per backend policy.

### ⏱️ Rate limiting and caching

Prefer caching stable responses and avoiding bursts of identical requests; exact limits depend on the instance.

> ⚠️ **Do not hammer the API**
> If a script fires hundreds of identical calls per second, you may hit limits or degrade the service for everyone. Reuse in-memory or on-disk data when it makes sense.

---

## 🔗 Documentation and extra resources

### Live exploration

| Resource                        | Link                                                                                             |
| ------------------------------- | ------------------------------------------------------------------------------------------------ |
| 📖 **Swagger (interactive)**    | [https://breathecode.herokuapp.com/swagger/](https://breathecode.herokuapp.com/swagger/)         |
| 🔧 **OpenAPI (machine schema)** | [https://breathecode.herokuapp.com/openapi.json](https://breathecode.herokuapp.com/openapi.json) |

For JSON field details, error codes, and request/response bodies, use those links. If your cohort shares a **STUDENT_API_REFERENCE.md** with runnable examples, use it as a companion.

### More material

- 📄 **Extended reference** — Ask your instructor for course material **STUDENT_API_REFERENCE.md** if it is available.
- 🤖 **Agent integration** — In the AI Engineering syllabus repository you can search for `OPENCLAW_BREATHECODE_*` guides as inspiration for working with OpenClaw.

### Mini glossary

| Term         | Quick meaning                                                     |
| ------------ | ----------------------------------------------------------------- |
| **Endpoint** | A concrete API route (method + URL).                              |
| **Query**    | Parameters after `?` in the URL.                                  |
| **Slug**     | Human-readable lowercase hyphenated id (e.g. cohort name in URL). |
| **Asset**    | A content item: lesson, exercise, or project in the registry.     |

---

### 🙌 Next step?

Open **Swagger**, pick an endpoint you already use in the platform (for example “my tasks”), and compare response fields with what you see in the LMS. That connects this guide to real practice.
