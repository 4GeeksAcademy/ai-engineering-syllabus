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

You don't have time (or the data) to train a model from scratch — and you don't need to. Plenty of pretrained models on Hugging Face already know how to read sentiment in text. Your job is to pick the right one, integrate it correctly, and turn raw text into something the account manager can actually use.

> The account manager shared this with you over email:
>
> "We're handing this client 500 written reviews next week. I need to know, in plain terms, how many of these reviews read as positive, neutral, or negative — and whether that breakdown lines up with their 4.5-star average. If there's a gap, I want to understand where it's coming from before we put it in front of the client."

**Model to use:** [`prajjwal1/bert-mini`](https://huggingface.co/prajjwal1/bert-mini) from Hugging Face.

#### A note on how to integrate the model

Don't download the model weights and commit them to your repository — that will bloat your repo and isn't how this works in a real team. Instead, load the model at runtime using `pipeline()` or `from_pretrained()`. The first time you run it, it downloads and caches the model locally (`~/.cache/huggingface`); every run after that reuses the cache. Keep your repo clean — it should contain your code and your data, not model binaries.

⚠️ **IMPORTANT:** Pin the model name/version you load — don't silently depend on whatever the "latest" version happens to be when someone else clones your repo.

Before you trust any output, sample a handful of reviews yourself and read them. Does the model's label match your own read of the text? A model is only useful once you've checked it against reality.

---

## 🌱 How to Start the Project

> Fork the following repository before you start: [github.com/4GeeksAcademy/python-hello](https://github.com/4GeeksAcademy/python-hello)

1. Fork the `python-hello` repository and, if available, select the 4GeeksAcademy account.
2. Open it in GitHub Codespaces, or clone it locally if you prefer to work on your own machine.
3. Download the provided [reviews.csv](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/ai-eng-sentiment-analysis-reviews/reviews.csv) file from the platform and place it in a `data/` folder in your repository.
4. Read the full [instructions on how to start a coding project](https://4geeks.com/lesson/how-to-start-a-project) if this is new to you.

---

## 💻 What You Need to Do

- [ ] Set up your environment and install the libraries you need (e.g. `transformers`, a backend like `torch`) — pin versions in your dependency file.
- [ ] Load the 500 reviews from the provided dataset.
- [ ] Load `prajjwal1/bert-mini` via `pipeline()` or `from_pretrained()` — load it once, not inside a loop that re-downloads or re-instantiates it per review.
- [ ] Run sentiment inference on every review and store the predicted label alongside each review.
- [ ] Calculate the overall sentiment breakdown (e.g. % positive / neutral / negative).
- [ ] Compare that breakdown against the business's 4.5-star average rating. Does it line up? Where doesn't it?
- [ ] Manually inspect a sample of predictions (at least 15–20 reviews) and note any cases where the model's label looks wrong to you. Don't skip this — this is how you catch a model that's silently failing.
- [ ] Write a short report in a markdown file that the account manager could actually hand to a client: total reviews analyzed, sentiment breakdown, comparison to the star rating, and any discrepancies you found and why you think they're happening.

---

## ✅ What We Will Evaluate

- [ ] The model is integrated via `pipeline()`/`from_pretrained()` — model weights are **not** committed to the repository.
- [ ] All 500 reviews were processed and have an associated sentiment prediction.
- [ ] The model version/name is pinned, not left to resolve to "latest."
- [ ] The model is loaded once and reused, not reloaded on every review.
- [ ] A sentiment breakdown is calculated and explicitly compared against the 4.5-star average.
- [ ] There's evidence of manual sanity-checking — specific examples of predictions reviewed by hand, with notes on whether they made sense.
- [ ] The final report is clear enough that a non-technical account manager could understand the conclusion and the reasoning behind it.

> **Note:** We are not evaluating model architecture, training, or fine-tuning — you're integrating an existing model, not building one.

---

## 📦 How to Submit

Push your code to your own GitHub repository, make sure your sentiment report is included in the repo (not just printed to your terminal and discarded), and submit your repository link following your instructor's submission process.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity), and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
