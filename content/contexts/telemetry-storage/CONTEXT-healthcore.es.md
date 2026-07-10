# CONTEXT — HealthCore · Telemetría Fase 3: Almacenamiento en el Backend

## Tu empresa

**HealthCore** es una empresa de servicios sanitarios ambulatorios con 12 clínicas en EE. UU. y Reino Unido. Formas parte de **HealthCore Digital**. El `TelemetryService` del backoffice ya está enviando batches de eventos al stub. Hoy reemplazas ese stub por la capa de almacenamiento real.

Esta es la implementación de almacenamiento de mayor riesgo del programa. Cada fila que escribas en `telemetry_events` debe estar libre de información identificable de pacientes — HIPAA en EE. UU. y UK GDPR en Reino Unido aplican desde el momento en que el dato se persiste, no solo cuando se transmite.

---

## Qué va en `tags` por cada evento

La columna `tags` JSONB almacena las propiedades específicas del evento de tu allowlist. Esto es lo que Supabase recibirá y guardará para cada evento de HealthCore.

| `event_type` | Contenido de `tags` |
|---|---|
| `supply_delivery_created` | `{ "supply_id": 3, "quantity": 500, "clinic_id": 1, "country": "US" }` |
| `supply_consumption_created` | `{ "supply_id": 3, "quantity": 20, "consumption_type": "clinical_use", "clinic_id": 10, "country": "UK" }` |
| `supply_consumption_failed` | `{ "error_code": "INSUFFICIENT_STOCK", "supply_id": 3, "clinic_id": 5, "country": "US" }` |
| `supply_list_viewed` | `{ "clinic_id": 1, "country": "US", "item_count": 67 }` |
| `user_login_succeeded` | `{ "country": "US" }` |
| `user_login_failed` | `{ "reason": "session_expired" }` |
| `session_expired` | `{}` |

Las columnas fijas (`event_type`, `timestamp`, `service`, `level`) se populan desde los campos del envelope. La capa de almacenamiento establece `service` en `backoffice` al persistir — no se envía en el envelope de captura. La columna `value` puede usarse para `quantity` en eventos de suministros si quieres que sea consultable sin parsear JSONB — documenta tu decisión.

---

## Bulk insert — Notas específicas de HealthCore

Las 12 clínicas de HealthCore en dos jurisdicciones implican que los eventos llegan de múltiples zonas horarias simultáneamente. El turno de mañana en Texas y Georgia se solapa con la mitad del día de las clínicas del Reino Unido. Tu bulk insert debe manejar batches con países mixtos — eventos con `country: "US"` y `country: "UK"` pueden llegar en el mismo batch y deben almacenarse de forma idéntica.

**Ejemplo de rechazo para HealthCore:** llega un batch de 5 eventos. El evento 2 es un `supply_consumption_created` sin `country` en `tags` — falla la validación. Los eventos 1, 3, 4 y 5 son válidos y se insertan. La respuesta es `{ "received": 5, "stored": 4, "rejected": 1 }`. Sin `country`, Claire Whitfield (CCO) no puede usar ese evento en ningún informe de cumplimiento — se rechaza correctamente.

---

## Checklist de verificación para HealthCore

Después de reemplazar el stub, verifica en el editor de tablas de Supabase:

- [ ] Todos los eventos tienen `country` en `tags` (`"US"` o `"UK"`) — Claire Whitfield (CCO) lo exige para cada informe de cumplimiento
- [ ] Todos los eventos de entregas/consumos de suministros tienen `clinic_id` en `tags` (entero 1–12) — el Dr. Reid (Director de Operaciones Clínicas) necesita visibilidad por clínica
- [ ] Las filas `supply_consumption_created` tienen `consumption_type` en `tags` — necesario para el análisis clínico vs. merma
- [ ] **Ninguna fila contiene nombres de pacientes, IDs de pacientes, fechas de nacimiento, diagnósticos ni ningún dato vinculado a un paciente en `tags` ni en ninguna otra columna** — este es un límite infranqueable bajo HIPAA y UK GDPR; si existe algún dato de este tipo, la tabla debe considerarse comprometida y los datos purgados
- [ ] Los valores de `userId` almacenados mediante el envelope son UUIDs opacos de TinyDB — nunca nombres, emails ni títulos de rol clínico del personal

---

_HealthCore Digital — Documento interno para el AI Engineering Track de 4Geeks Academy_
