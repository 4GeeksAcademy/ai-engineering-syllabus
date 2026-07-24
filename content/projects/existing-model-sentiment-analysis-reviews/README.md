# Sentiment Analysis on Customer Reviews — WeLoveReviews

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/repo-name/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

You're working as a freelance AI engineer for a small data consultancy. Your latest client, **WeLoveReviews**, helps companies understand what their customers really think. They've just onboarded a new account: a business with an average rating of **4.5 / 5**, but the account manager has a nagging doubt — _does the sentiment expressed in the written reviews actually match that score?_ Before they hand a report to their client, they want a second opinion built on data, not gut feeling.

You don't have time (or the data) to train a model from scratch — and you don't need to. Plenty of pretrained models on Hugging Face already know how to read sentiment in text. Your job is to explore the data, integrate one correctly, validate its output against reality, and turn raw text into something the account manager can actually use.

> The account manager shared this with you over email:
>
> "We're handing this client 500 written reviews next week. I need to know, in plain terms, how many of these reviews read as positive, neutral, or negative — and whether that breakdown lines up with their 4.5-star average. If there's a gap, I want to understand where it's coming from before we put it in front of the client."

---

## 📓 How this team communicates

On this team, leaders treat **Jupyter notebooks as communication documents** for analysis and data-processing work — not throwaway scratchpads. Your narrative deliverable is **`src/explore.ipynb`**: an executed notebook that walks a reader from objectives through exploration, insights, modeling decisions, results, and conclusions. Short markdown between major code blocks is expected; the notebook should stand on its own without a separate client-facing markdown report.

> **Work order:** You may run the EDA prompt first, then prepend objectives and continue with the rest of the project in the **same** `src/explore.ipynb` so the final file follows the full arc below.

---

## 🤖 Model note

**Model to use:** [`nlptown/bert-base-multilingual-uncased-sentiment`](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment) from Hugging Face.

> ⚠️ **Domain mismatch:** This model was fine-tuned on **product reviews** (e.g. Amazon-style ratings). Your dataset is **service reviews** — customers talk about staff, wait times, and ambiance. That mismatch can produce **false negatives**: reviews that read positive to a human (or carry a high star rating) but get classified as low sentiment. You must use this model first anyway — finding and explaining those false negatives is part of the assignment.

This model predicts sentiment as a **star rating from 1 to 5** (not a simple POSITIVE/NEGATIVE label). Map the output to sentiment bands:

| Model prediction | Sentiment band |
| ---------------- | -------------- |
| 1–2 stars        | Negative       |
| 3 stars          | Neutral        |
| 4–5 stars        | Positive       |

**Integration rules:**

- Load via `pipeline()` or `from_pretrained()` — do **not** download weights and commit them to your repo.
- Load the model **once** before the inference loop, not inside a per-review loop.
- **Pin** the model name/version in your code — don't silently depend on whatever "latest" resolves to when someone else clones your repo.

---

## 🌱 How to Start

1. Fork the [machine-learning-python-template](https://github.com/4GeeksAcademy/machine-learning-python-template) repository and, if available, select the 4GeeksAcademy account.
2. Open it in GitHub Codespaces, or clone it locally if you prefer to work on your own machine.
3. Download the provided [reviews.csv](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/existing-model-sentiment-analysis-reviews/reviews.csv) file from the platform and place it in **`data/raw/reviews.csv`** in your repository.
4. Extend **`requirements.txt`** with `transformers` and `torch` (or your chosen backend) — **pin versions**.
5. Read the full [instructions on how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project) if this is new to you.

---

## 🧪 EDA with your coding agent

Before modeling, explore the dataset with help from your coding agent:

1. Open **[PROMPT.md](./PROMPT.md)** in this project folder.
2. Copy everything below the header line into your agent (Cursor, Copilot, Claude Code, etc.).
3. Let the agent work in the **EDA section** of **`src/explore.ipynb`** — exploration, insights, and cleaning proposal only.

The prompt stops after EDA. Everything below is your job in the same notebook and in `src/app.py`.

---

## 💻 What You Need to Do

Complete the full notebook arc in **`src/explore.ipynb`** (with **executed outputs**):

- [ ] **Objectives** — frame the business question (written sentiment vs 4.5-star average).
- [ ] **EDA / insights / cleaning** — use the agent prompt output; short markdown between steps.
- [ ] **Action plan + model rationale** — justify next steps from your insights; commit to the fixed `nlptown` model and mapping above.
- [ ] **Inference on all 500 reviews** — load model once; store predicted stars and sentiment bands per review.
- [ ] **Breakdown vs 4.5-star average** — calculate % positive / neutral / negative; compare to the business rating; explain gaps.
- [ ] **False negatives** — find reviews where the model predicts 1–2 stars but the human rating is 4–5 (or where you read the text as positive/neutral but the model disagrees); document examples and shared patterns.
- [ ] **Manual sample (15–20 reviews)** — inspect predictions by hand; note cases where the label looks wrong.
- [ ] **Conclusions** — plain-language takeaway the account manager could use.

**Production deliverables:**

- [ ] Migrate clean inference logic to **`src/app.py`** (template pattern: notebook for story, script for production).
- [ ] Write enriched output to **`data/processed/reviews_with_sentiment.csv`**.
- [ ] Pin dependencies in **`requirements.txt`**.

---

## ✅ What We Will Evaluate

- [ ] **`src/explore.ipynb`** is submitted **with executed outputs** and a clear narrative arc: objectives → EDA → cleaning → plan/model → results/conclusions.
- [ ] Short transitional markdown appears between major code blocks.
- [ ] The model is integrated via `pipeline()`/`from_pretrained()` — model weights are **not** committed to the repository.
- [ ] All 500 reviews were processed and have an associated sentiment prediction.
- [ ] The model version/name is pinned, not left to resolve to "latest."
- [ ] The model is loaded once and reused, not reloaded on every review.
- [ ] A sentiment breakdown is calculated and explicitly compared against the 4.5-star average.
- [ ] There's evidence of manual sanity-checking — specific examples of predictions reviewed by hand, with notes on whether they made sense.
- [ ] False negatives are identified and analyzed — documented examples with a hypothesis about why the product-review model misclassified service-review text.
- [ ] **`src/app.py`** runs the production inference path and writes **`data/processed/reviews_with_sentiment.csv`**.
- [ ] Dependencies are pinned in **`requirements.txt`**.

> **Note:** We are not evaluating model architecture, training, or fine-tuning — you're integrating an existing model, not building one. We are **not** looking for a separate client markdown report; the notebook is your communication artifact.

---

## 📦 How to Submit

Push your code to your own GitHub repository. Make sure **`src/explore.ipynb`** (with outputs), **`src/app.py`**, and **`data/processed/reviews_with_sentiment.csv`** are included — not just printed to your terminal and discarded. Submit your repository link following your instructor's submission process.

---

## 🔍 Optional Extension: Find a Better Model

Once you've completed the analysis above, try this on your own:

1. Run [`tabularisai/multilingual-sentiment-analysis`](https://huggingface.co/tabularisai/multilingual-sentiment-analysis) on the same 500 reviews.
2. Compare: does the false-negative rate drop? Which reviews still fail?
3. Write a short addendum **inside the same `src/explore.ipynb`** recommending whether WeLoveReviews should switch models for this client — and why.

This step is not graded, but it's the kind of work that separates a model integrator from an AI engineer who understands **model selection**.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity), and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
