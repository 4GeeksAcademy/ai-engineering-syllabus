# CONTEXT — HealthCore

## Regression model for sales prediction

---

### 1. Why this matters to HealthCore

Sandra (CEO) needs to know whether it's possible to predict revenue for the coming months before investing in a network-wide executive dashboard. HealthCore's revenue is tied to visit demand, which varies predictably by season — something Marcus (Clinical Operations) and Tom (Revenue Cycle) notice every year but have never quantified with a model.

> **Regulatory note:** this dataset works with **aggregated monthly revenue**, not individual patient data. Do not include any patient identifier, diagnosis, or clinical data in the sales dataset — that keeps this exercise out of the scope of HIPAA and UK GDPR. If your pipeline were ever to touch patient-level data, you would need a BAA (US) or a DPA (UK) before processing it.

---

### 2. Data structure

The monthly consolidated revenue dataset for HealthCore is already included in your monorepo, at `data/raw/healthcore_sales.csv`, with these exact columns:

| Column | Type | Description |
|---|---|---|
| `month` | date (`YYYY-MM-01`) | First day of the reported month |
| `revenue_usd` | float | Total revenue for the month, consolidated in USD |
| `visits_count` | int | Total number of visits across all 12 clinics for the month |
| `avg_revenue_per_visit_usd` | float | Average revenue per visit for the month |
| `region` | string | `"us"`, `"uk"`, or `"consolidated"` — use `"consolidated"` as the main row for the model |

The model's target variable is `revenue_usd` from the `consolidated` row.

---

### 3. KPIs and what a good model means here

- A high **Gini** matters to Sandra to confidently distinguish a normal low-season month (e.g. August) from an atypical drop that warrants attention — for example, a clinical capacity issue.
- **PSI** helps detect whether the visit mix between the US and UK shifted significantly between training and test — report it if it does, since it could reflect a new clinic opening.
- Report **MSE** in USD², and also as a percentage of average monthly revenue, so Tom (Revenue Cycle) and Sandra can interpret it without extra translation.

---

### 4. About the provided dataset

The file `data/raw/healthcore_sales.csv` contains **10 years** of monthly data (120 `consolidated` rows), from `2016-01` to `2025-12`. It already reflects the following patterns — you don't need to generate them, but you do need to understand them to interpret your model's results:

**Growth pattern:** base annual growth `X = 4%`, with variation `Y = 2%`. Each year, the actual growth `d` alternates between `X+Y` and `X-Y` (between 2% and 6%), always positive.

**Seasonality pattern (present every year in the dataset):**
- **October–December:** revenue rise of 15–20% relative to the average, from flu season and the increase in year-end visits.
- **July–August:** revenue drop of 12–18% relative to the average, from the summer vacation season, which reduces non-urgent visits in both countries.
- All other months fluctuate moderately (±5%) around the annual growth trend.

The dataset was generated with a fixed random seed (`random_state=42`), so it's deterministic. Like the rest of the dataset, it contains only monthly aggregate figures — no individual patient-level data.

---

### 5. Business constraints

- All `revenue_usd` values must be positive.
- There must be no missing months in the 2016-01 to 2025-12 range.
- The provided dataset only includes the `consolidated` row and contains no individual patient-level data. If you break revenue down by region as an additional feature, remember the US holds most of the volume (9 of the 12 clinics) — use roughly 75/25 as a reference split between US and UK.

---

### 6. Expected deliverables

- Training script in `scripts/` that loads `data/raw/healthcore_sales.csv`, splitting the first 8 years as training and the last 2 as test.
- A trained model (XGBoost or Random Forest) with all 4 metrics (MSE, PSI, Gini, K2 Score) calculated on the test set.
- A visualization showing the prediction and its variability range against the real data from the 2 test years.
- A unit test in `tests/pipelines/` validating the 8/2-year split.
