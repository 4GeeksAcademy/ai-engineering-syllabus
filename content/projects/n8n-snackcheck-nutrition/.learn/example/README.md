# In-Class Example: Quick Barcode Health Ping

> **Instructor note:** Live classroom example for concepts in `n8n-snackcheck-nutrition`. Use during class to walk students through webhook → API → IF → AI → Respond. **Do not assign as homework — guided classroom exercise.**

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The Scenario

### Scope note

Scoped for one live session. Same stack and core patterns as the official student project, but drops secondary requirements (full SemVer CHANGELOG, full `TC-XXX` suite, concern-score Code node, multi-tone AI routing). Students still follow the full brief in the project root `README.md`.

A founder wants a **tiny demo** for investors: paste a barcode, get back one short sentence — healthy or not — using real Open Food Facts data and a Groq LLM line.

**What you are learning:**

- Webhook `POST` + Respond to Webhook
- Keyless HTTP GET to Open Food Facts
- IF branching for missing product vs success
- One Groq node to phrase a friendly one-liner
- Why continue-on-error matters for `404` product-not-found

---

## Prerequisites

- Working n8n workspace
- Groq credential already created in the AI-integration course
- No Open Food Facts signup or key

---

## Step-by-step tasks

### 1. Diagram (5 minutes)

- [ ] Sketch: Webhook → Validate barcode present → HTTP Request → IF (found?) → Set fields → Groq → Respond
- [ ] Draw the not-found exit to a JSON Respond

### 2. Webhook + validation

- [ ] Create webhook `POST` path `/nutrition-check-demo`
- [ ] If body has no `barcode`, Respond with a short JSON usage message

### 3. Open Food Facts

- [ ] HTTP Request GET: `https://world.openfoodfacts.org/api/v2/product/{{barcode}}.json?fields=product_name,nutriscore_grade,nutriments`
- [ ] Configure continue on error / branch so `404` does not kill the run
- [ ] On not found: Respond JSON `{ "error": "product not found" }` with status `404`

### 4. One-liner AI verdict

- [ ] Set: product name + `nutriscore_grade`
- [ ] Groq: one encouraging or cautionary sentence from the letter grade only (keep it simple for class)
- [ ] Respond plain text `200`

### 5. Live demo barcodes

- [ ] Nutella `3017620422003`
- [ ] One Nutri-Score `a` product the instructor picks live

---

## What students still must do at home

Full SnackCheck rules (traffic lights + worse-of-two), concern score, tone-routed AI prompts, professional README / test log / CHANGELOG, and node naming `[Action] - [Purpose]` — see root `README.md`.
