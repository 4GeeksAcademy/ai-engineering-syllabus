# Bookstore Stock Agent — In-Class Example

> **Instructor note:** This is a simplified in-class example for the "AI Basic Inventory Agent Loop" project. Use this scenario to demonstrate the agent loop (Observe → Think → Act → Update) and tool calling with a FastAPI backend in 1–2 hours. The original project covers the same technical patterns in a coffee shop supply context.

_Estas instrucciones tambien estan disponibles en [espanol](./README.es.md)._

---

## Scenario

### Scope note

This example is scoped for one live classroom session. It keeps the same stack and core patterns as the official student project in this folder but drops secondary requirements; see the instructor note above. Students still follow the full brief in the project root `README.md`.


**PageTurner Books** is a small indie bookstore. The owner, Mia, wants to stop checking spreadsheets and start asking questions in plain language: *"How many copies of Dune do we have?"* or *"We just received 20 copies of The Midnight Library."*

Your job is to build a two-part system:

1. **A FastAPI REST API** that manages the bookstore's stock in a CSV file.
2. **An AI agent** (`agent.py`) that connects to an LLM, uses the API as tools, and runs a conversation loop with Mia.

---

## System Architecture

```
Mia types a message
    → agent.py sends it to the LLM (with tool definitions)
        → LLM selects a tool and its parameters
            → agent.py calls the matching API endpoint
                → API result is injected back into the LLM context
                    → LLM produces a final response for Mia
```

This cycle is the **agent loop**: Observe → Think → Act → Update → Repeat.

---

## What You Need to Do

### Part 1 — FastAPI (`api/app.py`)

Build a FastAPI app that stores book data in `books.csv` with these fields: `id`, `title`, `author`, `quantity`.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/books` | `GET` | Returns the full book list |
| `/books` | `POST` | Adds a new book (`title`, `author`, `quantity`) |
| `/books/{book_id}` | `PATCH` | Updates stock — accepts a `delta` (positive = restock, negative = sale) |
| `/books/alerts` | `GET` | Returns books with quantity below the threshold (default: 5) |

- [ ] `books.csv` is created automatically if it doesn't exist.
- [ ] All endpoints return appropriate HTTP status codes.
- [ ] `PATCH` rejects requests that would bring quantity below 0.

### Part 2 — AI Agent (`agent.py`)

- [ ] Define the four API endpoints as **tools** for the LLM. Each tool needs:
  - `name` — a short identifier
  - `description` — plain English explanation of what it does
  - `parameters` — typed JSON schema for its inputs

- [ ] Implement the **agent loop**:

```python
while True:
    # 1. Observe: read user input
    # 2. Think: send messages + tool definitions to LLM
    # 3. Act: if LLM chose a tool, call the API
    # 4. Update: inject tool result into message history
    # 5. Repeat until LLM gives a final answer (no tool call)
```

- [ ] Keep the full **conversation history** in memory for the session.
- [ ] Expose a simple CLI: print `You:` prompt, print agent response.

### Part 3 — Conversation Log (`conversation_log.csv`)

Every event in the loop must be appended to `conversation_log.csv`:

| Field | Description |
|-------|-------------|
| `actor` | `user`, `agent`, or `tool` |
| `message` | Text or result content |
| `tool_call` | Tool name called (empty if not applicable) |
| `timestamp` | ISO 8601 datetime |

- [ ] The file is **append-only** — never overwritten between sessions.

---

## Minimal Tool Definition Example

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_books",
            "description": "Returns the current list of all books and their stock quantities.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_stock",
            "description": "Updates the stock of a book by a delta amount. Use positive values for restocking, negative for sales.",
            "parameters": {
                "type": "object",
                "properties": {
                    "book_id": {"type": "string", "description": "The book's ID"},
                    "delta": {"type": "integer", "description": "Amount to add (positive) or subtract (negative)"}
                },
                "required": ["book_id", "delta"]
            }
        }
    }
]
```

---

## How to Run

```bash
# Terminal 1 — start the API
uvicorn api.app:app --reload

# Terminal 2 — start the agent
python agent.py
```

Create a `.env` file with your API key before starting:

```
GROQ_API_KEY=your_key_here
```

> **Important:** Do not use any agent framework (LangChain, AutoGen, etc.). The loop must be hand-coded in plain Python.

---

## Sample Conversation to Test

```
You: What books do we have?
Agent: Here are the books currently in stock: ...

You: We just received 15 copies of Dune.
Agent: Done! I've added 15 copies to Dune's stock. Current quantity: ...

You: Which books are running low?
Agent: The following books are below the minimum threshold: ...
```

---

## Discussion Questions

1. What would happen if you removed the tool result from the message history before the next LLM call? How would this affect the agent's behavior?
2. Why is `conversation_log.csv` append-only? What problem would overwriting it cause?
3. The LLM chooses which tool to call based on your description strings. Write a better description for the `update_stock` tool that would help the model distinguish between a sale and a restock.
