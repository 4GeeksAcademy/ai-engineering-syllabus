# Maple Street Library — MCP Server (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-mcp-company-tools`. Same spine (FastMCP server, OAuth auth, discovery schemas, read-write + read-only tools, explicit write rejection, invocation logs, MCP Playground validation), different scope than the company monorepo. Builds on the Maple Street Library narrative from prior class examples. Students still follow the full brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Maple Street Library** desk staff already query loans and the catalog from inside a small agent. Any other integration would have to reimplement those same HTTP calls.

Your live demo goal: expose loan management and **read-only** catalog lookup as an independent **MCP Server** (OAuth protected) and validate it — without touching the full company monorepo.

### Scope note

| Graded project (`ai-eng-mcp-company-tools`) | This class example                                |
| ------------------------------------------- | ------------------------------------------------- |
| Company monorepo + real Incidents Manager   | Mini `library-api` with in-memory or TinyDB loans |
| Inventory module from Milestone 5           | Pre-seeded `catalog.json` (read-only)             |
| LangGraph agent migration                   | Discussed verbally; optional stretch only         |
| Streamable HTTP vs stdio debate in PR       | **stdio** transport only                          |
| TypeScript MCP client                       | Small Python client script                        |
| Full evaluation rubric                      | Local demo + one write-rejection test             |

---

## Prerequisites

- [ ] Python 3.11+ with `uv` (or venv)
- [ ] `fastmcp` installed: `uv add fastmcp`
- [ ] Optional: Maple Street `library-api` from earlier sessions — or use the stub data below

### Seed data (indicative)

**Loans** (mutable store):

```json
[
  {
    "loan_id": 1,
    "patron_id": "P-042",
    "book_isbn": "978-0143127550",
    "status": "active"
  }
]
```

**Catalog** (read-only file `data/catalog.json`):

```json
[
  {
    "isbn": "978-0143127550",
    "title": "The Night Circus",
    "copies_available": 2
  }
]
```

---

## What to build

### 1. MCP Server (`mcp_server/server.py`)

- [ ] FastMCP app with **stdio** transport
- [ ] OAuth access token from env / Authorization header — reject list + invoke without valid token

### 2. Tool: `manage_book_loan`

- [ ] Actions: `create`, `update`, `get_status`
- [ ] Input schema: `loan_id`, `action`, optional `patron_id`, `book_isbn`, `status`
- [ ] Description + output schema clear enough for MCP discovery alone

| Action       | Behavior                          |
| ------------ | --------------------------------- |
| `create`     | Insert new loan row               |
| `update`     | Change `status` (e.g. `returned`) |
| `get_status` | Return loan fields or `not_found` |

### 3. Tool: `query_catalog` (read-only)

- [ ] Lookup by `isbn` or list all titles
- [ ] If client sends `action: "update"` or any write field → reject explicitly:

```json
{
  "error_code": "CATALOG_WRITE_FORBIDDEN",
  "message": "Catalog tool is read-only.",
  "tool": "query_catalog"
}
```

### 4. Auth errors (distinct codes)

| Scenario              | Code                      |
| --------------------- | ------------------------- |
| Missing token         | `AUTH_MISSING_TOKEN`      |
| Invalid / expired     | `AUTH_INVALID_TOKEN`      |
| Catalog write attempt | `CATALOG_WRITE_FORBIDDEN` |
| Bad input             | `VALIDATION_ERROR`        |

### 5. Invocation logging

- [ ] One structured log line per call: `client_id`, `tool`, `result`, `duration_ms`

### 6. MCP client (`scripts/mcp_client_demo.py`)

- [ ] Connect with valid OAuth access token
- [ ] List tools — assert names + descriptions present
- [ ] Run: create loan → get status → catalog query → catalog write attempt (expect `CATALOG_WRITE_FORBIDDEN`)

---

## Verify together

- [ ] Server starts; client lists two tools via discovery
- [ ] Client without token cannot list tools
- [ ] `manage_book_loan` create + `get_status` returns expected fields
- [ ] `query_catalog` returns `copies_available` for known ISBN
- [ ] Catalog write attempt fails with `CATALOG_WRITE_FORBIDDEN` (not generic error)
- [ ] Terminal shows at least one log entry per tool invoked

---

## Discussion questions

1. Why is **stdio** enough for a local agent but insufficient when multiple remote teams need the same server?
2. What is the difference between **omitting** a write endpoint and **explicitly rejecting** write attempts on the catalog tool?
3. If you migrated the Maple Street LangGraph agent next, which node would you replace — and how would you avoid two paths to the same loan data?
