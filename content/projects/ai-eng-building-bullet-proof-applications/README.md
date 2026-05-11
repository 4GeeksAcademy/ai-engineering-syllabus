# Building Bullet-Proof Applications

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/building-bullet-proof-applications/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your Challenge

Your company's authentication API is live, handling real users and real sessions. Last week, a teammate pushed a small refactor that broke token expiration logic — no tests caught it, and users reported being locked out for two hours before someone noticed. Your CTO's response was brief and direct: _"We need a test suite. Untested code is not production code."_

Your task is to add a comprehensive battery of unit tests to the authentication API you built in the previous milestone. You'll work at the function and endpoint logic level — not testing serialisation or HTTP plumbing, but the actual business logic: does the token get generated correctly? Does an expired token get rejected? What happens when the password field is empty?

This is not about writing tests for their own sake. It's about building confidence that every endpoint behaves as expected under normal conditions, edge cases, and failure scenarios — the three pillars of any serious test plan.

> Your CTO has filed the following ticket:
>
> #### Ticket: AUTH-088 — Unit test coverage for the authentication API
>
> **Priority:** High
>
> **Context:** Following last week's regression, we are requiring unit tests on all authentication endpoints before any further changes are merged.
>
> **Scope:**
>
> - Test suite must cover all endpoints in the authentication API
> - Each endpoint must have at minimum: one happy-path test, one edge-case test, and one failure-mode test
> - Use `pytest` for the FastAPI backend and `Jest` for any TypeScript logic
> - Tests must pass cleanly with `pytest` and `jest --coverage`
> - Do not test HTTP serialisation — test the logic
>
> **Deliverable:** A working test suite committed alongside the existing API code, with a brief `TESTING.md` explaining how to run it.

Before writing your first test, define your test plan: list the cases you want to cover for each endpoint, identify the edge cases (empty fields, duplicate users, malformed tokens), and think through which inputs could produce unexpected behaviour. Then use AI to help you generate the test code — but you own the decisions about _what_ to test.

This is the kind of work that separates a junior who ships features from a professional who ships reliable software.

---

## 🌱 How to Start the Project

You will work on top of your existing authentication API project — there is no new repository to fork.

1. Open your authentication API project from the previous milestone.
2. If you are working locally, make sure your virtual environment is active and dependencies are installed.
3. If you are using GitHub Codespaces, reopen your existing project from your GitHub profile.

Install the testing dependencies if they are not already present:

```bash
# Python / FastAPI
pip install pytest pytest-cov httpx

# TypeScript (if applicable)
npm install --save-dev jest @types/jest ts-jest
```

