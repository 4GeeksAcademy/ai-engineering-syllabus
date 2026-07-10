# CONTEXT — Brasaland

## Regression model for sales prediction

---

### 1. Why this matters to Brasaland

Mariana (CEO) wants to know whether, before investing in a full executive dashboard, it's possible to predict how much the chain will sell in the coming months within a reasonable margin. Felipe (Operations) needs to anticipate ingredient purchases based on the expected trend, and Lucía (Procurement) wants to anticipate meat price fluctuations based on projected volume. A regression model over historical sales is the first concrete step toward that dashboard.

---

### 2. Data structure

The monthly consolidated sales dataset for all 14 locations is already included in your monorepo, at `data/raw/brasaland_sales.csv`, with these exact columns:

| Column | Type | Description |
|---|---|---|
| `month` | date (`YYYY-MM-01`) | First day of the reported month |
| `revenue_usd` | float | Total sales for the month, consolidated in USD (use a fixed COP→USD conversion rate for simplicity, e.g. 1 USD = 4,000 COP) |
| `covers_served` | int | Total number of guests served during the month, across all 14 locations |
| `avg_ticket_usd` | float | Average ticket for the month in USD |
| `market` | string | `"colombia"`, `"florida"`, or `"consolidated"` — use `"consolidated"` as the main row for the model; per-market rows are optional as additional features |

The model's target variable is `revenue_usd` from the `consolidated` row.

---

### 3. KPIs and what a good model means here

- A low **Gini** means the model doesn't distinguish well between "good" and "bad" months — for Mariana this matters as much as the absolute error, since she needs to identify underperforming months in advance.
- A high **PSI** between the training and test sets would signal that sales behavior changed structurally (e.g. new location openings, a market shift) and the model would need retraining — call this out explicitly if you detect it.
- Report **MSE** in USD², but also translate it into an average percentage error, since that's how Felipe and Mariana actually understand the number.

---

### 4. About the provided dataset

The file `data/raw/brasaland_sales.csv` contains **10 years** of monthly data (120 `consolidated` rows), from `2016-01` to `2025-12`. It already reflects the following patterns — you don't need to generate them, but you do need to understand them to interpret your model's results:

**Growth pattern:** the base annual growth is `X = 5%`, with variation `Y = 2%`. Each year, the actual growth `d` alternates between `X+Y` and `X-Y` (i.e. between 3% and 7%), always positive and never outside that range.

**Seasonality pattern (present every year in the dataset):**
- **January:** sales drop of 12–18% relative to the previous year's average, explainable by the "vacaciones colectivas" period and the typical post-December slump in Colombia.
- **December:** sales rise of 20–30% relative to the average, due to the holiday season in both markets.
- All other months fluctuate moderately (±5%) around the annual growth trend, with no abrupt patterns.

The dataset was generated with a fixed random seed (`random_state=42`), so it's deterministic: regenerating it with the same script and seed would produce exactly the same values.

---

### 5. Business constraints

- All `revenue_usd` values must be positive.
- There must be no missing months in the 2016-01 to 2025-12 range.
- The provided dataset only includes the `consolidated` row; if you want to analyze Colombia and Florida separately as an additional feature, keep in mind Florida is a smaller market (roughly 25% of the total) — don't assume similar magnitudes between the two.

---

### 6. Expected deliverables

- Training script in `scripts/` that loads `data/raw/brasaland_sales.csv`, splitting the first 8 years as training and the last 2 as test.
- A trained model (XGBoost or Random Forest) with all 4 metrics (MSE, PSI, Gini, K2 Score) calculated on the test set.
- A visualization showing the prediction and its variability range against the real data from the 2 test years.
- A unit test in `tests/pipelines/` validating the 8/2-year split.
