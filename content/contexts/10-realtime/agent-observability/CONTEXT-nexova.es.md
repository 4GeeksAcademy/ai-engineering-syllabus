# CONTEXT — Nexova: Observabilidad de Agentes (Parte 1)

> Este documento cubre solo la Parte 1. La Parte 2 (control) reutiliza las mismas entidades e identificadores de agente definidos aquí.

## 1. Introducción

El ticket viene de **Sergio Molina**, CTO. Nexova tiene dos agentes en producción sin ninguna forma compartida de revisar su funcionamiento: el **first-line support agent** que el equipo de Customer Support de Roberto Díaz usa para resolver consultas de clientes de outsourcing, y el **pipeline multiagente de propuestas** que procesa RFPs (headhunting, soporte outsourced, capacitación corporativa) para el equipo de Ventas de Marcos Ibáñez. Sergio quiere que su equipo pueda ver, de un vistazo, si alguno de los dos agentes se está comportando bien.

## 2. Agentes que Vas a Observar

| `agent_id` | Nombre | Tipo | Dueño / Área | Participa en |
|---|---|---|---|---|
| `first_line_support` | First-line support agent | Agente único, conversacional | Roberto Díaz — Customer Support | flujos `chat_session` |
| `rfp_pipeline` | Pipeline de propuestas de ventas | Multiagente (orquestador, generadores, evaluadores, sintetizador) | Marcos Ibáñez — Ventas | flujos `rfp_workflow` |

No cambies la lógica interna de ninguno de los dos agentes — solo estás instrumentando los puntos donde ya actúan, para emitir y persistir eventos.

## 3. Tipos de Flujo y Taxonomía de `action_type`

| `flow_type` | Descripción | Secuencia típica de `action_type` |
|---|---|---|
| `chat_session` | Una conversación entre un cliente de outsourcing y `first_line_support` | `query` (recupera contexto de la base de conocimiento) → `tool_call` (si consulta un ticket o cuenta) → `deliver` (respuesta final) |
| `rfp_workflow` | Un RFP de ventas pasando por intake, redacción y evaluación | `query` (clasifica/extrae del PDF) → `tool_call` (consulta datos de departamento) → `draft_start` / `write` (sección de departamento redactada) → `evaluate` (paso del evaluador) → `deliver` (el sintetizador entrega el borrador consolidado) |

Usa los valores de `department_id` ya definidos para el pipeline de RFP de Nexova — `seleccion`, `capacitacion`, `soporte` — como parte del payload de la tarea cuando un paso pertenece al generador o evaluador de un departamento específico.

## 4. Campos de Entidad Específicos de Nexova

- **Agent.needs_intervention** debe pasar a `true` automáticamente cuando: un `chat_session` lleva más de 20 segundos en `query`/`tool_call` sin un `deliver`, o una tarea de `rfp_workflow` pasó por `evaluate` más veces que el límite de reintentos configurado sin producir una evaluación aprobada.
- **Flow.triggered_by**: para `chat_session`, el mensaje entrante del cliente; para `rfp_workflow`, el registro del ticket de RFP (reutiliza el mismo `ticket_id` que tu pipeline ya genera).
- La moneda (EUR para clientes con sede en España, USD para clientes con sede en Miami) la determina el `client_country` del RFP — no es algo que los payloads de este milestone necesiten duplicar.

## 5. Eventos SSE Sugeridos

```json
{"event": "agent_step", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0318", "task_id": "task_1205", "action_type": "evaluate", "department_id": "seleccion"}}
{"event": "agent_status_changed", "data": {"agent_id": "first_line_support", "flow_id": "chat_0447", "status": "running"}}
{"event": "agent_status_changed", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0318", "status": "failed"}}
```

## 6. Restricciones

- Los nombres de campos, agentes y `action_type` deben coincidir exactamente con este documento — no inventes identificadores paralelos.
- No muestres ni dupliques aquí la lógica de aprobación por departamento del pipeline de RFP — este panel solo observa; la aprobación ya vive en el flujo de ese milestone.
- Persiste cada tarea aunque no haya ningún cliente SSE conectado en el momento en que ocurre.
