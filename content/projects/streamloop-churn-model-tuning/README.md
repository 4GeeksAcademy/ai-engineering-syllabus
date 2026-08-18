# StreamLoop — Tuning the Churn Model

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/python-hello/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your challenge

You're a freelance AI engineer working with **StreamLoop**, a mid-size streaming subscription platform. A few weeks ago you delivered a first version of their churn classifier — trained it, checked accuracy, called it done. The tech lead has come back with a follow-up:

> "The model works, but I have no idea if it's actually good, or just the first thing that came out of `.fit()`. Before we put this anywhere near production, I want to see that you've actually searched for the best configuration — not guessed at it. And I want to know _why_ you picked the final one, not just that it scored well."

That's a fair ask. A model trained with default hyperparameters is rarely the best version of itself, and "it scored well" isn't an answer if you can't explain how you got there or how stable that score really is.

Your job on this pass: take a classifier trained on StreamLoop's customer data, and systematically tune it — first with a broad, cheap search, then with a focused, precise one — while avoiding the mistakes that make tuning results meaningless (leaking the test set into your search, judging models on the wrong metric, or trusting a single number without checking how much it moves across folds).

#### The dataset

StreamLoop's customer data is publicly modeled after a well-known telecom churn dataset. Load it directly from this URL in your notebook — no need to download anything manually:

```
https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv
```

The target column is `Churn` (`Yes` / `No`). The rest are customer account, service, and billing attributes.

#### A note on what "good" means here

StreamLoop loses far more money from a customer who churns unnoticed than from a customer who gets a retention offer they didn't need. Keep that in mind when you're deciding what to optimize for — the metric that looks best on a leaderboard isn't automatically the metric that matches the business problem.

---

## 🌱 How to Start the Project

1. Fork or clone the template repo: [https://github.com/4GeeksAcademy/python-hello](https://github.com/4GeeksAcademy/python-hello)
2. Create your own GitHub repository from the template and update the remote URL
3. Open it in GitHub Codespaces, or clone it locally if you prefer your own machine
4. Install the required libraries (`scikit-learn`, `pandas`, at minimum) and start a notebook

Need a refresher? 📗 [How to start a coding project](https://4geeks.com/lesson/how-to-start-a-project)

---

## 💻 What You Need to Do

### Baseline

- [ ] Load the dataset and do the minimal cleaning needed to make it usable (handle the columns that aren't numeric, handle any missing/blank values)
- [ ] Split into train and test sets **before** doing anything else with the model
- [ ] Build a `Pipeline` that includes your preprocessing steps and a classifier of your choice — preprocessing must live inside the pipeline, not be applied separately beforehand
- [ ] Train that pipeline with **default hyperparameters** and record its performance on the test set — this is your baseline, and you only touch the test set here and at the very end

### Searching

- [ ] Define a hyperparameter search space for your chosen classifier, based on what that model actually supports
- [ ] Run a `RandomizedSearchCV` over that space first, using cross-validation and `n_jobs=-1`
- [ ] Use the results of the random search to narrow the space, then run a `GridSearchCV` to refine around that region
- [ ] Choose a `scoring` metric that reflects the business priority described in the challenge — not the sklearn default
- [ ] Let `refit=True` (the default) retrain the best estimator for you — do not manually re-fit `best_estimator_` afterward

### Selecting the final model

- [ ] Inspect `cv_results_` for your top candidates — don't just take the single best mean score at face value; look at how much it varies across folds
- [ ] Choose your final model and briefly justify the choice: is it the highest mean, or a slightly-lower-but-more-stable option? Either is defensible if you explain why
- [ ] Evaluate the final tuned model on the test set exactly once, using the same metric(s) as your baseline
- [ ] Write a short `tuning_report.md` comparing baseline vs. tuned performance, stating your final hyperparameters, and explaining the metric choice and the stability trade-off you considered

⚠️ **IMPORTANT:** Never fit `RandomizedSearchCV` or `GridSearchCV` on the full dataset — the search must only ever see the training split. The test set is touched exactly twice: once for the baseline, once for the final tuned model.

---

## ✅ What We Will Evaluate

- [ ] Preprocessing is inside a `Pipeline`, not applied separately before the split
- [ ] A default-hyperparameter baseline was trained and recorded before any tuning began
- [ ] `RandomizedSearchCV` was used to explore a broad space before `GridSearchCV` narrowed it
- [ ] The search was run with cross-validation and never touched the test set
- [ ] The `scoring` parameter was set deliberately, with a stated reason tied to the business problem — not left as accuracy by default
- [ ] `cv_results_` was inspected for variance across folds, not just the top mean score
- [ ] The final model choice is justified in the report, including any trade-off considered
- [ ] Baseline and tuned performance are both reported and compared using the same metric(s)

> Note: model architecture choice (which classifier you start from) is not graded — the tuning process and how you reason about it are what matter here.

---

## 📦 How to Submit

Push your repository to GitHub, including your notebook and `tuning_report.md`, and share the link following your instructor's submission instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/python-hello/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
