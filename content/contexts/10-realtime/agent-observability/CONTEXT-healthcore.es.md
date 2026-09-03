# CONTEXT — HealthCore: Observabilidad de Agentes (Parte 1)

> Este documento cubre solo la Parte 1. La Parte 2 (control) reutiliza las mismas entidades e identificadores de agente definidos aquí.
>
> ⚠️ **Restricción no negociable:** HealthCore opera bajo HIPAA (EE. UU.) y UK GDPR (Reino Unido). Ningún identificador de paciente ni Información de Salud Protegida (PHI) puede aparecer en ningún evento, payload, log o registro de tarea persistido por tu flujo — ni siquiera como ejemplo ilustrativo. Esto aplica a cada uno de los campos descritos abajo.

## 1. Introducción

El ticket viene de **James Osei**, CTO. HealthCore Digital tiene hoy dos agentes en producción sin ninguna forma compartida de revisarlos: el **Compliance assistant** en el que se apoya el equipo de Claire Whitfield para responder preguntas del personal sobre HIPAA y UK GDPR, y el **pipeline multiagente de propuestas** que procesa RFPs institucionales (contratos de salud ocupacional, bienestar corporativo, alianzas de referidos) para el equipo de Revenue Cycle de Tom Callahan. James quiere que su equipo vea, de un vistazo, si alguno de los dos agentes está sano — sin que ningún dato de paciente toque jamás este panel.

## 2. Agentes que Vas a Observar

| `agent_id` | Nombre | Tipo | Dueño / Área | Participa en |
|---|---|---|---|---|
| `compliance_assistant` | Compliance assistant | Agente único, conversacional | Claire Whitfield — Compliance | flujos `chat_session` |
| `rfp_pipeline` | Pipeline de propuestas institucionales | Multiagente (orquestador, generadores, evaluadores, sintetizador) | Tom Callahan — Revenue Cycle | flujos `rfp_workflow` |

No cambies la lógica interna de ninguno de los dos agentes — solo estás instrumentando los puntos donde ya actúan, para emitir y persistir eventos.

## 3. Tipos de Flujo y Taxonomía de `action_type`

| `flow_type` | Descripción | Secuencia típica de `action_type` |
|---|---|---|
| `chat_session` | Una conversación entre personal de HealthCore y `compliance_assistant` | `query` (recupera contexto de políticas relevantes) → `tool_call` (si consulta un documento de política) → `deliver` (respuesta final) |
| `rfp_workflow` | Un RFP institucional pasando por intake, redacción y evaluación | `query` (clasifica/extrae del PDF) → `tool_call` (consulta datos de departamento) → `draft_start` / `write` (sección de departamento redactada) → `evaluate` (paso del evaluador, incluyendo el chequeo obligatorio de PHI) → `deliver` (el sintetizador entrega el borrador consolidado) |

Usa los valores de `department_id` ya definidos para el pipeline de RFP de HealthCore — `revenue`, `clinical`, `compliance` — como parte del payload de la tarea cuando un paso pertenece al generador o evaluador de un departamento específico.

## 4. Campos de Entidad Específicos de HealthCore

- **Agent.needs_intervention** debe pasar a `true` automáticamente cuando: un `chat_session` lleva más de 20 segundos en `query`/`tool_call` sin un `deliver`, una tarea de `rfp_workflow` pasó por `evaluate` más veces que el límite de reintentos configurado, **o** el evaluador de `compliance` marca `contains_phi: true` en alguna sección — este último caso es siempre de prioridad alta.
- **Flow.triggered_by**: para `chat_session`, el mensaje entrante del personal (nunca un paciente); para `rfp_workflow`, el registro del ticket de RFP (reutiliza el mismo `ticket_id` que tu pipeline ya genera).
- El usuario de `chat_session` es siempre personal interno de HealthCore, nunca un paciente — esta restricción viene del precedente de la Parte 2 anterior y también aplica aquí.

## 5. Eventos SSE Sugeridos

```json
{"event": "agent_step", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0710", "task_id": "task_3112", "action_type": "evaluate", "department_id": "compliance"}}
{"event": "agent_status_changed", "data": {"agent_id": "compliance_assistant", "flow_id": "chat_0812", "status": "running"}}
{"event": "agent_status_changed", "data": {"agent_id": "rfp_pipeline", "flow_id": "flow_0710", "status": "waiting_for_human"}}
```

Ningún campo de ningún evento puede contener jamás un nombre de paciente, diagnóstico u otro identificador de paciente — revisa cada payload antes de emitirlo o persistirlo.

## 6. Restricciones

- Los nombres de campos, agentes y `action_type` deben coincidir exactamente con este documento — no inventes identificadores paralelos.
- No muestres ni dupliques aquí la lógica de aprobación por departamento del pipeline de RFP — este panel solo observa; la aprobación ya vive en el flujo de ese milestone, y el chequeo de PHI de Compliance sigue siendo obligatorio ahí sin importar lo que muestre este panel.
- Persiste cada tarea aunque no haya ningún cliente SSE conectado en el momento en que ocurre, sujeto a la restricción de PHI anterior.
