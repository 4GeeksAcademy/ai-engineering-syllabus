# In-Class Example: Connect Your Agent to Discord and Notion

> **Instructor note:** This is an in-class live example for teaching the concepts of the `openclaw-connection` project. Use this scenario during class to walk students through agent channel configuration and MCP-based external service integration. **Do not assign this as homework — it is a guided classroom exercise.**

---

## The Scenario

A small study group at a bootcamp uses **Discord** as their main communication channel and **Notion** to keep shared study notes. They want their OpenClaw assistant to live inside Discord so members can ask it questions and have it automatically create Notion pages with summaries of study sessions.

Your task: connect an existing OpenClaw instance to Discord and to Notion (via Zapier MCP), and verify the full flow works end to end.

**What you are learning:**
- How to create a bot token and register it with an external messaging platform
- What an MCP (Model Context Protocol) server does and how it acts as a skill bridge
- How Zapier MCP exposes pre-built service integrations as callable skills
- How to verify an agent integration end to end without writing application code

---

## Prerequisites

- A running OpenClaw instance (from the `openclaw-setup` exercise)
- A personal Discord account
- A Zapier free account
- A Notion free account (use a test workspace — not your personal one)

---

## Step-by-Step Tasks

### 1. Create the Discord Bot

- [ ] Go to [https://discord.com/developers/applications](https://discord.com/developers/applications) and create a new application
- [ ] Go to the **Bot** tab, enable the bot, and copy its **token**
- [ ] Under **OAuth2 → URL Generator**, select `bot` scope with `Send Messages` permission, and invite the bot to a test Discord server you own
- [ ] In OpenClaw, add Discord as the agent's messaging channel using the bot token
- [ ] Send a test message in Discord and confirm the agent responds

### 2. Set Up Zapier MCP

- [ ] Create a free Zapier account at [https://zapier.com](https://zapier.com)
- [ ] Navigate to Zapier's MCP configuration and generate an MCP endpoint URL
- [ ] In OpenClaw, add the Zapier MCP using that endpoint URL
- [ ] Confirm the MCP appears as an active skill provider in the agent's configuration

### 3. Connect Notion via Zapier

- [ ] In Zapier, connect your Notion account (test workspace)
- [ ] Enable the "Create Notion page" action through the Zapier MCP
- [ ] Verify that the agent lists "create Notion page" as an available skill

### 4. End-to-End Test

- [ ] In Discord, send the agent a message such as: _"Create a Notion page titled 'React Hooks — Class Summary' with a note that we covered useState and useEffect"_
- [ ] If the agent asks for clarification, respond and continue
- [ ] Confirm a new page appears in the connected Notion workspace
- [ ] Confirm the agent replies in Discord that the page was created

### 5. Screenshot Evidence

- [ ] Discord channel showing the conversation (request → agent reply)
- [ ] OpenClaw settings showing Discord connected
- [ ] OpenClaw settings showing Zapier MCP active
- [ ] Notion page that was created

---

## Discussion Questions

1. What is the difference between connecting a **messaging channel** (Discord) and connecting an **MCP skill provider** (Zapier)? Why are they configured separately?
2. The agent uses the Zapier MCP to create Notion pages without you writing any Notion API code. What are the trade-offs of using a generic connector like Zapier vs. building a direct integration?
3. If the user's message is ambiguous (e.g., "save what we just talked about"), what should happen? How would you design the system prompt or the agent's behavior to handle this gracefully?
