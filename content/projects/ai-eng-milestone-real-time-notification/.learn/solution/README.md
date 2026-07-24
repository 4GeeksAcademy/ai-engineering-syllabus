# Milestone 10 Part 1 — SSE Notifications — Reference Solution

Reference quality bar for the student's company monorepo fork. Field names and optional second events below are **indicative** — students must align payload shape and domain values with their assigned `CONTEXT-company.md` under `content/contexts/10-realtime/notification/`.

---

## Architecture overview

```mermaid
flowchart LR
  RFP[RFP ticket registered<br/>status=analyzing] --> PUB[Event bus / in-process pub-sub]
  PUB --> SSE["GET /events/stream<br/>text/event-stream"]
  SSE --> C1[Dashboard client A]
  SSE --> C2[Dashboard client B]
  C1 --> UI[Named toast / list row<br/>rfp_ticket_created]
  C2 --> UI
  C1 -.->|drop → backoff reconnect| SSE
```

**Design invariants:**

1. **Named event, not generic `message`** — wire format uses `event: rfp_ticket_created` (or CONTEXT-equivalent name) plus JSON `data:`.
2. **Publish on register** — emission happens in the same path that creates the RFP ticket (`status` initial value from CONTEXT, typically `analyzing`), not from a polling cron.
3. **One stream, many subscribers** — each dashboard tab opens its own SSE connection; the publisher fans out to all live subscribers.
4. **Keep-alive** — periodic comment/ping frames so proxies and browsers do not idle-close the socket.
5. **Reconnect without duplicates** — client tracks last seen `ticket_id` (or event id); after backoff reconnect, ignore events already applied.
6. **No AI in this part** — no model/agent calls on the notification path.

---

## Recommended layout (indicative)

| Path                                      | Responsibility                                           |
| ----------------------------------------- | -------------------------------------------------------- |
| `services/.../events/sse.py`              | SSE endpoint: headers, generator, keep-alive             |
| `services/.../events/bus.py`              | In-process (or Redis) pub-sub for ticket events          |
| `services/.../rfp/tickets.py` (existing)  | On create → `bus.publish("rfp_ticket_created", payload)` |
| `uis/.../dashboard/useSse.ts` (or equiv.) | `fetch` + `ReadableStream` parse loop + backoff          |
| `uis/.../dashboard/RfpTicketToast.tsx`    | Visually distinct notification UI                        |
| `tests/services/test_sse_payload.py`      | Payload shape / event name unit tests                    |

---

## SSE wire format (indicative)

HTTP response:

```http
HTTP/1.1 200 OK
Content-Type: text/event-stream
Cache-Control: no-cache
Connection: keep-alive
X-Accel-Buffering: no
```

Event body:

```text
event: rfp_ticket_created
data: {"ticket_id":"tkt_0192","rfp_id":"rfp_0088","client_name":"Andes Tech Solutions","status":"analyzing","created_at":"2026-07-24T14:32:00Z"}

: keepalive
```

Indicative JSON (must match CONTEXT fields — example aligned to Brasaland-style ticket):

```json
{
  "ticket_id": "tkt_0192",
  "rfp_id": "rfp_0088",
  "client_name": "Andes Tech Solutions",
  "location": "Medellín",
  "service_type": "recurring_catering",
  "status": "analyzing",
  "created_at": "2026-07-24T14:32:00Z"
}
```

**Acceptable:** streaming response from FastAPI/`StreamingResponse` (or stack equivalent) yielding encoded SSE frames.

**Not acceptable:** returning a one-shot JSON list and calling it “real-time”; using only `EventSource` without documenting stack constraints if the brief requires `fetch` + `ReadableStream`; a single catch-all `event: message` for every domain event.

---

## Backend sketch (indicative)

```python
# Pseudocode — adapt to monorepo FastAPI layout
async def ticket_event_stream(request: Request):
    queue = bus.subscribe()
    try:
        yield ": connected\n\n"
        while True:
            if await request.is_disconnected():
                break
            event = await queue.get(timeout=15)
            if event is None:
                yield ": keepalive\n\n"
                continue
            yield f"event: {event.name}\ndata: {event.json()}\n\n"
    finally:
        bus.unsubscribe(queue)
```

On ticket create:

```python
bus.publish(
    name="rfp_ticket_created",
    data={
        "ticket_id": ticket.id,
        "rfp_id": ticket.rfp_id,
        "status": ticket.status,  # CONTEXT initial status
        "created_at": ticket.created_at.isoformat(),
        # + CONTEXT-required display fields
    },
)
```

---

## Frontend sketch (indicative)

```javascript
// Progressive backoff; skip duplicate ticket_id
async function consumeSse(url, { onEvent, seenIds }) {
  let delayMs = 1000;
  for (;;) {
    try {
      const res = await fetch(url);
      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      delayMs = 1000; // reset after successful connect
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        // parse SSE frames from buffer → if event === "rfp_ticket_created"
        // and !seenIds.has(ticket_id) → onEvent(...); seenIds.add(ticket_id)
      }
    } catch (_) {
      /* fall through to backoff */
    }
    await sleep(delayMs);
    delayMs = Math.min(delayMs * 2, 30000);
  }
}
```

UI: dedicated banner/toast/list item for `rfp_ticket_created` — not the same row style as metrics charts or generic activity logs.

---

## Testing bar

| Check             | Pass criteria                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Payload unit test | Assert event name + required CONTEXT keys present; status matches initial value                                         |
| Reconnect         | Documented manual steps **or** automated test: drop stream → backoff → reconnect → no duplicate UI for same `ticket_id` |
| No AI             | Grep/review: notification path has zero model/agent invocations                                                         |

---

## Optional second event

If implementing the README optional case, reuse the same SSE endpoint with a **different** `event:` name and CONTEXT-grounded payload (e.g. `sales_drop_alert`, agent escalation, inactivity). Same reconnect and keep-alive rules apply.

---

## Common mistakes

| Mistake                               | Why it fails                                                       |
| ------------------------------------- | ------------------------------------------------------------------ |
| Generic `message` only                | Rubric requires distinguishable named RFP event                    |
| Inventing field names                 | Must match CONTEXT / existing RFP ticket model                     |
| Silent disconnect                     | Must reconnect with progressive backoff                            |
| Full page refetch on every event      | Notification should update UI without reloading all dashboard data |
| Shipping Part 2 WebSockets logic here | Out of scope for Part 1                                            |
