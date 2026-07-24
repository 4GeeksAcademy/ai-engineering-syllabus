---
name: lesson-generator
description: Generates a 4Geeks.com-style lesson as a bilingual pair of Markdown files (English + Spanish) using the breatheco content format — YAML frontmatter (title, description, author, tags), an H1, a two-paragraph hook, H2/H3 sections with fenced code blocks, images, a practical checklist, and a conclusion. Each lesson lives in its own folder under content/lessons/<slug>/ with <slug>.md and <slug>.es.md. Use when the user asks to "create a lesson", "generate a lesson", "write a 4Geeks lesson", "new lesson", "lesson in both languages", or references the breatheco/4Geeks lesson format. Trigger on "lesson", "lección", "frontmatter lesson".
disable-model-invocation: true
---

# 4Geeks Lesson Generator

Generates a lesson as **two files** in the same folder, matching the 4Geeks.com (breatheco-de/content) format — **frontmatter first**, then an H1 and body. Output is written to disk under `content/lessons/`.

## File layout (mandatory)

For a lesson with slug `my-example-lesson`:

```
content/lessons/my-example-lesson/
├── my-example-lesson.md      # English (canonical)
└── my-example-lesson.es.md   # Spanish
```

Rules:

- Folder name = slug = file base name. **kebab-case**, lowercase, ASCII, hyphen-separated.
- English file: `<slug>.md`. Spanish file: `<slug>.es.md`.
- Both files always created together. Never ship one language only.
- Path is relative to the `ai-engineering-syllabus` repo root: `content/lessons/<slug>/`.

## Frontmatter (mandatory, both files)

Every file starts with YAML frontmatter, then a blank line, then the H1. No content before the frontmatter.

```yaml
---
title: "Natural sentence-case title, only proper nouns capitalized"
description: "1–2 sentence SEO summary of what the reader will measure, build, or fix."
author: "<ask the user>"
tags: ["Tag One", "Tag Two", "Tag Three"]
---
```

