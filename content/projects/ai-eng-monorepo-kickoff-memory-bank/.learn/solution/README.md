# Monorepo Kickoff – Memory Bank and Project Context — Reference Solution

This README defines what a correct delivery looks like for **Monorepo Kickoff – Memory Bank and Project Context**.

The goal is not to choose a stack or ship product features. The goal is to leave the company monorepo **agent-ready**: a curated `memory-bank/`, a short `CONTEXT.md` index, selective `docs/` references, and evidence that a clean agent session can orient from the repository alone.

Students work on their fork of the company monorepo, on branch `feature/memory-bank`, using their assigned company BRIEFING and department documents as source material.

## Expected deliverables

A valid solution should include all of the following:

- A discovery conversation with the coding agent (conversational or planning mode) before content is written in agent mode.
- A `memory-bank/` folder with **separate files per concern**, not one dump document.
- A tech-stack document that records **no technology yet**, but includes the CTO entry policy and a record template (name, exact version, official source, verification date, reason).
- Reserved documents for architecture, conventions, commands, taboos, and environment/access — filled where evidence exists, otherwise marked **pending** with the event that unlocks each item.
- At least five user stories across at least three departments, each with stakeholder and verifiable acceptance criteria, plus a shared definition of done.
- Source citations (or `docs/` links) on every memory-bank file.
- Whole-kept source documents under `docs/`, organized by topic, linked from the memory bank with when-to-read guidance.
- A replaced root `CONTEXT.md`: short company description, index of every `memory-bank/` and `docs/` file with when to read each, and an instruction to update the index when tech, docs, architecture decisions, or status change.
- A Pull Request against `main` with clean-session test evidence and commit history that separates documents/decisions.

## Architecture of the context package

```text
monorepo/
├── CONTEXT.md                 ← entry point + index (when to read each file)
├── memory-bank/
│   ├── vision-and-acceptance.md   (or equivalent split)
│   ├── tech-stack.md              (policy + empty registry)
│   ├── architecture.md            (folder responsibilities; pending patterns)
│   ├── conventions.md
│   ├── commands.md
│   ├── taboos.md
│   ├── environment-and-access.md
│   └── current-status.md
└── docs/
    └── <topic>/...                ← full processes/policies kept whole
```

**Memory vs documentation:** memory summarizes what the agent needs to decide; `docs/` keeps full process/policy detail. Memory links to docs so the agent loads detail only when the task requires it.

## Discovery conversation (required process)

A reference-quality delivery shows that the student:

1. Asked the agent to read the BRIEFING and department docs and to surface ambiguities **before** proposing memory-bank content.
2. Answered, decided, and kept questions that changed what was written.
3. Reviewed every agent proposal against source documents.
4. Classified each source: synthesize into memory bank **or** keep whole under `docs/`.

Generic memory banks that would fit any company, or dumps of the BRIEFING without that classification, fail the rubric.

## Indicative examples

### Good: stack document (empty registry + policy)

```markdown
# Tech stack

## Entry policy

- Official sources verified by a human
- Well-known, maintained libraries only
- Exact pinned versions (no `latest`, no open ranges)
- API versions checked in current official docs, not model memory

## Registry

| Name | Exact version | Official source | Verified on | Reason                    |
| ---- | ------------- | --------------- | ----------- | ------------------------- |
| —    | —             | —               | —           | No technology decided yet |

## Pending

- First framework choice → unlock when product PRD requires an implementation language
```

### Bad: inventing a stack to look complete

```markdown
We use FastAPI 0.115, React 19, and PostgreSQL 16...
```

That invents undecided technology and violates the CTO ticket.

### Good: pending slot with trigger

```markdown
## Build / test / run commands

Pending until the first service lands in the monorepo and CI is introduced.
Unlock event: merge of the first app package with a documented run path.
```

### Good: `CONTEXT.md` index line

```markdown
- `memory-bank/tech-stack.md` — read before adding any dependency or accepting an agent library suggestion.
- `docs/hr/onboarding-policy.md` — read only when implementing or answering questions about employee onboarding deadlines/exceptions.
```

### Clean-session verification (PR evidence)

Document in the PR:

1. Three+ questions about company, users, and stack answered from the repo (no invention).
2. A probe where the agent proposes a library and must apply the stack policy (exact version + official source).
3. Fixes applied where the clean session failed, then a re-test.

## Validation checklist

- [ ] `CONTEXT.md` is not the placeholder, does not paste the BRIEFING, and indexes every `memory-bank/` and `docs/` file with when-to-read.
- [ ] `memory-bank/` has separate files for vision/acceptance, stack, architecture, conventions, commands, taboos, environment/access, and current status.
- [ ] Vision and user stories match the assigned company and cite sources.
- [ ] ≥5 user stories from ≥3 departments; each has stakeholder + verifiable acceptance criteria; shared definition of done exists.
- [ ] Stack document has zero technologies recorded; policy + template present.
- [ ] Unavailable information is pending with triggers — no invented commands, libraries, or conventions.
- [ ] Architecture captures each monorepo folder’s responsibility.
- [ ] No memory-bank file is a verbatim company-doc dump; whole docs live under `docs/` and are linked.
- [ ] PR documents discovery questions, clean-session Q&A, synthesize-vs-docs decisions, and pending unlock events.
- [ ] Commits separate documents/decisions (no single mega-commit).

## Notes for reviewers

- Evaluate stewardship quality, not prose volume.
- Penalize invented stack, generic multi-company memory banks, and BRIEFING dumps.
- Reward clear synthesize-vs-`docs/` decisions and a clean session that navigates from `CONTEXT.md` alone.
