# Harbor Desk — Tablero de Tickets en Vivo (Ejemplo de clase)

> **Para instructores:** Escenario paralelo de aula para `ai-eng-milestone-real-time-notification`. Misma columna vertebral (evento SSE nombrado, payload estructurado, keep-alive, `fetch` + `ReadableStream`, reconexión con backoff progresivo). Dominio distinto a los agentes CONTEXT de empresa. El alumnado sigue el brief completo del `README.md` en la raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Harbor Desk** es el tablero de operaciones de un puerto deportivo. Las reservas de amarres y los tickets de mantenimiento ya se crean con una API HTTP mínima — pero la pantalla de pared solo se actualiza cuando alguien pulsa refrescar. Demo de esta noche: cuando se registra un **ticket de mantenimiento** nuevo, cada tablero abierto empuja una notificación en vivo sin recargar todo. Si el Wi‑Fi parpadea, el tablero se reconecta solo.

### Nota de alcance

| Proyecto evaluado (`ai-eng-milestone-real-time-notification`)    | Este ejemplo de clase                                     |
| ---------------------------------------------------------------- | --------------------------------------------------------- |
| Monorepo de empresa + ticket RFP del CONTEXT                     | Solo tablero marina Harbor Desk                           |
| Enganchar al path de registro RFP existente                      | Stub `POST /tickets` que publica el evento                |
| Refactor completo del dashboard de empresa                       | Una sola página HTML/JS de tablero                        |
| Fidelidad de campos CONTEXT (cliente, location, service_type, …) | Campos demo fijos: `ticket_id`, `slip`, `issue`, `status` |
| PR de empresa + preguntas de diseño                              | Demo en vivo + 2 tests automatizados                      |

---

## Columna vertebral (debe cubrirse en vivo)

1. **Publicar al crear** — registrar un ticket emite un evento (sin cron de polling)
2. **Evento SSE nombrado** — `event: maintenance_ticket_created` (no `message` genérico)
3. **Payload JSON estructurado** — al menos id + estado inicial
4. **Keep-alive** — frames de comentario para que el stream no se cierre
5. **Cliente = `fetch` + `ReadableStream`** — parsear frames en un bucle
6. **Reconexión con backoff** — caer la red → reconectar sin toasts duplicados para el mismo id
7. **Sin modelo/agente** — solo capa de comunicación

---

## Payload semilla (indicativo)

```json
{
  "ticket_id": "mnt_0042",
  "slip": "B-17",
  "issue": "pump_out_clogged",
  "status": "open",
  "created_at": "2026-07-24T18:05:00Z"
}
```

Frame en el cable:

```text
event: maintenance_ticket_created
data: {"ticket_id":"mnt_0042","slip":"B-17","issue":"pump_out_clogged","status":"open","created_at":"2026-07-24T18:05:00Z"}
```

---

## Qué construir

### 1. Backend

- [ ] `POST /tickets` crea un ticket con `status: open` y publica a un bus en proceso
- [ ] `GET /events/stream` devuelve `text/event-stream` con eventos nombrados + keep-alive
- [ ] Test unitario: el payload publicado incluye `ticket_id` y `status`

### 2. Tablero frontend

- [ ] Abrir el stream con `fetch` + `ReadableStream`
- [ ] Mostrar card/toast visualmente distinto cuando llega `maintenance_ticket_created`
- [ ] Al desconectar: reconexión con backoff progresivo; saltar `ticket_id`s ya vistos

### 3. Guion de demo (en vivo)

1. Abrir dos pestañas del tablero
2. `POST` de un ticket nuevo → ambas pestañas muestran la notificación
3. Cortar la red un momento → la reconexión reanuda; el mismo ticket no hace toast dos veces

---

## Fuera de alcance del ejemplo

- WebSockets / chat bidireccional (Parte 2)
- Agentes LLM, RAG o pipelines de RFP
- Empresas del CONTEXT (Brasaland, HealthCore, …)
