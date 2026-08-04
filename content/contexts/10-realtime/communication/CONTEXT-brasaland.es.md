# CONTEXT — Brasaland: Sistemas en Tiempo Real (Partes 1 y 2)

> Este documento aplica a las Partes 1 y 2 de este proyecto. Da por hecho que ya tienes el sistema multiagente de generación de RFPs funcionando — aquí no se rediseña ese sistema, solo se le agrega comunicación en tiempo real.

## 1. Introducción

El ticket de RFP lo abre el equipo de **Camila Ospina**, Marketing and Digital Experience — son quienes hoy se enteran de una propuesta nueva revisando el dashboard por su cuenta. Son ellos quienes van a ver la notificación en tiempo real que vas a construir en esta parte.

## 2. El Ticket de RFP que Vas a Notificar

Reutiliza exactamente las mismas entidades que ya definiste para el sistema de RFPs:

- **Ticket**: `ticket_id`, `rfp_id`, `status` (`analyzing`, `intake_complete`, `drafting`, `under_evaluation`, `waiting_for_approval`, `done`, `discarded`), `created_at`, `updated_at`
- **RFP metadata**: `client_name`, `location`, `service_type`, `scope`, `deadline`, `budget_range` (opcional), `departments_needed`

La notificación en tiempo real debe dispararse en el momento exacto en que un ticket nuevo entra al sistema con `status = analyzing` — es decir, cuando el documento fue clasificado como una RFP válida y el flujo empieza a procesarlo.

## 3. Payload Sugerido para el Evento `rfp_ticket_created`

```json
{
  "event": "rfp_ticket_created",
  "data": {
    "ticket_id": "tkt_0192",
    "rfp_id": "rfp_0088",
    "client_name": "Andes Tech Solutions",
    "location": "Medellín",
    "service_type": "recurring_catering",
    "status": "analyzing",
    "created_at": "2026-07-24T14:32:00Z"
  }
}
```

No necesitas incluir el contenido completo del documento ni las secciones por departamento — solo lo suficiente para que quien vea el dashboard sepa qué llegó y decida si necesita revisarlo ahora.

## 4. Caso Opcional, con Datos Reales de Brasaland

Si decides implementar el caso opcional del README, aquí tienes dos puntos de partida ya definidos para tu empresa — no necesitas inventar el umbral:

- **Alerta de umbral de negocio**: Brasaland ya tiene esta regla definida — si las ventas de un país caen más de 15% frente a la semana anterior, se notifica de inmediato a Mariana (CEO) y Felipe (Operaciones). Puedes emitir un evento `sales_drop_alert` cuando tu pipeline de reporting detecte esta condición.
- **Alerta por inactividad operativa**: Brasaland también tiene esto definido — si una ubicación no registra ventas durante dos horas en horario de apertura, se notifica automáticamente a Felipe. Puedes emitir un evento `location_inactivity_alert` con al menos `location_id` y las horas transcurridas sin ventas.

## 5. Restricciones

- Los nombres de campos deben coincidir exactamente con los que ya usaste en el sistema de RFPs — no inventes nombres nuevos para las mismas entidades.

---

## 6. Parte 2 — Chat en Tiempo Real

### 6.1 Qué Agente Vas a Conectar

El agente que vas a exponer por WebSocket es el **Manager support agent**: el que responde preguntas operativas frecuentes de los encargados de local en el idioma base seleccionado. No cambies su lógica ni sus herramientas — solo el canal por el que habla con el usuario.

### 6.2 Entidad de Sesión de Chat

- **ChatSession**: `session_id`, `agent_id` (`manager_support`), `user_id` (el encargado de local que está chateando), `location_id`, `status` (`active`, `interrupted`, `closed`), `created_at`

### 6.3 Eventos Sugeridos sobre el WebSocket

Sigue la misma disciplina de nombres que usaste en la Parte 1 — eventos explícitos, payload estructurado:

```json
{"event": "token_chunk", "data": {"session_id": "chat_0044", "token": "Para", "sequence": 12}}
{"event": "interrupt_requested", "data": {"session_id": "chat_0044", "new_input": "espera, pregunté por el local de Miami"}}
{"event": "generation_completed", "data": {"session_id": "chat_0044", "message_id": "msg_0091"}}
```

### 6.4 Patrón Pub/Sub

Usa un canal por sesión (por ejemplo, `chat.<session_id>`) para que el productor (el agente generando tokens) esté desacoplado de los consumidores (las conexiones WebSocket suscritas). No necesitas Redis para esta entrega — un mecanismo en memoria es aceptable si tu implementación corre en un solo proceso.
