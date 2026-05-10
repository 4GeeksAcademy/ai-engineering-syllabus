# In-Class Example: Voice Notes Journal API

> **Instructor note:** This is an in-class live example for teaching the concepts of the `voice-to-do-list-api` project. Use this scenario to demonstrate FastAPI CRUD endpoints, in-memory storage, Groq API integration, and LLM prompt engineering for intent extraction. **Do not assign this as homework — it is a guided classroom exercise.**

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## The Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


A journalist uses a voice-first app to capture quick notes while reporting in the field. The browser frontend already records their voice, transcribes it with the Web Speech API, and sends the text to a backend. Your job is to build that backend.

Users speak things like:
- _"Save that the city council meeting is at 7 pm on Friday"_
- _"Show me all my notes"_
- _"Delete note 3"_
- _"Update note 2 to say the meeting was postponed"_

**What you are learning:**
- How to build a RESTful API with FastAPI and in-memory storage
- How to implement all five HTTP methods (GET, POST, PUT, PATCH, DELETE) for a resource
- How to call the Groq API from a FastAPI endpoint
- How to write a system prompt that forces an LLM to return structured JSON (intent extraction)
- Why prompt engineering matters: the LLM is your routing layer

---

## Data Model

Each note is stored as a Python dict:

```python
{ "id": 1, "content": "City council meeting at 7 pm on Friday", "archived": False }
```

Storage is a module-level list — no database, no file system:

```python
notes: list[dict] = []
```

---

## API Spec

### Notes endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/notes` | Return all notes as a JSON array |
| `POST` | `/notes` | Create a new note (`content` required, `archived` defaults to `False`) |
| `PUT` | `/notes/{note_id}` | Replace the note entirely (new `content` required) |
| `PATCH` | `/notes/{note_id}` | Partially update: change `content` and/or set `archived: true` |
| `DELETE` | `/notes/{note_id}` | Delete the note by ID; return a confirmation message |

### Instruction endpoint

| Method | Path | Description |
|---|---|---|
| `POST` | `/instruction` | Receives `{ "transcription": "..." }`, calls Groq, returns routing JSON |

The `/instruction` endpoint calls Groq with a system prompt that forces the LLM to respond **only** with:

```json
{
  "endpoint": "/notes",
  "method": "POST",
  "params": { "content": "City council meeting at 7 pm on Friday" }
}
```

---

## Tasks

### Setup

- [ ] Create a virtual environment and install `fastapi`, `uvicorn`, and `groq`
- [ ] Store your Groq API key in a `.env` file (add it to `.gitignore`)
- [ ] Configure CORS to allow requests from `localhost`

### In-memory storage

- [ ] Declare `notes: list[dict] = []` at the module level
- [ ] Each note has `id` (int, auto-incremented), `content` (str), `archived` (bool, default `False`)

### Notes endpoints

- [ ] Implement all five endpoints from the spec above
- [ ] IDs must be unique even after deletions (use `max(n["id"] for n in notes) + 1` or a counter)
- [ ] Return `404` with a message if a note ID is not found

### Instruction endpoint

- [ ] Implement `POST /instruction` that reads the `transcription` field
- [ ] Write a system prompt that instructs the LLM to return **only** a JSON object with `endpoint`, `method`, and `params`
- [ ] Call the Groq API (model: `llama3-8b-8192` or similar) and return the JSON response

> ⚠️ Do **not** hardcode intent matching (no `if "save" in transcription`). All routing logic must come from the LLM response.

### Verify end to end

- [ ] Test these spoken commands manually (using Postman, curl, or the frontend if available):

  | Spoken phrase | Expected LLM routing |
  |---|---|
  | "Save that I need to call the mayor's office" | `POST /notes` |
  | "Show all my notes" | `GET /notes` |
  | "Archive note 2" | `PATCH /notes/2` with `archived: true` |
  | "Delete note 1" | `DELETE /notes/1` |

---

## System Prompt Template (starting point)

```
You are an intent extractor for a voice notes API.
Given a spoken transcription, respond ONLY with a JSON object in this exact format:
{
  "endpoint": "<path>",
  "method": "<HTTP method in uppercase>",
  "params": { ... }
}
Available endpoints: GET /notes, POST /notes, PUT /notes/{id}, PATCH /notes/{id}, DELETE /notes/{id}.
Never return explanations. Never return free text. Only JSON.
```

---

## Discussion Questions

1. What happens if the LLM returns free text instead of JSON? How would you make your `/instruction` endpoint handle that gracefully?
2. The system prompt defines all available endpoints. What would you need to change in the prompt if you added a `GET /notes/{id}` endpoint to retrieve a single note?
3. Right now, the notes list is reset every time the server restarts. What would you need to change to persist notes across restarts — and what would that add in terms of complexity?
