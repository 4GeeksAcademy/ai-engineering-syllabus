# Is This Snack Healthy? — Reference Solution

## Purpose

This project is a **no-code capstone** in n8n. There is no application repository to clone. A complete submission is a working webhook workflow plus professional deliverables (diagram, workflow README, `TC-XXX` test log, SemVer CHANGELOG).

**Do not ship a finished workflow JSON here** — students must build the flow themselves. This file is an instructor grading checklist and expected architecture shape.

## Expected architecture (high level)

1. **Webhook** — `POST /nutrition-check` with body `{ "barcode": "..." }`.
2. **Empty / missing barcode** → self-documenting JSON (`200`, `application/json`).
3. **Validation** — barcode present and numeric; else structured `400` with example.
4. **HTTP Request** — Open Food Facts `GET .../product/{barcode}.json?fields=...`, continue-on-error (or branch) so `404` + `status: 0` does not crash the flow.
5. **Not found** → structured `404` JSON with a valid example barcode.
6. **Insufficient nutrients** → `200` JSON "not enough data" (never classify blank fields as healthy).
7. **Extract** — flat fields including bracket notation for `energy-kcal_100g`.
8. **Classify** — sugar / salt / fat traffic lights; traffic-light reading + Nutri-Score reading; **overall = worse of the two** (traffic-light alone if Nutri-Score `unknown`/missing); concern score `0–3` via single-item **Code** node.
9. **AI (Groq)** — short verdict paragraph; **tone routed by level** (encouraging vs cautionary), not one fixed prompt.
10. **Respond** — verdict as plain text (`200`); docs / insufficient-data / errors as JSON with correct status codes.

## Required nodes (minimum)

Webhook, Respond to Webhook, HTTP Request (GET), IF, Merge (Append), Set / Edit Fields, Code (single item), Groq LLM.

Naming: `[Action] - [Purpose]` on every node. Inline docs on nodes.

## Classification reminder

| Source              | healthy | moderate | unhealthy |
| ------------------- | ------- | -------- | --------- |
| High-nutrient count | 0       | 1        | 2 or 3    |
| Nutri-Score         | a, b    | c        | d, e      |

Soda trap: traffic-light alone may look safe; poor Nutri-Score must win → overall `unhealthy`.

## Deliverables checklist

- [ ] Excalidraw diagram done first (decisions + error paths)
- [ ] Exported workflow JSON
- [ ] Workflow README (Purpose, How It Works, Setup, Usage, Error Handling, Limitations)
- [ ] Test log `TC-XXX` (functional, integration, error, performance)
- [ ] CHANGELOG (SemVer)
- [ ] No secrets in exports; Groq key only via n8n credentials

## Suggested test barcodes

- Nutella `3017620422003` (Nutri-Score `e`) — cautionary path
- Coca-Cola `5449000000996` — soda / Nutri-Score override path
- Student-chosen Nutri-Score `a` — encouraging path
- Unknown barcode — `404` path
- Empty body / non-numeric — docs / `400` paths
