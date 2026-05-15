# My Agent, My Way: Teaching Your Personal Assistant New Skills — Reference Solution

## Purpose

This document describes what a **complete submission** looks like for this assignment: personalized agent configuration, documented skill design, and at least two working OpenClaw skills that use **only** tools already connected via Composio (and Telegram where applicable).

## Expected repository layout

- **`.openclaw/`** — five Markdown briefings the agent loads before acting:
  - `IDENTITY.md` — name and symbol; non-generic.
  - `SOUL.md` — concrete personality: uncertainty, ask vs act, tone.
  - `AGENTS.md` — hard limits; at least one privacy rule and one “stop and ask” rule.
  - `USER.md` — real student context: role, projects, tools, goals.
  - `TOOLS.md` — connected services, when to use each, and defaults (calendars, folders, channels).
- **`SKILLS_DESIGN.md`** (repo root) — for **each** planned skill: the three design questions answered **before** implementation commits.
- **Custom skills** — at least two skills implemented as proper OpenClaw skills (structured `SKILL.md` / skill folder per OpenClaw conventions), not one-off pasted prompts.

## Required coverage (from README)

- All five `.openclaw` files filled with specific, non-placeholder content.
- `openclaw doctor` completes with **zero** errors after edits.
- `SKILLS_DESIGN.md` committed before skill implementation work.
- At least two custom skills; each output should visibly reflect `SOUL.md`, `USER.md`, and related config.
- At least one skill produces **verifiable** output in a connected service (Google Docs, Calendar, Gmail, Tasks, Drive) **or** a Telegram message.
- No new external API, OAuth app, or Composio connection added for this project only — skills must use existing integrations.

## Validation evidence (what instructors look for)

1. **Doctor** — terminal log or screenshot showing `openclaw doctor` success after configuration.
2. **Design** — `SKILLS_DESIGN.md` git history (or clear commit message) shows it predates skill implementation.
3. **Skills** — trigger each skill with a real personal input; show the resulting Doc/Calendar/Task/Gmail/Drive artifact or Telegram message (link, id, or screenshot as appropriate).
4. **Consistency** — side-by-side: a quoted line from `SOUL.md` or `USER.md` and a matching trait in the skill output (tone, structure, or context).

## Indicative skill shapes (examples only)

These are **not** prescriptive; students choose their own repetitive workflows.

- **Doc append** — skill reads user bullets + `USER.md` journal preferences → appends a dated section to a known Google Doc.
- **Calendar block** — skill parses natural-language intent + `TOOLS.md` calendar defaults → creates Calendar event with reminders.
- **Telegram digest** — skill aggregates GitHub + `USER.md` repo list → sends formatted summary to Telegram.

## What is out of scope for a passing solution

- New OAuth clients, API keys for unrelated services, or “connect Slack/Notion” as part of this assignment.
- Generic one-line `SOUL.md` / empty `USER.md` / vague `TOOLS.md` with no real defaults or service conventions.

## Alignment with evaluation rubric

A submission can score well with a **strong `SKILLS_DESIGN.md` and partial automation**, if the design reasoning and config quality are excellent. Conversely, working skills with **no** design doc or **generic** five-file config should not expect top marks.
