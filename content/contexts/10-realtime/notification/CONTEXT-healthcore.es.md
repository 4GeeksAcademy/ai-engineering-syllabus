# CONTEXT — HealthCore: Sistemas en Tiempo Real (Parte 1)

> Este documento aplica a la Parte 1 de este proyecto. Da por hecho que ya tienes el sistema multiagente de generación de RFPs funcionando — aquí no se rediseña ese sistema, solo se le agrega notificación en tiempo real.
>
> ⚠️ **Restricción no negociable:** HealthCore opera bajo HIPAA (EE. UU.) y UK GDPR (Reino Unido). Ningún identificador de paciente ni dato de salud protegido (PHI) puede aparecer en ningún evento, payload, log o notificación generada por tu flujo — ni siquiera como ejemplo ilustrativo. Esto aplica también a esta parte del proyecto.

## 1. Introducción

El ticket de RFP lo abre el equipo de **Tom Callahan**, Revenue Cycle Director — son quienes hoy se enteran de una propuesta nueva revisando el dashboard por su cuenta. Son ellos quienes van a ver la notificación en tiempo real que vas a construir en esta parte.

## 2. El Ticket de RFP que Vas a Notificar

Reutiliza exactamente las mismas entidades que ya definiste para el sistema de RFPs:

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `intake_complete`, `drafting`, `under_evaluation`, `waiting_for_approval`, `done`, `discarded`)
- **RFP metadata**: `client_name`, `client_country` (US/UK), `program_type`, `covered_population`, `deadline`, `budget_range`, `departments_needed` — **nunca** un campo de dato individual de paciente

La notificación en tiempo real debe dispararse en el momento exacto en que un ticket nuevo entra al sistema con `status = analyzing` — es decir, cuando el documento fue clasificado como una RFP válida y el flujo empieza a procesarlo. Estos son contratos institucionales (con empleadores, universidades, aseguradoras), no expedientes de pacientes — el payload no toca PHI en ningún punto de este flujo.

## 3. Formato SSE sugerido para `rfp_ticket_created`

SSE usa una línea `event:` con nombre y un cuerpo JSON en `data:` (solo campos del ticket — no un sobre anidado `{"event","data"}`):

```text
event: rfp_ticket_created
data: { "ticket_id": "tkt_0508", "rfp_id": "rfp_0193", "client_name": "Westbrook Manufacturing", "client_country": "US", "program_type": "occupational_health", "status": "analyzing", "created_at": "2026-07-24T14:32:00Z" }

```

No necesitas incluir el contenido completo del documento ni las secciones por departamento — solo lo suficiente para que quien mire el dashboard sepa qué llegó y decida si necesita su atención ahora.

## 4. Caso Opcional, con Datos Reales de HealthCore

Si decides implementar el caso opcional del README, aquí tienes un punto de partida ya definido para tu empresa — no necesitas inventar el umbral:

- **Alerta de umbral de negocio**: HealthCore ya tiene esta regla definida a nivel ejecutivo — si la tasa de inasistencia (no-show) de una ubicación supera el 25%, o si la tasa de rechazo de facturación sube por encima del 10% en cualquier ubicación, se notifica de inmediato a Sandra (CEO) y al jefe de departamento correspondiente. Puedes emitir un evento `kpi_threshold_alert` cuando tu pipeline de reporting detecte esta condición — el payload solo necesita el identificador de la ubicación, el KPI y el valor, nunca datos de un paciente individual.

Si en cambio prefieres el caso de escalamiento de agente, ten especial cuidado: cualquier evento relacionado con seguimiento de pacientes crónicos debe limitarse a un identificador de caso interno (`case_id`), nunca al nombre del paciente ni a detalles clínicos — evalúa si ese caso es viable sin exponer PHI antes de implementarlo.

## 5. Restricciones

- Los nombres de campos deben coincidir exactamente con los que ya usaste en el sistema de RFPs — no inventes nombres nuevos para las mismas entidades.
- Ningún payload de esta parte puede contener PHI, sin excepción — revisa cada campo antes de emitirlo.
- La Parte 2 (chat WebSocket) vive en `10-realtime/communication/` — **no** copies el esquema RFP `Ticket` a ese CONTEXT; reutiliza solo la disciplina de nombres.
