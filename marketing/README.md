# AI Native Full Stack — Program modules

_Este contenido también está disponible en [espanol](./README.es.md)._

---

## Core AI and Agents

### Personal Assistants with OpenClaw

`AI` `Agents` `OpenClaw` `Deployment`

You will learn to deploy and configure an open-source, self-hosted AI assistant — yours, under your control, without relying on external vendors. The practical foundation for the program’s more advanced agent modules.

**Skills developed:**

- Configure an open-source AI agent as a personal assistant
- Assign tasks and integrate external applications with the agent

---

### Advanced Personal Assistants with OpenClaw

`Agent Skills` `Memory` `Tool Calling` `Advanced configuration`

You will take your basic assistant agent to a productive tool. You will learn to teach it new skills, choose the right memory type for each case, and configure it to operate with real autonomy in business contexts.

**Skills developed:**

- Identify scenarios where an agent solves real business problems
- Develop custom skills for OpenClaw
- Implement contextual memory (episodic, semantic, procedural)
- Advanced configuration and extension of the agent

---

### Working with AI Coding Agents

`Coding Agents` `Context Engineering` `Agent Rules` `Memory Banks` `Skills`

The leap from “using AI” to “working professionally with AI.” You will learn to build memory banks and context rules that turn a coding agent into a collaborator that understands your codebase. You will master writing specifications an agent can execute with precision.

**Skills developed:**

- Build memory banks and context rules from an existing codebase
- Write executable specifications for agents (agent specs)
- Synthesize reusable skills so agents act with precision

---

### LLMs, Training & RAG

`RAG` `Vector DBs` `Chunking` `Fine-tuning` `Embeddings` `Model Evaluation`

You will understand how the models that power agents work — and how to make them smarter for specific use cases. You will implement RAG so your agent answers with proprietary, up-to-date knowledge, and learn when and how to train or fine-tune a model.

**Skills developed:**

- Prepare data and select models for training
- Implement RAG techniques on proprietary knowledge bases
- Work with vector databases
- Evaluate, debug, and integrate models in production

---

### Agentic Engineering

`Tool Calling` `CLIs` `MCPs` `Guardrails` `Agent Memory`

The technical heart of the program. You will build agents that can call tools, access external systems via MCPs and CLIs, operate with persistent memory, and behave safely under guardrails. The knowledge that separates an AI engineer from someone who only uses chatbots.

**Skills developed:**

- Build agents with tool calling (real function calls)
- Implement guardrails as a security and control mechanism
- Provide tools to the agent via CLIs optimized for AI
- Extend agent capabilities with the Model Context Protocol (MCP)
- Give an agent persistent memory

---

### Agentic Workflows

`Multi-Agent Systems` `Routing` `Serverless` `Cronjobs`

When one agent is not enough. You will learn to design systems where multiple agents collaborate, distribute tasks, and share memory. You will implement agentic pipelines with serverless functions and cron jobs that run autonomously, continuously, and at scale.

**Skills developed:**

- Design multi-agent systems with routing and arbitration
- Implement shared memory across agents
- Deploy agentic workflows with serverless and durable functions

---

## Infrastructure for AI

### Backend Development with Coding Agents

`Python` `FastAPI` `Agent Loops` `APIs` `Document DBs`

The backend that brings agents to life. You will build robust APIs with FastAPI, implement agent loops in Python, and learn to design backend architectures oriented to AI use cases — from data processing to LLM integration.

**Skills developed:**

- Design backend architectures for AI-powered solutions
- Create agent loops integrating LLMs with APIs
- Implement lightweight storage and CSV data processing
- Build and expose REST APIs for frontends and agents

---

### Workflow Automations

`n8n` `LLM Nodes` `Webhooks` `Automation`

Business automation with integrated AI. You will learn to represent business processes as executable flows, implement them in n8n, and connect LLMs and third-party apps in those flows. The outcome: processes that run autonomously without manual intervention.

**Skills developed:**

- Model business logic with workflow diagrams
- Implement basic and advanced flows in n8n
- Integrate LLMs and external apps in automations
- Deploy maintainable workflows with error handling

---

### Data Pipelines

`Pandas` `ETL` `Data Pipelines`

