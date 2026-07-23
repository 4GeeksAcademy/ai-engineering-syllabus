# Is This Snack Healthy? — A Nutrition-Check Automation

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo), [@WaficMikati](https://github.com/WaficMikati) and [other contributors](https://github.com/4GeeksAcademy) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

---

## 🎯 Challenge

This is your **capstone**: one automation that puts together everything you have built across this microsyllabus. No new nodes, no new tricks — just you, proving you can take a real product idea and turn it into a working, well-documented automation on your own.

Here is the situation.

A founder is building a small consumer app called **SnackCheck**. The idea is simple: a shopper points their phone at a packaged food, the app reads the barcode, and a moment later it tells them — in plain, friendly language — whether that product is a smart everyday choice or something to keep as an occasional treat. The founder is not technical. They know exactly what they want the experience to feel like, but they have no idea how to build it, and they have hired you to make the engine behind it.

They have sent you a rough brief by email:

> Hey — thanks again for taking this on. Here's what I'm picturing.
>
> The app sends a product's **barcode** to your automation, and your automation sends back a short **verdict** the user can read. Something human, like a knowledgeable friend at the supermarket — encouraging when the product is fine, and gently honest when it really isn't.
>
> I don't want to invent nutrition data ourselves. I've heard there's a free, open database (**Open Food Facts**) that already has this for millions of products, including that "Nutri-Score" letter. Please use real data from there.
>
> A few things I care about a lot:
>
> - If someone hits the automation with **no barcode**, it should politely **explain itself** — what it does and how to use it. I don't want a scary blank error.
> - If the barcode is **missing or not a number**, or if the product **isn't in the database**, the answer should be a clear, helpful message — never a crash.
> - The final verdict a shopper reads should be **easy on the eyes**: a headline, the key numbers with a red/green marker, then the friendly paragraph.
>
> I attached my "healthy vs not" rules on the next page. Excited to see it work!

The rules the founder attached become your specification. Read them carefully — some of what you need is written here, not in a checklist:

> #### SnackCheck classification rules
>
> Look at three nutrients, measured **per 100 g**, and label each one using a traffic-light rule:
>
> - **Sugar** — `low` under 5 g · `medium` between 5 and 22.5 g · `high` over 22.5 g
> - **Salt** — `high` over 1.5 g
> - **Fat** — `high` over 17.5 g
>
> Then work out **two independent readings** of the product, and let the verdict level be the **worse** of the two:
>
> 1. **Traffic-light count** — based on **how many** nutrients came out `high`:
>    - `0` high nutrients → **healthy**
>    - exactly `1` high nutrient → **moderate**
>    - `2` or `3` high nutrients → **unhealthy**
> 2. **Nutri-Score** (`nutriscore_grade`, straight from the API):
>    - `a` or `b` → **healthy**
>    - `c` → **moderate**
>    - `d` or `e` → **unhealthy**
>
> The **overall verdict level is whichever of the two is worse** — a product only counts as `healthy` if _both_ readings agree it's fine. This matters: a sugary soda can look "safe" on the traffic-light count alone (its numbers per 100 ml don't cross the `high` thresholds), but its Nutri-Score already tells the real story, and that must win.
>
> If `nutriscore_grade` is **`unknown` or missing**, fall back to the **traffic-light count alone**. And if the **nutrient fields are also missing or empty**, **don't classify at all**: respond that the product **doesn't have enough data**. A product with no data should never come out as "healthy" just because the fields are blank.
>
> Also produce a **concern score**: simply the count of `high` nutrients (a number from 0 to 3). It's a quick at-a-glance signal we may show later — it is not part of how the verdict level itself is decided.
>
> The written verdict's **tone must match the level**: encouraging for `healthy` and `moderate`, gently cautionary for `unhealthy`.

You have built every piece of this before — a webhook that answers, an API call, branching logic, a small calculation, an AI step, a formatted response. The capstone is doing it **end to end, by yourself, cleanly**, and shipping it like a professional would.

### 📚 A little context you'll need

Two pieces of background that live outside the automation itself:

**The Nutri-Score and traffic lights.** Nutri-Score is a single letter (`a` = best to `e` = worst) that summarizes how healthy a product is; it comes straight from the database. The **traffic-light** idea (green/amber/red per nutrient) is a well-known public-health way of flagging sugar, salt, and fat at a glance. Your automation reproduces that traffic-light judgment using the founder's thresholds — you are not inventing nutrition science, just applying a rule sheet.

