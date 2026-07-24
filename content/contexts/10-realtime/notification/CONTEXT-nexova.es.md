# CONTEXT — Nexova: Sistemas en Tiempo Real (Parte 1)

> Este documento aplica a la Parte 1 de este proyecto. Da por hecho que ya tienes el sistema multiagente de generación de RFPs funcionando — aquí no se rediseña ese sistema, solo se le agrega notificación en tiempo real.

## 1. Introducción

El ticket de RFP lo abre el equipo de **Marcos Ibáñez**, Sales Director — son quienes hoy se enteran de una propuesta nueva revisando el dashboard por su cuenta. Son ellos quienes van a ver la notificación en tiempo real que vas a construir en esta parte.

## 2. El Ticket de RFP que Vas a Notificar

Reutiliza exactamente las mismas entidades que ya definiste para el sistema de RFPs:

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `waiting_for_approval`, `drafting`, `under_evaluation`, `done`, `discarded`)
- **RFP metadata**: `client_name`, `client_hq` (Spain/Miami), `services_requested`, `scope`, `deadline`, `budget_range`, `departments_needed`

La notificación en tiempo real debe dispararse en el momento exacto en que un ticket nuevo entra al sistema con `status = analyzing` — es decir, cuando el documento fue clasificado como una RFP válida y el flujo empieza a procesarlo.

## 3. Payload Sugerido para el Evento `rfp_ticket_created`

```json
{
  "event": "rfp_ticket_created",
  "data": {
    "ticket_id": "tkt_0341",
    "rfp_id": "rfp_0127",
    "client_name": "NubeSoft",
    "client_hq": "Miami",
    "services_requested": ["soporte"],
    "status": "analyzing",
    "created_at": "2026-07-24T14:32:00Z"
  }
}
```

No necesitas incluir el contenido completo del documento ni las secciones por departamento — solo lo suficiente para que quien vea el dashboard sepa qué llegó y decida si necesita revisarlo ahora.

## 4. Caso Opcional, con Datos Reales de Nexova

Si decides implementar el caso opcional del README, aquí tienes dos puntos de partida ya definidos para tu empresa — no necesitas inventar el umbral:

- **Alerta de umbral de negocio**: Nexova ya tiene esta regla definida a nivel ejecutivo — si cualquier KPI cae por debajo de un umbral, se notifica de inmediato a la dirección. Puedes emitir un evento `kpi_threshold_alert` cuando tu pipeline de reporting detecte esta condición, usando el umbral que definas para el KPI que elijas (por ejemplo, el pipeline de ventas).
- **Escalamiento de agente**: el equipo de Soporte al Cliente de Nexova ya tiene esta regla definida — si un ticket queda sin atender por más de X horas, se reasigna y se notifica al supervisor. Puedes emitir un evento `support_ticket_escalated` con al menos `support_ticket_id` y las horas transcurridas sin atención.

## 5. Restricciones

- Los nombres de campos deben coincidir exactamente con los que ya usaste en el sistema de RFPs — no inventes nombres nuevos para las mismas entidades.
- Si más adelante se agrega la Parte 2 (WebSockets) a este proyecto, este mismo documento se extenderá — no dupliques la definición del ticket en otro archivo.
