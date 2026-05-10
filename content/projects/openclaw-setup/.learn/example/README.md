# In-Class Example: Deploy OpenClaw as a Customer Support Assistant

> **Instructor note:** This is an in-class live example for teaching the concepts of the `openclaw-setup` project. Use this scenario during class to walk students through VPS access via SSH, OpenClaw installation, and LiteLLM configuration. **Do not assign this as homework — it is a guided classroom exercise.**

---

## The Scenario

A small online bookshop wants to deploy a self-hosted AI assistant to handle common customer questions (order status, return policy, book recommendations). They don't want to pay for a SaaS chatbot subscription and prefer to keep their data on their own server.

Your task: deploy and configure OpenClaw on a VPS, connect it to an AI model via LiteLLM, and verify it can respond to a customer-style question in the local chat.

**What you are learning:**
- How to connect to a remote server securely via SSH
- What LiteLLM does and why it is used as a model proxy
- How OpenClaw's configuration file controls the agent's identity and model
- How to verify a running AI service before sharing it with others

---

## Prerequisites

- VPS credentials provided by the instructor
- A terminal or VS Code with SSH extension
- An API key for a model provider (e.g., OpenAI, Groq, or Mistral — use the one provided in class)

---

## Step-by-Step Tasks

### 1. Connect to the VPS via SSH

- [ ] Open your terminal and run:

  ```bash
  ssh your_user@your_vps_ip
  ```

- [ ] Confirm you are logged in and check available disk and memory:

  ```bash
  df -h && free -h
  ```

### 2. Install OpenClaw

- [ ] Follow the 4Geeks OpenClaw installation guide step by step
- [ ] Do not skip or reorder any phase

### 3. Configure the Agent

Follow this configuration order — do not skip steps:

- [ ] Set the **LiteLLM provider** as the model backend
- [ ] Enter a valid **API key** for the chosen model provider
- [ ] Skip the Skills step (not needed for this exercise)
- [ ] Enable **hooks** when prompted
- [ ] Skip Channel Workflows (not needed for this exercise)
- [ ] Give the agent a persona name and a short system prompt, for example:
  > "You are a helpful assistant for a small online bookshop. Answer customer questions about orders, returns, and book recommendations politely and concisely."

### 4. Verify the Agent Responds

- [ ] Open **Try Local Chat** in the OpenClaw interface
- [ ] Send a test customer-style message, for example: _"What is your return policy for damaged books?"_
- [ ] Confirm the agent replies in character

### 5. Review the Configuration File

- [ ] Locate `openclaw.json` on the server
- [ ] Read through the file and identify which fields control: model provider, API key, system prompt
- [ ] Copy the file to your local machine

> ⚠️ Before saving `openclaw.json` anywhere, replace any real API key with a placeholder: `"api_key": "YOUR_KEY_HERE"`

---

## Configuration Reference

| Field | What it controls |
|---|---|
| `model_provider` | Which LiteLLM backend is used |
| `api_key` | Credential for the model provider |
| `system_prompt` | The agent's persona and instructions |
| `hooks_enabled` | Whether OpenClaw runs lifecycle hooks |

---

## Discussion Questions

1. Why is it important to set a system prompt when deploying an AI assistant for a specific business? What happens if you leave it empty?
2. OpenClaw is not a multi-tenant system — anyone with the VPS URL can use it. What authentication options would you add before exposing it to real customers?
3. You chose a specific AI model for this assistant. What criteria would you use to decide between a fast/cheap model and a more capable/expensive one for a customer support use case?
