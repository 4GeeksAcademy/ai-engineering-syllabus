# Backend Architecture Proposal - Reference Solution

This solution defines the expected quality bar for `ARCHITECTURE_PROPOSAL.md` in the student's transversal repository.

The deliverable is not executable code. It is a technical proposal that explains architectural decisions before implementation starts.

## Expected Deliverable

A complete submission includes:

- `ARCHITECTURE_PROPOSAL.md` at the repository root.
- A chosen architecture pattern (for example layered architecture) with business-specific justification.
- A proposed backend folder/module structure with clear responsibility boundaries.
- A FastAPI router strategy grouped by domain.
- Documented considerations for frontend-backend separation.
- A risks section with concrete mitigation actions.

## Reference Document Structure

The proposal should follow this structure:

1. **Business context and backend goals**
2. **Chosen architectural pattern and justification**
3. **Backend structure proposal (folders/modules/domains)**
4. **FastAPI endpoint and router organization**
5. **Frontend-backend separation strategy**
6. **Risks and attention points with mitigations**
7. **Initial technical decisions and next steps**

## Example of a Strong Solution

The following outline is an indicative example of what "done well" looks like:

- Company context: multi-role users, operational workflows, and audit requirements.
- Pattern chosen: layered/domain-oriented architecture to keep API, business logic, and persistence separated.
- Module split:
  - `app/api`: routers per domain (`incidents`, `users`, `reports`, `auth`)
  - `app/services`: business use-cases
  - `app/repositories`: DB access layer
  - `app/schemas`: request/response contracts
  - `app/core`: config, security, logging, dependency wiring
- FastAPI routing approach:
  - One router file per domain
  - Common API prefix versioning (`/api/v1`)
  - Clear separation between public and protected endpoints
- Frontend-backend separation:
  - API contract-first integration
  - Explicit CORS policy by environment
  - `.env` strategy for local/staging/production
  - Decision note on monorepo vs split repositories
- Risks:
  - Domain boundaries not enforced -> duplicated logic and coupling
  - Business rules inside routers -> low testability and maintenance debt
  - Environment drift -> configuration-related production incidents

## FastAPI Conventions That Should Be Referenced

The document should explicitly connect decisions to standard FastAPI practices:

- Routers split by domain instead of a single routes file.
- Pydantic schemas separated from business services.
- Dependency injection for shared concerns.
- Centralized settings/configuration management.
- Predictable folder layout that scales with new domains.

## Evaluation Checklist

- [ ] Pattern choice is justified with company context, not generic claims.
- [ ] Proposed structure matches the chosen pattern.
- [ ] Router organization is domain-based and coherent for FastAPI.
- [ ] Frontend-backend communication concerns are explicitly addressed.
- [ ] At least two realistic risks are documented with mitigation ideas.
- [ ] Writing is concrete, decision-oriented, and technically consistent.

## Reviewer Notes

- Evaluate quality of reasoning, not implementation details.
- Accept different valid patterns if justification and trade-offs are clear.
- Prioritize coherence between business needs, architecture, and operational risks.
