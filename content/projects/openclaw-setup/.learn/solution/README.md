# Setting Up Your Personal AI Agent with OpenClaw - Reference Solution

## Purpose

This reference solution describes the expected setup evidence for a successful OpenClaw deployment project on a VPS.

## Solution Deliverables

- GitHub repository named `openclaw-<student_username>` containing the complete `~/.openclaw/workspace` folder.
- `.openclaw/workspace/IDENTITY.md` in the workspace showing personalized Name, Emoji, and Greeting.
- Git commit history showing at least one commit pushed from the VPS.
- Optional: Screenshot of the GitHub repository page showing the uploaded workspace.

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
- Verify that `.openclaw/workspace/IDENTITY.md` contains the personalized configuration.
- Generate SSH key on the VPS server.
- Add the SSH public key to GitHub account.
- Create GitHub repository named `openclaw-<username>`.
- Navigate to `~/.openclaw/workspace` folder.
- Initialize git repository (if not already done).
- Add GitHub remote origin.
- Stage, commit, and push workspace contents to GitHub.
- Verify successful upload on GitHub web interface.

## Security Requirements

- **NEVER commit to GitHub:** API keys, tokens, credentials, `.env` files, `openclaw.json`, or any file containing sensitive configuration.
- The workspace folder (`~/.openclaw/workspace`) should **only** contain safe files created by OpenClaw.
- Before pushing, students must verify no sensitive files are in the workspace:

  ```bash
  cd ~/.openclaw/workspace
  ls -la
  cat .gitignore
  ```

- The `.openclaw/workspace/IDENTITY.md` file contains only public personalization data (Name, Emoji, Greeting) and is **safe to share**.
- If `openclaw.json`, `.env`, or credential files are accidentally in the workspace, students must:
  1. NOT push to GitHub
  2. Contact instructor for guidance
  3. Remove sensitive files before attempting upload
- Treat the VPS URL as sensitive if authentication is not configured.
- Instructors will verify configuration directly on the server — students must never expose secrets in their repositories.
- If sensitive files are accidentally pushed, students must immediately delete the repository and recreate it without the sensitive data.

## Validation Checklist

- OpenClaw is reachable on the VPS.
- Local chat returns a valid model response.
- GitHub repository `openclaw-<username>` exists and is public/accessible.
- Repository contains the complete workspace folder structure.
- `.openclaw/workspace/IDENTITY.md` is present in the repository showing personalized Name, Emoji, and Greeting.
- Personalization was done through conversation with OpenClaw (not manual file editing).
- Git commit history shows at least one commit from the VPS (verifiable by commit author/timestamp).
- SSH key was properly configured (verifiable by successful git push).
- No sensitive files (API keys, tokens, `openclaw.json`, `.env`) were pushed to the repository.
- Repository structure matches the expected `~/.openclaw/workspace` layout.
- Instructor can verify the assistant's configuration directly on the server if needed.
