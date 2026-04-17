# AI basic Inventory Agent Loop

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/exercise-ai-inventory-agent/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

A small local business — a coffee shop supply store with two physical locations — is losing money. Not because sales are down, but because no one on the team can answer a simple question at any given moment: _"Do we have enough of this product to cover the week?"_

Stock is tracked in a shared spreadsheet that no one updates consistently. The owner, Carla, has reached out to you after seeing a demo of an AI assistant at a trade fair. She doesn't want a dashboard she has to maintain manually — she wants to be able to talk to a system and get answers. She also wants the system to act: register deliveries, log sales, and tell her when something is running low, all through natural language.

Your job is to build that system. It has two parts that must work together:

**1. A REST API** built with FastAPI that manages the inventory data. It exposes endpoints for listing products, registering new ones, updating stock levels, and retrieving low-stock alerts. Products are stored in a CSV file so the data persists between sessions.

**2. An AI agent** written in Python that connects to an LLM and uses your API as its set of tools. The agent runs in a loop — it receives a message from Carla, reasons about what action to take, calls the appropriate API endpoint as a tool, and responds with the result. Every step of that loop is logged to a separate `conversation_log.csv` file.

### Complementary knowledge: the agent loop and tool calling

At this point in the course you know how to build a FastAPI and how to call an external API from Python. An AI agent adds one layer on top: instead of _you_ deciding when to call which endpoint, the **LLM decides**. You describe your endpoints as tools — each with a name, a description, and its expected parameters — and the model selects the right one based on the user's message.

The loop follows this cycle:

```
Observe (read user input)
    → Think (send to LLM with tool definitions)
        → Act (call the tool the LLM selected)
            → Update (inject the result back into the LLM context)
                → Repeat until the LLM gives a final response
```

Your agent must implement this cycle in a single Python file (`agent.py`). It should keep the full message history in memory during a session so the LLM can reason about prior exchanges.

### Conversation log

Every event in the loop must be appended to `conversation_log.csv` with these four fields:

| Field       | Description                                       |
| ----------- | ------------------------------------------------- |
| `actor`     | `user`, `agent`, or `tool`                        |
| `message`   | The text or result content of the event           |
| `tool_call` | Name of the tool called (empty if not applicable) |
| `timestamp` | ISO 8601 datetime of the event                    |

This file is append-only. Each session adds rows — it does not overwrite previous sessions.

> Carla has shared the following requirements via email:
>
> _"I need to be able to tell the system things like 'we just received 30 units of oat milk' or 'we sold 12 bags of arabica today'. It should understand me and update the stock. I also want to ask things like 'what products are running low?' and get a direct answer. Everything should feel like a conversation, not a form."_

You have full creative freedom over the product catalog and data structure, as long as it supports names, quantities, and a unit of measure (units, kg, liters, etc.).

Build something Carla could actually use on Monday morning.

---

## 🌱 How to Start the Project

This project uses a Python starter template. Fork and clone it:

```
https://github.com/4GeeksAcademy/python-hello
```

You can work either in **GitHub Codespaces** (open the repo and click _Code → Codespaces → Create_) or by cloning it locally. Once cloned, create your own GitHub repository and update the remote URL so your progress is tracked there.

Full instructions: [how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project)

**Starting the system:**

You need two terminal sessions running at the same time — one for the API, one for the agent.

```bash
# Terminal 1 — start the API
uvicorn api.app:app --reload

# Terminal 2 — start the agent
python agent.py
```

**Stopping the system:**

Press `Ctrl + C` in each terminal to stop the corresponding process. Stop the agent first, then the API. The `conversation_log.csv` file is written incrementally, so no data is lost when you stop mid-session.

**Relaunching the agent:**

Run `python agent.py` again in Terminal 2. The API does not need to be restarted. The agent will start a new session, but all previous conversation history will remain intact in `conversation_log.csv` — new rows are always appended, never overwritten.

Once the environment is ready:

```bash
pip install fastapi uvicorn openai python-dotenv
```

Create a `.env` file at the root with your LLM API key:

```
OPENAI_API_KEY=your_key_here
```

⚠️ **IMPORTANT:** Never commit your `.env` file. Add it to `.gitignore` before your first commit.

---

## 💻 What You Need to Do

### API (`api/app.py`)

- [ ] Create a FastAPI application that stores inventory data in a `products.csv` file
- [ ] `GET /inventory` — Returns the full product list
- [ ] `POST /inventory` — Adds a new product (`name`, `quantity`, `unit`)
- [ ] `PATCH /inventory/{product_id}` — Updates the stock of an existing product (accepts a `delta` value: positive for incoming stock, negative for outgoing)
- [ ] `GET /inventory/alerts` — Returns all products whose quantity is below a configurable threshold (default: 10 units)
- [ ] All endpoints must return appropriate HTTP status codes and descriptive messages on error

### Agent (`agent.py`)

- [ ] Define your API endpoints as **tools** for the LLM — each tool must have a clear `name`, `description`, and typed `parameters`
- [ ] Implement the full **agent loop**: Observe → Think → Act → Update → Repeat
- [ ] The agent must keep the conversation history in memory for the duration of the session
- [ ] When the LLM selects a tool, the agent must call the corresponding API endpoint and inject the result back into the context
- [ ] The loop must terminate cleanly when the LLM returns a final response with no pending tool calls
- [ ] The agent must expose a simple CLI interface: it should read user input from the terminal and print the agent's response

### Conversation log

- [ ] Every event (user message, agent response, tool call, tool result) must be appended to `conversation_log.csv`
- [ ] The CSV must include the four required fields: `actor`, `message`, `tool_call`, `timestamp`
- [ ] The file must persist across sessions (append-only, never overwrite)

### General

- [ ] The API must be running before the agent starts. Document how to launch both in the README
- [ ] ⚠️ **IMPORTANT:** Do not use any agent framework (LangChain, LlamaIndex, AutoGen, etc.). The agent loop must be implemented manually in plain Python

---

## ✅ What We Will Evaluate

- [ ] The FastAPI exposes all four required endpoints and they return correct responses
- [ ] Products are persisted in `products.csv` and survive a server restart
- [ ] The agent loop correctly implements the Observe → Think → Act → Update → Repeat cycle
- [ ] Tools are defined with names, descriptions, and typed parameters that the LLM can reliably use
- [ ] The agent calls the correct API endpoint when the LLM selects a tool
- [ ] The LLM result is injected back into the conversation history before the next iteration
- [ ] `conversation_log.csv` is created and populated with all four fields on every event
- [ ] The log is append-only across multiple sessions
- [ ] The agent handles at least one multi-step interaction (e.g., add a product and immediately ask for alerts)
- [ ] No agent framework is used — the loop is hand-coded in Python

> Note: UI design and visual presentation are not evaluated. A terminal interface is sufficient.

---

## 📦 How to Submit

Push your repository to GitHub and share the link following your instructor's instructions. Make sure both `api/app.py` and `agent.py` are included, along with a brief note in your README on how to start both processes.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/exercise-ai-inventory-agent/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
