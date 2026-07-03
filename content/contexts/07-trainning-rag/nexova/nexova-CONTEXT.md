# CONTEXT — Nexova

## Milestone 7 — RAG & Knowledge Base

---

## 1. Introduction

Marcos Ibáñez (Sales Director) has 18 people between account managers and SDRs repeating the same explanations to every prospect: what each service line includes, how the pricing model works, how long a typical headhunting process takes. When an SDR is new, it takes them weeks to give confident answers without escalating to a senior account manager.

The **brief** Marcos sent through an internal **RFP** asks for an assistant any SDR can use before or during a call with a prospect, answering **from the perspective of a Nexova salesperson**: confident, closing-oriented, and never inventing commercial terms that don't exist.

Your knowledge base must be built from the source documents in section 2.

---

## 2. Knowledge Base Source Documents

Use the following source documents as the base for your knowledge base. Each has been split into its own file so you can load it directly into your chunking pipeline.

| File | Content |
|---|---|
| [`nexova-service-lines.md`](nexova-service-lines.md) | Service Lines |
| [`nexova-pricing-model.md`](nexova-pricing-model.md) | Pricing Model |
| [`nexova-hiring-process-sla.md`](nexova-hiring-process-sla.md) | Hiring Process SLA |
| [`nexova-objection-handling.md`](nexova-objection-handling.md) | Handling Common Prospect Objections |

---

## 3. Domain Data Structure

```json
{
  "id": "chunk-uuid",
  "vector": [/* embedding */],
  "payload": {
    "company": "nexova",
    "source_document": "service-lines | pricing-model | hiring-process-sla | objection-handling",
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
- **Faithfulness**: no percentage, amount, or timeframe mentioned in the
  answer may differ from what's stated in the retrieved chunks.
- For questions about discounts or conditions not covered in the documents
  (for example, a discount from 22% to 15%), the answer must state that
  condition requires approval and must not invent it.

---

## 5. Seed Data Instructions

- Index all four complete source documents listed in section 2.
- Each document must produce at least 3 chunks.
- Create `data/eval/test-queries.json` with at least 8 questions, including
  at least two real sales objections taken from `nexova-objection-handling.md`.

---

## 6. Business Constraints

- A discount below the 22% fee must never be offered in a generated
  answer — the system must defer that decision to a human.
- Delivery times must always be presented as averages, not guarantees,
  except for the 6-month replacement guarantee, which is contractual.
- Answers about competitor clients must maintain the transparency indicated
  in `objection-handling.md`.

---

## 7. Expected Deliverables

- A knowledge base indexed in Qdrant containing all four source documents.
- A FastAPI endpoint that answers questions like "how much does an 8-week
  training program cost?" or "what happens if the shortlist doesn't work
  for me?" with a generated answer traceable back to its source.
- A minimal query interface working against that endpoint.
