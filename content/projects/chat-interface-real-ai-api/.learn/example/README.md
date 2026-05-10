# In-Class Example: Recipe Suggestion Chatbot

> **Instructor note:** This is an in-class example designed to introduce the core technical concepts of the main project in a 60–90 minute live-coding session. The domain is a cooking assistant chatbot instead of a general-purpose consultancy chat interface — same technical patterns, much smaller scope.

## The Scenario

A small cooking school wants an AI-powered assistant where students can type questions and get recipe suggestions or cooking tips. You will build a React/Next.js page that talks to the Groq API, tracks token consumption per session, and keeps the conversation alive after a page refresh.

---

## Concepts Covered

| Concept | Where it appears |
|---|---|
| `fetch` with Bearer token | Every Groq API call |
| `async/await` | Handling the async API response |
| `useState` | Messages list, input value, loading flag |
| `useEffect` | Load/save conversation to `localStorage` |
| Token usage tracking | Reading `response.usage` after each reply |
| Session persistence | `localStorage` read on mount, write on send |

---

## What to Build

### Setup

- [ ] Create a free account at [console.groq.com](https://console.groq.com) and generate an API Key
- [ ] Store it as `NEXT_PUBLIC_GROQ_API_KEY` in a `.env.local` file — never hardcode it
- [ ] Create a Next.js project (or scaffold the layout with [v0.dev](https://v0.dev))

### Chat interface

- [ ] A text input and a "Send" button
- [ ] A message list showing user questions and AI answers, visually differentiated (e.g., different background color)
- [ ] Use `useState` for the `messages` array and the `currentInput` string

### Async flow

- [ ] Call the Groq endpoint using `fetch` — no SDK wrappers:
  - URL: `https://api.groq.com/openai/v1/chat/completions`
  - Headers: `Authorization: Bearer <key>` and `Content-Type: application/json`
  - Model: `llama3-8b-8192`
- [ ] Show a "Thinking…" indicator while waiting (a `loading` state via `useState`)
- [ ] Catch errors and display a readable message instead of crashing

### Token tracking

- [ ] After each response, read `data.usage.prompt_tokens` and `data.usage.completion_tokens`
- [ ] Accumulate and display running totals for the session (prompt tokens, completion tokens, combined)

### Session persistence

- [ ] On component mount (`useEffect`), load the message history from `localStorage`
- [ ] After every new message, save the updated history to `localStorage`
- [ ] Add a "Clear chat" button that resets state and removes the `localStorage` entry

---

## Minimal API Call Example

```js
const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.NEXT_PUBLIC_GROQ_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "llama3-8b-8192",
    messages: conversationHistory, // full array of { role, content }
  }),
});
const data = await response.json();
// data.choices[0].message.content → AI reply
// data.usage.prompt_tokens, data.usage.completion_tokens → token counts
```

> **Important:** Always send the full `conversationHistory` array, not just the latest message. The API is stateless — it needs the full context on every request.

---

## Suggested UI Layout

```
┌────────────────────────────────────────────────┐
│  🍳 Recipe Assistant                           │
├─────────────────────────────┬──────────────────┤
│  [message history]          │  Session stats:  │
│                             │  Prompt: 312 tok │
│                             │  Reply:  145 tok │
│                             │  Total:  457 tok │
├─────────────────────────────┴──────────────────┤
│  [text input]                        [Send]    │
│                              [Clear chat]      │
└────────────────────────────────────────────────┘
```

---

## Discussion Questions

1. Why do we send the entire conversation history on every API request, rather than just the latest message?
2. What security risk would occur if we stored the API key directly in the React component instead of in `.env.local`?
3. How would the token count change if the system prompt described the assistant as a very detailed cooking expert with long instructions?
