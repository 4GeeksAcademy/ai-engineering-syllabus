# Error Handling

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/error-handling-audit/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

You've been building the company's platform for several milestones: a corporate website, a Next.js frontend, a Python/FastAPI backend, and scripts that process real data. The codebase is growing — and so is the surface area for things to go wrong.

Your tech lead has opened a code review ticket with a clear message: the system currently has no coherent error handling strategy. API calls can silently fail, loading states are missing, users see raw technical messages (or nothing at all), and background scripts crash without useful output. Before the next milestone introduces more complexity, the team needs to fix this.

Your task is to audit the entire existing repository and apply a consistent error handling strategy across all layers: frontend, backend, and scripts.

> The tech lead has shared the following notes in the ticket:
>
> #### What we need
>
> - No error should crash the application or leave the user in an undefined state.
> - Every async operation on the frontend must have three visible states: loading, success, and error.
> - Error messages shown to users must be human-readable — never a raw stack trace, status code, or JSON parsing error.
> - Every error state must offer a clear exit: a retry button, a link back to home, or instructions to contact support.
> - On the backend and scripts, exceptions must be caught at the right scope — not with a single try/catch wrapping the entire function.
> - Sensitive information must never appear in error output sent to the client.

This is a cross-cutting engineering task — not a new feature. The deliverable is a cleaner, more resilient version of the codebase you've already built. By the end of this project, any user who encounters a problem in your platform will know what happened and what to do next.

---

## 🌱 How to Start the Project

This project works directly on your existing company monorepo — the same one you've been building since Milestone 1.

1. Open the monorepo in your editor or Codespace.
2. Create a new branch for this work: `git switch -c feature/error-handling-audit`.
3. Work through each layer of the codebase systematically (see checklist below).
4. Commit your changes with clear messages that explain what you fixed and why.

No new repository or boilerplate is needed.

---

## 🤖 Using Your Coding Agent to Detect Opportunities

Before making any changes manually, use your coding agent to scan the codebase and surface the most critical gaps. Below is a reference prompt you can adapt and run in your agent of choice (Cursor, Copilot, Claude Code, etc.).

Study it, adjust the parts marked with `[brackets]`, and make it your own — a well-crafted detection prompt will save you hours of manual reading.

```
You are a senior software engineer auditing a codebase for error handling quality.

Analyse the entire repository located at [path or describe your repo structure, e.g. "a Next.js frontend in /apps/web, a FastAPI backend in /apps/api, and Python scripts in /scripts"].

For each file or module you review, identify and report:

1. MISSING TRY/CATCH — async operations (fetch, await, file I/O, JSON parsing) that have no error handling at all.
2. OVERLY BROAD CATCH — try/catch or try/except blocks that wrap entire functions or large sections of code instead of the specific dangerous operation.
3. SILENT FAILURES — caught errors that are swallowed (empty catch blocks, bare `except: pass`).
4. RAW ERROR EXPOSURE — places where a raw exception message, stack trace, or status code could reach the user interface or API response.
5. SENSITIVE DATA LEAKS — error outputs or logs that may include secrets, database connection strings, internal paths, or personal data.
6. MISSING LOADING/ERROR UI STATES — frontend components that fetch data but render nothing (or crash) when the request is loading or fails.
7. NO USER CALL TO ACTION — error states that display a message but offer no way forward (no retry, no navigation, no support contact).
8. MISSING sys.exit ON SCRIPT FAILURE — Python scripts that encounter a critical error but exit with code 0 or no explicit exit code.

For each finding, report:
- File path and line number (or range)
- Category (from the list above)
- A one-line description of the problem
- Suggested fix (brief — implementation is the developer's responsibility)

Do not make any changes. Output only the audit report.
Prioritise findings by severity: CRITICAL > HIGH > MEDIUM > LOW.
```

Run the audit, read the report carefully, and use the checklist below to track your fixes.

---

## 💻 What You Need to Do

### Frontend (Next.js / TypeScript)

- [ ] Identify all `fetch` or API calls in the frontend and verify each one has a `try/catch` block scoped specifically to that call.
- [ ] For every async data-fetching operation, implement the **three-state UI pattern**: loading (spinner or skeleton), fulfilled (data renders), rejected (error message with a call to action).
- [ ] Replace any raw error messages (`Error 500`, `Unexpected token`, etc.) with human-readable explanations.
- [ ] Ensure every error state includes a meaningful **call to action**: a retry button, a link to the home page, or a contact support prompt.
- [ ] Use `optional chaining` (`?.`) where accessing potentially undefined nested properties.
- [ ] Add safe `defaults` or `fallbacks` for values that could be `null` or `undefined` when rendering.
- [ ] Use `finally` blocks to ensure loading states are always cleared, regardless of outcome.

### Backend (Python / FastAPI)

- [ ] Review every route handler and ensure exceptions are caught at the correct scope — avoid single large `try/except` blocks that swallow all errors.
- [ ] Return appropriate HTTP error responses (`400`, `404`, `422`, `500`) with a clean, structured JSON body — no raw Python tracebacks.
- [ ] Ensure error responses do **not** expose sensitive data (database connection strings, internal paths, secret keys).
- [ ] Add error handling to all external API calls made from the backend (e.g., calls to an LLM or third-party service).

### Scripts (Python)

- [ ] Wrap file I/O and CSV parsing operations in `try/except` blocks with informative error messages printed to `stderr`.
- [ ] Ensure scripts exit with a non-zero code (`sys.exit(1)`) when a critical error occurs.
- [ ] Add defensive checks for missing or malformed input data before processing begins.

### General

- [ ] Review the codebase for any `console.error` or `print` statements that expose sensitive internal information and remove or replace them.

⚠️ **IMPORTANT:** Do not introduce new features or refactor code unrelated to error handling. The scope of this project is strictly the resilience and error communication of existing code.

---

## ✅ What We Will Evaluate

- [ ] All async frontend operations implement the three-state UI pattern (loading / fulfilled / rejected).
- [ ] Error messages shown to users are human-readable and include a call to action.
- [ ] `try/catch` and `try/except` blocks are scoped to specific operations, not wrapped around entire functions.
- [ ] `finally` blocks are used correctly to clean up loading state.
- [ ] `optional chaining` and `fallbacks` are applied where appropriate to prevent undefined rendering errors.
- [ ] Backend routes return structured, clean error responses with the correct HTTP status codes.
- [ ] No sensitive information appears in any error output delivered to the client.
- [ ] Python scripts handle I/O errors and exit with appropriate codes on failure.

> Note: The evaluation focuses on the correctness and consistency of error handling patterns — not on whether new features were added.

---

## 📦 How to Submit

Push your `feature/error-handling-audit` branch to GitHub and share the pull request URL (or repository link) with your instructor as indicated in your cohort's submission instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/error-handling-audit/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
