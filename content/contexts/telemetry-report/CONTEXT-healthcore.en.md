# CONTEXT — HealthCore · Telemetry Phase 4: Report from the Data

## Your Company

**HealthCore** is an outpatient healthcare services company with 12 clinics across the US and UK. You are part of **HealthCore Digital**. The `telemetry_events` table is populated with real events from the backoffice. Today you build the pipeline that turns those events into the metrics Dr. Marcus Reid (Director of Clinical Operations) and Dr. Sandra Okonkwo (CEO) need.

---

## Your Two Metrics

These are the two KPI calculations your `analysis.py` must implement. Each maps directly to the KPIs defined in your Phase 1 plan.

### Metric 1 — Supply consumption volume per day by clinic and country

**Business question:** how many supply consumption events were created per day, segmented by clinic and country?

**Answers the KPI:** Critical supply availability rate — volume by clinic reveals which locations consume supplies fastest.

```python
# Pseudocode — implement using Pandas operations only
def supply_consumption_volume_per_day(start_date, end_date):
    # Load from telemetry_events where event_type = 'supply_consumption_created'
    # and timestamp between start_date and end_date
    # Convert timestamp to datetime (utc=True)
    # Extract date from timestamp
    # Extract clinic_id and country from tags JSONB
    # groupby(['date', 'clinic_id', 'country'])['id'].count()
    # Return as list of dicts: [{ "date": "...", "clinic_id": N, "country": "...", "count": N }]
```

**Grouping dimension:** date + clinic_id + country (all from `tags`).
**Aggregation:** `.count()` on event `id`.

---

### Metric 2 — Clinical consumption frequency per day by country

**Business question:** how many clinical use consumption events occurred per day, segmented by country?

**Answers the KPI:** Clinical consumption frequency — the metric that triggers proactive stock level adjustments.

```python
# Pseudocode — implement using Pandas operations only
def clinical_consumption_per_day(start_date, end_date):
    # Load from telemetry_events where event_type = 'supply_consumption_created'
    # and tags.consumption_type = 'clinical_use'
    # and timestamp between start_date and end_date
    # Convert timestamp to datetime (utc=True)
    # Extract date and country from tags
    # groupby(['date', 'country'])['id'].count()
    # Return as list of dicts: [{ "date": "...", "country": "...", "count": N }]
```

**Grouping dimension:** date + country (from `tags`).
**Aggregation:** `.count()` on event `id`.

---

## Expected JSON Output

```json
{
  "period": { "from": "2025-01-13", "to": "2025-01-20" },
  "metrics": {
    "supply_consumption_volume_per_day": [
      { "date": "2025-01-13", "clinic_id": 1, "country": "US", "count": 42 },
      { "date": "2025-01-13", "clinic_id": 10, "country": "UK", "count": 31 }
    ],
    "clinical_consumption_per_day": [
      { "date": "2025-01-13", "country": "US", "count": 4 },
      { "date": "2025-01-13", "country": "UK", "count": 2 }
    ]
  }
}
```

---

## Additional Activity — Auth Failure Rate

If you instrumented authentication events in D47, implement:

**Business question:** what percentage of login attempts fail each day, per country?

```python
# event_type IN ('user_login_succeeded', 'user_login_failed')
# groupby(['date', 'country from tags'])
# failure_rate = failed / (failed + succeeded)
```

Claire Whitfield (CCO) requires this metric segmented by country — a combined rate across US and UK is not acceptable for compliance reporting.

---

## Business Constraints for Your Pipeline

- **`clinic_id` and `country` must come from `tags`**, not from fixed columns. Extract both before grouping: `df['clinic_id'] = df['tags'].apply(lambda x: x.get('clinic_id'))` — filter out rows where either is null before grouping.
- **US and UK must always be segmented separately** — Claire Whitfield (CCO) requires country-level data for every compliance report. A combined metric that mixes both countries has no compliance value.
- **No patient data will appear in your pipeline** — if any field in `tags` contains what appears to be a patient name, ID, or diagnosis, stop immediately, do not include it in any metric, and escalate to the tech lead. Your pipeline must only touch `supply_id`, `clinic_id`, `country`, `consumption_type`, and `event_type`.

---

_HealthCore Digital — Internal document for 4Geeks Academy AI Engineering Track_
