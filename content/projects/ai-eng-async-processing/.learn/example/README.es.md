# Cabina fotográfica — SMS async de confirmación (ejemplo de clase)

> **Para instructores:** No es proyecto del estudiante. Misma columna vertebral que `ai-eng-async-processing`: encolar fuera del ciclo request, worker, backoff exponencial, DLQ, clave idempotencia, estado consultable. Dominio = cabina de evento que envía SMS cuando la foto está lista.

_These instructions are also available in [English](./README.md)._

---

## El reto

API de cabina hoy llama pasarela SMS dentro de `POST /sessions/{id}/notify`. Gateway falla → cliente no recibe "tu foto está lista" y la petición hace timeout. Mover notify a cola; usuario recibe 202 al instante.

### Nota de alcance

Una sesión, un endpoint, proveedor SMS mockeado. Redis + RQ o Celery OK. Sin Flower ni monorepo completo. Alumnado sigue brief completo en `README.md` raíz.

---

## Qué construir

### Cola + worker

- [ ] `POST /sessions/{id}/notify` → 202 + `task_id`
- [ ] Worker envía SMS vía stub `SmsGateway.send(phone, message)`
- [ ] Proceso worker separado de la API

### Resiliencia

- [ ] Máx 3 reintentos, backoff exponencial (p. ej. 2s, 4s, 8s)
- [ ] Tareas fallidas → lista/tabla DLQ con `task_id`, `error`, `attempts`

### Idempotencia

- [ ] Header `Idempotency-Key: session-{id}-notify`
- [ ] Segundo enqueue misma clave → mismo `task_id`, gateway llamado una vez

### Estado

- [ ] `GET /tasks/{task_id}` → `pending` | `in_progress` | `completed` | `failed`, `retry_count`

---

## Verificar juntos

- [ ] Camino feliz: notify → poll → `completed`
- [ ] Stub falla 2 veces y luego OK → `retry_count: 2`
- [ ] Stub siempre falla → DLQ + `failed`
- [ ] POST duplicado misma clave → mock provider `call_count == 1`

---

## Preguntas de discusión

1. ¿Por qué 202 gana a bloquear hasta que responda la pasarela SMS?
2. Si el reintento tuvo éxito en proveedor pero se perdió el ACK, ¿cómo salva la clave de idempotencia?
3. ¿Quién monitoriza DLQ en producción — y qué alerta dispara?
