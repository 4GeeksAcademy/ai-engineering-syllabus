# Evaluating a Regression Model

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/sales-forecasting)** — you need your company's sales data to interpret the real cost of your model's errors.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

You already trained a regression model to predict your company's sales and tuned its hyperparameters. But a trained model is not the same as a trustworthy one: your tech lead has opened a **ticket** requesting a **formal technical evaluation** before approving its promotion to staging. No one is going to move a model to production just because "the final error looks fine."

The ticket is specific and includes three questions your report must answer without ambiguity:

1. Does the model show **underfitting**, **overfitting**, or is it reasonably well fitted?
2. How **stable** is its performance when you change which portion of the data you train on?
3. If there is a problem, what is the **specific corrective action** — not a generic one — that should be taken?

Answering "the model works fine" without evidence isn't a technical evaluation, it's an opinion. Your report must be backed by learning curves, cross-validation, and justified metrics.

### 📚 Complementary knowledge: bias, variance, and learning curves

A model with **underfitting** fails even on the training data: it didn't capture the pattern. A model with **overfitting** memorizes the training noise and fails to generalize. The most reliable way to diagnose which one is happening (or whether neither is) is a **learning curve**: plotting the training error and the validation error as the training set size increases.

- If both curves converge at a **high** error → underfitting. The typical fix is increasing model complexity or reviewing feature quality — never adding more data as the first response.
- If there is a **wide, persistent gap** between training (low) and validation (high) → overfitting. The typical fix is regularization, reducing complexity, or more data — never increasing complexity as the first response.
- If both curves converge at a **low, close** error → the model is reasonably well fitted.

There is no universal "correct" curve — what matters is the relative pattern between the two lines.

---

## 🌱 How to Start the Project

1. Continue on your existing copy of the [company's monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) assigned to you at the beginning of the course (if you don't have one yet, fork the repository).
2. Clone your fork and create a branch for this work.
3. Confirm that the trained model and the temporal split (8 years train / 2 years test) from your previous project are still available and reproducible.
4. Install any additional dependencies with `uv add` — never use `pip install` or `pipenv`.
5. Read your `CONTEXT-company.md` to understand which error is more costly for your business: overestimating sales or underestimating them.

---

## 💻 What You Need to Do

**Time-aware cross-validation:**

- [ ] Implement a temporal cross-validation strategy (e.g. `TimeSeriesSplit`) with at least 5 folds over the training set.
- [ ] Explicitly verify that no fold mixes or shuffles the data — chronological order must be preserved within each fold.
- [ ] Report the chosen metric as **mean ± standard deviation** across folds, not just a single aggregate number.

**Learning curve:**

- [ ] Generate a learning curve plotting training error and validation error as the training set size grows.
- [ ] Save the resulting image to `data/eval/`.

**Metric selection and calculation:**

- [ ] Calculate **MAE** and **RMSE** for training and validation.
- [ ] Justify in writing which one better reflects the business cost of your errors, based on what your `CONTEXT-company.md` indicates.

⚠️ **IMPORTANT:** Field names, entity IDs, and domain-specific values in your implementation must match what is specified in your CONTEXT.md. A generic implementation that ignores the context will not be accepted.

**Diagnosis and technical report:**

- [ ] Write a technical report (`data/eval/evaluation_report.md`) that explicitly classifies the model as **well fitted**, **underfitting**, or **overfitting**, backed by the learning curve and the cross-validation results.
- [ ] Propose a concrete corrective action consistent with the diagnosis — not a generic answer like "add more data" or "increase complexity" without justifying why that is the root cause.

**Testing:**

- [ ] Write a unit test in `tests/pipelines/` that validates the temporal cross-validation strategy preserves the chronological order of the data within each fold (no index from a later fold appears before one from an earlier fold).

---

## ✅ What We Will Evaluate

- [ ] The learning curve is generated correctly and its pattern (underfitting / overfitting / good fit) is explicitly interpreted in the report.
- [ ] The temporal cross-validation does not shuffle the data and reports mean ± standard deviation.
- [ ] At least two regression metrics are calculated and compared, with a business justification for the one chosen as primary.
- [ ] The report gives an explicit diagnosis (well fitted / underfitting / overfitting) backed by evidence, not just an assertion.
- [ ] The proposed corrective action is specific and consistent with the given diagnosis — not a generic recommendation.
- [ ] The unit test on fold chronological order passes correctly.

---

## 📦 How to Submit

1. Commit and push your changes to your fork.
2. Open a Pull Request to the main branch of your copy of the monorepo.
3. In the PR description, summarize your diagnosis in one or two sentences (e.g., "The model shows moderate overfitting; I recommend regularization before adding more data").
4. Verify the unit test passes in CI before requesting review.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
