# Task Manager API — Test Suite (In-Class Example)

> **Instructor note:** This is a simplified in-class example for the "Building Bullet-Proof Applications" project. Use this scenario to introduce pytest, test plans, and the three-tier test structure (happy path / edge case / failure mode) in 1–2 hours. The original project applies the same concepts to an authentication API with higher coverage requirements.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


Your team built a small **Task Manager API** with FastAPI. It has been working fine in development, but last week a teammate added a "complete task" feature that silently ignored tasks that didn't exist. No one noticed until a user reported it.

Your tech lead filed a ticket:

> *"We need a test suite. Each endpoint must have at least one happy-path test, one edge-case test, and one failure-mode test. Use pytest. Aim for 70% coverage on the task module."*

---

## The API Under Test

The Task Manager API has these endpoints:

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/tasks` | Return all tasks |
| `POST` | `/tasks` | Create a task (`title`, optional `description`) |
| `PATCH` | `/tasks/{task_id}/complete` | Mark a task as complete |
| `DELETE` | `/tasks/{task_id}` | Delete a task |

Each task has: `id` (auto-generated), `title` (string, required), `description` (string, optional), `completed` (bool, default `False`).

---

## What You Need to Do

### Step 1 — Write the test plan first

- [ ] Create `TESTING.md` at the root of the project.
- [ ] Before writing any test, list in `TESTING.md` which cases you plan to cover for each endpoint: happy path, edge case, and failure mode.

Example for `POST /tasks`:

| Test | Type | Input | Expected result |
|------|------|-------|-----------------|
| Create task with valid title | Happy path | `{"title": "Buy milk"}` | 201, task returned with `completed: false` |
| Create task without title | Edge case | `{}` | 422, validation error |
| Create task with empty string title | Failure mode | `{"title": ""}` | 422 or 400, error message |

### Step 2 — Write the tests

- [ ] Create a `tests/` directory at the project root.
- [ ] Create one test file per endpoint group:

```
tests/
├── test_list_tasks.py
├── test_create_task.py
├── test_complete_task.py
└── test_delete_task.py
```

- [ ] For each endpoint, implement at minimum:
  - [ ] **One happy-path test** — valid input, expected successful response.
  - [ ] **One edge-case test** — boundary input: empty title, non-existent ID, already-completed task, etc.
  - [ ] **One failure-mode test** — invalid or malformed input that should be rejected.

### Step 3 — Run and verify coverage

```bash
# Install dependencies
pip install pytest pytest-cov httpx

# Run all tests
pytest

# Run with coverage report
pytest --cov=app --cov-report=term-missing
```

- [ ] All tests pass with `pytest`.
- [ ] Coverage on the task module is at or above **70%** (`pytest --cov`).
- [ ] Document the coverage result in `TESTING.md`.

---

## Example Test Structure

```python
# tests/test_create_task.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task_happy_path():
    response = client.post("/tasks", json={"title": "Buy milk"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Buy milk"
    assert data["completed"] is False

def test_create_task_missing_title():
    # Edge case: required field is absent
    response = client.post("/tasks", json={})
    assert response.status_code == 422

def test_create_task_empty_title():
    # Failure mode: title is present but invalid
    response = client.post("/tasks", json={"title": ""})
    assert response.status_code in (400, 422)
```

> **Important:** Do not test HTTP serialization or framework internals. Every test must assert something about the **business logic** — what the endpoint *decides*, not how FastAPI formats the response.

---

## Test Cases to Cover (Starter List)

Use this as a starting point. Add more cases as you think of them.

| Endpoint | Happy path | Edge case | Failure mode |
|----------|-----------|-----------|--------------|
| `GET /tasks` | Returns list (can be empty) | Returns list with multiple tasks | — |
| `POST /tasks` | Creates task with title + description | Creates task with title only (no description) | Empty title |
| `PATCH /tasks/{id}/complete` | Marks existing task as complete | Task already marked complete | Non-existent task ID |
| `DELETE /tasks/{id}` | Deletes existing task | — | Non-existent task ID |

---

## AI-Assisted Workflow

- [ ] Paste your endpoint logic into your AI coding agent and ask: *"What edge cases am I missing for this endpoint?"*
- [ ] Review every suggested test case before adding it — you own the decisions about what to test.
- [ ] If a test reveals a bug in the existing code, fix the bug and note it in `TESTING.md` under a "Bugs Found" section.

---

## Discussion Questions

1. What is the difference between an edge case test and a failure mode test? Give an example of each for `DELETE /tasks/{id}`.
2. Why is 70% coverage a goal rather than 100%? What would a test suite focused only on reaching 100% look like, and what would it miss?
3. Your AI agent suggested testing that the response body contains an `id` field after creating a task. Is this testing business logic or HTTP serialization? Justify your answer.
