---
name: transversal-project-context-generator
description: Generates BRIEFING.md files for one or more company scenarios for a 4Geeks Academy transversal project milestone. A BRIEFING file is the company-specific document a student reads before implementing their milestone — it provides the real-world domain data (event schemas, KPIs, entity tables, seed instructions, restrictions) that turns a generic README into a concrete assignment. Requires an existing README for the milestone as input. Use this skill when adding a new company scenario to an existing milestone, when onboarding a new sector into the transversal project, or when generating briefing files after a README has already been written. Trigger on phrases like "generate the context for [company]", "add a new company to milestone N", "create BRIEFING files for this README", "generate BRIEFING for [sector] scenario", or when a user provides a README and one or more company descriptions. Do NOT use this skill to generate READMEs — use transversal-project-readme-generator for that.
---

# 4Geeks Academy Transversal Project Context Generator

This skill generates company-specific BRIEFING.md files for transversal project milestones in the 4Geeks Academy AI Engineering bootcamp.

## Repository Structure

### Base Company References

The base company information and reference materials are located at:

```text
https://github.com/4GeeksAcademy/course-outline-generator/tree/main/ai-engineering/project-milestone-context-base
```

This repository contains:

- Foundational company profiles
- Sector descriptions
- Domain data templates
- Reference schemas and examples

Always consult this repository when generating briefing files to ensure consistency and accuracy.

### Output Repository

Generated BRIEFING files are saved to:

```text
https://github.com/4GeeksAcademy/ai-engineering-sylllabus
```

**Directory Structure:**

- Folder format: `<two-digit-milestone>-<milestone-context>/`
  - `<two-digit-milestone>`: Zero-padded milestone number (01, 02, 03, etc.)
  - `<milestone-context>`: Descriptive context like "web-fundamentals", "automations", "training-rag", "backend-development"
- File format: `<company>-BRIEFING.en.md` / `<company>-BRIEFING.es.md` (pattern `*-BRIEFING.(en|es).md`)
  - `<company>`: Company/scenario name (retail, ecommerce, fintech, etc.)
  - Prefer bilingual pair `.en.md` + `.es.md`. Unlocalized `<company>-BRIEFING.md` only when a single-language draft is intentional.

**Examples:**

```text
01-web-fundamentals/retail-BRIEFING.en.md
01-web-fundamentals/retail-BRIEFING.es.md
01-web-fundamentals/ecommerce-BRIEFING.en.md
02-automations/fintech-BRIEFING.en.md
03-training-rag/healthcare-BRIEFING.en.md
04-backend-development/logistics-BRIEFING.en.md
```

## Overview

A BRIEFING file bridges the gap between the universal project statement (README) and the student's implementation. It provides:

- Real company scenario details
- Domain-specific event schemas and data structures
- Concrete KPIs and metrics relevant to the company
- Entity tables and seed data instructions
- Business constraints and requirements specific to that company

## When to Use This Skill

Use this skill when:

1. Adding a new company scenario to an existing milestone
2. Onboarding a new sector/industry into the transversal project
3. Generating briefing files after a README has been written
4. A user provides a README and one or more company descriptions
5. Updating or refreshing existing briefing files for a milestone

**Do NOT use this skill to:**

- Generate README files (use `transversal-project-readme-generator` instead)
- Create the universal project statement

## Required Inputs

1. **Existing README.md** for the milestone
   - Must contain the universal project statement
   - Should be sector-agnostic and generic

2. **Milestone Context Information**
   - Milestone number (will be zero-padded to two digits)
   - Milestone context name (e.g., "web-fundamentals", "automations")

3. **Company Description(s)**
   - Can be one or more companies
   - Should include sector, business model, and relevant domain details
   - Reference the base company materials from the repository when available

## Workflow

1. **Receive Input**
   - Confirm you have the milestone README
   - Confirm milestone number and context name
   - Confirm you have company description(s)
   - Fetch base company materials from repository if needed

