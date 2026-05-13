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
2. Connect to the VPS via your Codespaces/VS Code editor so you can get help from your Copilot in case you needed. Or you can connect via SSH from your terminal:

   ```bash
   ssh your_user@your_vps_ip
   ```

3. Follow the 4Geeks OpenClaw installation guide (read the lesson "Setting Up Your Personal AI Assistant") step by step — do not skip any phase.
4. Create a **new GitHub repository** named `openclaw-setup-<your_github_username>` to store your delivery files (screenshot + config).

> If you are working locally instead of on a VPS, confirm this with your instructor first. The setup steps differ.

---

## 💻 What You Need to Do

### VPS & SSH Access

- [ ] Successfully connect to the VPS via SSH from your Code Editor or your local terminal.
- [ ] Confirm the server OS and available resources before starting the installation.

### OpenClaw Installation

- [ ] Install OpenClaw on the VPS following the 4Geeks installation guide.

### Core Configuration (in order)

- [ ] Configure the **LiteLLM provider** as the model backend.
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

- [ ] Once configured, locate the `.openclaw/IDENTITY.md` file on your server.
- [ ] Read through it to confirm your personalization was applied correctly.
- [ ] Copy the `.openclaw/IDENTITY.md` file to your local machine and include it in your delivery repository.

⚠️ **SECURITY WARNING:** Never commit files containing API keys, tokens, credentials, or sensitive data to GitHub. The `.openclaw/IDENTITY.md` file is safe to share because it only contains public personalization data (Name, Emoji, Greeting). However, **never upload** files like `openclaw.json`, `.env`, configuration files with secrets, or any file containing sensitive information.

### Delivery Evidence

- [ ] Take a screenshot of the OpenClaw local chat interface showing a successful AI response.
- [ ] Add the screenshot to your GitHub repository as `proof.png` (or `.jpg`).
- [ ] Add the `.openclaw/IDENTITY.md` file to your repository (this proves you successfully personalized your assistant).
- [ ] Add a `README.md` to your repository with: the VPS provider used, the model chosen, and one sentence explaining why you selected that model for a general-purpose assistant task.

---

## ✅ What We Will Evaluate

- [ ] OpenClaw is correctly installed and accessible on the VPS.
- [ ] LiteLLM provider is configured and connected to a working AI model.
- [ ] The local chat interface returns a valid AI response (evidenced by screenshot).
- [ ] `.openclaw/IDENTITY.md` is present in the repository showing personalized Name, Emoji, and Greeting.
- [ ] The personalization was done by conversing with OpenClaw (not by manually editing files).
- [ ] The delivery `README.md` includes the required fields: VPS provider, model name, and model selection rationale.
- [ ] SSH was used to connect to the VPS (not a web-based console or GUI tool).
- [ ] Configuration steps were followed in the correct order as specified in the 4Geeks guide.

> Note: The instructor may verify the assistant's personalization directly on the server to ensure the configuration was applied correctly.

---

## 📦 How to Submit

Push your repository to GitHub (it should contain `proof.png`, `.openclaw/IDENTITY.md`, and a `README.md` with your VPS/model documentation) and share the link according to your instructor's instructions.

⚠️ **BEFORE PUSHING:** Double-check that you are NOT uploading any files with API keys, tokens, credentials, or sensitive configuration. Only upload:

- `proof.png` (screenshot)
- `.openclaw/IDENTITY.md` (safe - only Name, Emoji, Greeting)
- `README.md` (your documentation)

**Never upload:** `openclaw.json`, `.env`, credential files, or any configuration containing secrets.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/openclaw-setup/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