If you have any questions about how to set up a project from scratch, visit: [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 What You Need to Do

### Test plan

- [ ] Create a `TESTING.md` file at the root of your project documenting: how to run the tests, what each test suite covers, and which cases you decided to include and why.
- [ ] Before writing any test, list in `TESTING.md` the cases you plan to cover: happy path, edge cases, and failure modes for each endpoint.

### FastAPI — pytest

- [ ] Create a `tests/` directory at the root of your FastAPI project.
- [ ] Write a test module for each authentication endpoint (e.g., `test_register.py`, `test_login.py`, `test_token.py`).
- [ ] For each endpoint, implement at minimum:
  - [ ] One happy-path test (valid input, expected response)
  - [ ] One edge-case test (boundary input: empty field, duplicate user, etc.)
  - [ ] One failure-mode test (invalid credentials, expired token, malformed request)
- [ ] All tests must pass when running `pytest` from the project root.
- [ ] Run `pytest --cov` and ensure your test suite achieves at least **70% coverage** on the authentication module.

### TypeScript — Jest (if your project includes TypeScript utility logic)

- [ ] Configure Jest with a `jest.config.ts` or `jest.config.js` at the root of your TypeScript project.
- [ ] Write unit tests for any authentication-related utility functions (token generation, validation, password hashing helpers).
- [ ] For each function, implement at minimum: one happy-path test and one failure-mode test.
- [ ] All tests must pass when running `jest --coverage`.

### AI-assisted workflow

- [ ] Use your AI coding agent to help identify test cases you might have missed — prompt it with your endpoint logic and ask it to suggest edge cases.
- [ ] Use AI to generate test boilerplate, but review and understand every test before committing it.
- [ ] If a generated test reveals a bug in your existing code, fix the bug and document it in `TESTING.md`.

⚠️ **IMPORTANT:** Do not test HTTP serialisation or framework internals. Every test must assert something about the business logic of your application — what the endpoint _decides_, not how it _responds_.

### 🏆 Extra activity — Close out the backlog while you're at it

The CTO just marked AUTH-088 as the blocker, but two other tickets have been sitting in the backlog for weeks. They're low priority — no one is chasing them — but now that you have the testing infrastructure in place, it would be a shame not to close them. If you finish early, knock them out.

> #### Ticket: API-042 — Unit tests for backoffice endpoints
>
> **Priority:** Low
>
> **Context:** The backoffice API has never had a test suite. No regressions have been reported, but that's probably because the team is small, not because the code is solid. Now that we have `pytest` configured, let's extend coverage before the team grows.
>
> **Scope:**
>
> - Pick at least two non-authentication endpoint groups from your backoffice API (e.g., resources, users, items — whatever your company's domain has)
> - Apply the same three-tier structure: happy path, edge case, failure mode
> - Aim for 60% coverage on the modules you test — lower bar than auth, but still meaningful
>
> **Deliverable:** New test modules added to the existing `tests/` directory. Update `TESTING.md` with the new coverage results.

> #### Ticket: FE-019 — Unit tests for frontend utility functions
>
> **Priority:** Low
>
> **Context:** The frontend has accumulated utility functions over the past milestones — form validators, data formatters, API response handlers — that have never been tested. A bug in any of them could silently break the UI in ways that are hard to trace.
>
> **Scope:**
>
> - Identify at least three utility or helper functions in your Next.js / TypeScript frontend
> - Write Jest unit tests for each: one happy-path test and one failure-mode test per function
> - Functions that are good candidates: input validators, date or currency formatters, response parsers, token storage helpers
>
> **Deliverable:** A `__tests__/` directory inside your frontend project with the test files. Update `TESTING.md` with instructions to run frontend tests separately.

- [ ] _(Extra)_ Write pytest tests for at least two backoffice endpoint groups, reaching 60% coverage on those modules.
- [ ] _(Extra)_ Write Jest tests for at least three frontend utility functions (happy path + failure mode each).
- [ ] _(Extra)_ Update `TESTING.md` with coverage results and run instructions for both extra suites.

---

## ✅ What We Will Evaluate

- [ ] A `TESTING.md` file is present and documents the test plan, how to run tests, and coverage results.
- [ ] `pytest` runs without errors from the project root and all tests pass.
- [ ] The test suite includes happy-path, edge-case, and failure-mode tests for each authentication endpoint.
- [ ] Test coverage on the authentication module is at or above 70% (verified with `pytest --cov`).
- [ ] Tests assert business logic, not HTTP serialisation or framework behaviour.
- [ ] If TypeScript utility functions exist, Jest tests are present and passing.
- [ ] The AI-assisted workflow is evident: `TESTING.md` notes at least one case identified with AI assistance or one bug caught by the test suite.
- [ ] Code is clean: tests are named clearly, follow a consistent structure, and include brief comments explaining non-obvious assertions.

> **Note:** The evaluation does not require 100% coverage. The quality and intent of the test cases matter more than the coverage number. A well-reasoned 70% is worth more than a mechanical 95%.

> **Extra activity:** The backoffice and frontend test suites are not required for a passing grade, but they will be recognised in the evaluation if present and passing.

---

## 📦 How to Submit

Push your updated repository to GitHub — it should contain your existing API code plus the new `tests/` directory and `TESTING.md` — and share the repository URL with your instructor following their instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/building-bullet-proof-applications/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
