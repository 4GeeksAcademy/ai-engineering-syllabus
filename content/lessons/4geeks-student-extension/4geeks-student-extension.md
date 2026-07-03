# Your academy AI models in Codespaces — 4Geeks Student + Copilot Chat

<!-- hide -->

_Estas instrucciones también están disponibles en [español](./4geeks-student-extension.es.md)._

<!-- endhide -->

Use your included academy AI models in **Copilot Chat** while working inside a **GitHub Codespace** — no separate Copilot subscription required.

If you reach the limit of your **Copilot Business** usage, you can continue coding with AI by switching to a **4Geeks Student** model from the chat model picker.

---

## What you will achieve

Enabling additional AI models provided by 4Geeks Academy doing the following steps:

- Install **4Geeks Student** extension inside your Codespace.
- Sign in with your 4Geeks account (OAuth).
- Register the LLM models assigned to your academy.
- Select a 4Geeks model in Copilot Chat and chat as usual.

```mermaid
flowchart LR
  codespace[Open Codespace]
  install[Install extension]
  login[4Geeks Login]
  models[4Geeks Add Models]
  chat[Open Copilot Chat]
  pick[Pick 4Geeks model]
  codespace --> install --> login --> models --> chat --> pick
```

---

## Important — repeat this on every Codespace

In the course you work mainly in **GitHub Codespaces**. Each Codespace is a **fresh cloud environment**:

- Extensions installed in one Codespace **do not carry over** to another.
- When you start a **new exercise**, open a **new repository**, or create a **new Codespace**, you must run the setup again: **install → login → add models**.

This is normal. Budget a minute or two at the start of each session.

---

## Requirements

- A running **GitHub Codespace** (browser or VS Code connected to the Codespace)
- [VS Code](https://code.visualstudio.com/) **1.109** or newer (included in the Codespace)
- A **4Geeks student account** with **LLM budget** entitlement
- **Copilot Chat** available in the editor (no paid Copilot subscription required)

---

## Part A — Setup (each Codespace session)

Run these steps **every time** you open a Codespace that does not already have the extension configured.

### 1. Install the extension

1. Open the **Extensions** view (`Ctrl+Shift+X` / `Cmd+Shift+X`).
2. Search for **4Geeks Student** (publisher: **4Geeks**) and install it.
3. **Reload** the window when prompted.

### 2. Sign in

1. Click **Sign in** on the connect invite, **or**
2. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run **`4Geeks: Login`**.
3. Complete the OAuth flow in your browser with your **4geeks.com** account.

### 3. Register your models

1. Run **`4Geeks: Add Models`** from the Command Palette.
2. The extension provisions and registers the models assigned to your academy. Model names are **not fixed** — they depend on your cohort and entitlement.

---

## Part B — Use academy models in Copilot Chat

1. Open **Copilot Chat**.
2. Open the **model picker** in the chat panel.
3. Select a **4Geeks Student** model. If you do not see it in the main list, check **Other Models**.
4. Start chatting — the selected model uses your academy **LLM budget**.

### Extending your AI usage

Your academy includes its own LLM budget. Use it when:

- You want a model configured for your cohort, or
- You have consumed your **Copilot Business** token allowance and need to keep working with AI in the same chat interface.

If no model is available for your account, the extension will show an error — contact your academy if that happens.

---

## Part C — Connect to your VPS (optional)

If your account includes **VPS credits** and you work outside Codespaces:

1. Run **`4Geeks: Connect to VPS`** from the Command Palette.
2. The extension connects via **Remote SSH** (it installs **Remote - SSH** if needed).

To sign out and remove registered models, run **`4Geeks: Logout`**.

---

## Switching to another Codespace

When you move to a new exercise or repository:

1. Open the new Codespace.
2. Repeat **Part A** (install → login → add models).
3. Pick your **4Geeks Student** model again in Copilot Chat.

---

## Commands reference

| Command                    | Description                                    |
| -------------------------- | ---------------------------------------------- |
| **4Geeks: Login**          | Sign in with your 4Geeks account               |
| **4Geeks: Add Models**     | Provision and register your academy LLM models |
| **4Geeks: Connect to VPS** | Connect to your 4Geeks VPS via Remote SSH      |
| **4Geeks: Logout**         | Sign out and remove registered models          |

---

## Checklist

### Each new Codespace

```text
□ Open Codespace
□ Install 4Geeks Student (publisher: 4Geeks)
□ Reload window
□ 4Geeks: Login (OAuth at 4geeks.com)
□ 4Geeks: Add Models
□ Copilot Chat → model picker → 4Geeks Student model
```

---

## One-sentence summary

On **every new Codespace**, install **4Geeks Student**, run **`4Geeks: Login`** and **`4Geeks: Add Models`**, then pick a **4Geeks Student** model in **Copilot Chat** to use your academy AI budget.

---

## Useful links

- [VS Code Marketplace](https://marketplace.visualstudio.com/) — search **4Geeks Student** (publisher: **4Geeks**)
- [4Geeks.com](https://4geeks.com/)
- [GitHub Codespaces documentation](https://docs.github.com/en/codespaces)
