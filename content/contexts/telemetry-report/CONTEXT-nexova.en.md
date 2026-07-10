# CONTEXT — Nexova · Telemetry Phase 4: Report from the Data

## Your Company

**Nexova** is an HR consulting and talent acquisition firm with offices in Valencia, Spain and Miami, Florida. You are part of the internal AI Engineering team. The `telemetry_events` table is populated with real events from the backoffice. Today you build the pipeline that turns those events into the metrics Patricia Solís (HR Manager) and Sergio Molina (CTO) need.

---

## Your Two Metrics

These are the two KPI calculations your `analysis.py` must implement. Each maps directly to the KPIs defined in your Phase 1 plan.

### Metric 1 — Asset exits per day by office

**Business question:** how many asset exit events were registered per day, segmented by office?

**Answers the KPI:** Stock-out frequency by asset category — exit volume per day reveals demand patterns that precede stock-outs.

```python
# Pseudocode — implement using Pandas operations only
def asset_exits_per_day_by_office(start_date, end_date):
    # Load from telemetry_events where event_type = 'asset_exit_created'
    # and timestamp between start_date and end_date
    # Convert timestamp to datetime (utc=True)
    # Extract date from timestamp
    # Extract office from tags JSONB
    # groupby(['date', 'office'])['id'].count()
    # Return as list of dicts: [{ "date": "...", "office": "...", "count": N }]
```

**Grouping dimension:** date + office (from `tags`).
**Aggregation:** `.count()` on event `id`.

---

### Metric 2 — Asset exit failure rate per day

**Business question:** what proportion of asset exit attempts failed each day?

**Answers the KPI:** Procurement cycle time (indirectly — failures indicate assets were not procured in time).

```python
# Pseudocode — implement using Pandas operations only
def asset_exit_failure_rate_per_day(start_date, end_date):
    # Load from telemetry_events where event_type IN (
    #   'asset_exit_created', 'asset_exit_failed'
    # ) and timestamp between start_date and end_date
    # Convert timestamp to datetime (utc=True)
    # Extract date
    # Create boolean column: is_failure = event_type == 'asset_exit_failed'
    # groupby('date').agg(total=('id', 'count'), failures=('is_failure', 'sum'))
    # Calculate failure_rate = failures / total
    # Return as list of dicts: [{ "date": "...", "total": N, "failures": M, "failure_rate": 0.08 }]
```

**Grouping dimension:** date.
**Aggregation:** `.agg()` with count and sum, then derived ratio.

---

## Expected JSON Output

```json
{
  "period": { "from": "2025-01-13", "to": "2025-01-20" },
  "metrics": {
    "asset_exits_per_day_by_office": [
      { "date": "2025-01-13", "office": "Valencia", "count": 5 },
      { "date": "2025-01-13", "office": "Miami", "count": 3 }
    ],
    "asset_exit_failure_rate_per_day": [
      { "date": "2025-01-13", "total": 8, "failures": 1, "failure_rate": 0.125 }
    ]
  }
}
```

---

## Additional Activity — Auth Failure Rate

If you instrumented authentication events in D47, implement:

**Business question:** what percentage of login attempts fail each day, per office?

```python
# event_type IN ('user_login_succeeded', 'user_login_failed')
# groupby(['date', 'office from tags'])
# failure_rate = failed / (failed + succeeded)
```

---

## Business Constraints for Your Pipeline

- **`office` must come from `tags`**, not from a fixed column. Use Pandas to extract it: `df['office'] = df['tags'].apply(lambda x: x.get('office'))` — then filter out rows where it is null before grouping.
- **Valencia and Miami must be segmented** in the exits metric — Sergio needs to compare both offices. Never aggregate across both offices without a grouping dimension.
- **Hardware exits** (`exit_type = allocation`) can be isolated in a third function if you implement the additional activity — load relevant events via SQL (`event_type` + timestamp), extract `exit_type` in Pandas, then filter before grouping.

---

_Nexova AI Engineering Team — Internal document for 4Geeks Academy AI Engineering Track_
