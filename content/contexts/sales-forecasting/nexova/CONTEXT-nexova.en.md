# CONTEXT — Nexova

## Regression model for sales prediction

---

### 1. Why this matters to Nexova

Laura (CEO) needs to know whether the team can predict revenue for the coming months before committing budget to a full executive dashboard. Nexova's business (headhunting, support outsourcing, and corporate training) has hiring cycles strongly shaped by the Spanish and Miami labor calendars — something Javier (Operations) and Marcos (Sales) feel firsthand every August and every January.

---

### 2. Data structure

The monthly consolidated revenue dataset for Nexova is already included in your monorepo, at `data/raw/nexova_sales.csv`, with these exact columns:

| Column | Type | Description |
|---|---|---|
| `month` | date (`YYYY-MM-01`) | First day of the reported month |
| `revenue_usd` | float | Total revenue for the month, consolidated in USD |
| `active_contracts` | int | Number of active contracts (headhunting + outsourcing + training) during the month |
| `avg_contract_value_usd` | float | Average active contract value for the month |
| `business_line` | string | `"headhunting"`, `"outsourcing"`, `"training"`, or `"consolidated"` — use `"consolidated"` as the main row for the model |

The model's target variable is `revenue_usd` from the `consolidated` row.

---

### 3. KPIs and what a good model means here

- A high **Gini** matters a lot for Nexova: Laura needs to confidently tell apart a normally-slow month (typical in August) from an anomalous drop that deserves immediate attention.
- **PSI** helps detect whether the business-line mix (headhunting vs. outsourcing vs. training) shifted significantly between the training and test periods — report it if it does.
- Report **MSE** in USD², and also as a percentage of average monthly revenue, so Marcos and Laura can interpret it without extra translation.

---

### 4. About the provided dataset

The file `data/raw/nexova_sales.csv` contains **10 years** of monthly data (120 `consolidated` rows), from `2016-01` to `2025-12`. It already reflects the following patterns — you don't need to generate them, but you do need to understand them to interpret your model's results:

**Growth pattern:** base annual growth `X = 4%`, with variation `Y = 3%`. Each year, the actual growth `d` alternates between `X+Y` and `X-Y` (between 1% and 7%), always positive.

**Seasonality pattern (present every year in the dataset):**
- **August:** revenue drop of 15–25% relative to the average, due to the summer vacation period in Spain, which stalls most corporate hiring activity.
- **January–February:** revenue rise of 15–20% relative to the average, driven by budget renewals and hiring plans at client companies at the start of the fiscal year.
- All other months fluctuate moderately (±5%) around the annual growth trend.

The dataset was generated with a fixed random seed (`random_state=42`), so it's deterministic.

---

### 5. Business constraints

- All `revenue_usd` values must be positive.
- There must be no missing months in the 2016-01 to 2025-12 range.
- The provided dataset only includes the `consolidated` row; if you break revenue down by business line as an additional feature, remember "outsourcing" (customer support) is the highest-volume line (~45% of the total), followed by headhunting (~35%) and training (~20%).

---

### 6. Expected deliverables

- Training script in `scripts/` that loads `data/raw/nexova_sales.csv`, splitting the first 8 years as training and the last 2 as test.
- A trained model (XGBoost or Random Forest) with all 4 metrics (MSE, PSI, Gini, K2 Score) calculated on the test set.
- A visualization showing the prediction and its variability range against the real data from the 2 test years.
- A unit test in `tests/pipelines/` validating the 8/2-year split.
