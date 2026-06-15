# Biblioteca Maple Street — Almacenamiento de telemetría (Ejemplo de clase)

> **Para instructores:** Escenario paralelo en aula para `ai-eng-telemetry-storage`. Misma columna vertebral (Supabase `telemetry_events`, bulk insert, validación por evento, batch parcial, frontend sin cambios), dominio distinto. Los estudiantes siguen el enunciado completo del monorepo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Biblioteca Maple Street** ya tiene `desk-app` enviando eventos en batch a un stub FastAPI. Hoy: capa de almacenamiento real. La app de mostrador **no** cambia.

### Nota de alcance

| Proyecto evaluable (`ai-eng-telemetry-storage`) | Este ejemplo de clase                              |
| ----------------------------------------------- | -------------------------------------------------- |
| Monorepo completo + `TelemetryEvent` Fase 2     | Mini `library-api` + servicio de captura existente |
| Tabla 8 columnas + 3 índices                    | Mismo esquema, dataset pequeño                     |
| Prueba E2E inventario                           | 2 eventos de préstamo en demo                      |
| PR al fork del estudiante                       | Proyecto Supabase local                            |

---

## Qué construir

### 1. Tabla Supabase `telemetry_events`

- [ ] Crear tabla con columnas: `id`, `timestamp`, `service`, `event_type`, `level`, `value`, `message`, `tags`
- [ ] Índices en `timestamp`, `event_type`, GIN en `tags`
- [ ] Sin lógica UPDATE/DELETE

### 2. Sustituir endpoint stub

- [ ] `POST /telemetry/events` — misma ruta y body que el stub
- [ ] Validar cada evento con el modelo `TelemetryEvent` existente (sin modificar)
- [ ] Bulk insert de filas válidas en **una** transacción
- [ ] Devolver `{ "received", "stored", "rejected" }`
- [ ] Eventos inválidos rechazados individualmente; válidos del mismo lote se guardan

### 3. Verificar

- [ ] Préstamo en `desk-app` → filas en Supabase
- [ ] `curl` con batch mixto válido/inválido → conteos correctos
- [ ] Confirmar cero cambios bajo `desk-app/`

---

## Verificar juntos

- [ ] `SELECT count(*) FROM telemetry_events` sube tras actividad en mostrador
- [ ] JSONB `tags` contiene propiedades del préstamo (`loanId`, `bookId`)
- [ ] Batch mixto: `stored + rejected === received`
- [ ] `git diff` del frontend vacío

---

## Preguntas de discusión

1. ¿Por qué el bulk insert es crítico cuando llegan batches cada 10 segundos de muchos usuarios?
2. ¿Por qué un evento inválido no debe hacer rollback de todo el batch?
3. ¿Qué se rompe si el frontend empieza a parsear `{ stored, rejected }` del body?
