# CONTEXT — TrackFlow · Telemetry Phase 4: Report from the Data

## Your Company

**TrackFlow** is a last-mile delivery and warehouse management company operating in Los Angeles (US) and Zaragoza (Spain). You are part of **TrackFlow Tech**. The `telemetry_events` table is populated with real events from the backoffice. Today you build the pipeline that turns those events into the metrics Ana Whitfield (Head of Warehouse Operations) and Thomas Harry (CEO) need.

---

## Your Two Metrics

These are the two KPI calculations your `analysis.py` must implement. Each maps directly to the KPIs defined in your Phase 1 plan.

### Metric 1 — Stock exit volume per day by warehouse

**Business question:** how many stock exit events (dispatches) were created per day, segmented by warehouse?

**Answers the KPI:** Order fulfilment rate — volume trends reveal capacity patterns before SLA breaches occur.

```python
# Pseudocode — implement using Pandas operations only
def stock_exit_volume_per_day_by_warehouse(start_date, end_date):
    # Load from telemetry_events where event_type = 'stock_exit_created'
    # and tags.exit_type = 'dispatch'
    # and timestamp between start_date and end_date
    # Convert timestamp to datetime (utc=True)
    # Extract date from timestamp
    # Extract warehouse from tags JSONB
    # groupby(['date', 'warehouse'])['id'].count()
    # Return as list of dicts: [{ "date": "...", "warehouse": "...", "count": N }]
```

**Grouping dimension:** date + warehouse (from `tags`).
**Aggregation:** `.count()` on event `id`.

---

### Metric 2 — Stock exit failure rate per day by warehouse

**Business question:** what proportion of stock exit attempts failed each day, per warehouse?

**Answers the KPI:** Order fulfilment rate — failure rate directly measures the inverse of fulfilment success.

```python
# Pseudocode — implement using Pandas operations only
def stock_exit_failure_rate_per_day(start_date, end_date):
    # Load from telemetry_events where event_type IN (
    #   'stock_exit_created', 'stock_exit_failed'
    # ) and timestamp between start_date and end_date
    # Convert timestamp to datetime (utc=True)
    # Extract date and warehouse from tags
    # Create boolean column: is_failure = event_type == 'stock_exit_failed'
    # groupby(['date', 'warehouse']).agg(total=('id', 'count'), failures=('is_failure', 'sum'))
    # Calculate failure_rate = failures / total
    # Return as list of dicts: [{ "date": "...", "warehouse": "...", "total": N, "failures": M, "failure_rate": 0.05 }]
```

**Grouping dimension:** date + warehouse.
**Aggregation:** `.agg()` with count and sum, then derived ratio.

---

## Expected JSON Output

```json
{
  "period": { "from": "2025-01-13", "to": "2025-01-20" },
  "metrics": {
    "stock_exit_volume_per_day_by_warehouse": [
      { "date": "2025-01-13", "warehouse": "LA", "count": 87 },
      { "date": "2025-01-13", "warehouse": "ZGZ", "count": 34 }
    ],
    "stock_exit_failure_rate_per_day": [
      {
        "date": "2025-01-13",
        "warehouse": "LA",
        "total": 90,
        "failures": 3,
        "failure_rate": 0.033
      },
      {
        "date": "2025-01-13",
        "warehouse": "ZGZ",
        "total": 35,
        "failures": 1,
        "failure_rate": 0.029
      }
    ]
  }
}
```

---

## Additional Activity — Auth Failure Rate

If you instrumented authentication events in D47, implement:

**Business question:** what percentage of login attempts fail each day, per warehouse?

```python
# event_type IN ('user_login_succeeded', 'user_login_failed')
# groupby(['date', 'warehouse from tags'])
# failure_rate = failed / (failed + succeeded)
```

---

## Business Constraints for Your Pipeline

- **`warehouse` must come from `tags`**, not from a fixed column. Use Pandas to extract it: `df['warehouse'] = df['tags'].apply(lambda x: x.get('warehouse'))` — then filter out rows where it is null before grouping.
- **Los Angeles (`LA`) and Zaragoza (`ZGZ`) must always be segmented separately** — Thomas Harry will never accept a global number that mixes both warehouses. If `warehouse` is missing from a row, exclude it from the metric rather than grouping it under a null value.
- **Loss exits** (`exit_type = loss`) can be extracted from `tags` in a third function if you implement the additional activity — load `stock_exit_created` with SQL, extract `exit_type` in Pandas, then filter before grouping.

---

_TrackFlow Tech — Internal document for 4Geeks Academy AI Engineering Track_
