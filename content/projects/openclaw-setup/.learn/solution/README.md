# Setting Up Your Personal AI Agent with OpenClaw - Reference Solution

## Purpose

This reference solution describes the expected setup evidence for a successful OpenClaw deployment project on a VPS.

## Solution Deliverables

- `proof.png` (or `.jpg`) showing a successful response in **Try Local Chat**.
- `openclaw.json` copied from the VPS with sensitive keys sanitized.
- A delivery `README.md` in the student's repository including:
  - VPS provider used
  - Model selected
  - Short model selection rationale

## Required Completion Criteria

- Connect to the VPS via SSH from a local terminal.
- Confirm OS and available server resources before installation.
- Install OpenClaw following the 4Geeks installation guide in the specified order.
- Use the instructor-approved installation path (1-click, Docker, or manual).
- Configure LiteLLM as model provider.
- Add a valid API key for the chosen provider.
- Skip Skills setup and Channel Workflows as instructed.
- Enable hooks when prompted.
- Validate end-to-end response in local chat.

## Security Requirements

- Never commit real API keys.
- Replace secret values with placeholders (for example: `"api_key": "YOUR_KEY_HERE"`).
- Treat the VPS URL as sensitive if authentication is not configured.

## Validation Checklist

- OpenClaw is reachable on the VPS.
- Local chat returns a valid model response.
- `openclaw.json` is present and sanitized.
- Submission README includes VPS provider, model, and justification.
- Evidence files are uploaded to the delivery repository.
