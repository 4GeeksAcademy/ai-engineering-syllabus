# CONTEXT — TrackFlow: Observabilidad de Agentes (Parte 1)

> Este documento cubre solo la Parte 1. La Parte 2 (control) reutiliza las mismas entidades e identificadores de agente definidos aquí.

## 1. Introducción

El ticket viene de **Andrés Kim**, CTO. TrackFlow Tech tiene hoy dos agentes en producción sin ninguna visibilidad compartida: el **first-line CX agent** en el que se apoya el equipo de Valentina Cruz para tracking, devoluciones y preguntas frecuentes, y el **pipeline multiagente de propuestas** que procesa RFPs (almacenamiento, última milla, logística inversa) para el equipo Comercial de Miguel Torres. Andrés está cansado de enterarse de que algo anda mal por un mensaje de WhatsApp entre Los Ángeles y Zaragoza en vez de por el propio sistema.

## 2. Agentes que Vas a Observar

| `agent_id` | Nombre | Tipo | Dueño / Área | Participa en |
|---|---|---|---|---|
| `first_line_cx` | First-line CX agent | Agente único, conversacional | Valentina Cruz — Customer Experience | flujos `chat_session` |
| `rfp_pipeline` | Pipeline de propuestas comerciales | Multiagente (orquestador, generadores, evaluadores, sintetizador) | Miguel Torres — Comercial | flujos `rfp_workflow` |

No cambies la lógica interna de ninguno de los dos agentes — solo estás instrumentando los puntos donde ya actúan, para emitir y persistir eventos.

## 3. Tipos de Flujo y Taxonomía de `action_type`

| `flow_type` | Descripción | Secuencia típica de `action_type` |
|---|---|---|
| `chat_session` | Una conversación entre un cliente (marca B2B o destinatario B2C) y `first_line_cx` | `query` (recupera contexto de tracking/políticas) → `tool_call` (si consulta un envío o devolución) → `deliver` (respuesta final) |
| `rfp_workflow` | Un RFP comercial pasando por intake, redacción y evaluación | `query` (clasifica/extrae del PDF) → `tool_call` (consulta datos de departamento) → `draft_start` / `write` (sección de departamento redactada) → `evaluate` (paso del evaluador) → `deliver` (el sintetizador entrega el borrador consolidado) |

Usa los valores de `department_id` ya definidos para el pipeline de RFP de TrackFlow — `warehouse`, `lastmile`, `reverse` — como parte del payload de la tarea cuando un paso pertenece al generador o evaluador de un departamento específico.

## 4. Campos de Entidad Específicos de TrackFlow

- **Agent.needs_intervention** debe pasar a `true` automáticamente cuando: un `chat_session` lleva más de 20 segundos en `query`/`tool_call` sin un `deliver`, o una tarea de `rfp_workflow` pasó por `evaluate` más veces que el límite de reintentos configurado sin producir una evaluación aprobada.
- **Flow.triggered_by**: para `chat_session`, el mensaje entrante del cliente; para `rfp_workflow`, el registro del ticket de RFP (reutiliza el mismo `ticket_id` que tu pipeline ya genera).
- La moneda (USD para clientes de EE. UU., EUR para clientes con sede en España) la determina el `client_country` del RFP — no es algo que los payloads de este milestone necesiten duplicar.

## 5. Eventos SSE Sugeridos

```json
{"event": "agent_step", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0509", "task_id": "task_2044", "action_type": "write", "department_id": "warehouse"}}
{"event": "agent_status_changed", "data": {"agent_id": "first_line_cx", "flow_id": "chat_0698", "status": "running"}}
{"event": "agent_status_changed", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0509", "status": "waiting_for_human"}}
```

## 6. Restricciones

- Los nombres de campos, agentes y `action_type` deben coincidir exactamente con este documento — no inventes identificadores paralelos.
- No muestres ni dupliques aquí la lógica de aprobación por departamento del pipeline de RFP — este panel solo observa; la aprobación ya vive en el flujo de ese milestone.
- Persiste cada tarea aunque no haya ningún cliente SSE conectado en el momento en que ocurre.
