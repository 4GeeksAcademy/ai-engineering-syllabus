# Setting Up Your Personal AI Agent with OpenClaw

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/openclaw/openclaw/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

You’ve probably used commercial AI chat tools for a while. They work, but they never truly belong to you. Now you want your own AI assistant — self-hosted on a VPS, private, configurable to your needs, and adaptable for any task. No dependence on third-party platforms. 100% yours.

The tool you’ll use is **OpenClaw**. Your objective is to deploy and configure a functional OpenClaw instance on a VPS, connect it to an AI model via LiteLLM, and verify it responds correctly using the local chat.

This is not a coding project — it's an infrastructure and configuration task. The primary outcome is a running system, not a repository. That said, if you end up customizing OpenClaw's code, a repository is the right place to track those changes — good engineers version-control their work. For now, you will use a repository to document your setup with a screenshot and a configuration file as proof of delivery.

> **Before you start, make sure you understand:**
>
> - OpenClaw is only as useful as the model powering it. Without a connected model, it does nothing. Part of building your own assistant is knowing which model to use for each task — not always the most powerful one, but the most appropriate one given the context, cost, and latency requirements.
> - OpenClaw is **not** a multi-tenant boundary. Anyone with access to your VPS URL can use it. Never expose it publicly without authentication in place.
> - Always follow the 4Geeks-provided installation guide. The order of configuration steps matters — skipping or reordering them causes hard-to-debug failures.

Get it running.

---

## 🌱 How to Start the Project

This project does not use a starter repository — it is a server configuration project. Follow these steps to begin:

1. Access the VPS provided by the platform (credentials will be shared via the course platform).
2. Connect to the VPS via your VS Code editor so you can get help from your Copilot in case you needed. Or you can connect via SSH from your terminal:

   ```bash
   ssh your_user@your_vps_ip
   ```

3. Follow the 4Geeks OpenClaw installation guide (read the lesson "Setting Up Your Personal AI Assistant") step by step — do not skip any phase.

> If you are working locally instead of on a VPS, confirm this with your instructor first. The setup steps differ.

---

## 💻 What You Need to Do

### VPS & SSH Access

- [ ] Successfully connect to the VPS via SSH from your Code Editor or your local terminal.
- [ ] Confirm the server OS and available resources before starting the installation.

### OpenClaw Installation

- [ ] Install OpenClaw on the VPS following the 4Geeks installation guide.

### Core Configuration (in order)

- [ ] Configure the **LiteLLM provider** as the model provider.
- [ ] Enter a valid **API Key** for the chosen model provider.
- [ ] Skip the Skills configuration step (this will be addressed in a future session).
- [ ] Enable **hooks** when prompted during setup.
- [ ] Skip the Channel Workflows step (this will be addressed in a future session).
- [ ] Open **Try Local Chat** and send a test message to confirm the instance is responding.

### Personalizing Your Assistant

Now that OpenClaw is running, it's time to make it truly yours. Instead of manually editing configuration files, you'll **converse with OpenClaw itself** to personalize it.

- [ ] Open the local chat interface again.
- [ ] Ask OpenClaw to configure the following personal attributes by chatting with it:
  - **Name:** The name of your assistant (e.g., "Name: Kai")
  - **Emoji:** The avatar representing your agent (e.g., "Emoji: 🤖")
  - **Greeting:** The initial message when starting a chat (e.g., "Greeting: Hello!")

> **Tip:** You can say something like: _"I want to configure you. Set your name to Kai, your emoji to 🤖, and your greeting to 'Hello, I'm Kai, how can I help you today?'"_

- [ ] Once configured, verify that your personalization was applied by checking the greeting in the chat interface.

### Setting Up GitHub Backup

OpenClaw creates a workspace folder at `~/.openclaw/workspace` where it stores your assistant's configuration and chat history. You'll push this workspace to GitHub as your project delivery.

#### Step 1: Create SSH Key on the Server

