# Company Incident File Analysis - Reference solution

This README defines what a correct reference delivery should include for the **Company Incident File Analysis** project.

The expected output is a robust CLI analysis script that validates incident records against `CONTEXT-company.md`, reports trustworthy metrics, and supports CSV export for non-terminal users.

## Expected deliverables

A valid solution should include:

- `analyze.py` at the project root.
- A supported dataset file (for example `incidents-brasaland.csv` or equivalent company file).
- Console summary output with clear formatting (labels, separators, aligned values).
- Optional CSV export (`results.csv`) triggered by user confirmation.

## Required implementation structure

The reference solution should be organized into clear, testable functions with single responsibilities:

- Argument parsing (`python analyze.py incidents.csv`).
- CSV loading/parsing.
- Record validation by context rules.
- Metrics aggregation on valid records.
- Console report rendering.
- Export serialization (CSV).

## Validation rules that must be enforced

A record is invalid when any required constraint from the selected context is violated. At minimum:

- Missing required fields.
- Invalid category/status value (outside allowed set).
- Incomplete description (for contexts that require minimum length).
- Closed incidents without score (when the context requires score for closed status).
- Scores outside accepted numeric range.

Invalid records must be:

- Counted.
- Classified by reason.
- Excluded from valid-only metrics.
- Explicitly reported (never silently ignored).

## Metrics the script must output

On **valid records**, the solution must report:

1. Total processed records, split into valid and invalid totals.
2. Breakdown by category.
3. Breakdown by status.
4. Satisfaction metrics for closed incidents with score:
   - Number of scored closed incidents.
   - Average satisfaction score.
   - Optional distribution by score if available in context.

Where expected values are provided in `CONTEXT-company.md`, numeric totals must match exactly for the official sample CSV.

## CSV export expectations

At the end of execution, the script prompts:

`Export results to CSV? [y / n]`

Behavior:

- `y` -> generates `results.csv` with one row per metric.
- `n` -> exits without generating export.

Recommended export schema:

- `metric`
- `value`
- `percentage` (optional for ratio-based rows)

## Quality checklist (reviewer-ready)

- [ ] Script accepts CSV path via command-line argument.
- [ ] Input file is parsed safely, with clear error handling.
- [ ] Invalid records are detected and grouped by rule type.
- [ ] Valid/invalid totals are correct and visible in output.
- [ ] Category and status breakdowns are correct for valid records.
- [ ] Satisfaction average is computed only on eligible closed records.
- [ ] Console output is readable and professional (not raw dict output).
- [ ] CSV export prompt and behavior (`y/n`) work as specified.
- [ ] For the official sample file, results match context expected values.

## Notes for reviewers

- Minor spacing/styling differences in the console report are acceptable if all required values and sections are present.
- Prioritize data correctness, validation completeness, and clarity of script structure over cosmetic formatting.
