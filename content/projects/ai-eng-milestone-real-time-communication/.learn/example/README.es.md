# Lighthouse Desk — Chat de Ayuda con Streaming (Ejemplo de clase)

> **Para instructores:** Escenario paralelo de aula para `ai-eng-milestone-real-time-communication`. Misma columna vertebral (WebSocket, stream de tokens, interrupción real, pub/sub por sesión, reconexión con backoff). Dominio distinto a los agentes CONTEXT de empresa. El alumnado sigue el brief completo del `README.md` en la raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Lighthouse Desk** es un bot mínimo de ayuda en un puerto deportivo. Hoy el empleado escribe una pregunta, espera, y recibe la respuesta entera de golpe — si el bot se desvía, hay que esperar a que termine. Demo de esta noche: las respuestas aparecen **token a token**, y el empleado puede **interrumpir a mitad de respuesta** con una corrección. Una segunda pestaña de “supervisor” en la misma sesión ve el mismo stream sin llamar al bot dos veces.

### Nota de alcance

| Proyecto evaluado (`ai-eng-milestone-real-time-communication`) | Este ejemplo de clase                                         |
| -------------------------------------------------------------- | ------------------------------------------------------------- |
| Monorepo de empresa + agente de soporte existente              | Stub “bot” que emite tokens falsos (o una llamada LLM mínima) |
| Abort del stream (cancelar tarea); HITL `interrupt()` opcional | `asyncio` cancel + turno nuevo con nuevo prompt               |
| UI de chat completa de la empresa                              | Una página HTML/JS + pestaña opcional                         |
| Fidelidad CONTEXT `ChatSession` / agent_id                     | Demo fija: `session_id`, `status`                             |
| PR de empresa + preguntas de diseño                            | Demo en vivo + 2 tests automatizados                          |

---

## Columna vertebral (debe cubrirse en vivo)

1. **Por qué WebSocket** — el cliente debe enviar mientras el servidor sigue streameando (SSE no alcanza)
2. **Eventos de token** — `token_chunk` nombrado, no un blob al final
3. **Pub/sub** — un productor, muchos consumidores WS en `chat.<session_id>`
4. **Abort real** — cancelar la tarea de generación (sin más tokens); conservar parcial como `interrupted`; siguiente respuesta = turno nuevo con `new_input`
5. **UI de tipado en vivo** — anexar tokens conforme llegan
6. **Reconexión + rehidratación** — caer el socket → mismo `session_id` → restaurar historial, no chat vacío
7. **No reconstruir el “agente”** — solo el canal (stub OK en clase)

---

## Eventos semilla (indicativos)

```json
{"event": "token_chunk", "data": {"session_id": "chat_demo_1", "token": "Slip ", "sequence": 1}}
{"event": "interrupt_requested", "data": {"session_id": "chat_demo_1", "new_input": "I meant slip B-17, not A-3"}}
{"event": "generation_interrupted", "data": {"session_id": "chat_demo_1", "message_id": "msg_00", "status": "interrupted"}}
{"event": "generation_completed", "data": {"session_id": "chat_demo_1", "message_id": "msg_01"}}
```

---

## Qué construir

### 1. Backend

- [ ] `WS /ws/chat/{session_id}` — aceptar, suscribirse al bus en memoria
- [ ] En `user_message`: arrancar productor de tokens; publicar frames `token_chunk`
- [ ] En `interrupt_requested`: detener productor; nueva generación con `new_input`
- [ ] Test unitario: contrato de eventos token / interrupt / completed

### 2. Frontend

- [ ] Conectar WebSocket; anexar tokens al bubble del asistente
- [ ] Enviar interrupt cuando el usuario envía mientras hay stream
- [ ] Reconexión con backoff progresivo al caer

### 3. Guion de demo (en vivo)

1. Abrir pestaña empleado + pestaña supervisor con el mismo `session_id`
2. Pregunta larga → ambas ven tokens en stream
3. Interrumpir a mitad con una corrección → ambas ven stop + nueva respuesta
4. Cortar la red un momento → la reconexión reanuda la sesión

---

## Fuera de alcance del ejemplo

- SSE de RFP de empresa (proyecto evaluado Parte 1)
- Agente LangGraph real de empresa / herramientas MCP
- Backplane Redis (pub/sub en memoria basta)
