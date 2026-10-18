# Rename BRIEFING artifact → BRIEFING

Branch: main (no commit until user asks)
Delivery: ask-on-risk
Test runner: structural (rg counts + analyzer dry-run)

## Specs

- S1: User: "Lets call it \"CASE\"" then "Use BRIEFING" then "no" (keep folder `content/contexts/`).
- S2: File prefix `*-BRIEFING` → `*-BRIEFING` (md + pdf); student root name `BRIEFING.md` → `BRIEFING.md` in docs.
- S3: Keep directory `content/contexts/` and `00-general-contexts` folder names.
- S4: Update skills/scripts/READMEs that refer to the artifact as BRIEFING to BRIEFING.
- S5: Do not rename unrelated "context" (AI agent context, folder paths, project slugs like `*-context-project`).

## Tasks

- T1 S2-S3: rename files under content/contexts — done
- T2 S4: rewrite references in content + .cursor — done
- T3 S4: update project-analyzer regex/CLI — done
- T4 S2-S5: verify leftover BRIEFING artifact refs — pending

## Log

- L1: User chose BRIEFING; declined renaming content/contexts/ folder.

- L2: Implemented file rename CONTEXT*→BRIEFING* (220), text rewrites, analyzer --group-briefing. Folder content/contexts/ kept.
- L3: Renamed again to `*-BRIEFING.(en|es).md` (e.g. `brasaland-BRIEFING.en.md`); skills + analyzer regex updated; general profiles no longer `*-briefing-BRIEFING.*`.
