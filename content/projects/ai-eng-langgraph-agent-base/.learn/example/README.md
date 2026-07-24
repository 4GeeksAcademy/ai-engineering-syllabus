# Maple Street Library — LangGraph Agent Migration (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-langgraph-agent-base`. Same spine (minimal LangGraph state, three single-responsibility nodes, conditional edges, compile + checkpoint, queryable trace, evals, thin `POST /agent/query`), different scope than the company monorepo. Assumes students already have the Maple Street RAG from the prior RAG class example — or you provide a pre-built `retrieve`/`query` in `data/pipelines/`. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Maple Street Library** desk staff use the RAG assistant from the prior class session. It works, but every answer is a black box — nobody can see whether retrieval ran before generation or what the graph decided.

Your live demo goal: wrap the existing `retrieve` and `query` functions in a **compiled LangGraph** so each patron question produces a **queryable trace**, without rewriting the RAG pipeline.

### Scope note

| Graded project (`ai-eng-langgraph-agent-base`)    | This class example                            |
| ------------------------------------------------- | --------------------------------------------- |
| Full company monorepo fork + `CONTEXT-company.md` | Mini `library-api` + `maple_knowledge` corpus |
| LangSmith or production-grade tracing             | In-memory trace list + optional JSON export   |
| Checkpointing with durable store                  | `MemorySaver` checkpointer only               |
| PR with trace screenshot + eval output            | Local demo + `pytest tests/pipelines/`        |
| Coexist with existing RAG monorepo endpoint       | Replace or add beside `POST /knowledge/query` |

---

## Prerequisites (from RAG class example)

- [ ] Qdrant running with collection `maple_knowledge` indexed
- [ ] `data/pipelines/rag.py` exposes working `retrieve()` and `generate_answer()` (the generation step factored out of `query()`) — **import them; do not copy logic into nodes, and do not call the monolithic `query()` inside a single node**

---

## What to build

### 1. Graph state (`services/agent/state.py`)

- [ ] TypedDict with: `question`, `retrieved_context`, `answer`, `trace_steps`, `error`
- [ ] No full chat history — justify any extra field verbally if you add one

### 2. Nodes (`services/agent/nodes.py`)

| Node               | Calls                                | Responsibility                                                                                     |
| ------------------ | ------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `receive_question` | —                                    | Validate non-empty question; append trace step                                                     |
| `retrieve_node`    | `data.pipelines.rag.retrieve`        | Fetch context; record chunk count in trace                                                         |
| `query_node`       | `data.pipelines.rag.generate_answer` | Generate desk-staff answer from the passed context — **not** `query()`, which would retrieve again |

### 3. Graph + checkpoint (`services/agent/graph.py`)

- [ ] Conditional edges: empty question → `END`; else `receive` → `retrieve` → `query` → `END`
- [ ] `builder.compile(checkpointer=MemorySaver())` at startup — not per request
- [ ] Broken graph (e.g. orphan node) must fail at compile time during demo setup

### 4. Tracing

- [ ] Each node appends to `trace_steps`, e.g. `{"node": "retrieve", "order": 2, "summary": "3 chunks"}`
- [ ] After one run, export or print trace JSON students can inspect

### 5. Endpoint

- [ ] `POST /agent/query` body `{ "question": "..." }` → `{ "answer": "...", "trace_id": "..." }`
- [ ] Route only invokes compiled graph — no RAG logic in the router
- [ ] Node failure → `{ "detail": "..." }` without raw stack trace

### 6. Evals (`tests/pipelines/test_agent_evals.py`)

- [ ] **Eval 1:** trace shows `retrieve` before `query` for a loan-policy question
- [ ] **Eval 2:** empty question never reaches `query` node in trace
- [ ] **Eval 3:** mocked pipeline — answer field populated when retrieve returns fixtures

Run: `uv run pytest tests/pipelines/ -q`

---

## Verify together

- [ ] Ask: _"How long can I keep a fiction book?"_ — inspect trace: `receive` → `retrieve` → `query`
- [ ] Ask with empty string — graph ends early; API returns clear error
- [ ] Break an edge on purpose — confirm compile fails before serving
- [ ] Show checkpoint history for one `thread_id` after two questions

---

## Discussion questions

1. Why is minimal state safer than passing the full conversation into every node?
2. What breaks if you compile the graph on every HTTP request instead of once at startup?
3. How would you add a fourth node (e.g. "escalate to human") without rewriting `retrieve` and `query`?
