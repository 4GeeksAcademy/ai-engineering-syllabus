# CONTEXT — HealthCore

## Milestone 7 — RAG & Knowledge Base

---

## 1. Introduction

Priya Nair (Head of Patient Experience) has 8 patient coordinators who constantly answer the same questions at the front desk and over the phone: which insurance is accepted, how the cancellation policy works, how long an internal referral takes, what documents a new patient needs. When a coordinator is new, they make mistakes due to inconsistent information across the 12 clinics.

The **memo** Priya sent to the HealthCore Digital team asks for an assistant any coordinator can use at the desk **the way the clinic's best service salesperson would**: clear, empathetic, and never inventing insurance coverage or policies that don't exist.

> ⚠️ **Regulatory note:** this milestone works exclusively with policy, procedure, and service-catalog content — **never with real patient data**. No document in this knowledge base should contain real PHI (Protected Health Information). The examples here are fictional and for educational use only.

Your knowledge base must be built from the source documents in section 2.

---

## 2. Knowledge Base Source Documents

Use the following source documents as the base for your knowledge base. Each has been split into its own file so you can load it directly into your chunking pipeline.

| File | Content |
|---|---|
| [`healthcore-insurance-coverage.md`](healthcore-insurance-coverage.md) | Accepted Insurance Coverage |
| [`healthcore-appointment-policy.md`](healthcore-appointment-policy.md) | Appointment and Cancellation Policy |
| [`healthcore-referral-process.md`](healthcore-referral-process.md) | Internal Referral Process |
| [`healthcore-new-patient-checklist.md`](healthcore-new-patient-checklist.md) | New Patient Checklist |

---

## 3. Domain Data Structure

```json
{
  "id": "chunk-uuid",
  "vector": [/* embedding */],
  "payload": {
    "company": "healthcore",
    "source_document": "insurance-coverage | appointment-policy | referral-process | new-patient-checklist",
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
- **Faithfulness**: no coverage, fee, or timeframe data in the answer may
  differ from the retrieved chunks.
- For questions about insurance coverage not listed, the answer must state
  it needs to be verified with billing — it must never confirm undocumented
  coverage.

---

## 5. Seed Data Instructions

- Index all four complete source documents listed in section 2.
- Each document must produce at least 3 chunks.
- Create `data/eval/test-queries.json` with at least 8 questions covering
  all four documents.
- **Do not add any additional data that simulates a real patient record**
  (name, diagnosis, medical record number). The entire knowledge base must
  be limited to policies and procedures.

---

## 6. Business Constraints

- No chunk or generated answer may contain real or simulated-to-look-real
  PHI — this is a HIPAA / UK GDPR constraint that applies across the whole
  project.
- Answers about insurance coverage must explicitly distinguish between the
  United States and the United Kingdom when the question doesn't specify
  the country.
- No-show fees must never be applied to Medicare or Medicaid patients in a
  generated answer — `healthcore-appointment-policy.md` must be followed literally.

---

## 7. Expected Deliverables

- A knowledge base indexed in Qdrant containing all four source documents.
- A FastAPI endpoint that answers questions like "is there a charge for
  cancelling 12 hours in advance?" or "what do I need to bring to my first
  appointment?" with a generated answer traceable back to its source.
- A minimal query interface working against that endpoint.
