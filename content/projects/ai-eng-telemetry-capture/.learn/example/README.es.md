# Biblioteca Maple Street — Captura de telemetría en frontend (Ejemplo de clase)

> **Para instructores:** Escenario paralelo en aula para `ai-eng-telemetry-capture`. Misma columna vertebral (stub FastAPI, `TelemetryService`, cola/batch/sendBeacon/retry, `track()` única, endpoint por env, métricas obligatorias + piso técnico), dominio distinto. Los estudiantes siguen el enunciado completo del monorepo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Biblioteca Maple Street** tiene una app de mostrador (`desk-app`, Next.js) y una API pequeña (`library-api`, FastAPI). Los bibliotecarios registran préstamos y devoluciones; el CTO quiere eventos de uso **antes** de construir el almacenamiento analítico.

En una sesión: receptor stub + servicio de captura en frontend + instrumentar métricas **obligatorias** del mostrador más un piso técnico mínimo.

### Nota de alcance

| Proyecto evaluable (`ai-eng-telemetry-capture`)                                  | Este ejemplo de clase                       |
| -------------------------------------------------------------------------------- | ------------------------------------------- |
| CONTEXT de empresa + esquemas Fase 1                                             | Contrato mini de biblioteca (abajo)         |
| Todas las métricas obligatorias del CONTEXT + piso técnico + catálogo priorizado | 2 eventos obligatorios + 1 técnico + 1 auth |
| Batch 10s / 20 eventos                                                           | Batch 5s / 10 eventos (ritmo demo)          |
| PR al fork del estudiante                                                        | Solo demo local                             |

**Contrato mini de eventos (usar como `event-schemas.json` en clase):**

| Evento                    | Clase                    | Allowlist de propiedades                            |
| ------------------------- | ------------------------ | --------------------------------------------------- |
| `book_checkout_completed` | obligatorio              | `loanId`, `bookId`                                  |
| `book_checkout_failed`    | obligatorio              | `reason`, `bookId`                                  |
| `page_viewed`             | piso técnico             | `route`                                             |
| `login_failed`            | identificado / adicional | `reason` (`invalid_credentials` \| `network_error`) |

---

## Qué construir

### 1. Stub FastAPI (`library-api`)

- [ ] `POST /telemetry/events` acepta `{ "events": [...] }`
- [ ] Modelo Pydantic con `eventId`, `timestamp`, `sessionId`, `userId`, `event_type`, `schemaVersion`, `requestId`, `properties`
- [ ] Log de cantidad + `event_type`; devuelve `{ "received": N }`
- [ ] Lee `TELEMETRY_ENDPOINT` del env (puede no usarse aún)

### 2. `TelemetryService` (`desk-app/src/services/telemetry.ts`)

- [ ] Cola en memoria; flush cada **5s** o **10 eventos**
- [ ] `track(eventType, properties)` — única API pública
- [ ] Añade automáticamente `eventId`, `sessionId`, `userId`, `timestamp`, `schemaVersion`, `requestId`
- [ ] `visibilitychange` → `sendBeacon`
- [ ] 3 reintentos con backoff exponencial, luego descartar lote
- [ ] URL desde `NEXT_PUBLIC_TELEMETRY_ENDPOINT`

### 3. Instrumentación

- [ ] Préstamo exitoso → `track("book_checkout_completed", { loanId, bookId })`
- [ ] Error de validación/API → `track("book_checkout_failed", { reason, bookId })`
- [ ] Entrada a ruta principal → `track("page_viewed", { route })`
- [ ] En hook de auth → `track("login_failed", { reason })` — nunca email/contraseña

---

## Verificar juntos

- [ ] Pestaña Network muestra **un batch** con varios eventos tras ráfaga de actividad
- [ ] Stub devuelve `200` y `{ "received": N }`
- [ ] Ambas métricas obligatorias instrumentadas
- [ ] Sin `fetch` de telemetría fuera de `telemetry.ts`
- [ ] `properties` de login fallido solo con `reason` — sin credenciales

---

## Preguntas de discusión

1. ¿Por qué batch en lugar de una llamada HTTP por `track()`?
2. ¿Cuándo importa más `sendBeacon` que `fetch`?
3. ¿Qué se rompe si `NEXT_PUBLIC_TELEMETRY_ENDPOINT` está hardcodeado?
