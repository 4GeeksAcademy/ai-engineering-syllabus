# Maple Street Library — RAG Knowledge Base (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-milestone-rag-knowledge-base`. Same spine (four functions, Qdrant, similarity threshold, model-generated answers, FastAPI endpoint, minimal UI), different domain. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Maple Street Library** desk staff answer the same patron questions daily — loan periods, fine policy, how to reserve a room — buried in internal Markdown docs. Build a salesperson-style assistant for the **front-desk team**: natural-language answers from indexed policies, never raw search hits.

### Scope note

| Graded project (`ai-eng-milestone-rag-knowledge-base`) | This class example              |
| ------------------------------------------------------ | ------------------------------- |
| Full monorepo + `CONTEXT-company.md` documents         | Mini `library-api` + 3 MD files |
| Company-specific collection name                       | `maple_knowledge`               |
| Backoffice UI integration                              | Single page under `uis/`        |
| PR to student fork                                     | Local Qdrant via Docker         |

---

## Source documents (mini corpus)

Place under `data/raw/knowledge/`:

| File                   | Content hint                         |
| ---------------------- | ------------------------------------ |
| `loan-policy.md`       | Loan lengths, renewals, late fees    |
| `room-reservations.md` | Study room booking rules             |
| `membership-faq.md`    | Card types, guest passes, lost cards |

Chunk by `##` headings — each section becomes one or more chunks with `document` + `section` metadata.

---

## What to build

### 1. `data/process/rag.py`

- [ ] `setup()` — parse the three files, chunk by section, upsert to Qdrant collection `maple_knowledge`
- [ ] `embed(text)` — same model for chunks and queries (e.g. `sentence-transformers` or API embeddings)

### 2. `data/pipelines/rag.py`

- [ ] `retrieve(query, k=5, min_score=0.72)` — filter below threshold
- [ ] `query(question)` — desk-staff voice prompt + generation LLM; never return chunk list

### 3. API + UI

- [ ] `POST /knowledge/query` → `{ "answer": "..." }`
- [ ] Minimal page: text input, submit, answer area, loading/error states

### 4. Tests

- [ ] `tests/pipelines/test_rag.py` — mock Qdrant + LLM for `retrieve()` and `query()`

---

## Verify together

- [ ] Ask: _"How long can I keep a fiction book?"_ → answer cites loan policy, not raw JSON
- [ ] Ask nonsense: _"What's the weather on Mars?"_ → honest "not in knowledge base" style reply
- [ ] `retrieve()` with mocked low scores returns fewer than k hits
- [ ] Qdrant UI shows payloads with `document` and `section`

---

## Docker snippet (Qdrant)

```yaml
qdrant:
  image: qdrant/qdrant:latest
  ports:
    - "6333:6333"
```

Run `setup()` once after Qdrant is up; confirm point count matches chunk count.
