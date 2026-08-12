# CONTEXT — Brasaland: Sistemas en Tiempo Real (Parte 1)

> Este documento aplica a la Parte 1 de este proyecto. Da por hecho que ya tienes el sistema multiagente de generación de RFPs funcionando — aquí no se rediseña ese sistema, solo se le agrega notificación en tiempo real.

## 1. Introducción

El ticket de RFP lo abre el equipo de **Camila Ospina**, Marketing and Digital Experience — son quienes hoy se enteran de una propuesta nueva revisando el dashboard por su cuenta. Son ellos quienes van a ver la notificación en tiempo real que vas a construir en esta parte.

## 2. El Ticket de RFP que Vas a Notificar

Reutiliza exactamente las mismas entidades que ya definiste para el sistema de RFPs:

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `intake_complete`, `drafting`, `under_evaluation`, `waiting_for_approval`, `done`, `discarded`), `created_at`, `updated_at`
- **RFP metadata**: `client_name`, `location`, `service_type`, `scope`, `deadline`, `budget_range` (opcional), `departments_needed`

La notificación en tiempo real debe dispararse en el momento exacto en que un ticket nuevo entra al sistema con `status = analyzing` — es decir, cuando el documento fue clasificado como una RFP válida y el flujo empieza a procesarlo.

## 3. Formato SSE sugerido para `rfp_ticket_created`

SSE usa una línea `event:` con nombre y un cuerpo JSON en `data:` (solo campos del ticket — no un sobre anidado `{"event","data"}`):

```text
event: rfp_ticket_created
data: { "ticket_id": "tkt_0192", "rfp_id": "rfp_0088", "client_name": "Andes Tech Solutions", "location": "Medellín", "service_type": "recurring_catering", "status": "analyzing", "created_at": "2026-07-24T14:32:00Z" }

```

No necesitas incluir el contenido completo del documento ni las secciones por departamento — solo lo suficiente para que quien mire el dashboard sepa qué llegó y decida si necesita su atención ahora.

## 4. Caso Opcional, con Datos Reales de Brasaland

Si decides implementar el caso opcional del README, aquí tienes dos puntos de partida ya definidos para tu empresa — no necesitas inventar el umbral:

- **Alerta de umbral de negocio**: Brasaland ya tiene esta regla definida — si las ventas de un país caen más de 15% frente a la semana anterior, se notifica de inmediato a Mariana (CEO) y Felipe (Operaciones). Puedes emitir un evento `sales_drop_alert` cuando tu pipeline de reporting detecte esta condición.
- **Alerta por inactividad operativa**: Brasaland también tiene esto definido — si una ubicación no registra ventas durante dos horas en horario de apertura, se notifica automáticamente a Felipe. Puedes emitir un evento `location_inactivity_alert` con al menos `location_id` y las horas transcurridas sin ventas.

## 5. Restricciones

- Los nombres de campos deben coincidir exactamente con los que ya usaste en el sistema de RFPs — no inventes nombres nuevos para las mismas entidades.
- La Parte 2 (chat WebSocket) vive en `10-realtime/communication/` — **no** copies el esquema RFP `Ticket` a ese CONTEXT; reutiliza solo la disciplina de nombres.