> **GitHub guide:** For the official walkthrough (key generation, passphrase, and adding the key to the `ssh-agent` on Linux), see [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

- [ ] Generate an SSH key on your VPS:

  ```bash
  ssh-keygen -t ed25519 -C "your_email_in_github@example.com"
  ```

- [ ] Press Enter to accept the default file location.
- [ ] Press Enter twice to skip the passphrase (optional, but recommended for automation).
- [ ] Display your public key:

  ```bash
  cat ~/.ssh/id_ed25519.pub
  ```

- [ ] Copy the entire output (starts with `ssh-ed25519`).

#### Step 2: Add SSH Key to GitHub

- [ ] Go to [GitHub SSH Settings](https://github.com/settings/keys).
- [ ] Click **"New SSH key"**.
- [ ] Give it a title (e.g., "OpenClaw VPS").
- [ ] Paste your public key into the "Key" field.
- [ ] Click **"Add SSH key"**.

#### Step 3: Create GitHub Repository

- [ ] Go to [GitHub](https://github.com/new) and create a **new repository**.
- [ ] Name it: `openclaw-setup-<your_github_username>` (replace with your actual username).
- [ ] Make it **Public** or **Private** (your choice).
- [ ] **Do NOT** initialize with README, .gitignore, or license.
- [ ] Click **"Create repository"**.

#### Step 4: Connect Workspace to GitHub

- [ ] On your VPS, navigate to the OpenClaw workspace:

  ```bash
  cd ~/.openclaw/workspace
  ```

- [ ] Initialize git if not already initialized:

  ```bash
  git init
  git branch -M main
  ```

- [ ] Add the GitHub remote (replace with your repository URL):

  ```bash
  git remote add origin git@github.com:your_username/openclaw-setup-your_username.git
  ```

- [ ] Stage all files:

  ```bash
  git add .
  ```

- [ ] Commit your changes:

  ```bash
  git commit -m "Initial OpenClaw setup with personalized identity"
  ```

- [ ] Push to GitHub:

  ```bash
  git push -u origin main
  ```

#### Step 5: Verify Upload

- [ ] Go to `https://github.com/your_username/openclaw-setup-your_username` in your browser.
- [ ] Confirm that your workspace files are visible, including `.openclaw/IDENTITY.md`.
- [ ] Take a screenshot of your GitHub repository page showing the uploaded workspace.

⚠️ **SECURITY WARNING:** The workspace folder should **only** contain safe files created by OpenClaw (like `IDENTITY.md` and chat logs). However, **before pushing**, verify that no sensitive files accidentally ended up in the workspace:

```bash
cd ~/.openclaw/workspace
ls -la
cat .gitignore  # Check what's being ignored
```

If you see files like `openclaw.json`, `.env`, or any configuration with API keys in the workspace, **do NOT push**. Contact your instructor first.

---

## ✅ What We Will Evaluate

- [ ] OpenClaw is correctly installed and accessible on the VPS.
- [ ] LiteLLM provider is configured and connected to a working AI model.
- [ ] The local chat interface returns a valid AI response (verified on server or by screenshot).
- [ ] GitHub repository `openclaw-setup-<your_username>` exists and is accessible.
- [ ] The workspace folder (`~/.openclaw/workspace`) has been successfully pushed to GitHub.
- [ ] `.openclaw/IDENTITY.md` is present in the repository showing personalized Name, Emoji, and Greeting.
- [ ] The personalization was done by conversing with OpenClaw (not by manually editing files).
- [ ] SSH key was properly configured to enable git push from the VPS.
- [ ] Git commit history shows at least one commit with workspace contents.
- [ ] No sensitive files (API keys, tokens, credentials) were pushed to the repository.
- [ ] SSH was used to connect to the VPS (not a web-based console or GUI tool).
- [ ] Configuration steps were followed in the correct order as specified in the 4Geeks guide.

> Note: The instructor may verify the assistant's configuration directly on the server and review your Git commit history to ensure proper workflow was followed.

---

## 📦 How to Submit

Your delivery is the entire `~/.openclaw/workspace` folder pushed to GitHub from your VPS. Share your repository URL according to your instructor's instructions.

**Your repository should contain:**

- `.openclaw/IDENTITY.md` (your personalized assistant identity)
- Any chat logs or workspace files created by OpenClaw
- Git commit history showing the push from the VPS

**Submission format:** `https://github.com/your_username/openclaw-setup-your_username`

⚠️ **FINAL SECURITY CHECK:** Before submitting, verify that your workspace does NOT contain:

- `openclaw.json` (main config file - contains secrets)
- `.env` files
- API keys or tokens
- Any credential files

If you accidentally pushed sensitive files, **immediately**:

1. Delete the repository on GitHub
2. Remove sensitive files from workspace
3. Create a new repository and push again
4. Contact your instructor for guidance

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/openclaw-setup/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
