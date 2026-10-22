# Campus Bike Share — Memory Bank Kickoff (Class Example)

> **For instructors:** Not the student project. Live demo (~60–90 min) of the same spine as `ai-eng-monorepo-kickoff-memory-bank`: discovery conversation → synthesize vs keep-whole → empty stack policy → pending slots → `CONTEXT.md` index → clean-session check. Domain is a tiny campus bike-share co-op, not the company monorepo.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

A campus bike-share co-op has a nearly empty repo: folders with names, a placeholder `CONTEXT.md`, and a one-page “BRIEFING” plus two short department notes (Ops and Membership). Before any feature code, the class must leave an agent-ready memory bank so a fresh agent session understands what is being built, for whom, and under which rules — without inventing a stack.

### Scope note

| Keep (same spine)                        | Drop vs full project                           |
| ---------------------------------------- | ---------------------------------------------- |
| Discovery Q&A before writing             | Full company BRIEFING + many departments       |
| Memory bank as separate concern files    | Five user stories from three depts (use **3**) |
| Empty stack + entry policy + template    | Full monorepo folder map (use **3** folders)   |
| Pending + unlock event                   | Long PR write-up (verbal is enough in class)   |
| Short `CONTEXT.md` index + clean session | Multiple whole docs under `docs/` (use **1**)  |

Students still follow the full brief in the project root `README.md`.

---

## What to build

### Prep (5 min)

Provide a toy folder (or paste) with:

```text
campus-bike-share/
├── CONTEXT.md          ← placeholder only
├── apps/               ← empty, “rider-facing tools”
├── services/           ← empty, “ops APIs later”
├── docs/               ← empty
└── briefing/
    ├── BRIEFING.md     ← vision, users, non-goals (1 page)
    ├── ops-notes.md    ← checkout process with exceptions (keep whole)
    └── membership.md   ← short; safe to synthesize
```

### Discovery conversation

- [ ] In planning/chat mode, ask the agent to read the three sources and list ambiguities before proposing files
- [ ] Decide together: `ops-notes.md` → keep whole under `docs/`; `membership.md` + BRIEFING → synthesize
- [ ] Keep 1–2 agent questions that change what you write

### Memory bank (minimal set)

- [ ] Create `memory-bank/` with separate files: vision + acceptance (incl. **3** user stories from Ops, Membership, and one more role), tech stack (empty + policy + template), architecture (folder responsibilities only), commands (pending + unlock), taboos (at least “no invented stack”), current status
- [ ] Cite source on each file; link `docs/ops-notes.md` with when-to-read

### Context entry point

- [ ] Replace `CONTEXT.md`: 3–4 line co-op blurb + index of every memory-bank and docs file with when to read + “update this index when tech/docs/status change”

### Verify together

- [ ] New chat, “start from `CONTEXT.md`”: ask who the users are, what is out of scope, and whether FastAPI is the stack → agent must say stack undecided and cite policy
- [ ] Ask it to propose a library → must demand exact version + official source
- [ ] Fix any hallucination, re-ask once

---

## Discussion questions

1. Why is dumping the BRIEFING into `CONTEXT.md` worse than a short index with when-to-read lines?
2. When should a process stay whole under `docs/` instead of being summarized in the memory bank?
3. How does an empty stack document with an entry policy stop the agent from inventing technology?
