# MCP Server: Connecting Your Agent to the Company's Tools

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[build by developers](https://4geeks.com)
[4Geeks Academy](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** selected at the beginning of the course — not on a new repository.

**About MCP Servers**

An MCP Server exposes a system's capabilities (tools, resources, prompts) through a standard protocol that any compatible agent can discover and consume, without coupling to your backend's internal code. Unlike the tools you already wired directly into your agent's graph, an MCP Server can be reused by multiple clients — other agents, other teams, other companies in the ecosystem — as long as they authenticate correctly. That's why authentication and the principle of least privilege aren't a nice-to-have: an MCP server without auth is a real vulnerability from day one.

Your agent already knows how to call tools directly. Now your tech lead has filed a **ticket** asking those capabilities to stop being hardcoded inside the graph and instead be exposed as an independent, reusable service protected by an API Key — and for the agent itself to stop calling the Incidents Manager directly, consuming it through the MCP server instead.

> **From:** Your tech lead
> **To:** Your squad
> **Subject:** RFP — MCP Server for company tools
>
> The agent we built already queries the Incidents Manager from inside the graph, but any future integration (another agent, another team, an external partner) would have to reimplement those same calls. We need to expose them as an independent **MCP Server**, authenticated with an API Key, so that any authorized MCP client can:
>
> - Manage Incidents Manager tickets (create, update, check status).
> - Query — **never edit** — inventory data.
>
> The server must not grant more permissions than strictly necessary for each tool. Document the discovery well: any client should be able to understand what the server can do without needing additional human context.
>
> And don't leave the migration half-done: I want the agent itself to replace its direct Incidents Manager tool with a call to the MCP Server as a client. If the agent is still calling the Incidents Manager outside the server, the ticket isn't resolved.
>
> Acceptance criteria are in the checklist. Let me know when it's ready to test from an MCP client.

As part of the challenge, your implementation must resolve — without being told explicitly in a checklist — the following design decisions:

- Which transport to use (stdio vs. Streamable HTTP) depending on whether the server is consumed locally or by multiple remote clients, and what that choice implies for authentication.
- How to structure the permission system so the inventory tool is, by design, read-only — it's not enough to simply "not implement" the write endpoint; the server must explicitly reject any attempt.
- What information to expose in discovery (tool names, descriptions, and schemas) so an external agent, with no prior human context, understands what it can and cannot do.
- How to replace, inside the agent's graph, the node that called the Incidents Manager directly with tools from the MCP Server via `langchain-mcp-adapters` — without breaking the existing routing between RAG and tools.

---

## 🌱 How to Start the Project

1. Go to your copy of the [company monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) (if you don't have your own fork yet, create one before continuing).
2. Work on top of the Incidents Manager backend and the inventory module you already built in previous milestones — the MCP Server relies on those services, it doesn't replace them.
3. Install the dependencies you need with `uv add` (e.g., `fastmcp`, `langchain-mcp-adapters`) — never use `pip install` directly in this monorepo.
4. Create the MCP server inside `services/`, following the structure of the rest of the backend services.
5. Locate the agent node that currently calls the Incidents Manager directly — that's the point you'll migrate so it consumes the new MCP Server as a client instead of calling the API outside of it.

---

## 💻 What You Need to Do

**MCP Server**

- [ ] Implement the MCP Server in Python using FastMCP (or an equivalent MCP SDK).
- [ ] Expose at least one tool to manage Incidents Manager tickets (create, update, and check status).
- [ ] Expose at least one **read-only** tool over the inventory — any modification attempt must be explicitly rejected by the server, not simply omitted.
- [ ] Document each tool with a name, description, and input/output schema sufficient for an external agent to discover it without additional human context (an MCP-discovery equivalent of `--help`).

⚠️ **IMPORTANT:** Field names, entity IDs, and domain-specific values in your implementation must match the incident and inventory APIs you already built. A generic implementation that ignores your existing services will not be accepted. Status changes must go through the Incidents Manager lifecycle endpoint (`PATCH /api/incidents/{id}/status`), not a generic `PATCH` on the incident resource.

**Authentication and security**

- [ ] Protect the server with API Key authentication — no client without a valid key can list or invoke tools.
- [ ] Apply the principle of least privilege: each tool only has access to the data and operations it needs to do its job.
- [ ] Define and document the expected error and exit codes for authentication, authorization, or validation failures (not a generic "error").
- [ ] Log every tool invocation (which tool, which client, what result) for traceability.

**Validation (MCP Playground)**

- [ ] First, test your MCP server in [MCP Playground](https://www.mcpplayground.tech/playground): enter the server URL, connect, and run at least one complete flow per exposed tool.
- [ ] Test and document the server's behavior when a write attempt is made on the inventory tool (it must fail in a controlled, explainable way).

**Agent migration**

- [ ] Connect the LangGraph agent you already built to the MCP Server using [`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters): replace the node that called the Incidents Manager directly with tools loaded from the MCP Server.
- [ ] Remove (or explicitly deprecate and stop using) the previous direct tool implementation — the agent must not have two possible paths to the Incidents Manager.
- [ ] Confirm that the existing routing between RAG and tools still works the same as before, now with the new MCP client node in place of the previous one.

---

## ✅ What We Will Evaluate

- [ ] The MCP server starts correctly and exposes its tools through the standard MCP discovery mechanism.
- [ ] A client without a valid API Key cannot list or execute any tool.
- [ ] The ticket management tool creates, updates status via `PATCH /api/incidents/{id}/status`, and queries against the company's real Incidents Manager.
- [ ] The inventory tool responds correctly to queries and explicitly rejects any write operation.
- [ ] Each tool has a clear description and schema, verifiable from the server's own discovery without reading the source code.
- [ ] Authentication, authorization, and validation errors return distinct codes and messages from one another.
- [ ] There is at least one log entry per tool invocation with client, tool, and result.
- [ ] The agent no longer calls the Incidents Manager directly: every interaction goes through the MCP Server as a client.

---

## 📦 How to Submit

Follow the monorepo's standard delivery flow: push your branch, open a Pull Request against your fork, and describe in the PR which transport you chose and why. Let your tech lead know when the server is ready to be tested from an external MCP client.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
