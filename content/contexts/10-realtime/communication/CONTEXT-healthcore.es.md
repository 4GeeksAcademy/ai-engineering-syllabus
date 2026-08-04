# CONTEXT — HealthCore: Sistemas en Tiempo Real (Partes 1 y 2)

> Este documento aplica a las Partes 1 y 2 de este proyecto. Da por hecho que ya tienes el sistema multiagente de generación de RFPs funcionando — aquí no se rediseña ese sistema, solo se le agrega comunicación en tiempo real.
>
> ⚠️ **Restricción no negociable:** HealthCore opera bajo HIPAA (EE. UU.) y UK GDPR (Reino Unido). Ningún identificador de paciente ni dato de salud protegido (PHI) puede aparecer en ningún evento, payload, log o notificación generada por tu flujo — ni siquiera como ejemplo ilustrativo. Esto aplica a ambas partes de este proyecto.

## 1. Introducción

El ticket de RFP lo abre el equipo de **Tom Callahan**, Revenue Cycle Director — son quienes hoy se enteran de una propuesta nueva revisando el dashboard por su cuenta. Son ellos quienes van a ver la notificación en tiempo real que vas a construir en esta parte.

## 2. El Ticket de RFP que Vas a Notificar

Reutiliza exactamente las mismas entidades que ya definiste para el sistema de RFPs:

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `intake_complete`, `drafting`, `under_evaluation`, `waiting_for_approval`, `done`, `discarded`)
- **RFP metadata**: `client_name`, `client_country` (US/UK), `program_type`, `covered_population`, `deadline`, `budget_range`, `departments_needed` — **nunca** un campo de dato individual de paciente

La notificación en tiempo real debe dispararse en el momento exacto en que un ticket nuevo entra al sistema con `status = analyzing` — es decir, cuando el documento fue clasificado como una RFP válida y el flujo empieza a procesarlo. Estos son contratos institucionales (con empleadores, universidades, aseguradoras), no expedientes de pacientes — el payload no toca PHI en ningún punto de este flujo.

## 3. Payload Sugerido para el Evento `rfp_ticket_created`

```json
{
  "event": "rfp_ticket_created",
  "data": {
    "ticket_id": "tkt_0508",
    "rfp_id": "rfp_0193",
    "client_name": "Westbrook Manufacturing",
    "client_country": "US",
    "program_type": "occupational_health",
    "status": "analyzing",
    "created_at": "2026-07-24T14:32:00Z"
  }
}
```

No necesitas incluir el contenido completo del documento ni las secciones por departamento — solo lo suficiente para que quien vea el dashboard sepa qué llegó y decida si necesita revisarlo ahora.

## 4. Caso Opcional, con Datos Reales de HealthCore

Si decides implementar el caso opcional del README, aquí tienes un punto de partida ya definido para tu empresa — no necesitas inventar el umbral:

- **Alerta de umbral de negocio**: HealthCore ya tiene esta regla definida a nivel ejecutivo — si la tasa de inasistencia (no-show) de una ubicación supera el 25%, o si la tasa de rechazo de facturación sube por encima del 10% en cualquier ubicación, se notifica de inmediato a Sandra (CEO) y al jefe de departamento correspondiente. Puedes emitir un evento `kpi_threshold_alert` cuando tu pipeline de reporting detecte esta condición — el payload solo necesita el identificador de la ubicación, el KPI y el valor, nunca datos de un paciente individual.

Si en cambio prefieres el caso de escalamiento de agente, ten especial cuidado: cualquier evento relacionado con seguimiento de pacientes crónicos debe limitarse a un identificador de caso interno (`case_id`), nunca al nombre del paciente ni a detalles clínicos — evalúa si ese caso es viable sin exponer PHI antes de implementarlo.

## 5. Restricciones

- Los nombres de campos deben coincidir exactamente con los que ya usaste en el sistema de RFPs — no inventes nombres nuevos para las mismas entidades.
- Ningún payload de esta parte puede contener PHI, sin excepción — revisa cada campo antes de emitirlo.

---

## 6. Parte 2 — Chat en Tiempo Real

### 6.1 Qué Agente Vas a Conectar

HealthCore no tiene todavía un agente de chat en tiempo real orientado a pacientes en su hoja de ruta — y por la restricción de PHI, no es el punto de partida más seguro para este ejercicio. En su lugar, vas a exponer por WebSocket el **Compliance assistant** del área de Claire Whitfield: el que responde preguntas del personal sobre qué está permitido bajo HIPAA y UK GDPR. Es una conversación entre personal interno y el agente, nunca entre un paciente y el agente. No cambies la lógica ni las herramientas del agente — solo el canal por el que habla con el usuario.

### 6.2 Entidad de Sesión de Chat

- **ChatSession**: `session_id`, `agent_id` (`compliance_assistant`), `user_id` (el miembro del staff que está chateando — nunca un paciente), `status` (`active`, `interrupted`, `closed`), `created_at`

### 6.3 Eventos Sugeridos sobre el WebSocket

Sigue la misma disciplina de nombres que usaste en la Parte 1 — eventos explícitos, payload estructurado, sin PHI en ningún campo:

```json
{"event": "token_chunk", "data": {"session_id": "chat_0076", "token": "Según", "sequence": 9}}
{"event": "interrupt_requested", "data": {"session_id": "chat_0076", "new_input": "espera, mi pregunta era sobre UK GDPR, no HIPAA"}}
{"event": "generation_completed", "data": {"session_id": "chat_0076", "message_id": "msg_0163"}}
```

### 6.4 Patrón Pub/Sub

Usa un canal por sesión (por ejemplo, `chat.<session_id>`) para que el productor (el agente generando tokens) esté desacoplado de los consumidores (las conexiones WebSocket suscritas). No necesitas Redis para esta entrega — un mecanismo en memoria es aceptable si tu implementación corre en un solo proceso.
