# CONTEXT — TrackFlow

## Milestone 7 — RAG & Knowledge Base

---

## 1. Introduction

Miguel Torres (Commercial Director) has 8 people between account managers and business development who constantly answer the same questions from prospect and current client brands: what delivery SLA they offer, how the returns policy works, which carriers cover which zones, how storage fees are calculated.

The **ticket** the commercial team handed off to tech asks for an assistant any account manager can use **the way a TrackFlow salesperson would** on a call with a client: with exact data, and never promising terms that don't exist in the standard agreements.

Your knowledge base must be built from the source documents in section 2.

---

## 2. Knowledge Base Source Documents

Use the following source documents as the base for your knowledge base. Each has been split into its own file so you can load it directly into your chunking pipeline.

| File | Content |
|---|---|
| [`trackflow-sla-delivery.en.md`](trackflow-sla-delivery.en.md) | Delivery SLA |
| [`trackflow-returns-policy.en.md`](trackflow-returns-policy.en.md) | Returns Policy |
| [`trackflow-carrier-coverage.en.md`](trackflow-carrier-coverage.en.md) | Carrier Coverage |
| [`trackflow-storage-pricing.en.md`](trackflow-storage-pricing.en.md) | Storage Pricing |

---

## 3. Domain Data Structure

```json
{
  "id": "chunk-uuid",
  "vector": [/* embedding */],
  "payload": {
    "company": "trackflow",
    "source_document": "sla-delivery | returns-policy | carrier-coverage | storage-pricing",
    "section": "title or subtitle of the source section",
    "language": "en",
    "chunk_index": 0
  }
}
```

---

## 4. Answer KPIs and Thresholds

- **Recall@3**: at least 80% of test questions must have the correct chunk
  among the top 3 retrieved results.
- **Faithfulness**: no percentage, rate, or timeframe in the answer may
  differ from the retrieved chunks.
- Questions about storage discounts or carrier exceptions outside what's
  documented must answer that they require approval, never invent a
  condition.

---

## 5. Seed Data Instructions

- Index all four complete source documents listed in section 2.
- Each document must produce at least 3 chunks.
- Create `data/eval/test-queries.json` with at least 8 questions covering
  all four documents, including at least one about high-demand peaks
  (Black Friday / Sales).

---

## 6. Business Constraints

- A delivery SLA must never be promised during declared high-demand dates —
  the warning in `trackflow-sla-delivery.en.md` must be followed.
- International returns must never be described as "automatic" — they must
  always be referred to manual handling.
- No storage discount can be offered without mentioning it requires Miguel
  Torres's approval.

---

## 7. Expected Deliverables

- A knowledge base indexed in Qdrant containing all four source documents.
- A FastAPI endpoint that answers questions like "what's the standard
  return window?" or "which carrier best covers rural Aragón?" with a
  generated answer traceable back to its source.
- A minimal query interface working against that endpoint.
