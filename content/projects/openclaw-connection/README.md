# Connect Your Agent: Telegram, Google Docs & Calendar

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/openclaw-integrations/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

Your OpenClaw instance is already running as a personal assistant. It responds, it has a personality, it's connected to a model of your choice. But it's still a desktop assistant — you have to be in front of the VPS or the web interface to use it.

You want more. You want to be able to talk to it from anywhere — from your phone, while you're on the go — and have it take actions in the services you already use every day.

Your next step: connect the assistant to **Telegram**, **Google Docs**, and **Google Calendar**. That way you can send it a message from your phone, and it will create a document, block time in your calendar, and confirm it's done — no laptop required. No dashboards. Just a message and a result.

To integrate Google Docs and Google Calendar quickly without building custom connectors, you'll use the **Zapier MCP** — a platform that exposes hundreds of pre-built integrations as skills your agent can call directly. It handles OAuth, token refresh, and scopes automatically, so you focus on wiring the tools, not managing auth. It's not the only way to connect these services, but it's one of the fastest paths to a working prototype.

This project is about **configuration, not code**. You are assembling a working agent from existing services and connectors. Think about how each integration transforms a third-party API into a skill your agent can use — because that's exactly what you're doing.

---

## 🌱 How to Start the Project

This project does not require forking a code repository. Instead, you will configure an OpenClaw agent and connect it to external services.

1. Make sure you have an active **OpenClaw** instance running (set up in the [openclaw-setup project](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/projects/openclaw-setup)).
2. Create a **Telegram bot** via BotFather if you haven't already.
3. Create a **Zapier account** at [zapier.com](https://zapier.com) (free tier is sufficient) and set up the MCP connection.
4. Access **Google Docs** and **Google Calendar** through Zapier's pre-built integrations.
5. Document your setup steps and capture screenshots as evidence of each connection.

> ⚠️ **IMPORTANT:** Do not connect personal accounts holding sensitive or private information to OpenClaw during this exercise. Use a dedicated test account for Google Docs and Google Calendar. Never expose API keys or tokens in screenshots or submitted files.

---

## 💻 What You Need to Do

### Telegram Connection

- [ ] Create a Telegram bot using BotFather and obtain its token
- [ ] Configure OpenClaw to use Telegram as its messaging channel
- [ ] Validate the connection: send a test message and confirm the agent responds

### Zapier MCP Setup

- [ ] Create a free Zapier account at [zapier.com](https://zapier.com)
- [ ] Navigate to Zapier's MCP configuration and generate an MCP endpoint URL
- [ ] Add the MCP to your OpenClaw agent using that endpoint URL
- [ ] Connect Google Docs via Zapier and verify the agent has create-document access
- [ ] Connect Google Calendar via Zapier and verify the agent has create-event access

### End-to-End Workflow

- [ ] Send a message via Telegram asking the agent to create a document (specify a title or topic)
- [ ] If the agent requires additional information to complete the task, confirm that it asks for it before proceeding
- [ ] Verify that a new document is created in Google Docs
- [ ] Verify that a new calendar event is created to schedule time to review the document
- [ ] Confirm that the agent sends a Telegram message reporting the task is complete

### Evidence & Submission

- [ ] Capture a screenshot of each integration successfully connected in OpenClaw
- [ ] Capture a screenshot of the full Telegram conversation (request → agent questions if any → confirmation)
- [ ] Capture a screenshot showing the created Google Docs document
- [ ] Capture a screenshot showing the created calendar event

> ⚠️ **IMPORTANT:** Blur or crop out any personal information (full names, email addresses) in your screenshots before submitting.

---

## ✅ What We Will Evaluate

- [ ] Telegram bot is correctly created and connected to OpenClaw
- [ ] Zapier MCP is added and active in the agent's configuration
- [ ] Google Docs integration works: agent can create a document in response to a user request
- [ ] Google Calendar integration works: agent creates an event associated with the document review
- [ ] Agent confirms task completion via Telegram
- [ ] Agent requests missing information when the user's message is not specific enough
- [ ] Screenshots document each integration and the complete end-to-end conversation
- [ ] No sensitive credentials or personal data are exposed in submitted materials

> Note: The agent's response quality or tone is not evaluated. What matters is that the workflow executes correctly end to end.

---

## 📦 How to Submit

Create a folder named `openclaw-connection` containing:

- All screenshots (named clearly, e.g., `01-telegram-connected.png`, `02-zapier-mcp.png`, etc.)
- A short `notes.md` file (5–10 lines) describing any configuration decisions you made or issues you ran into

Share the folder as a ZIP file or GitHub repo link according to your instructor's instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/openclaw-integrations/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
