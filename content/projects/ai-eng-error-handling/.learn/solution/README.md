# Error Handling Audit — Reference Solution

## Purpose

Reference quality bar for the **cross-cutting error-handling audit** on the company monorepo. No new features — only resilience and user-facing error communication across frontend, backend, and scripts.

## Scope of Work

Students work on branch `error-handling-audit` and fix existing code in:

- `uis/` — Next.js / TypeScript frontends
- `services/api/` — FastAPI backend
- `scripts/` or `packages/` — Python data/analysis scripts

## Required Coverage (From README)

### Frontend

- Scoped `try/catch` around each `fetch`/API call — not one catch around entire component.
- **Three-state UI**: loading → success → error on every async data fetch.
- Human-readable error copy — no raw status codes or `Unexpected token` messages.
- Every error state has a **call to action**: retry, go home, or contact support.
- `optional chaining` and fallbacks for nullable nested fields.
- `finally` clears loading flags.

### Backend

- Exceptions caught at operation scope inside route handlers.
- Structured JSON errors with correct status (`400`, `404`, `422`, `500`).
- No tracebacks, secrets, or internal paths in client responses.
- External API calls (LLM, third-party) wrapped with timeout/failure handling.

### Scripts

- `try/except` on file I/O and CSV parsing with messages to `stderr`.
- `sys.exit(1)` on critical failure.
- Defensive checks before processing malformed input.

### General

- Remove or redact `console.error` / `print` that leak sensitive data.

## Indicative Frontend Pattern

```tsx
const [state, setState] = useState<"idle" | "loading" | "success" | "error">(
  "idle",
);
const [errorMessage, setErrorMessage] = useState<string | null>(null);

async function loadSuppliers() {
  setState("loading");
  setErrorMessage(null);
  try {
    const res = await fetch(`${API_URL}/suppliers`, { headers: authHeader() });
    if (!res.ok) {
      throw new Error("We could not load the supplier list. Please try again.");
    }
    const data = await res.json();
    setSuppliers(data);
    setState("success");
  } catch (err) {
    setErrorMessage(
      err instanceof Error
        ? err.message
        : "Something went wrong. Please try again.",
    );
    setState("error");
  } finally {
    // loading cleared via state transition above
  }
}
```

Error UI must include retry or navigation — not a dead end.

## Indicative Backend Pattern

```python
@router.get("/suppliers/{supplier_id}")
def get_supplier(supplier_id: str, db: Session = Depends(get_db)):
    try:
        supplier = supplier_service.get_by_id(db, supplier_id)
    except DatabaseUnavailable as exc:
        logger.exception("supplier_lookup_failed")
        raise HTTPException(
            status_code=503,
            detail="The supplier directory is temporarily unavailable. Try again shortly.",
        ) from exc

    if supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found.")

    return SupplierPublic.model_validate(supplier)
```

Never return `str(exc)` from uncaught exceptions to the client.

## Indicative Script Pattern

```python
import sys

def main() -> None:
    try:
        rows = load_csv(path)
    except FileNotFoundError:
        print(f"Error: file not found: {path}", file=sys.stderr)
        sys.exit(1)
    except csv.Error as exc:
        print(f"Error: invalid CSV format — {exc}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

## Agent Audit Workflow

Before manual fixes, students may run the detection prompt from the project README. A strong submission often includes:

- Prioritised findings list (CRITICAL → LOW)
- Commits grouped by layer (`fix(web): …`, `fix(api): …`, `fix(scripts): …`)
- PR description summarising patterns applied

## Evaluation Checklist

- [ ] All audited async frontend fetches use loading / success / error states.
- [ ] User-facing errors are readable and include a call to action.
- [ ] `try/catch` and `try/except` blocks are narrowly scoped.
- [ ] `finally` (or equivalent) clears loading state.
- [ ] Backend returns structured errors without sensitive leaks.
- [ ] Scripts exit non-zero on critical failures.
- [ ] No unrelated feature work mixed into the audit branch.

## Reviewer Notes

- Evaluate consistency of patterns across layers, not perfection on every file.
- Accept different wording for user messages if intent is clear.
- Do not require new tests unless the student's cohort adds them separately.
