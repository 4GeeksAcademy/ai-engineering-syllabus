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

You've just been hired as the AI engineer at a small consulting firm. Your tech lead hands you a task on your first day: the team needs a self-hosted AI assistant that runs on a VPS, keeps sensitive client conversations off third-party servers, and can be configured to use different AI models depending on the task at hand.

"We can't send everything through commercial APIs," she explains. "Compliance reasons. We need our own instance — private, controllable, ours."

The tool the team uses is **OpenClaw**. Your job is to deploy and configure a working OpenClaw instance on a VPS, connect it to an AI model via LiteLLM, and verify that it responds correctly in the local chat interface.

This is not a coding project — it's an infrastructure and configuration task. The primary outcome is a running system, not a repository. That said, if you end up customizing OpenClaw's code, a repository is the right place to track those changes — good engineers version-control their work. For now, you will use a repository to document your setup with a screenshot and a configuration file as proof of delivery.

> **Before you start, make sure you understand:**
>
> - OpenClaw is only as useful as the model powering it. Without a connected model, it does nothing. Part of your job as an AI engineer is knowing which model to use for each task — not always the most powerful one, but the most appropriate one given the context, cost, and latency requirements.
> - OpenClaw is **not** a multi-tenant boundary. Anyone with access to your VPS URL can use it. Never expose it publicly without authentication in place.
> - Always follow the 4Geeks-provided installation guide. The order of configuration steps matters — skipping or reordering them causes hard-to-debug failures.

Your tech lead is counting on you to deliver a functional instance by end of day. Get it running.

---

## 🌱 How to Start the Project

This project does not use a starter repository — it is a server configuration project. Follow these steps to begin:

1. Access the VPS provided by the platform (credentials will be shared via the course platform).
2. Connect to the VPS via SSH from your terminal:

   ```bash
   ssh your_user@your_vps_ip
   ```

3. Follow the [4Geeks OpenClaw installation guide](https://4geeks.com) step by step — do not skip any phase.
4. Create a **new GitHub repository** named `openclaw-setup-<your_github_username>` to store your delivery files (screenshot + config).

> If you are working locally instead of on a VPS, confirm this with your instructor first. The setup steps differ.

---

## 💻 What You Need to Do

### VPS & SSH Access

- [ ] Successfully connect to the VPS via SSH from your local terminal.
- [ ] Confirm the server OS and available resources before starting the installation.

### OpenClaw Installation

- [ ] Install OpenClaw on the VPS following the 4Geeks installation guide.
- [ ] Select the installation method indicated by your instructor (1-click, Docker, or manual).

### Core Configuration (in order)

- [ ] Configure the **LiteLLM provider** as the model backend.
- [ ] Enter a valid **API Key** for the chosen model provider.
- [ ] Skip the Skills configuration step (this will be addressed in a future session).
- [ ] Enable **hooks** when prompted during setup.
- [ ] Skip the Channel Workflows step (this will be addressed in a future session).
- [ ] Open **Try Local Chat** and send a test message to confirm the instance is responding.

### Configuration File

- [ ] Locate the `openclaw.json` file on your server.
- [ ] Read through its main attributes and make sure you understand what each section controls.
- [ ] Copy the `openclaw.json` file to your local machine and include it in your delivery repository.

⚠️ **IMPORTANT:** Do not share API keys in your repository. Before committing `openclaw.json`, remove or replace any real API key values with a placeholder (e.g., `"api_key": "YOUR_KEY_HERE"`).

### Delivery Evidence

- [ ] Take a screenshot of the OpenClaw local chat interface showing a successful AI response.
- [ ] Add the screenshot to your GitHub repository as `proof.png` (or `.jpg`).
- [ ] Add a `README.md` to your repository with: the VPS provider used, the model chosen, and one sentence explaining why you selected that model for a general-purpose assistant task.

---

## ✅ What We Will Evaluate

- [ ] OpenClaw is correctly installed and accessible on the VPS.
- [ ] LiteLLM provider is configured and connected to a working AI model.
- [ ] The local chat interface returns a valid AI response (evidenced by screenshot).
- [ ] `openclaw.json` is present in the repository with API key values removed.
- [ ] The delivery `README.md` includes the required fields: VPS provider, model name, and model selection rationale.
- [ ] SSH was used to connect to the VPS (not a web-based console or GUI tool).
- [ ] Configuration steps were followed in the correct order as specified in the 4Geeks guide.

> Note: The correctness of the `openclaw.json` internal values will be reviewed by the instructor directly on the server — the file in the repo is for reference only.

---

## 📦 How to Submit

Push your repository to GitHub (it should contain `proof.png` and `openclaw.json` with sanitized keys) and share the link according to your instructor's instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/openclaw-setup/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
