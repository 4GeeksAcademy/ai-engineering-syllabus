# Connect Your Agent: Telegram, Google Drive & Calendar — Reference Solution

## Purpose

This project is **configuration-only**: there is no application codebase to implement. A complete submission proves that an OpenClaw agent is wired to **Telegram** for messaging and to **Google Drive** and **Google Calendar** through the **Zapier MCP**, and that a single user request can trigger document creation, calendar blocking, and a Telegram confirmation.

## Expected configuration (high level)

1. **OpenClaw** — Running instance (from the [openclaw-setup](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/projects/openclaw-setup) project), with the agent able to receive messages and invoke configured tools/MCPs.
2. **Telegram** — Bot created with BotFather; token stored only in secure configuration (never in screenshots or `notes.md`); OpenClaw configured to use this bot as the messaging channel.
3. **Zapier MCP** — Enabled in Zapier; MCP endpoint/credentials added to OpenClaw so the agent can call Zapier actions as tools.
4. **Google (via Zapier)** — Test Google account connected in Zapier; Zaps or MCP-exposed actions allow **creating a Drive document** and **creating a Calendar event** when the agent invokes them.

## Reference workflow (end-to-end)

1. User sends a Telegram message asking the agent to create a document (with enough detail, or the agent asks clarifying questions first).
2. Agent uses Zapier-backed tools to create the document in Google Drive.
3. Agent creates a calendar event for reviewing that document.
4. Agent replies on Telegram confirming completion.

## Evidence package (submission)

The learner’s deliverable folder (`openclaw-connection`) should include:

- Screenshots of OpenClaw showing Telegram, Zapier MCP, Drive, and Calendar integrations connected (no tokens or secrets visible).
- Full Telegram thread: request → optional follow-up questions → final confirmation.
- Screenshot of the new Drive document and the new Calendar event.
- Short `notes.md` / `notas.md` (5–10 lines) on configuration choices or issues.

## Evaluation alignment

- Telegram bot exists and responds through OpenClaw.
- Zapier MCP is present and active in the agent configuration.
- Drive and Calendar actions work from the agent (not only manually in Zapier).
- Clarifying behavior when the user message is vague.
- No sensitive credentials or personal data in submitted files.

## Validation notes

- Use **dedicated test accounts** for Google; do not connect highly sensitive personal data.
- Redact or crop screenshots before submit.
- The rubric cares about **correct execution of the flow**, not the agent’s writing style.
