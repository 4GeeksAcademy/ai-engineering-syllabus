# CONTEXT — Brasaland: Sistemas en Tiempo Real (Parte 2)

> Da por hecho que tu agente de soporte ya existe y funciona — aquí no se rediseña el agente, solo el canal por el que habla con el usuario.

## 1. Introducción

La solicitud viene del equipo de **Felipe Guerrero**, Operations — la misma área que posee el Manager support agent que usan los encargados de local en los sitios de Brasaland. Hoy un encargado envía una pregunta, espera, y recibe la respuesta completa de una sola vez. Si el agente se desvía (local equivocado, horario de proveedor incorrecto), no puede corregirlo hasta que termina la respuesta. Felipe lo convirtió en un ticket: que la conversación se sienta en vivo — tokens conforme se generan, y poder interrumpir a mitad de respuesta y redirigir sin recargar ni empezar de cero. Quienes van a usar lo que construyas son los **encargados de local** que chatean con ese agente.

## 2. Qué Agente Vas a Conectar

El agente que vas a exponer por WebSocket es el **Manager support agent**: el que responde preguntas operativas frecuentes de los encargados de local en el idioma base seleccionado. No cambies su lógica ni sus herramientas — solo el canal por el que habla con el usuario.

## 3. Entidad de Sesión de Chat

- **ChatSession**: `session_id`, `agent_id` (`manager_support`), `user_id` (el encargado de local que está chateando), `location_id`, `status` (`active`, `interrupted`, `closed`), `created_at`

Usa `session_id` (y el mismo valor como LangGraph `thread_id` si haces checkpoint) en el handshake del WebSocket para poder rehidratar la conversación al reconectar.

Autentica el WebSocket con el **mismo JWT** que la API del backoffice (y el SSE de la Parte 1). Preferible `?token=` en la URL y/o un primer frame de auth del cliente — rechaza antes de eventos de chat si falta o es inválido.

## 4. Eventos Sugeridos sobre el WebSocket

Usa nombres de evento explícitos y payloads estructurados (misma disciplina de nombres que en la Parte 1 — no los mismos esquemas RFP/SSE):

```json
{"event": "token_chunk", "data": {"session_id": "chat_0044", "token": "Para", "sequence": 12}}
{"event": "interrupt_requested", "data": {"session_id": "chat_0044", "new_input": "espera, pregunté por el local de Miami"}}
{"event": "generation_interrupted", "data": {"session_id": "chat_0044", "message_id": "msg_0090", "status": "interrupted"}}
{"event": "generation_completed", "data": {"session_id": "chat_0044", "message_id": "msg_0091"}}
{"event": "session_snapshot", "data": {"session_id": "chat_0044", "messages": []}}
{"event": "user_message", "data": {"session_id": "chat_0044", "text": "..."}}

```

También soporta rehidratación en reconnect (`session_snapshot`) y turnos de usuario entrantes (`user_message`) — necesarios para restaurar el handshake y la entrada de chat.

## 5. Patrón Pub/Sub

Usa un canal por sesión (por ejemplo, `chat.<session_id>`) para que el productor (el agente generando tokens) esté desacoplado de los consumidores (las conexiones WebSocket suscritas). No necesitas Redis para esta entrega — un mecanismo en memoria es aceptable si tu implementación corre en un solo proceso.

## 6. Restricciones

- Los nombres de campos y entidades de la sesión de chat deben coincidir con este CONTEXT — no inventes ids paralelos para la misma sesión.
- No mezcles los payloads de notificación de ticket RFP de la Parte 1 en el contrato WebSocket del chat.
