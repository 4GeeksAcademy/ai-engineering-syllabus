# CONTEXT — TrackFlow: Sistemas en Tiempo Real (Parte 2)

> Da por hecho que tu agente de soporte ya existe y funciona — aquí no se rediseña el agente, solo el canal por el que habla con el usuario.

## 1. Introducción

La solicitud viene del área de **Valentina Cruz**, Customer Experience — el equipo que opera el First-line CX agent de tracking, devoluciones y preguntas frecuentes. Hoy un cliente envía un mensaje, espera, y recibe la respuesta completa de una sola vez. Si el agente está respondiendo al intent equivocado (rastreo cuando querían una devolución), no puede redirigirlo hasta que termina la respuesta. Valentina lo convirtió en un ticket: streamear la respuesta token a token y permitir interrumpir a mitad de respuesta para que el chat se sienta como una conversación real. Quienes van a usar lo que construyas son los **clientes** (marcas B2B y destinatarios B2C de paquetes) que chatean con ese agente.

## 2. Qué Agente Vas a Conectar

El agente que vas a exponer por WebSocket es el **First-line CX agent** del área de Valentina Cruz: el que hoy resuelve consultas de tracking, estado de devoluciones y preguntas frecuentes. No cambies su lógica ni sus herramientas — solo el canal por el que habla con el usuario.

## 3. Entidad de Sesión de Chat

- **ChatSession**: `session_id`, `agent_id` (`first_line_cx`), `user_id` (el cliente que está chateando), `client_id`, `status` (`active`, `interrupted`, `closed`), `created_at`

Usa `session_id` (y el mismo valor como LangGraph `thread_id` si haces checkpoint) en el handshake del WebSocket para poder rehidratar la conversación al reconectar.

Autentica el WebSocket con el **mismo JWT** que la API del backoffice (y el SSE de la Parte 1). Preferible `?token=` en la URL y/o un primer frame de auth del cliente — rechaza antes de eventos de chat si falta o es inválido.

## 4. Eventos Sugeridos sobre el WebSocket

Usa nombres de evento explícitos y payloads estructurados (misma disciplina de nombres que en la Parte 1 — no los mismos esquemas RFP/SSE):

```json
{"event": "token_chunk", "data": {"session_id": "chat_0219", "token": "Tu", "sequence": 7}}
{"event": "interrupt_requested", "data": {"session_id": "chat_0219", "new_input": "espera, quiero hacer una devolución, no rastrear el pedido"}}
{"event": "generation_interrupted", "data": {"session_id": "chat_0219", "message_id": "msg_0449", "status": "interrupted"}}
{"event": "generation_completed", "data": {"session_id": "chat_0219", "message_id": "msg_0450"}}
{"event": "session_snapshot", "data": {"session_id": "chat_0219", "messages": []}}
{"event": "user_message", "data": {"session_id": "chat_0219", "text": "..."}}

```

También soporta rehidratación en reconnect (`session_snapshot`) y turnos de usuario entrantes (`user_message`) — necesarios para restaurar el handshake y la entrada de chat.

## 5. Patrón Pub/Sub

Usa un canal por sesión (por ejemplo, `chat.<session_id>`) para que el productor (el agente generando tokens) esté desacoplado de los consumidores (las conexiones WebSocket suscritas). No necesitas Redis para esta entrega — un mecanismo en memoria es aceptable si tu implementación corre en un solo proceso.

## 6. Restricciones

- Los nombres de campos y entidades de la sesión de chat deben coincidir con este CONTEXT — no inventes ids paralelos para la misma sesión.
- No mezcles los payloads de notificación de ticket RFP de la Parte 1 en el contrato WebSocket del chat.
