# Support Agent with LangGraph — Part 1 — Reference Solution

Reference quality bar for the student's company monorepo fork. Paths and collection names below are **indicative** — students must align with their assigned `CONTEXT-company.md` and existing RAG pipeline layout.

---

## Architecture overview

```mermaid
flowchart LR
  UI[Client / UI] -->|POST question| API[POST /agent/query]
  API --> GRAPH[Compiled LangGraph]
  GRAPH --> RECV[receive_question]
  RECV -->|needs_retrieval| RETN[retrieve_node]
  RETN -->|context_ready| QN[query_node]
  QN --> ANS[answer + trace]
  ANS --> API
  RETN -.->|imports| RAG[data/pipelines retrieve]
  QN -.->|imports| QFN[data/pipelines query]
  GRAPH --> CP[(Checkpointer)]
  GRAPH --> TR[Trace store / LangSmith]
```

**Design invariants:**

1. Existing RAG functions (`retrieve`, `query`, `embed`, `setup`) stay in `data/pipelines/` — graph nodes import them, never duplicate logic.
2. Graph state is minimal: question, retrieved context, partial/final answer, trace metadata — not full chat history.
3. Graph is compiled once at startup; structural errors fail at import/compile time.
4. Endpoint is a thin adapter: validate input, invoke graph, map errors — no RAG business logic in the route.
5. Every run produces a queryable trace (LangSmith run, structured JSON log, or checkpoint history).

---

## Expected file layout

| Area          | Path (indicative)                     | Purpose                                           |
| ------------- | ------------------------------------- | ------------------------------------------------- |
| Graph state   | `services/agent/state.py`             | TypedDict / Pydantic state schema                 |
| Nodes         | `services/agent/nodes.py`             | `receive_question`, `retrieve_node`, `query_node` |
| Graph builder | `services/agent/graph.py`             | Nodes, conditional edges, compile + checkpointer  |
| Tracing       | `services/agent/tracing.py`           | Trace collector or LangSmith callback wiring      |
| API router    | `services/app/routers/agent.py`       | `POST /agent/query`                               |
| Evals         | `tests/pipelines/test_agent_evals.py` | ≥3 trace/answer assertions                        |

---

## Graph state (minimal)

```python
from typing import TypedDict, Annotated, Sequence
import operator

class AgentState(TypedDict):
    question: str
    retrieved_context: list[dict] | None
    answer: str | None
    trace_steps: Annotated[Sequence[dict], operator.add]
    error: str | None
```

Justification: nodes only need the current question, retrieval output, and accumulated trace — not prior turns.

---

## Nodes and conditional edges

| Node               | Responsibility                                           | Output condition                                                 |
| ------------------ | -------------------------------------------------------- | ---------------------------------------------------------------- |
| `receive_question` | Normalize/validate input, seed trace                     | Always route to retrieval when question non-empty                |
| `retrieve_node`    | Call `data.pipelines.retrieve(question)`                 | Route to `query_node` when context returned (even if empty list) |
| `query_node`       | Call `data.pipelines.generate_answer(question, context)` | End graph with final answer                                      |

> **Contract:** `query_node` calls the isolated generation step (`generate_answer`), **not** the monolithic `query()`. Reusing `query()` here would re-run `retrieve()` inside the node, duplicating work and hiding the retrieval step from the trace. If a student's RAG only exposes `query(question)`, the accepted fix is to overload it as `query(question, context=None)` that skips retrieval when `context` is passed — never a single node doing retrieve + generate silently.

Routing function example (not a hardcoded linear chain only):

```python
def after_receive(state: AgentState) -> str:
    if not state.get("question", "").strip():
        return "end"
    return "retrieve"

def after_retrieve(state: AgentState) -> str:
    if state.get("error"):
        return "end"
    return "query"
```

---

## Compilation and checkpointing

```python
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

def build_agent_graph():
    builder = StateGraph(AgentState)
    builder.add_node("receive_question", receive_question)
    builder.add_node("retrieve", retrieve_node)
    builder.add_node("query", query_node)
    builder.set_entry_point("receive_question")
    builder.add_conditional_edges("receive_question", after_receive, {"retrieve": "retrieve", "end": END})
    builder.add_conditional_edges("retrieve", after_retrieve, {"query": "query", "end": END})
    builder.add_edge("query", END)
    checkpointer = MemorySaver()
    return builder.compile(checkpointer=checkpointer)
```

Compile at module load or FastAPI lifespan — never per request without caching.

---

## Tracing

Each node appends to `trace_steps`:

```python
{"node": "retrieve", "order": 2, "output_summary": "3 chunks above threshold"}
```

Alternative: LangSmith via `LANGCHAIN_TRACING_V2=true` and run metadata. PR must include screenshot or JSON export of one full run.

---

## Endpoint contract

**Request**

```json
{ "question": "What is the return policy for enterprise clients?" }
```

**Success (200)**

```json
{
  "answer": "Enterprise clients may return within 30 days...",
  "trace_id": "run-abc123"
}
```

**Graph/node failure (4xx/5xx — no raw stack trace)**

```json
{ "detail": "Agent failed during retrieval. Check trace run-abc123." }
```

---

## Evals (`tests/pipelines/`)

Run with a single command, e.g. `uv run pytest tests/pipelines/ -q`.

| Eval            | Input                        | Criterion                                                    |
| --------------- | ---------------------------- | ------------------------------------------------------------ |
| Node order      | Fixed FAQ question           | Trace shows `retrieve` before `query`                        |
| Grounded answer | Policy question from CONTEXT | Answer mentions expected entity; not empty                   |
| Error path      | Empty question               | Trace ends without `query`; clear error in state or response |

Evals assert against saved trace fixtures or checkpoint snapshots — not live LLM calls on every CI run when mocked.

The "Grounded answer" eval is an **acceptance gate**, not optional color: the existing RAG tests must still pass alongside these agent evals. A submission with correct node order/routing but answers that drift from CONTEXT policies fails review.

---

## Validation checklist

- [ ] State schema is minimal; no unjustified full history.
- [ ] Three single-responsibility nodes; edges use conditional routing (≥1 real condition, e.g. empty question or no-context → honest/END branch).
- [ ] Generation node calls the isolated `generate_answer`/`query(question, context)` — no single node re-runs the monolithic retrieve + generate.
- [ ] Graph compiled before serving; broken graph fails at startup.
- [ ] Checkpointer attached; at least one transition inspectable.
- [ ] Queryable trace per run.
- [ ] ≥3 evals in `tests/pipelines/`.
- [ ] `POST /agent/query` delegates to graph only.
- [ ] Existing RAG pipeline functions reused from `data/pipelines/`.
