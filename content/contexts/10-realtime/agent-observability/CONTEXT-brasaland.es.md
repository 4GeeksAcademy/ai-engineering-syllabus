# CONTEXT — Brasaland: Observabilidad de Agentes (Parte 1)

> Este documento cubre solo la Parte 1. La Parte 2 (control) reutiliza las mismas entidades e identificadores de agente definidos aquí.

## 1. Introducción

El ticket viene de **Nicolás Park**, CTO. Brasaland Digital tiene hoy dos agentes corriendo en producción, y nadie fuera del equipo de ingeniería puede saber qué está haciendo cualquiera de los dos en un momento dado: el **Manager support agent** que el equipo de Operaciones de Felipe Guerrero usa a diario, y el **pipeline multiagente de propuestas** que procesa RFPs corporativos (contratos de catering, co-branding, concesiones de eventos) para el equipo de Marketing de Camila Ospina. Nicolás quiere un panel que su equipo pueda abrir cuando algo se sienta lento o atascado, sin tener que entrar por SSH a un servidor y buscar en logs.

## 2. Agentes que Vas a Observar

| `agent_id` | Nombre | Tipo | Dueño / Área | Participa en |
|---|---|---|---|---|
| `manager_support` | Manager support agent | Agente único, conversacional | Felipe Guerrero — Operaciones | flujos `chat_session` |
| `rfp_pipeline` | Pipeline de propuestas corporativas | Multiagente (orquestador, generadores, evaluadores, sintetizador) | Camila Ospina — Marketing | flujos `rfp_workflow` |

No cambies la lógica interna de ninguno de los dos agentes — solo estás instrumentando los puntos donde ya actúan, para emitir y persistir eventos.

## 3. Tipos de Flujo y Taxonomía de `action_type`

| `flow_type` | Descripción | Secuencia típica de `action_type` |
|---|---|---|
| `chat_session` | Una conversación entre un manager de local y `manager_support` | `query` (recupera contexto relevante) → `tool_call` (si consulta datos de un local) → `deliver` (respuesta final) |
| `rfp_workflow` | Un RFP corporativo pasando por intake, redacción y evaluación | `query` (clasifica/extrae del PDF) → `tool_call` (consulta datos de departamento) → `draft_start` / `write` (sección de departamento redactada) → `evaluate` (paso del evaluador) → `deliver` (el sintetizador entrega el borrador consolidado) |

Usa los valores de `department_id` ya definidos para el pipeline de RFP de Brasaland — `marketing`, `operaciones`, `procurement`, `training` — como parte del payload de la tarea cuando un paso pertenece al generador o evaluador de un departamento específico.

## 4. Campos de Entidad Específicos de Brasaland

- **Agent.needs_intervention** debe pasar a `true` automáticamente cuando: un `chat_session` lleva más de 20 segundos en `query`/`tool_call` sin un `deliver`, o una tarea de `rfp_workflow` pasó por `evaluate` más veces que el límite de reintentos configurado sin producir una evaluación aprobada.
- **Flow.triggered_by**: para `chat_session`, el mensaje del manager de local; para `rfp_workflow`, el registro del ticket de RFP (reutiliza el mismo `ticket_id` que tu pipeline ya genera).
- Los campos de moneda y ubicación (`COP`/`USD`, Colombia/Florida) no forman parte de los payloads de este milestone — no los agregues salvo que una tarea realmente los necesite como contexto.

## 5. Eventos SSE Sugeridos

```json
{"event": "agent_step", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0142", "task_id": "task_0891", "action_type": "draft_start", "department_id": "marketing"}}
{"event": "agent_status_changed", "data": {"agent_id": "manager_support", "flow_id": "chat_0231", "status": "running"}}
{"event": "agent_status_changed", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0142", "status": "waiting_for_human"}}
```

## 6. Restricciones

- Los nombres de campos, agentes y `action_type` deben coincidir exactamente con este documento — no inventes identificadores paralelos.
- No muestres ni dupliques aquí la lógica de aprobación por departamento del pipeline de RFP — este panel solo observa; la aprobación ya vive en el flujo de ese milestone.
- Persiste cada tarea aunque no haya ningún cliente SSE conectado en el momento en que ocurre.
