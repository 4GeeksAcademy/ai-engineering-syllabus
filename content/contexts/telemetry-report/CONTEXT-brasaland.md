# CONTEXT — Brasaland · Telemetry Phase 4: Report from the Data

## Your Company

**Brasaland** is a grilled food restaurant chain with 14 locations across Colombia and Florida. You are part of **Brasaland Digital**. The `telemetry_events` table is populated with real events from the backoffice. Today you build the pipeline that turns those events into the metrics Felipe Guerrero (Operations Director) and Mariana Restrepo (CEO) need.

---

## Your Two Metrics

These are the two KPI calculations your `analysis.py` must implement. Each maps directly to the KPIs defined in your Phase 1 plan.

### Metric 1 — Daily consumption by location

**Business question:** how many consumption order events were registered per day, segmented by location?

**Answers the KPI:** Daily consumption rate by ingredient and location.

```python
# Pseudocode — implement using Pandas operations only
def consumption_by_location_per_day(start_date, end_date):
    # Load from telemetry_events where event_type = 'consumption_order_created'
    # and timestamp between start_date and end_date
    # Convert timestamp to datetime (utc=True)
    # Extract date from timestamp
    # Extract location_id from tags JSONB
    # groupby(['date', 'location_id'])['id'].count()
    # Return as list of dicts: [{ "date": "...", "location_id": "...", "count": N }]
```

**Grouping dimension:** date + location_id (from `tags`).
**Aggregation:** `.count()` on event `id`.

---

### Metric 2 — Order failure rate per day

**Business question:** what proportion of order attempts (supply + consumption) failed each day?

**Answers the KPI:** Stock-out frequency (indirectly — failures signal supply chain stress).

```python
# Pseudocode — implement using Pandas operations only
def order_failure_rate_per_day(start_date, end_date):
    # Load from telemetry_events where event_type IN (
    #   'consumption_order_created', 'supply_order_created',
    #   'consumption_order_failed', 'supply_order_failed'
    # ) and timestamp between start_date and end_date
    # Convert timestamp to datetime (utc=True)
    # Extract date
    # Create boolean column: is_failure = event_type ends with '_failed'
    # groupby('date').agg(total=('id', 'count'), failures=('is_failure', 'sum'))
    # Calculate failure_rate = failures / total
    # Return as list of dicts: [{ "date": "...", "total": N, "failures": M, "failure_rate": 0.12 }]
```

**Grouping dimension:** date.
**Aggregation:** `.agg()` with both count and sum, then derived ratio.

---

## Expected JSON Output

```json
{
  "period": { "from": "2025-01-13", "to": "2025-01-20" },
  "metrics": {
    "consumption_by_location_per_day": [
      { "date": "2025-01-13", "location_id": "medellin_centro", "count": 12 },
      { "date": "2025-01-13", "location_id": "miami_south", "count": 8 }
    ],
    "order_failure_rate_per_day": [
      { "date": "2025-01-13", "total": 20, "failures": 3, "failure_rate": 0.15 }
    ]
  }
}
```

---

## Additional Activity — Auth Failure Rate

If you instrumented authentication events in D47, implement:

**Business question:** what percentage of login attempts fail each day, per location?

```python
# event_type IN ('user_login_succeeded', 'user_login_failed')
# groupby(['date', 'location_id from tags'])
# failure_rate = failed / (failed + succeeded)
```

---

## Business Constraints for Your Pipeline

- **`location_id` must come from `tags`**, not from a fixed column. Use Pandas to extract it: `df['location_id'] = df['tags'].apply(lambda x: x.get('location_id'))` — then filter out rows where it is null before grouping.
- **Separate Colombia and Florida** in the consumption metric — Felipe needs to compare both markets. The `location_id` naming convention (`medellin_*`, `bogota_*` for Colombia; `miami_*` for Florida) is what enables this segmentation.
- **The waste ratio KPI** (ConsumptionOrders with `reason = waste/spoilage/theft`) can be added as a third function if you implement the additional activity — load via SQL (`event_type` + timestamp), extract `reason` from `tags` in Pandas, then `df[df['reason'].isin(['waste', 'spoilage', 'theft'])]` before grouping.

---

_Brasaland Digital — Internal document for 4Geeks Academy AI Engineering Track_
