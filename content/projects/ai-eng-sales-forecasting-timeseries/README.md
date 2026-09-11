# Sales Forecasting with Time Series Feature Engineering

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

<!-- endhide -->

**Before you start**: Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/sales-forecasting)** before writing any code — it documents what each column means and the seasonality pattern of your company's historical sales, which is already included as a CSV in `content/contexts/sales-forecasting/<company>/<company>_sales.csv` in this repository.

---

## 🎯 Your challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

You've already prepared and split your company's historical data into training and test sets, and trained a first classification model. Now your tech lead needs something different: Leadership wants to know **how much the company is going to sell in the coming months**, not just classify an outcome into categories. Your first attempt fed the raw columns straight into a model — but a sales series isn't just a table of independent rows, it's a **sequence in time**, and it hides information a plain regression setup ignores: what happened last month, what happened this month last year, and whether the trend is accelerating or flattening.

Your tech lead has opened a **ticket** based on an **RFI** that came in from Finance: they want to know whether, with the available historical data, it's feasible to predict future sales behavior with an acceptable margin of error before committing to building a full executive dashboard around it.

> **From:** Your tech lead
> **Subject:** Ticket — Sales forecasting model
>
> Finance wants to know if we can predict sales for the coming months from the historical data. Before we promise them anything, I need a model trained and evaluated honestly: no claiming a low error just because the model memorized the past.
>
> Non-negotiable criteria:
>
> - Use the **first 8 years** of data for training and the **2 most recent years** to check the prediction — the model must not have seen those recent years during training.
> - Don't just throw the raw columns at the model — engineer **time-aware features** (lags, rolling stats, calendar signals) so it can actually learn the sales rhythm, not just averages.
> - I want a **visualization** showing the prediction along with its variability range (not a single optimistic number).
> - Justify why you chose XGBoost or Random Forest for this case — don't assume one is "better" without arguing it.
> - Report the error with a metric I can explain to Finance without it sounding like a black box.

**Complementary knowledge: reading a time series before modeling it.** Before engineering features, decompose the series into three components: **trend** (the long-term direction), **seasonality** (the repeating pattern tied to the calendar, e.g. a December spike), and **residual** (what's left over — noise or events the other two don't explain). A tool like `statsmodels.tsa.seasonal_decompose` plots the three separately so you can *see* whether the seasonality you engineer as a feature actually matches what's in the data, instead of guessing. This decomposition is a diagnostic lens, not a model — you still forecast with a regressor below.

Once you understand the shape of the series, translate that into features a regressor can consume:

- **Lag features**: `sales(t-1)`, `sales(t-12)` — what happened last month and the same month last year.
- **Rolling statistics**: rolling mean/std over the last 3–12 months — captures the recent trend and volatility.
- **Calendar features**: month, quarter, or a cyclical encoding of month (`sin`/`cos`) — captures recurring seasonality without hardcoding it.

**Complementary knowledge: Random Forest vs. XGBoost.** Random Forest trains many decision trees on different subsets of the data and averages their results — it's simpler to explain and a good starting point. XGBoost trains trees sequentially, where each one corrects the errors of the previous one — it usually predicts better but is harder to explain and needs more tuning. Choose based on what your stakeholder actually needs: explainability or maximum accuracy.

---

## 🌱 How to Start the Project

1. If you still don't have a fork of your company's [monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo), create it on GitHub. We recommend opening and working on that fork in **GitHub Codespaces**; if you prefer to work locally, clone it to your machine.
2. From `main` in your fork, create a new branch for this project: `git switch -c feature/sales-forecast-model` (in Codespaces or in your local environment).
3. Verify that `uv` is installed with `uv --version`; if you don't have it, install it with `curl -LsSf https://astral.sh/uv/install.sh | sh` and, at the project root, initialize the environment with `uv init` (only if `pyproject.toml` does not already exist). Then add dependencies with `uv add` (for example `scikit-learn`, `xgboost`, `pandas`, `matplotlib`, `statsmodels`) — never use `pip install` or `pipenv`.
4. Use your company's historical sales dataset already provided: in the monorepo it is located at `data/raw/<company>_sales.csv`, and in this reference repository at `content/contexts/sales-forecasting/<company>/<company>_sales.csv`; do not generate or simulate it.
5. Read your full `CONTEXT-company.md` before writing code: it contains each column's meaning, the date range, and the seasonality pattern the dataset already reflects.

