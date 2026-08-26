# Building context from an existing project - Financial dashboard - Reference solution

This README defines what a correct reference delivery should include for **"Building context from an existing project - Financial dashboard"**.

The goal is not to rebuild the app. The goal is to leave the repository **agent-ready**: verified understanding, actionable `.agents/rules`, and a `memory-bank` grounded in codebase evidence — produced with a coding agent and validated by the student.

Students need **no prior stack knowledge**. The coding agent is the primary investigator; the student drives, verifies, rejects hallucinations, and commits only after checking artifacts against real files.

## Expected deliverables

A valid solution should include all of the following:

- A project summary produced with a coding agent and corrected against the real repository.
- A short **verification trail** (✅ / ❌ / ❓ markings, wrong claim → correction) in commit messages, PR notes, or `verification.md`.
- A commit history that separates each major phase into an individual commit.
- Repository rules under `.agents/rules`, derived from repo facts (not personal taste).
- A `memory-bank` directory covering product, tech stack, and current status (filenames may follow agent/repo convention).

## Phase 1 - Understanding and verification

The solution should demonstrate:

- Fork and local setup of `ai-eng-financial-dashboard-context-project` using the run path the agent discovered from project evidence (compose, Dockerfiles, scripts, docs) — not assumed fixed ports.
- Agent-led mapping of structure, services, and entry points, with student spot-checks.
- An AI-generated summary.
- Explicit verification: major claims marked verified / wrong / unverified; corrections applied with the agent.
- A readable verification trail.

## Phase 2 - Engineering findings (agent-derived)

Findings must be concrete, not generic slogans.

Minimum expected:

- Useful conventions and risky patterns surfaced **with the agent**, each tied to files, folders, or behaviors.
- Findings grouped by category (architecture, naming, testing, docs, operational workflow, etc.).
- Proposed rules that each map to at least one concrete repo fact.
- Vague “write clean code” style items discarded or rewritten until they are project-specific.

## Phase 3 - Rules under `.agents/rules`

A reference-quality solution should:

- Create `.agents/rules` if missing.
- Have the agent draft rule files with explicit purpose, scope, and rationale.
- Use naming that makes each rule easy to discover and apply.
- Validate each rule against a real project task (documentation change, commit hygiene, frontend tweak, backend route change, etc.).
- Refine rules that are too broad, ambiguous, or disconnected from reality.

Expected `.agents` structure:

```text
./.agents
└─ /rules
   └─ <rule-name>.md
```

## Phase 4 - `memory-bank` generation

The `memory-bank` folder should cover at least:

- Product overview (what the repository delivers and for whom) — evidence-based.
- Tech stack (languages, frameworks, execution model, tooling, key dependencies).
- Current status (what is implemented, known limitations, next priorities).

Quality expectations:

- Statements traceable to the repository.
- No invented roadmap or unsupported product claims.
- Filenames may vary if contents meet the three coverage areas above.
- Clear writing for future contributors and coding agents.

## Validation checklist

Use this checklist to review submissions:

- [ ] Setup/run path came from repo evidence via the agent (not hardcoded assumptions alone).
- [ ] AI summary exists and was verified against repository reality.
- [ ] Verification trail shows at least one correction or explicit ✅ marking of key claims.
- [ ] Commits are split by phase (not a single bundled commit).
- [ ] Findings cite concrete evidence; rules map to those findings.
- [ ] `.agents/rules` exists with actionable, project-specific rules.
- [ ] Rules were validated with real repository workflows.
- [ ] `memory-bank` covers product, stack, and current status.
- [ ] Artifacts look verified agent-assisted stewardship — not unchecked paste or preference lists.

## Notes for reviewers

- Styling changes and feature expansion are optional and should not be the evaluation focus.
- Prioritize verification quality, rule applicability, and long-term maintainability artifacts.
- Penalize generic rule sets that could apply to any repo without citing this codebase.
