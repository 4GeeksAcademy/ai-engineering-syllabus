# CONTEXT — Brasaland

## Milestone 7 — RAG & Knowledge Base

---

## 1. Introduction

At Brasaland, the **Operations** and **Marketing** teams constantly get the same questions from location managers, customers, and even new hires: how the points program works, what the waste protocols are, which dishes contain which allergens, how to order from suppliers. Today, every manager answers "their own way" based on what they remember — and that produces inconsistent answers between Colombia and Florida.

Felipe Guerrero (Operations Director) requested, via a **ticket**, an assistant that any location manager can use to answer **the way a trained salesperson would**: confidently, with the correct data, and without inventing information that isn't in the official manuals.

Your knowledge base must be built from the source documents in section 2. You must chunk them and turn them into embeddings — do not invent additional content beyond what these documents contain.

---

## 2. Knowledge Base Source Documents

Use the following source documents as the base for your knowledge base. Each has been split into its own file so you can load it directly into your chunking pipeline.

| File | Content |
|---|---|
| [`brasaland-loyalty-program.md`](brasaland-loyalty-program.md) | "Brasa Points" Loyalty Program |
| [`brasaland-waste-protocol.md`](brasaland-waste-protocol.md) | Waste Control Protocol |
| [`brasaland-menu-allergens.md`](brasaland-menu-allergens.md) | Menu Allergen Guide |
| [`brasaland-supplier-ordering.md`](brasaland-supplier-ordering.md) | Supplier Ordering Procedure |

---

## 3. Domain Data Structure

Every point you insert into Qdrant must include, at minimum, the following
payload:

```json
{
  "id": "chunk-uuid",
  "vector": [/* embedding */],
  "payload": {
    "company": "brasaland",
    "source_document": "loyalty-program | waste-protocol | menu-allergens | supplier-ordering",
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
- **Faithfulness**: the generated answer must not contain any numeric data
  (percentages, amounts, kg) that doesn't appear in the retrieved chunks.
- **Minimum similarity threshold**: define a threshold and document why you
  chose it; if no chunk exceeds it, the answer must explicitly state there
  isn't enough information — it must never make something up.

---

## 5. Seed Data Instructions

- At minimum, index all four complete source documents listed in section 2.
- Each document must produce at least 3 chunks (neither one chunk per
  document, nor one chunk per line).
- Save a `data/eval/test-queries.json` file with at least 8 test questions
  and the expected answer (or expected source chunk), covering all four
  documents.

---

## 6. Business Constraints

- Answers must stay in the base language chosen for the project; if you
  implement bilingual support, the answer must match the language of the
  question.
- Never answer "zero risk" to allergen questions — the wording of `brasaland-menu-allergens.md`
  must be followed literally.
- Dollar and Colombian peso amounts must be kept exactly as they appear in
  the source document; do not auto-convert currency unless a later
  milestone's CONTEXT explicitly asks for it.

---

## 7. Expected Deliverables

- A knowledge base indexed in Qdrant containing all four source documents.
- A FastAPI endpoint that answers questions like "how many points do I need
  for Gold tier?" or "does the BBQ Ribs dish have allergens?" with a
  generated, accurate answer traceable back to its source.
- A minimal query interface working against that endpoint.