- `title` — quoted; matches the H1 **text without any emoji** (in that file's language). **Write naturally in sentence case** — capitalize only the first word and proper nouns/tech names (e.g. "Performance and profiling in practice for React Native"), not every word. **No emojis in frontmatter.**
- `description` — quoted; concrete and outcome-oriented (what they learn/do/measure). **Max 250 characters.** Avoid marketing fluff.
- `author` — **always ask the user for this value before generating.** Never invent it.
- `tags` — JSON-style array of quoted strings. **Keep tags in English in BOTH files** (they are taxonomy, not prose). **1–5 tags**, capitalized as proper nouns/tech names.

### Bilingual frontmatter rule

`title` and `description` are **translated** per file (English in `.md`, Spanish in `.es.md`). `author` and `tags` are **identical** in both files.

## Language cross-link block (mandatory)

Immediately **after the H1**, insert the hide block linking to the other language, using the **global GitHub URL** (repo `4GeeksAcademy/ai-engineering-syllabus`, branch `main`):

English file (`<slug>.md`) — links to Spanish:

```markdown
<!-- hide -->

_Estas instrucciones también están disponibles en [español](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/lessons/<slug>/<slug>.es.md)._

<!-- endhide -->
```

Spanish file (`<slug>.es.md`) — links to English:

```markdown
<!-- hide -->

_These instructions are also available in [English](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/lessons/<slug>/<slug>.md)._

<!-- endhide -->
```

Replace `<slug>` with the real slug. The link text stays in the reader's language; the link points at the OTHER language file.

## Document structure (in order)

1. **Frontmatter** (above).
2. **H1** — `# <title>` matching frontmatter `title`. **Emojis are allowed here** (and in section headings), outside frontmatter — e.g. `# 🎯 RAG from scratch with Python and Qdrant` while frontmatter `title` stays `"RAG from scratch with Python and Qdrant"`.
3. **Cross-link hide block** (above).
4. **Hook** — 2 short paragraphs, no heading:
   - Paragraph 1: a concrete, relatable problem/scenario the reader recognizes.
   - Paragraph 2: reframe — what the lesson delivers and why the approach works. Set the stakes.
5. **Body** — `## H2` sections, each optionally split into `### H3` subsections. Progress from setup → core technique → deeper cases → strategies.
6. **Checklist** — a `## ...Checklist` section near the end: concrete, verifiable pass/fail items the reader runs before considering the work done.
7. **Conclusion** — a `## Conclusion` section: restate the systematic takeaway; no new material.

Use `---` horizontal rules between major sections **only if** it improves scanability (existing repo lessons use them; the breatheco reference mostly does not). Be consistent within a file.

## Content & style rules

- **Second person, practical, measurable.** Tell the reader what to do and how to verify it worked. Prefer numbers and observable signals over adjectives.
- **Sentence-case headings.** Write the title, H1, and all section headings naturally — capitalize only the first word and proper nouns/tech names. Never Title-Case every word. **Emojis are allowed in H1 and section headings only — never in frontmatter `title`.**
- **Code blocks** must carry a language tag: ` ```typescript `, ` ```python `, ` ```bash `, ` ```ruby `, ` ```yaml `, ` ```mermaid `, etc. Keep snippets realistic and self-contained; show the problem version then the improved version when teaching a fix.
- **Images**: `![descriptive alt](url)`. Use real asset URLs when the user provides them; otherwise insert a clearly-marked placeholder URL and list it in the delivery summary so the user can replace it. Never fabricate a URL that looks real.
- **Diagrams**: prefer a `mermaid` fenced block for flows (matches existing repo lessons).
- **No time-sensitive phrasing** ("as of 2024…"). Write evergreen; version-pin inside code/commands only when needed.
- **Length**: match depth to topic. Reference lessons run ~400–500 lines. Don't pad.

## Spanish translation rules (`.es.md`)

- Translate **all prose and headings** to natural, native classroom Spanish — not literal word-for-word.
- Translate `title` and `description` in frontmatter; keep `author` and `tags` identical to English.
- **Do not translate**: code (identifiers, keywords, string values), CLI commands, file paths, brand/tech names, URLs.
- Code comments: translate to Spanish (they are prose).
- Keep section order and structure identical across both files so they stay in sync.

## Required inputs — ask before generating

Confirm you have (or ask for) these. If multiple are missing, ask for all at once.

| Input             | Description                        | Required                                |
| ----------------- | ---------------------------------- | --------------------------------------- |
| `topic` / `title` | What the lesson teaches            | Required                                |
| `slug`            | kebab-case folder/file base name   | Derive from title if not given; confirm |
| `author`          | Frontmatter `author` value         | **Always ask**                          |
| `description`     | SEO summary, max 250 characters    | Draft it; confirm                       |
| `tags`            | 1–5 English tags                   | Draft them; confirm                     |
| `key_points`      | Core concepts / sections to cover  | Recommended                             |
| `audience_level`  | Beginner / intermediate / advanced | Optional (calibrates depth)             |
| `assets`          | Image/diagram URLs, if any         | Optional                                |

## Workflow

1. **Gather inputs** — resolve `title`, `slug`, and **ask for `author`**. Draft `description` + `tags` and confirm. Collect `key_points`/level if available.
2. **Check for collisions** — if `content/lessons/<slug>/` already exists, stop and confirm overwrite vs. new slug.
3. **Outline** — plan H2/H3 sections following the structure order. Keep hook → setup → technique → cases → strategies → checklist → conclusion.
4. **Write English** `<slug>.md` — frontmatter → H1 → cross-link block → hook → body → checklist → conclusion. Follow style rules.
5. **Write Spanish** `<slug>.es.md` — same structure; translate prose/headings, translate frontmatter `title`/`description`, keep `author`/`tags`; cross-link block points to the English file.
6. **Create the folder and both files** under `content/lessons/<slug>/`.
7. **Verify** against the checklist below, then report paths and any placeholder URLs the user must replace.

## Quality self-check before delivering

- [ ] Folder `content/lessons/<slug>/` contains exactly `<slug>.md` and `<slug>.es.md`.
- [ ] Slug is kebab-case; folder name = file base names.
- [ ] Both files start with valid YAML frontmatter (`title`, `description`, `author`, `tags`); nothing precedes it.
- [ ] `author` was provided by the user (not invented).
- [ ] `title`/`description` translated per language; `description` ≤ 250 characters in both files; `author`/`tags` identical; tags in English in both files; 1–5 tags.
- [ ] H1 text matches frontmatter `title` (same language), ignoring any leading emoji on the H1.
- [ ] Title, H1, and section headings are sentence case (only first word + proper nouns capitalized), not Title Case. Emojis only outside frontmatter (H1 / section headings).
- [ ] Cross-link hide block present right after H1, using the global GitHub `main` URL, pointing to the OTHER language file with the correct slug.
- [ ] Two-paragraph hook (problem → reframe), no heading.
- [ ] Body uses `##`/`###`; every code block has a language tag.
- [ ] Checklist section and Conclusion section present.
- [ ] Spanish reads natural (not literal); code/commands/paths/brands untranslated; comments translated.
- [ ] Both files share identical section order/structure.
- [ ] No fabricated real-looking image URLs; placeholders reported to the user.
- [ ] Output is valid Markdown.

## Additional resources

- Annotated template and a filled example: [reference.md](reference.md)
