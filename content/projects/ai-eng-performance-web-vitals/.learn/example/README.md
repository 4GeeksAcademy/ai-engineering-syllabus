# Pet Shelter Frontends — Lighthouse Mini-Audit (Class Example)

> **For instructors:** Parallel classroom scenario for `ai-eng-frontend-performance-audit`. Same loop (measure → analyze → fix → remeasure) and documentation pattern, different domain. Students still follow the full monorepo brief in the project root `README.md`.

_Estas instrucciones también están disponibles en [español](./README.es.md)._

---

## The challenge

**Paws & Co. Rescue** runs a small Next.js monorepo: a public adoption site (`adopt-site`) and a staff intake app (`intake-app`). Adoption traffic is growing; intake staff complain the dashboard feels sluggish. In one session, demo the audit loop on **one page per app** — not the full corporate/backoffice scope of the graded project.

### Scope note

| Graded project                          | This class example                       |
| --------------------------------------- | ---------------------------------------- |
| Corporate site + company backoffice     | Adoption site + intake dashboard         |
| Desktop + mobile on public site         | Desktop only (save time)                 |
| ≥2 refactor candidates documented       | 1 duplicate pattern → 1 shared hook      |
| Full CTO checklist + agent skills       | Lighthouse + 1 targeted fix + short docs |
| `audit/before` + `audit/after` full set | 2 screenshots per phase (4 total)        |

---

## What to build

### 1. Baseline Lighthouse

- [ ] Run Lighthouse (Chrome DevTools) on `adopt-site` home (`/`) — **desktop**.
- [ ] Run Lighthouse on `intake-app` main list view (e.g. `/animals`) — **desktop**.
- [ ] Save PNGs to `audit/before/adopt-home.png` and `audit/before/intake-list.png`.

Record four scores per run: Performance, Accessibility, Best Practices, SEO (SEO may be N/A on intake if not applicable — note it).

### 2. Quick code review

- [ ] Find **one** duplicated pattern (e.g. identical `useEffect` fetch + loading UI in two components).
- [ ] Note in a short `AUDIT.md`: file paths, why it hurts maintainability, proposed hook name.

### 3. One fix + one refactor

- [ ] Apply **one** Lighthouse-driven fix (e.g. `next/image` on the largest LCP image, or `font-display: swap`).
- [ ] Extract **one** `useAsyncList(url)` (or similar) hook used in at least one component.

### 4. Re-measure

- [ ] Re-run Lighthouse on the same two URLs.
- [ ] Save to `audit/after/` with matching filenames.
- [ ] Write `REPORT.md` (½ page): what changed, before/after table for Performance only.

---

## Verify together

- [ ] Both `audit/` folders exist in the repo with committed images.
- [ ] `AUDIT.md` has a root-cause sentence for the chosen fix (not copy-paste Lighthouse labels only).
- [ ] Shared hook is imported somewhere real (not dead code).
- [ ] Apps still serve in production mode (`npm run build` + `npm run start`, or your monorepo command); Lighthouse screenshots must come from that server, not `npm run dev`.

---

## Discussion questions

1. Why is auditing only the homepage insufficient for a multi-route app? When would you add a second URL?
2. What is the difference between a Lighthouse **opportunity** and a fix that addresses **root cause**?
3. How would you adapt this loop into CI later (budgets, Lighthouse CI, or synthetic checks)?