---

## 💻 What You Need to Do

**Data preparation**

- [ ] Load your company's historical sales dataset from the path that matches your working environment: `data/raw/<company>_sales.csv` in your monorepo or `content/contexts/sales-forecasting/<company>/<company>_sales.csv` in this reference repository, and verify the columns match those described in your `CONTEXT-company.md`.
- [ ] Handle null or empty values before training.
- [ ] Decompose the series (trend / seasonality / residual) with `statsmodels.tsa.seasonal_decompose` (or equivalent) and briefly note in a comment or your report whether the pattern matches what `CONTEXT-company.md` describes.
- [ ] Engineer time-aware features: at least one lag feature (e.g. `t-1`, `t-12`), one rolling statistic (mean or std over a window), and a calendar/seasonal feature (month, quarter, or cyclical encoding).
- [ ] Compute every lag and rolling feature **causally** (only past values, e.g. `shift(1)` before `rolling()`) — a feature that peeks at the current or future row invalidates the whole forecast.
- [ ] Split the dataset into **training** (the first 8 years) and **checking/test** (the 2 most recent years), so the model never sees the test years during training.
- [ ] Scale the variables that need it to avoid faulty comparisons between different magnitudes.

**Model training**

- [ ] Train a model using **XGBoost or Random Forest** (pick one and document why) with `scikit-learn`, fed with the engineered time-aware features.
- [ ] Document, in code or in a comment, the criteria used to choose the algorithm (data size, need for explainability, time available for tuning).

**Evaluation**

- [ ] Calculate and report at least the following metrics on the test set: **MSE**, **PSI**, **Gini**, and **K2 Score**.
- [ ] Explain in your implementation's README (or in a comment) what each metric measures and why a low MSE alone isn't enough.

**Visualization**

- [ ] Generate a visualization showing the model's prediction along with the variability area of the result, compared against the real data from the 2 test years.

⚠️ **IMPORTANT:** Column names, dataset format, and specific values in your implementation must match what is specified in your CONTEXT.md. A generic implementation that ignores your company's context will not be accepted.

**Testing**

- [ ] Add at least one unit test in `tests/pipelines/` that validates the training/test split respects the 8-year / 2-year rule and that there is no data leakage between the two sets.
- [ ] Add at least one unit test in `tests/pipelines/` that validates your lag/rolling features are computed causally (e.g. the lag feature for row `t` equals the raw value at `t-1`, never at `t` or later).

---

## ✅ What We Will Evaluate

- [ ] The training/test split respects the 8-year / 2-year rule and does not mix data between the two sets.
- [ ] At least one lag feature, one rolling statistic, and one calendar/seasonal feature were engineered and used to train the model.
- [ ] Lag and rolling features are computed causally, with no leakage from future rows.
- [ ] The trained model is XGBoost or Random Forest, with the choice explicitly justified.
- [ ] All four metrics (MSE, PSI, Gini, K2 Score) are calculated and reported on the test set, not the training set.
- [ ] There is a visualization showing the prediction along with its variability range, not just a point estimate.
- [ ] The dataset used is the one provided in `data/raw/<company>_sales.csv`, with no alterations that break the seasonality and growth pattern described in the company's CONTEXT.md.
- [ ] The random seed (`random_state`/`seed`) is fixed so the experiment is reproducible.
- [ ] Both unit tests (split rule and no-leakage-in-features) pass correctly.

---

## 📦 How to Submit

1. Commit your changes with clear, descriptive messages.
2. Push your branch to your fork of the monorepo.
3. Open a **Pull Request** against the `main` branch of your own fork, briefly describing which algorithm you chose and why.
4. Include the metrics obtained on the test set in the PR description.
5. Wait for your tech lead's review before merging.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