**The data source (Open Food Facts).** It is free, open, and needs **no key and no signup**. You fetch one product at a time by its barcode:

```
GET https://world.openfoodfacts.org/api/v2/product/{barcode}.json?fields=product_name,brands,nutriscore_grade,nutriments
```

- It always returns **one flat product object**. Read the fields you need by key: `product_name`, `brands`, `nutriscore_grade`, and inside `nutriments` → `sugars_100g`, `salt_100g`, `fat_100g`, and `energy-kcal_100g`.
- ⚠️ The energy field has a hyphen in its name, so read it with **bracket notation**: `{{ $json.nutriments['energy-kcal_100g'] }}`.
- The API tells you whether the product was found through **both** the HTTP status and the response body. A found product answers `200` with `status: 1`. A **missing** product answers `404`, with a body like `{"code":"...", "status":0, "status_verbose":"product not found"}`. ⚠️ Because it's a `404`, your **HTTP Request** node will treat it as a failed call by default — configure it to continue on error (or branch on the response) so you can read that body and route it to your "not found" response instead of crashing the workflow.
- Test barcodes: **Nutella `3017620422003`** (Nutri-Score `e`) and **Coca-Cola `5449000000996`**. Find a product with **Nutri-Score `a`** yourself, so you can prove the "encouraging" path works too.

---

## 🌱 How to Start the Project

There is no repository to clone here — this is a **no-code** build. You work entirely inside **n8n**, the same way you have all course long.

1. Open your n8n workspace and **create a new, empty workflow**.
2. **Diagram before you build.** Open Excalidraw and sketch the whole flow first — the trigger, the decisions, the error exits, the AI step, the final response. Building from a diagram is the professional habit you practiced in the capstone-process course; do not skip it.
3. The **only credential** this project needs is your **Groq key** for the AI step — and you already created it back in the AI-integration course. Everything else (Open Food Facts) is keyless.
4. Build layer by layer, testing each part before moving on, exactly as you learned.

---

## 💻 What You Need to Do

Build a single n8n workflow that takes a barcode and returns a health verdict, following the founder's brief and rules above.

**Design first**

- [ ] Produce a **workflow diagram** in Excalidraw before building: standard shapes, decision diamonds, clearly drawn error paths, one clean flow direction.

**Input & validation**

- [ ] Accept a **`POST`** request on a webhook at the path `/nutrition-check`, expecting a body like `{ "barcode": "3017620422003" }`.
- [ ] If the request arrives **empty / with no barcode**, respond with a **self-documenting** JSON message that explains the service, the required field, and an example.
- [ ] **Validate** the input: the barcode must be present **and** numeric. If not, respond with a clear, structured error (with a helpful message and an example).

**Data**

- [ ] Call the **Open Food Facts** endpoint with the barcode injected into the URL.
- [ ] Handle the **not-found** case (a `404` response with `status: 0` in the body) with a friendly, structured "product not found" response that includes a valid example barcode.
- [ ] **Check for missing nutrient data**: if the found product's nutrient fields are also missing or empty, don't attempt to classify it — respond with a clear "not enough data" message instead.
- [ ] **Extract** the fields you need into flat variables — remember the bracket notation for the energy field.

**Logic**

- [ ] **Classify** sugar, salt, and fat per 100 g using the founder's traffic-light thresholds, and set a flag for each. (Only reached once you've confirmed the product has usable nutrient data.)
- [ ] Work out the **traffic-light reading** (`healthy` / `moderate` / `unhealthy`) from the number of `high` nutrients, and the **Nutri-Score reading** from `nutriscore_grade`.
- [ ] Set the **overall verdict level** to the **worse of the two readings** — falling back to the traffic-light reading alone when `nutriscore_grade` is `unknown` or missing.
- [ ] Compute the **concern score** (0–3) with a single-item calculation, from the traffic-light flags only.

**Intelligence (AI)**

- [ ] Have the **AI write a short verdict paragraph** using the product name, the numbers, and the flags.
- [ ] Make the **tone adapt to the verdict level** — encouraging for `healthy`/`moderate`, gently cautionary for `unhealthy`. (This is the "AI inside your decision logic" pattern; make sure it is genuinely exercised, not a single fixed prompt.)

