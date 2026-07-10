# CONTEXT — TrackFlow

## Regression model for sales prediction

---

### 1. Why this matters to TrackFlow

Thomas (CEO) needs to know whether it's feasible to predict revenue volume for the coming months before investing in a full executive dashboard. TrackFlow bills mainly on shipment volume managed for e-commerce brands, and that volume has sharp peaks and valleys driven by the e-commerce calendar — something Ana (Warehouse) and Carlos (Carriers) already anticipate manually every year.

---

### 2. Data structure

The monthly consolidated revenue dataset for TrackFlow is already included in your monorepo, at `data/raw/trackflow_sales.csv`, with these exact columns:

| Column | Type | Description |
|---|---|---|
| `month` | date (`YYYY-MM-01`) | First day of the reported month |
| `revenue_eur` | float | Total revenue for the month, consolidated in EUR |
| `shipments_processed` | int | Total number of shipments processed during the month (both countries) |
| `avg_revenue_per_shipment_eur` | float | Average revenue per shipment for the month |
| `market` | string | `"us"`, `"spain"`, or `"consolidated"` — use `"consolidated"` as the main row for the model |

The model's target variable is `revenue_eur` from the `consolidated` row.

---

### 3. KPIs and what a good model means here

- A high **Gini** matters to Thomas to confidently distinguish a normal low-season month (e.g. February) from an atypical drop that warrants investigation.
- **PSI** helps detect whether the volume mix between Los Angeles and Zaragoza shifted significantly between training and test — report it if it does, since it could signal an expansion or contraction of operations in one country.
- Report **MSE** in EUR², and also as a percentage of average monthly revenue, so Thomas and Ana can interpret it directly.

---

### 4. About the provided dataset

The file `data/raw/trackflow_sales.csv` contains **10 years** of monthly data (120 `consolidated` rows), from `2016-01` to `2025-12`. It already reflects the following patterns — you don't need to generate them, but you do need to understand them to interpret your model's results:

**Growth pattern:** base annual growth `X = 6%`, with variation `Y = 3%`. Each year, the actual growth `d` alternates between `X+Y` and `X-Y` (between 3% and 9%), always positive.

**Seasonality pattern (present every year in the dataset):**
- **November–December:** revenue rise of 25–35% relative to the average, from the Black Friday shipping peak and the holiday e-commerce season.
- **February:** revenue drop of 10–15% relative to the average, from the typical e-commerce slowdown after the peak season.
- All other months fluctuate moderately (±5%) around the annual growth trend.

The dataset was generated with a fixed random seed (`random_state=42`), so it's deterministic.

---

### 5. Business constraints

- All `revenue_eur` values must be positive.
- There must be no missing months in the 2016-01 to 2025-12 range.
- The provided dataset only includes the `consolidated` row; if you break revenue down by market as an additional feature, remember Los Angeles (US) carries a larger volume than Zaragoza (Spain) — use roughly 60/40 as a reference split.

---

### 6. Expected deliverables

- Training script in `scripts/` that loads `data/raw/trackflow_sales.csv`, splitting the first 8 years as training and the last 2 as test.
- A trained model (XGBoost or Random Forest) with all 4 metrics (MSE, PSI, Gini, K2 Score) calculated on the test set.
- A visualization showing the prediction and its variability range against the real data from the 2 test years.
- A unit test in `tests/pipelines/` validating the 8/2-year split.
