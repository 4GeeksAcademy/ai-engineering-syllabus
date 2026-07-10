# Report template

Emit this in chat. Omit categories with zero findings. Keep descriptions to one line.

Emoji legend — severity: ⛔️ blocker · ⚠️ warning · 🧴 cosmetic. Category: 👷‍♂️ intra-project · 📄 context · 💡 solution · ❎ cross-project.

```markdown
# Project analysis — <scope description>

**Scope:** <single | list | prefix:<x> | context:<company>> · **Projects:** N · **Findings:** ⛔️ B · ⚠️ W · 🧴 C

## Summary

| ID       | Sev         | Category         | Location                                     | Issue                                          |
| -------- | ----------- | ---------------- | -------------------------------------------- | ---------------------------------------------- |
| INTRA-01 | ⛔️ blocker  | 👷‍♂️ intra-project | README · What We Will Evaluate               | Eval "X" has no matching deliverable           |
| CTX-01   | ⚠️ warning  | 📄 context       | README · Challenge                           | README says 5 roles; CONTEXT-brasaland lists 3 |
| SOL-01   | ⚠️ warning  | 💡 solution      | .learn/solution/README.md                    | Requirement "daily summary" not covered        |
| XPROJ-01 | 🧴 cosmetic | ❎ cross-project | openclaw-memory vs openclaw-onboarding-agent | Wording drift in shared terminology            |

## Findings

### INTRA-01 · ⛔️ blocker · 👷‍♂️ intra-project

- **Where:** _What We Will Evaluate_ item 4 ↔ _What You Need to Do_
- **README:** [content/projects/<slug>/README.md](content/projects/<slug>/README.md)
- **Conflict:** <one line: what disagrees with what>
- **Alternatives:**
  - A) <change side 1 to match side 2>
  - B) <change side 2 to match side 1>

### CTX-01 · ⚠️ warning · 📄 context

- **Where:** _Challenge_ ↔ `CONTEXT-<company>.en.md`
- **README:** [content/projects/<slug>/README.md](content/projects/<slug>/README.md)
- **Context:** [content/contexts/<ctx>/CONTEXT-<company>.en.md](content/contexts/<ctx>/CONTEXT-<company>.en.md)
- **Conflict:** <one line>
- **Alternatives:**
  - A) <align README to context>
  - B) <align context to README>

### XPROJ-01 · ⚠️ warning · ❎ cross-project

- **Where:** <project-a> ↔ <project-b>
- **READMEs:** [<project-a>](content/projects/<project-a>/README.md) · [<project-b>](content/projects/<project-b>/README.md)
- **Conflict:** <one line>
- **Alternatives:**
  - A) <...>
  - B) <...>

<!-- repeat per finding -->
```

## Notes

- Never recommend which alternative to take unless the user asks — present both.
- If a project is clean, say so explicitly instead of inventing findings.
- Issue IDs are report-global: number each category continuously across the whole report and never reset per project. Tell projects apart via the location + README link.
- Every finding must include a clickable **README** link so the user can jump to the file. Make link paths workspace-root-relative, i.e. prefix with the repo folder: `ai-engineering-syllabus/content/projects/<slug>/README.md` (same for context: `ai-engineering-syllabus/<ctx-folder>/CONTEXT-<company>.en.md`). Use the `dir` field from the script output to build these.