**Output**

- [ ] Build a **formatted, multi-section** verdict message: an emoji headline, the key numbers aligned with red/green markers, then the AI paragraph.
- [ ] Return the **verdict as plain text**; return **self-documentation, insufficient-data, and error responses as JSON** — with the matching `Content-Type` and status codes: `200` for the verdict and for docs/insufficient-data, `400` for validation errors, `404` for not-found.

⚠️ **IMPORTANT — a few ground rules:**

- Make sure you use, at least, the nodes you learned across this course: Webhook, Respond to Webhook, HTTP Request (GET), IF, Merge (Append), Set / Edit Fields, Code (single item), and the Groq LLM node.
- The **Code** node does **one small calculation on one item** (the concern score). No loops over arrays.
- Every API must be **keyless and signup-free**. Your Groq key is the only account in the whole project — and it already exists.

**Ship it like a professional**

- [ ] Rename **every node** with the `[Action] - [Purpose]` convention (e.g. `API Call - Open Food Facts Product`, `Validate - Barcode Present`, `AI - Health Verdict (Cautionary)`).
- [ ] Add **inline documentation** to your nodes, and write a **workflow README** with the sections you practiced: Purpose, How It Works, Setup, Usage, Error Handling, Limitations.
- [ ] Keep a **test log in `TC-XXX` format** covering the four test types: functional (valid barcode → verdict), integration (the live API), error (unknown barcode, malformed input, empty body, product with no nutrition data), and a short performance note.
- [ ] Maintain a **CHANGELOG** following SemVer.

---

## ✅ What We Will Evaluate

- [ ] A **diagram** exists and was clearly done first: correct shapes, decision diamonds, visible error paths, one clean direction.
- [ ] The webhook accepts a `POST` barcode and returns a response through the Respond node.
- [ ] An **empty request** returns a self-documenting JSON usage message.
- [ ] **Validation** rejects a missing or non-numeric barcode with a structured `400` and a helpful example.
- [ ] The **Open Food Facts** call works with the barcode injected, and the **not-found path** (a `404` with `status: 0`) is handled without crashing and returns a structured `404` of your own to the user.
- [ ] A product that is found but has no nutrition data returns an "insufficient data" response, not a verdict.
- [ ] Fields are **extracted correctly**, including the energy field via bracket notation.
- [ ] Sugar, salt, and fat are **classified correctly** against the thresholds; the **overall level** correctly takes the **worse** of the traffic-light reading and the Nutri-Score reading (with the fallback applied when `nutriscore_grade` is `unknown` or missing); the **concern score** is correct.
- [ ] A high-sugar product with a poor Nutri-Score (e.g. a soda) is **not** misclassified as `healthy` just because none of its per-100g numbers cross the `high` thresholds.
- [ ] An **AI verdict** is produced, and its **tone changes** with the verdict level through conditional routing (not one fixed prompt).
- [ ] The final verdict is a **clean, multi-section** plain-text message with red/green markers; docs, insufficient-data, and error responses are all JSON, with correct `Content-Type` and status codes (`200` / `400` / `404` as applicable).
- [ ] **Node names** follow `[Action] - [Purpose]`; nodes are documented inline; the **workflow README** has all required sections.
- [ ] The **test log** uses `TC-XXX` and covers functional, integration, error, and performance.
- [ ] A **CHANGELOG** with SemVer is present.
- [ ] The build uses the nodes learned in this course, and every API besides Groq is **keyless**.

> Note: this is a single-request, single-product automation, so you won't need array handling or loops to solve it — keep the Code node's calculation to a single item.

---

## 📦 How to Submit

1. **Export your finished workflow** from n8n as a JSON file (workflow menu → _Download_).
2. Gather the full set of deliverables: the **workflow JSON**, your **Excalidraw diagram**, the **workflow README**, the **test log**, and the **CHANGELOG**.
3. Submit them together the way your instructor indicates.

Make sure your automation is proven end to end: an unhealthy product returns a cautionary verdict, a Nutri-Score `a` product returns an encouraging one, a high-sugar/poor-Nutri-Score product like a soda is correctly caught as unhealthy, a product with no nutrition data gets the insufficient-data response instead of a verdict, and every error path answers gracefully.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo), [@WaficMikati](https://github.com/WaficMikati) and [other contributors](https://github.com/4GeeksAcademy). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
