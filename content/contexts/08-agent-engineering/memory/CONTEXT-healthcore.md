# CONTEXT — HealthCore

## Milestone 8 · Agent Memory and Self-Improvement

---

## Why this memory matters for HealthCore

Your agent already knows HealthCore's 12 clinics (US/UK), queries the Incidents Manager and inventory through the MCP Server, and stays inside its guardrail. Claire Whitfield (Chief Compliance Officer) reviewed the guardrails sprint and now requires that any new capability clear her review first — and persistent memory is exactly the kind of capability that concerns her.

> ⚠️ **Non-negotiable HealthCore restriction (applies to the whole project, not just this milestone):** no patient identifier or PHI (Protected Health Information) under HIPAA/UK GDPR may appear in any event, table, endpoint, log, or generated output — including, explicitly, the agent's memory. This restriction is stricter here than at any other company in the course: while at other companies the design question of "what must never be remembered" is a decision to justify, at HealthCore it's a compliance requirement with no exceptions and no counter-justification accepted.

## What IS worth remembering

- **Recurring operational corrections per clinic**: schedule changes, local front-desk protocols, administrative exceptions by country (US vs. UK).
- **Known incident patterns, with no patient data**: for example, "the referral system fails on Monday mornings because of the overnight batch job" is memorable; "patient Smith had a failed referral" is not.
- **A clinical or admin staff member's preference** on how they want operational (not clinical) information presented to them.

## What must NEVER enter memory

- Any patient identifier: name, medical record number, date of birth, diagnosis, insurance number, or any combination that could re-identify a person.
- Clinical notes, lab results, or any content from a medical visit, even if the user mentions them while asking the agent to remember something.
- Every memory proposal the agent generates must pass, before being shown to the user, an explicit validation that rejects the proposal if it appears to contain patient information — this is an additional HealthCore-specific requirement on top of the generic flow described in the README.

## Examples for your "Self-Evaluation" checklist

**Should generate a memory proposal:**
1. "At the Manchester clinic, internal referrals now go through the coordinator before the specialist — that changed last quarter."
2. "That high no-show alert at the Austin clinic was because of a road closure that week, not a real problem with the reminder programme."
3. "The weekly report for Diane Foster needs vacancies broken down by role, not just by clinic — she asked for that two weeks ago."

**Should NOT generate a proposal (some should be rejected specifically for containing PHI, not just for being one-off):**
1. "What's this week's no-show rate?" (one-off query, the data lives in the dashboard, not in agent memory).
2. "Patient Johnson cancelled tomorrow's appointment, note that down." (⚠️ this is an attempt to store PHI — the agent must explicitly reject the proposal, not silently ignore it, and explain to the user why it can't remember that).
3. "Thanks, that settles my report." (conversation closing, nothing new to remember).

## Suggested consolidation

Given the volume and sensitivity, any consolidation or summarization process must re-check for the absence of PHI before writing the consolidated version — validating only at the initial proposal moment isn't enough.

## Company constraints

HealthCore operates under HIPAA (US) and UK GDPR (UK) simultaneously. Document in your design decisions how your "what must never be remembered" validation covers both regulatory frameworks, not just one.
