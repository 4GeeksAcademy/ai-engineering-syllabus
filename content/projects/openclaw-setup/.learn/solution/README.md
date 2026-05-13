# Setting Up Your Personal AI Agent with OpenClaw - Reference Solution

## Purpose

This reference solution describes the expected setup evidence for a successful OpenClaw deployment project on a VPS.

## Solution Deliverables

- `proof.png` (or `.jpg`) showing a successful response in **Try Local Chat**.
- `.openclaw/IDENTITY.md` copied from the VPS showing personalized Name, Emoji, and Greeting.
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
- Personalize the assistant by conversing with OpenClaw to set Name, Emoji, and Greeting.
- Verify that `.openclaw/IDENTITY.md` contains the personalized configuration.

## Security Requirements

- **NEVER commit to GitHub:** API keys, tokens, credentials, `.env` files, `openclaw.json`, or any file containing sensitive configuration.
- The `.openclaw/IDENTITY.md` file contains only public personalization data (Name, Emoji, Greeting) and is **safe to share**.
- Only the following files should be uploaded to the delivery repository:
  - `proof.png` (screenshot)
  - `.openclaw/IDENTITY.md` (safe - only public personalization)
  - `README.md` (documentation)
- Treat the VPS URL as sensitive if authentication is not configured.
- Instructors will verify configuration directly on the server — students must never expose secrets in their repositories.

## Validation Checklist

- OpenClaw is reachable on the VPS.
- Local chat returns a valid model response.
- `.openclaw/IDENTITY.md` is present showing personalized Name, Emoji, and Greeting.
- Personalization was done through conversation with OpenClaw (not manual file editing).
- Submission README includes VPS provider, model, and justification.
- Evidence files (`proof.png` and `.openclaw/IDENTITY.md`) are uploaded to the delivery repository.
