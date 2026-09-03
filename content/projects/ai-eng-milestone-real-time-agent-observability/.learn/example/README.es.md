# Signal Yard — Tablero de Vigilancia de Agentes (Ejemplo de clase)

> **Para instructores:** Escenario paralelo de aula para `ai-eng-milestone-real-time-agent-observability`. Misma columna vertebral (Agente / Flujo / Tarea, persistir-luego-SSE, eventos nombrados `agent_step` / `agent_status_changed`, auth JWT opcional en demo, acciones disponibles solo informativas, cadena de tarea trazable). Dominio distinto a los agentes CONTEXT de empresa. El alumnado sigue el brief completo del `README.md` en la raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Signal Yard** es un escritorio nocturno ficticio de carga ferroviaria. Ya corren dos sistemas:

- `yard_desk` — un bot conversacional que responde preguntas del turno (`chat_session`)
- `inbound_wave` — un flujo multi-paso de recepción (`rail_wave`) con inspect → classify → assign → deliver

Demo de esta noche: un tablero que lista ambos agentes, abre el detalle (últimos flujos + últimas tareas), lista olas y reconstruye la cadena de cualquier `task_id`. **Solo mirar** — no implementes pausa/kill.

### Nota de alcance

| Proyecto evaluado (`ai-eng-milestone-real-time-agent-observability`) | Este ejemplo de clase                           |
| -------------------------------------------------------------- | ----------------------------------------------- |
| Monorepo de empresa + agentes / `action_type` del CONTEXT      | Solo Signal Yard                                |
| Instrumentar LangGraph / pipeline RFP real                     | Runners stub que emiten tareas                  |
| `uis/backoffice` completo + JWT de empresa                     | Un tablero HTML/JS; token demo OK               |
| Reglas CONTEXT de `needs_intervention`                         | Simple: atascado > 20s en `query` sin `deliver` |
| PR de empresa + preguntas de diseño                            | Demo en vivo + 5 tests automatizados            |

---

## Columna vertebral (debe cubrirse en vivo)

1. **Tres entidades** — Agente ≠ Flujo ≠ Tarea
2. **Dos arquitecturas, un esquema** — conversacional + multi-paso
3. **Persistir primero, luego SSE** — matar la pestaña, recargar, el historial sigue
4. **Eventos nombrados** — `agent_step`, `agent_status_changed` (no `message` genérico)
5. **Cadena de tarea** — disparador, derivadas, prev, next reconstruibles por `task_id`
6. **Acciones solo informativas** — muestra `pause` como disponible; no la ejecutes
7. **Reconexión con backoff** — caer el stream → reconectar; sin filas duplicadas para el mismo `task_id`

---

## Agentes semilla (indicativo)

| `agent_id`     | Tipo           | `flow_type`    |
| -------------- | -------------- | -------------- |
| `yard_desk`    | Conversacional | `chat_session` |
| `inbound_wave` | Multi-paso     | `rail_wave`    |

`action_type` típico en `rail_wave`: `query` → `tool_call` → `write` → `deliver`.

Frames SSE de ejemplo:

```text
event: agent_step
data: {"agent_id":"inbound_wave","flow_id":"wave_07","task_id":"task_21","action_type":"write"}

event: agent_status_changed
data: {"agent_id":"yard_desk","flow_id":"chat_03","status":"running"}
```

---

## Qué construir

### 1. Datos + API

- [ ] Persistir Agente, Flujo, Tarea (disparador / derivadas / prev / next)
- [ ] `GET /agents`, `GET /agents/{id}` (incluir `available_actions` informativas)
- [ ] `GET /agents/{id}/flows?limit=5`, `GET /agents/{id}/tasks?limit=10`
- [ ] `GET /flows`, `GET /flows/{id}`, `GET /tasks/{id}`, `GET /log` paginado
- [ ] `GET /events/stream` como `text/event-stream`

### 2. Runners stub (no un LLM real)

- [ ] `POST /demo/chat` inicia un `chat_session` y emite 2–3 tareas
- [ ] `POST /demo/wave` inicia un `rail_wave` con ≥3 tareas y al menos una hija derivada
- [ ] Opcional: retrasar un `query` > 20s para que `needs_intervention` cambie

### 3. Tablero UI

- [ ] Listado de agentes con indicador de intervención
- [ ] Detalle: últimos 5 flujos anidados, últimas 10 tareas planas
- [ ] Detalle de flujo + campos de cadena visibles
- [ ] SSE actualiza listado/detalle; `fetch` + `ReadableStream`; backoff + dedupe

### 4. Tests

| #   | Escenario          | Esperado                                                     |
| --- | ------------------ | ------------------------------------------------------------ |
| 1   | Frame SSE          | `text/event-stream` + `event:` nombrado + JSON `data`        |
| 2   | Listado de agentes | Ambos agentes semilla; `needs_intervention` booleano         |
| 3   | Detalle de flujo   | Todas las tareas en orden para `wave_07` (o id creado)       |
| 4   | Trazabilidad       | Dado un `task_id` intermedio, prev/next/disparador/derivadas |
| 5   | Paginación         | Dos páginas de log: sin solape, sin hueco                    |

---

## Guion de demo (en vivo)

1. Abrir dos pestañas del tablero
2. `POST /demo/wave` → ambas pestañas actualizan estado; aparece el flujo
3. Abrir un `task_id` → cadena visible
4. Refrescar → el historial sigue ahí
5. Cortar la red un momento → reconectar; el mismo `task_id` no se duplica

---

## Fuera de alcance del ejemplo

- Pausa / reanudar / kill (Parte 2)
- Empresas del CONTEXT (Brasaland, HealthCore, Nexova, TrackFlow)
- Pipeline RFP real ni reescritura del agente RAG
