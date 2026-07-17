# CONTEXT — Nexova

## Milestone 8 · Agent Memory and Self-Improvement

---

## Why this memory matters for Nexova

Your agent already knows Nexova's three business lines (headhunting, support outsourcing, corporate training), queries the Incidents Manager and inventory through the MCP Server, and stays inside its guardrail. Roberto Díaz (Customer Support Lead) reports that his 30 support agents, when using the internal assistant, have to re-explain the same escalation procedure every time they talk to it — the assistant retains nothing between sessions.

## What IS worth remembering

- **Corrected escalation procedures**: if a ticket's SLA or reassignment criteria changed and an agent corrects it, that's worth remembering.
- **Preferences of recurring Nexova clients** (outsourcing client companies, not individual candidates): for example, that a tech client always prefers email communication over calls.
- **Known helpdesk incident patterns**: "billing tickets from finance-sector clients usually escalate straight to Tom Callahan, not first-line support."

## What must NEVER enter memory

- Personal data from selection process candidates (résumés, ratings, interview notes) — that lives in the ATS and the candidate RAG system, not the agent's conversational memory.
- Salary information from active headhunting negotiations.
- One-off corrections with no repeatable pattern that only apply to a single ticket.

## Examples for your "Self-Evaluation" checklist

**Should generate a memory proposal:**
1. "Actually payroll tickets for retail clients now resolve in 24 hours, not 48 like the old SLA said."
2. "That finance client always wants email confirmation before we close a ticket, even though the system lets us close it directly."
3. "Tickets flagged 'urgent' from premium-contract clients should go straight to a senior agent, not the general queue — that changed this month."

**Should NOT generate a proposal:**
1. "How many open tickets are there right now?" (one-off query, the data lives in the dashboard).
2. "Perfect, thanks for the explanation." (conversation closing).
3. "Summarize this ticket in two lines for Laura's report." (single-use task).

## Suggested consolidation

Nexova mixes data from three distinct business lines (headhunting, support, training). Consider whether memory should be separated by business line or kept unified — justify your choice in the design decisions.

## Company constraints

Nexova operates between Spain and Miami; if your agent supports bilingual operation, the memory proposal and confirmation must work in the chosen base language.