2. **Analyze the README**
   - Identify what needs to be made concrete
   - Note any placeholders or generic references
   - Understand the technical requirements

3. **Research the Company Domain**
   - Consult base company references: `https://github.com/4GeeksAcademy/course-outline-generator/tree/main/ai-engineering/project-milestone-context-base`
   - Understand the sector-specific terminology
   - Identify relevant data structures and events

4. **Generate BRIEFING.md**
   - Create company-specific versions of generic concepts
   - Provide concrete examples in the company's domain
   - Include realistic seed data requirements
   - Add domain-specific constraints

5. **Structure for Repository**
   - Format milestone number as two digits (01, 02, etc.)
   - Construct folder name: `<two-digit-milestone>-<milestone-context>/`
   - Name files as: `<company>-BRIEFING.en.md` and `<company>-BRIEFING.es.md`
   - Full path: `<two-digit-milestone>-<milestone-context>/<company>-BRIEFING.en.md`

6. **Present to User**
   - Show the generated BRIEFING file
   - Display the target repository path
   - Explain how it connects to the README
   - Confirm it aligns with the corresponding README

## Output Format

Each BRIEFING.md file should include:

### 1. Company Introduction

- Company name and sector
- Brief business description
- Why this milestone matters to this company

### 2. Domain-Specific Data Structures

- Event schemas relevant to the company
- Data models and entity definitions
- Example data in the company's domain

### 3. Business Metrics and KPIs

- Specific metrics this company cares about
- How to calculate them
- Success thresholds

### 4. Seed Data Instructions

- What data the student should create
- Format and structure requirements
- Minimum data requirements

### 5. Business Constraints

- Company-specific rules and restrictions
- Edge cases to handle
- Domain-specific validations

### 6. Expected Deliverables

- What the student should produce
- How it should work for this specific company
- Acceptance criteria

## Quality Standards

A good BRIEFING file should:

- ✅ Be completely self-contained (student shouldn't need to reference other docs)
- ✅ Use terminology authentic to the company's sector
- ✅ Provide concrete, realistic data examples
- ✅ Make all abstract concepts from the README concrete
- ✅ Be at the right difficulty level for the milestone
- ✅ Give students everything they need to implement without ambiguity
- ✅ Align with base company references when applicable

## Example Interaction

```text
User: "Generate the context for an e-commerce company for milestone 2 (automations)"

[Skill confirms:]
- Milestone number: 02
- Milestone context: "automations"
- Company: ecommerce
- Target path: 02-automations/ecommerce-BRIEFING.en.md (+ `.es.md`)

[Skill consults base company references]
[Skill generates ecommerce-BRIEFING.en.md / ecommerce-BRIEFING.es.md with:]
- E-commerce events (purchase, cart_abandon, product_view)
- Automation triggers (low inventory, abandoned cart, price change)
- Metrics (conversion rate, automation success rate, time saved)
- Seed data for products, customers, automation rules
- E-commerce specific constraints (inventory thresholds, pricing rules)
```

## Notes

- Always maintain consistency with the universal README
- The BRIEFING should NOT contradict or override the README's requirements
- Each company's BRIEFING can have different complexity levels if appropriate
- Students will use ONE BRIEFING file for their implementation
- Multiple BRIEFING files for the same milestone = multiple possible implementations
- Milestone context names should be kebab-case (lowercase with hyphens)

## Repository Workflow

When generating files:

1. Create the briefing content (English + Spanish)
2. Determine the folder structure: `<XX>-<milestone-context>/`
3. Name the files: `<company>-BRIEFING.en.md` and `<company>-BRIEFING.es.md`
4. Inform the user of the complete path in the repository
5. Optionally, if the user has repository access, offer to help prepare the file for commit

## References

- Base company materials: <https://github.com/4GeeksAcademy/course-outline-generator/tree/main/ai-engineering/project-milestone-context-base>
- Output repository: <https://github.com/4GeeksAcademy/ai-engineering-syllabus>
- Universal README files: Generated by `transversal-project-readme-generator` skill
