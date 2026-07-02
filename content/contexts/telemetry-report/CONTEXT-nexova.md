# CONTEXT — Nexova · Telemetry Phase 4: Report from the Data

## Your Company

**Nexova** is an HR consulting and talent acquisition firm with offices in Valencia, Spain and Miami, Florida. You are part of the internal AI Engineering team. The `telemetry_events` table is populated with real events from the backoffice. Today you build the pipeline that turns those events into the metrics Patricia Solís (HR Manager) and Sergio Molina (CTO) need.

---

## Your Two Metrics

These are the two KPI calculations your `analysis.py` must implement. Each maps directly to the KPIs defined in your Phase 1 plan.

### Metric 1 — Asset assignments per day by office

**Business question:** how many asset assignment events were registered per day, segmented by office?

**Answers the KPI:** Stock-out frequency by asset category — assignments per day reveal demand patterns that precede stock-outs.

```python
# Pseudocode — implement using Pandas operations only
def assignments_per_day_by_office(start_date, end_date):
    # Load from telemetry_events where event_type = 'assignment_order_created'
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

### Metric 2 — Assignment failure rate per day

**Business question:** what proportion of asset assignment attempts failed each day?

**Answers the KPI:** Procurement cycle time (indirectly — failures indicate assets were not procured in time).

```python
# Pseudocode — implement using Pandas operations only
def assignment_failure_rate_per_day(start_date, end_date):
    # Load from telemetry_events where event_type IN (
    #   'assignment_order_created', 'assignment_order_failed'
    # ) and timestamp between start_date and end_date
    # Convert timestamp to datetime (utc=True)
    # Extract date
    # Create boolean column: is_failure = event_type == 'assignment_order_failed'
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
    "assignments_per_day_by_office": [
      { "date": "2025-01-13", "office": "valencia", "count": 5 },
      { "date": "2025-01-13", "office": "miami", "count": 3 }
    ],
    "assignment_failure_rate_per_day": [
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
- **Valencia and Miami must be segmented** in the assignments metric — Sergio needs to compare both offices. Never aggregate across both offices without a grouping dimension.
- **Software licence assignments** (`asset_category = software_licence` in `tags`) can be isolated in a third function if you implement the additional activity — load relevant events via SQL (`event_type` + timestamp), extract `asset_category` in Pandas, then filter `df[df['asset_category'] == 'software_licence']` before grouping.

---

_Nexova AI Engineering Team — Internal document for 4Geeks Academy AI Engineering Track_
