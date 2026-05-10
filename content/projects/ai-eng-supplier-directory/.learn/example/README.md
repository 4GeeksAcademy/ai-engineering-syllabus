# Library Book Catalog — Lightweight Storage API (Class Example)

> **For instructors:** This is a simplified in-class example that introduces the same core concepts as the Supplier Directory project — TinyDB, Pydantic validation, seeders, and filtered endpoints — using a familiar domain. It is intentionally shorter so it can be built live during a session.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## 🎯 The challenge

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


A small community library currently tracks its book catalog in a text file. You have been asked to replace it with a small FastAPI + TinyDB + Pydantic API that starts preloaded with data and rejects any invalid input before it hits the database.

---

## 💻 What you need to build

### Data model

Define a Pydantic `Book` model with the following fields:

| Field    | Type  | Constraints                                                           |
| -------- | ----- | --------------------------------------------------------------------- |
| `title`  | `str` | required                                                              |
| `author` | `str` | required                                                              |
| `genre`  | `str` | must be one of: `"fiction"`, `"non-fiction"`, `"mystery"`, `"sci-fi"` |
| `pages`  | `int` | must be greater than 0                                                |
| `status` | `str` | must be one of: `"available"`, `"checked_out"`                        |

Use an `Enum` or a Pydantic field validator to enforce `genre` and `status`. Pydantic must reject invalid values with `422` before any data reaches TinyDB.

### Seeder

Create a `seed.py` script that loads these four books into TinyDB on startup:

```python
[
    {"title": "The Pragmatic Programmer", "author": "Hunt & Thomas", "genre": "non-fiction", "pages": 352, "status": "available"},
    {"title": "Dune",                     "author": "Frank Herbert",  "genre": "sci-fi",      "pages": 412, "status": "available"},
    {"title": "The Big Sleep",            "author": "Raymond Chandler","genre": "mystery",    "pages": 231, "status": "checked_out"},
    {"title": "Nineteen Eighty-Four",     "author": "George Orwell",  "genre": "fiction",     "pages": 328, "status": "available"},
]
```

- Running the seeder twice must not create duplicate records.
- Print the number of records inserted when it finishes.

### Endpoints

| Method   | Path                 | Description                                                                    |
| -------- | -------------------- | ------------------------------------------------------------------------------ |
| `POST`   | `/books`             | Register a new book. Return the created book with its TinyDB ID.               |
| `GET`    | `/books`             | List all books. Accept optional `?genre=` and `?status=` query params.         |
| `GET`    | `/books/{id}`        | Return a book by ID. Return `404` if not found.                                |
| `PATCH`  | `/books/{id}/status` | Change status to `available` or `checked_out`. Reject other values with `422`. |
| `DELETE` | `/books/{id}`        | Remove a book. Return `404` if not found.                                      |

---

## ✅ Key concepts to verify

- [ ] `genre` values outside the allowed set return `422`.
- [ ] `pages` with zero or negative value returns `422`.
- [ ] `status` values outside the allowed set return `422`.
- [ ] `GET /books?genre=mystery` returns only mystery books.
- [ ] `GET /books?status=available` returns only available books.
- [ ] Running the seeder a second time produces no duplicates.
- [ ] Data persists after restarting the server.

---

## 💡 Discussion questions

1. Why use TinyDB instead of a full SQL database for a project like this?
2. Where exactly does Pydantic stop an invalid request — before or after TinyDB?
3. What would need to change to migrate this to PostgreSQL later?
