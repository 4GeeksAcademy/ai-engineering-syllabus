# Capstone — Final Project Video — Reference solution

This is an **explanatory** reference. There is no single correct video. A passing submission is a ~5-minute landscape pitch of **the student's own company system**, delivered as a **Google Drive (or similar) folder link** with the required files.

Do not treat the sample names below as a company students may copy. They illustrate shape, timing, and voice. The student's CONTEXT supplies the real entities.

## Expected deliverable set

The student uploads **one shared folder** (Google Drive, Dropbox, OneDrive, or equivalent). Anyone with the link can view. The folder contains:

| File                                                       | Spec                                                                                                                                                           |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FirstnameLastname-ProjectName.mp4`                        | MP4 preferred, 1080p if possible, ~5 minutes, landscape                                                                                                        |
| `FirstnameLastname-ProjectName-description.txt`            | 1–2 sentence written project description for showcasing                                                                                                        |
| `FirstnameLastname-media-release.pdf` (or `.jpg` / `.png`) | Signed media release. Cohort-private opt-out is allowed via marked form or a one-line `FirstnameLastname-media-release.txt`. Opt-out does not fail the project |

The LMS field receives **the folder URL**, not a GitHub PR, not an email attachment, not the MP4 as a repo file.

No new application code is required.

## What “done” looks like in the video

```
0:00–0:30  Camera. Hook = problem or result. Then name + project + process.
0:30–1:20  Problem & opportunity (who, what, why it pays).
1:20–3:20  Live demo of the company workflow + what the AI actually does.
3:20–4:05  One hard problem, one X-over-Y trade-off, one pride point.
4:05–4:50  Camera. Three Q&A answers, 2s silence before/after each.
```

Total stays near five minutes. A 12-minute tour of every project in the course fails the brief.

## Sample description file

`JordanLee-IntakePilot-description.txt`:

```text
Operations staff spent hours answering the same intake questions. I built an AI
workflow that triages those requests against company knowledge and hands a
draft to the right department for human sign-off.
```

## Sample spoken script (indicative, not to be read)

**Hook (do this, not a name-first intro):**

> Repeat intake questions were eating four hours a week from operations. I'm Jordan, and I built Intake Pilot — an agentic workflow that drafts the response from our knowledge base and stops for human sign-off before anything leaves the building.

**Engineering voice (pass):**

> I chose a per-department interrupt over a single global pause because one team waiting on approval must not freeze the others. The checkpointer stores that branch; a full restart would have dropped work already approved.

**Engineering voice (fail — sounds like homework):**

> In this project I learned how LangGraph interrupts work.

**Q&A (pass — complete sentence includes the question):**

> What made me decide to pursue AI Engineering was watching tools ship without anyone who could own the system around them — and what almost held me back was my full-time job; I did not think I would have the hours.

> There was a moment during the RAG project when things really clicked for me: the first time a wrong chunk produced a confident lie, and retrieval quality stopped being theoretical.

> What I would tell someone who's on the fence about joining 4Geeks is this: if you want a portfolio that is one company system, not ten disconnected tutorials, this is the program that forces that.

**Q&A (fail):**

> Probably time, yeah.

Leave **two full seconds** of silence before and after each of those three answers. Editors cut on the silence.

## Architecture of the pitch (not of the product)

```text
Hook (result) → Problem (stakeholder pain) → Demo (value on screen)
        → Trade-off (how you think) → Q&A clips (4Geeks story)
```

The product architecture lives in the monorepo. The video only needs enough of it to make the demo intelligible. Dumping every service (auth, telemetry, Prefect, Qdrant, SSE) in two minutes hides the story.

## Common failures vs acceptable

| Fail                                                      | Pass                                                              |
| --------------------------------------------------------- | ----------------------------------------------------------------- |
| “Hi, my name is…” as first line                           | Problem or metric first, name second                              |
| Vertical phone video                                      | Landscape                                                         |
| Laptop mic, echo, music bed drowning speech               | Headset/close mic, quiet room                                     |
| Slides of boxes, no running UI                            | Screen recording of the real workflow                             |
| Generic chatbot unrelated to CONTEXT                      | Same entities, fields, and constraints as CONTEXT.md              |
| Tool laundry list (FastAPI, Next, Qdrant, LangGraph…)     | One sentence on the AI piece that makes the workflow work         |
| “I learned a lot this bootcamp” in section 4              | “I chose X over Y because…”                                       |
| Q&A answers that cannot stand alone                       | Question restated in a full sentence, eyes on lens                |
| GitHub PR / YouTube-only / missing description or release | Drive (or similar) folder with MP4 + description + signed release |
| `video.mp4` or spaces/`final video.mp4`                   | `FirstnameLastname-ProjectName.mp4`                               |
| Link set to “restricted” / request access                 | Anyone-with-the-link can view (or instructor explicitly added)    |

## Reviewer checklist

- [ ] ~5 minutes, landscape, face and voice usable
- [ ] Hook is not name-first
- [ ] Demo is this company's system
- [ ] One explicit trade-off
- [ ] Three Q&A answers, cut-ready (sentence includes question, 2s pads, lens)
- [ ] MP4 named `FirstnameLastname-ProjectName.mp4`, 1080p if possible
- [ ] 1–2 sentence description file present
- [ ] Signed media release or explicit cohort-private opt-out present
- [ ] Google Drive (or similar) folder link opens without an access request

## Notes for reviewers

Grade the **communication of value** and evidence that the system is real. Do not fail a video for missing color grading or a fancy intro bumper. Do fail a video that recites the syllabus, ignores CONTEXT, delivers Q&A as one-word replies, or is missing required files / a working Drive-style link.
