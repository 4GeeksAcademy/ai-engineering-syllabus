# CONTEXT — TrackFlow

## Milestone 8 · Agent Memory and Self-Improvement

---

## Why this memory matters for TrackFlow

Your agent already knows TrackFlow's operations in Los Angeles and Zaragoza, queries the Incidents Manager and inventory through the MCP Server, and stays inside its guardrail. Valentina Cruz (CX Manager) reports that her 15 support agents, split across both countries, have to correct the assistant on the same carrier rules over and over — the assistant doesn't learn from one session to the next.

## What IS worth remembering

- **Corrected carrier assignment rules**: if a carrier changed its coverage for a certain zone, or stopped operating a certain route, that's worth remembering.
- **Context from known, recurring incidents**: "the delays on the Zaragoza-to-Catalonia route this week are due to a carrier strike, not a TrackFlow problem" — useful so the same alert isn't re-escalated.
- **Recurring B2B clients' preferences** for their monthly report (format, highlighted metrics).

## What must NEVER enter memory

- Exact end-customer (B2C) addresses or internal warehouse routes — this is sensitive physical-security information, as the company's own guardrails README already flags.
- Data from a single, non-repeating package incident (an isolated customer complaint isn't memorable).
- Information from active commercial contract negotiations (that's handled by the commercial team's CRM, not the support agent's memory).

## Examples for your "Self-Evaluation" checklist

**Should generate a memory proposal:**
1. "Actually SEUR no longer covers that rural area of Zaragoza, we've had to use the local carrier since last month."
2. "Those delays reported in Los Angeles incidents this week are from the port strike, not something on our end — that's the third ticket about it already."
3. "The cosmetics client always wants their monthly report with the returns breakdown first, before shipment volume."

**Should NOT generate a proposal:**
1. "Where's the package with tracking XJ4471?" (one-off tracking query, not a pattern).
2. "Great, that's resolved." (conversation closing).
3. "Translate this into English for the client." (single-use task).

## Suggested consolidation

TrackFlow works with 8 carriers across two countries. Consider consolidating memory by carrier + country rather than by individual ticket, so assignment rules don't end up fragmented across dozens of loose entries.

## Company constraints

TrackFlow distinguishes between B2B clients (brands) and B2C clients (end recipients). Your "what must never be remembered" validation must explicitly cover sensitive location data for both client types, not just one.
