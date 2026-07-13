# Biblioteca Maple Street — Almacenamiento de telemetría (Ejemplo de clase)

> **Para instructores:** Escenario paralelo en aula para `ai-eng-telemetry-storage`. Misma columna vertebral (Supabase `telemetry_events`, bulk insert, `model_validate` por evento, batch parcial, frontend sin cambios), dominio distinto. Los estudiantes siguen el enunciado completo del monorepo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Biblioteca Maple Street** ya tiene `desk-app` enviando eventos en batch a un stub FastAPI. Hoy: capa de almacenamiento real. La app de mostrador **no** cambia.

### Nota de alcance

| Proyecto evaluable (`ai-eng-telemetry-storage`) | Este ejemplo de clase                              |
| ----------------------------------------------- | -------------------------------------------------- |
| CONTEXT de empresa + mapeo `tags` Fase 1        | Contrato mini de biblioteca del demo de captura    |
| Monorepo completo + `TelemetryEvent` Fase 2     | Mini `library-api` + servicio de captura existente |
| Tabla 8 columnas + 3 índices                    | Mismo esquema, dataset pequeño                     |
| E2E inventario + técnico                        | 1 préstamo + 1 `login_failed` / `page_viewed`      |
| PR al fork del estudiante                       | Proyecto Supabase local                            |

---

## Qué construir

### 1. Tabla Supabase `telemetry_events`

- [ ] Crear tabla con columnas: `id`, `timestamp`, `service`, `event_type`, `level`, `value`, `message`, `tags`
- [ ] Índices en `timestamp`, `event_type`, GIN en `tags`
- [ ] Sin lógica UPDATE/DELETE

### 2. Sustituir endpoint stub

- [ ] `POST /telemetry/events` — misma ruta; aceptar `{ "events": [...] }` de forma laxa (**no** tipar `events: list[TelemetryEvent]` en el body)
- [ ] `TelemetryEvent.model_validate(...)` por evento en un loop (sin modificar el modelo)
- [ ] Bulk insert de filas válidas en **una** transacción
- [ ] Devolver `{ "received", "stored", "rejected" }`
- [ ] Eventos inválidos rechazados individualmente; válidos del mismo lote se guardan

### 3. Verificar

- [ ] Préstamo en `desk-app` → fila de negocio en Supabase
- [ ] Login fallido o page view → fila técnica/auth
- [ ] `curl` con batch mixto válido/inválido → conteos correctos
- [ ] Confirmar cero cambios bajo `desk-app/`

---

## Verificar juntos

- [ ] `SELECT count(*) FROM telemetry_events` sube tras actividad en mostrador
- [ ] JSONB `tags` contiene `properties` del envelope desde la allowlist (`loanId`, `bookId`)
- [ ] Al menos un `event_type` de negocio y uno técnico/auth
- [ ] Batch mixto: `stored + rejected === received`
- [ ] `git diff` del frontend vacío

---

## Preguntas de discusión

1. ¿Por qué el bulk insert es crítico cuando llegan batches cada 10 segundos de muchos usuarios?
2. ¿Por qué un evento inválido no debe hacer rollback de todo el batch?
3. ¿Qué se rompe si el frontend empieza a parsear `{ stored, rejected }` del body?
