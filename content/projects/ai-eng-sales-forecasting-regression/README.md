# Sales Forecasting with a Regression Model

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/sales-forecasting)** before writing any code — it documents what each column means and the seasonality pattern of your company's historical sales, which is already included as a CSV in `data/raw/`.

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

You've already prepared and split your company's historical data into training and test sets, and trained a first classification model. Now your tech lead needs something different: Leadership wants to know **how much the company is going to sell in the coming months**, not just classify an outcome into categories. That's a regression problem.

Your tech lead has opened a **ticket** based on an **RFI** that came in from Finance: they want to know whether, with the available historical data, it's feasible to predict future sales behavior with an acceptable margin of error before committing to building a full executive dashboard around it.

> **From:** Your tech lead
> **Subject:** Ticket — Sales prediction model
>
> Finance wants to know if we can predict sales for the coming months from the historical data. Before we promise them anything, I need a model trained and evaluated honestly: no claiming a low error just because the model memorized the past.
>
> Non-negotiable criteria:
>
> - Use the **first 8 years** of data for training and the **2 most recent years** to check the prediction — the model must not have seen those recent years during training.
> - I want a **visualization** showing the prediction along with its variability range (not a single optimistic number).
> - Justify why you chose XGBoost or Random Forest for this case — don't assume one is "better" without arguing it.
> - Report the error with a metric I can explain to Finance without it sounding like a black box.

**Complementary knowledge:** Random Forest trains many decision trees on different subsets of the data and averages their results — it's simpler to explain and a good starting point. XGBoost trains trees sequentially, where each one corrects the errors of the previous one — it usually predicts better but is harder to explain and needs more tuning. Choose based on what your stakeholder actually needs: explainability or maximum accuracy.

---

## 🌱 How to Start the Project

1. Fork and clone your copy of your company's [monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) (if you don't already have it locally).
2. Create a new branch off `main` for this project.
3. Install the required dependencies with `uv add` (e.g. `scikit-learn`, `xgboost`, `pandas`, `matplotlib`) — never use `pip install` or `pipenv`.
4. Your company's historical sales dataset is already included in `data/raw/` in your monorepo (e.g. `data/raw/<company>_sales.csv`) — you don't need to generate or simulate it.
5. Read your `CONTEXT-company.md` in full before writing any code: it explains what each column means, the date range, and the seasonality pattern the dataset already reflects.

---

## 💻 What You Need to Do

**Data preparation**

- [ ] Load your company's historical sales dataset from `data/raw/<company>_sales.csv` (already included in your monorepo) and verify the columns match what's described in your `CONTEXT-company.md`.
- [ ] Handle null or empty values before training.
- [ ] Split the dataset into **training** (the first 8 years) and **checking/test** (the 2 most recent years), so the model never sees the test years during training.
- [ ] Scale the variables that need it to avoid faulty comparisons between different magnitudes.

**Model training**

- [ ] Train a regression model using **XGBoost or Random Forest** (pick one and document why) with `scikit-learn`.
- [ ] Document, in code or in a comment, the criteria used to choose the algorithm (data size, need for explainability, time available for tuning).

**Evaluation**

- [ ] Calculate and report at least the following metrics on the test set: **MSE**, **PSI**, **Gini**, and **K2 Score**.
- [ ] Explain in your implementation's README (or in a comment) what each metric measures and why a low MSE alone isn't enough.

**Visualization**

- [ ] Generate a visualization showing the model's prediction along with the variability area of the result, compared against the real data from the 2 test years.

⚠️ **IMPORTANT:** Column names, dataset format, and domain-specific values in your implementation must match what is specified in your CONTEXT.md. A generic implementation that ignores your company's context will not be accepted.

**Testing**

- [ ] Add at least one unit test in `tests/pipelines/` that validates the training/test split respects the 8-year / 2-year rule and that there is no data leakage between the two sets.

---

## ✅ What We Will Evaluate

- [ ] The training/test split respects the 8-year / 2-year rule and does not mix data between the two sets.
- [ ] The trained model is XGBoost or Random Forest, with the choice explicitly justified.
- [ ] All four metrics (MSE, PSI, Gini, K2 Score) are calculated and reported on the test set, not the training set.
- [ ] There is a visualization showing the prediction along with its variability range, not just a point estimate.
- [ ] The dataset used is the one provided in `data/raw/<company>_sales.csv`, with no alterations that break the seasonality and growth pattern described in the company's CONTEXT.md.
- [ ] The random seed (`random_state`/`seed`) is fixed so the experiment is reproducible.
- [ ] The split's unit test passes correctly.

---

## 📦 How to Submit

1. Commit your changes with clear, descriptive messages.
2. Push your branch to your fork of the monorepo.
3. Open a **Pull Request** against the `main` branch of your own fork, briefly describing which algorithm you chose and why.
4. Include the metrics obtained on the test set in the PR description.
5. Wait for your tech lead's review before merging.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