Data is the fuel of any AI solution. You will learn to build pipelines that take raw data from an application, transform it, and leave it ready to feed models, reports, or agents — the link that determines output quality.

**Skills developed:**

- Manipulate and prepare datasets with Python
- Build data pipelines from the application to analysis systems

---

### Telemetry

`Observability` `Reporting` `Data Collection` `Analysis`

You cannot improve what you do not measure. You will learn to instrument applications to collect behavioral data, build reports from that data, and make business decisions based on real evidence — not intuition.

**Skills developed:**

- Optimize storage for reporting and data integrity
- Identify data collection opportunities in real scenarios
- Collect telemetry and user context from the application
- Build reports from telemetry data

---

### Real-Time

`WebSockets` `Streaming` `Pub/Sub` `Event Architecture`

The layer that makes AI feel alive. You will implement real-time communication between users and language models using streaming, WebSockets, and event-driven architectures — the same technology behind modern conversational interfaces.

**Skills developed:**

- Build support chats with LLMs in real time
- Implement response streaming with generators (yield)
- Integrate webhooks and pub/sub in AI applications

---

### Asynchronous Processing and Offloading

`Queues` `Background jobs` `Workers` `Redis`

Tasks that must not block the user go to the queue. You will learn to implement background processing and queue systems that let agents and applications delegate heavy work without sacrificing response time — an essential pattern in productive AI architectures.

**Skills developed:**

- Implement background processing for costly tasks
- Manage process queues with workers
- Use queues to delegate work between agents and services

---

### Web Application Authentication

`JWT` `FastAPI` `Auth flows` `Security`

Every productive application needs to know who is who. You will learn to implement secure authentication in FastAPI and build complete login flows that define what each user can do — and what agents can invoke on their behalf.

**Skills developed:**

- Implement authentication and route restrictions in FastAPI
- Build complete authentication flows (login, tokens, sessions)

---

### Error Handling, Debugging and Testing

`Error Handling` `Testing` `Debugging` `TDD`

Code that agents generate must be verified. You will learn to handle errors in a controlled way, write test suites that validate expected behavior, and debug applications with judgment — the quality standards that separate professional software from prototypes.

**Skills developed:**

- Understand and manage runtime errors with flow control
- Develop test suites for robust applications

---

### Cybersecurity in AI Applications

`OWASP` `AI Security` `LLM Auditing` `Guardrails`

AI introduces attack vectors traditional security does not cover. You will learn to identify the most critical vulnerabilities in AI applications, implement safe practices in model integration, and use LLMs themselves to audit a system.

**Skills developed:**

- Identify and fix OWASP Top 10 vulnerabilities in web applications
- Implement security practices specific to AI integrations
- Use LLMs as a cybersecurity auditing tool

---

## Other complementary knowledge

### Foundations and technical support skills

`Algorithms` `Data Structures` `Docker` `TypeScript` `React` `Next.js` `Tailwind` `SQL` `Git` `Command Line`

These modules provide the essential foundations to collaborate effectively with software agents and review their work:

- **Programming:** Logic, algorithms, data structures, and OOP with TypeScript and Python to understand and improve AI-generated code.
- **Modern frontend:** Building and reviewing interfaces with React, Next.js, and visual specs; accessible, optimized styling with HTML, CSS, and Tailwind.
- **Databases:** SQL, PostgreSQL, and ORMs for robust data handling and relational queries.
- **Containerization:** Packaging and deploying full applications with Docker for productive, reproducible environments.
- **Optimization:** Performance strategies on frontend and backend: caching, serializers, lazy loading, and practices for high load.
- **Collaboration tools:** Command line, Git, and GitHub for collaborative, safe workflows.

This knowledge complements and strengthens the full development cycle of AI- and agent-driven systems.

---

## Capstone

### AI-transformed company

`Final Project` `AI-First Company`

The program closes with a real deliverable: the full transformation of a company through AI. You will integrate everything you have learned — agent-generated frontend, authenticated APIs, telemetry, automated workflows, a RAG knowledge layer, and agents with tool calling — into a working, deployed system. Not an academic exercise: a demonstration of professional capability.

**Deliverable components:**

- AI-generated frontend
- API with full authentication
- Telemetry and reporting pipeline
- Agent-generated automated workflows
- RAG knowledge layer
- Agents with tool calling
- Real-time communication
