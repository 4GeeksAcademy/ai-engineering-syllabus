# CONTEXT — Brasaland

## Milestone 8 · Agent Memory and Self-Improvement

---

## Why this memory matters for Brasaland

Your agent already knows Brasaland's 14 locations (Colombia and Florida), queries the Incidents Manager and inventory through the MCP Server, and stays inside its guardrail. The problem Felipe Guerrero (Operations Director) reports: the same location managers repeat the same corrections week after week — "the Medellín meat supplier delivers on Tuesdays, not Mondays," "the Miami location closes at 10pm on Fridays, not 9pm" — and the agent keeps treating them as brand-new questions every time.

## What IS worth remembering

- **Recurring operational corrections per location**: real opening/closing hours, specific supplier delivery days, local exceptions to a standard procedure.
- **Context from a resolved escalation**: if a "no sales in 2 hours" alert at a location turned out to be a known issue (e.g., a scheduled power outage in that area), it's worth remembering so it isn't re-escalated.
- **A location manager's communication preferences**: if Carlos Jiménez (senior supervisor) always wants reports in a specific format, that's memorable.

## What must NEVER enter memory

- Brasa Points customer personal data beyond what's strictly operational (that doesn't need agent memory — it lives in the CRM).
- Payroll figures or individual staff compensation across the 14 locations.
- Anything that only applies to a one-off conversation with no repeatable pattern (a single customer complaint on a single day isn't memorable).

## Examples for your "Self-Evaluation" checklist

**Should generate a memory proposal:**
1. "Actually the vegetable supplier in Zaragoza... wait, I mean Medellín, delivers on Wednesdays, not Tuesdays like you said before."
2. "The Miami Beach location now closes at 11pm on weekends, that changed last month."
3. "That zero-sales alert at location 7 was because of a power outage, not a POS error — it's happened twice this month already."

**Should NOT generate a proposal:**
1. "What was yesterday's average ticket in Bogotá?" (one-off query, the data already lives in the telemetry pipeline, not in agent memory).
2. "Thanks, that answers my question." (conversation closing, nothing new to remember).
3. "Can you translate this into English for Ashley's report?" (single-use task, no lasting value).

## Suggested consolidation

With 14 active locations, episodic memory can grow fast if it isn't grouped by location. Consider having consolidation summarize by location + category (hours, suppliers, known incidents) instead of storing every correction as a loose entry — this is a design decision you must justify yourself, not a fixed requirement.

## Company constraints

Brasaland operates across two currencies (COP/USD) and two languages. If your agent supports bilingual operation, the memory proposal and user confirmation must work in the chosen base language — don't assume the user will always correct it in Spanish.
