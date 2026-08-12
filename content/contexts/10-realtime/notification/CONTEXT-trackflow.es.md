# CONTEXT — TrackFlow: Sistemas en Tiempo Real (Parte 1)

> Este documento aplica a la Parte 1 de este proyecto. Da por hecho que ya tienes el sistema multiagente de generación de RFPs funcionando — aquí no se rediseña ese sistema, solo se le agrega notificación en tiempo real.

## 1. Introducción

El ticket de RFP lo abre el equipo de **Miguel Torres**, Commercial Director — son quienes hoy se enteran de una propuesta nueva revisando el dashboard por su cuenta. Son ellos quienes van a ver la notificación en tiempo real que vas a construir en esta parte.

## 2. El Ticket de RFP que Vas a Notificar

Reutiliza exactamente las mismas entidades que ya definiste para el sistema de RFPs:

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `intake_complete`, `drafting`, `under_evaluation`, `waiting_for_approval`, `done`, `discarded`)
- **RFP metadata**: `client_name`, `client_country`, `services_requested`, `monthly_volume`, `deadline`, `budget_range`, `departments_needed`

La notificación en tiempo real debe dispararse en el momento exacto en que un ticket nuevo entra al sistema con `status = analyzing` — es decir, cuando el documento fue clasificado como una RFP válida y el flujo empieza a procesarlo.

## 3. Formato SSE sugerido para `rfp_ticket_created`

SSE usa una línea `event:` con nombre y un cuerpo JSON en `data:` (solo campos del ticket — no un sobre anidado `{"event","data"}`):

```text
event: rfp_ticket_created
data: { "ticket_id": "tkt_0225", "rfp_id": "rfp_0071", "client_name": "Northline Apparel", "client_country": "US", "services_requested": ["warehouse", "lastmile"], "status": "analyzing", "created_at": "2026-07-24T14:32:00Z" }

```

No necesitas incluir el contenido completo del documento ni las secciones por departamento — solo lo suficiente para que quien mire el dashboard sepa qué llegó y decida si necesita su atención ahora.

## 4. Caso Opcional, con Datos Reales de TrackFlow

Si decides implementar el caso opcional del README, aquí tienes dos puntos de partida ya definidos para tu empresa — no necesitas inventar el umbral:

- **Alerta de umbral de negocio**: TrackFlow ya tiene esta regla definida — si el SLA de entrega cae por debajo de 90% en cualquiera de los dos países, se notifica de inmediato a Thomas (CEO) y Ana (Warehouse Operations). Puedes emitir un evento `sla_threshold_alert` cuando tu pipeline de reporting detecte esta condición.
- **Escalamiento de agente**: el equipo de Customer Experience de TrackFlow ya tiene esta regla definida — la detección de sentimiento identifica clientes frustrados antes de que escalen y los asigna automáticamente a un agente senior. Puedes emitir un evento `ticket_escalated_to_senior` con al menos `ticket_id` y el motivo del escalamiento.

## 5. Restricciones

- Los nombres de campos deben coincidir exactamente con los que ya usaste en el sistema de RFPs — no inventes nombres nuevos para las mismas entidades.
- La Parte 2 (chat WebSocket) vive en `10-realtime/communication/` — **no** copies el esquema RFP `Ticket` a ese CONTEXT; reutiliza solo la disciplina de nombres.
