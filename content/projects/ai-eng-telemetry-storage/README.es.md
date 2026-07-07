# Telemetría de la compañía – Almacenamiento

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Necesitas el `TelemetryService` del frontend funcionando y enviando batches al stub del proyecto anterior. Si los eventos no llegan al stub con respuesta 200, resuélvelo antes de continuar — hoy construyes el destino real de esos eventos.

Tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** explica qué campos del envelope y dimensiones de `tags` importan para el análisis de tu empresa — confirma que los campos opcionales guardados en `tags` coinciden con lo documentado en `telemetry-plan.md`.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Los eventos fluyen desde el frontend. El stub los recibe y los descarta. Hoy construyes lo que el stub prometía: el sistema que los guarda de verdad.

El entregable es un único cambio en el backend — pero un cambio que lo transforma todo: el stub se convierte en un endpoint real que valida cada evento contra el contrato de esquemas de la Fase 1, persiste los válidos en Supabase en una sola operación y reporta exactamente qué se guardó y qué se rechazó. El frontend no cambia ni una línea.

> Tu tech lead te ha enviado este mensaje:
>
> > "El stub ha cumplido su función — sé que los eventos llegan con el formato correcto. Ahora necesito que los guardes.
> >
> > Crea la tabla en Supabase y reemplaza el stub por el endpoint real. El modelo Pydantic que definiste en la fase anterior es el contrato — úsalo para validar. Los eventos que no cumplan el contrato se rechazan individualmente, pero el resto del batch se persiste igualmente.
> >
> > El frontend no toca nada. La URL del endpoint es la misma — solo cambia lo que ocurre dentro del backend cuando llega el batch. Si el frontend necesita cambiar algo para que esto funcione, el diseño está mal."

---

### 📚 Conocimiento complementario — Por qué el bulk insert importa

La telemetría no se escribe igual que los datos de negocio. Un formulario de inventario genera un INSERT cuando el usuario pulsa "Guardar". El `TelemetryService` puede enviar 20 eventos de golpe cada 10 segundos desde múltiples usuarios en paralelo.

Si el endpoint hace un INSERT por evento, cada batch de 20 abre 20 transacciones separadas en la base de datos. Con 10 usuarios activos son 200 transacciones por cada ciclo de flush — y eso en un sistema pequeño. En producción ese patrón colapsa el pool de conexiones.

El bulk insert resuelve esto: todos los eventos válidos de un batch se insertan en una sola transacción. La diferencia entre uno y otro no es visible cuando la tabla tiene 100 filas; es catastrófica cuando tiene 10 millones.

**La tabla de telemetría no es una tabla CRUD.** Sus invariantes son distintos:

- Solo se escribe, nunca se actualiza ni se borra — los eventos son hechos inmutables
- Las columnas fijas (`event_type`, `timestamp`, `service`) son las que soportan las queries analíticas del día siguiente
- La columna `tags` JSONB almacena el objeto `properties` del envelope (solo claves de la allowlist) sin necesidad de alterar el esquema

### 📚 Conocimiento complementario — Validación parcial (parseo por evento)

El modelo Pydantic `TelemetryEvent` es el contrato — pero **cómo** lo aplicas en FastAPI importa.

**No tipes el body completo como `list[TelemetryEvent]`.** Si la firma del endpoint es algo como `batch: TelemetryBatch` con `events: list[TelemetryEvent]`, Pydantic valida todos los eventos antes de entrar al handler. Un evento inválido en el batch → FastAPI devuelve `422` para toda la petición → el frontend reintenta o descarta el lote entero. Eso contradice la aceptación parcial.

Usa **parseo por evento** en su lugar:

1. Acepta el envelope de forma laxa: `{ "events": [...] }` — cada elemento de la lista es un dict en bruto, no un `TelemetryEvent` ya validado
2. Itera dentro del handler y llama a `TelemetryEvent.model_validate(raw)` en cada ítem dentro de `try/except ValidationError`
3. Los eventos válidos van a la lista de bulk insert; los inválidos incrementan `rejected` — el bucle continúa
4. Devuelve HTTP `200` con `{ "received", "stored", "rejected" }` siempre que el envelope sea parseable (tiene un array `events`)

| Enfoque                                       | Qué pasa con un batch mixto                                 |
| --------------------------------------------- | ----------------------------------------------------------- |
| Body tipado (`events: list[TelemetryEvent]`)  | Toda la petición falla con `422` — no se guarda nada        |
| Parseo por evento (`model_validate` en bucle) | Los válidos se guardan; los inválidos cuentan en `rejected` |

El modelo se reutiliza sin cambios respecto a la Fase 2 — lo usas como **validador por ítem**, no como tipo del body completo.

---

## 🌱 Cómo Empezar el Proyecto

1. Abre tu fork del monorepo y localiza `services/` (backend FastAPI).
2. Ten a mano tu `docs/telemetry/event-schemas.json` y `telemetry-plan.md` — confirma que el mapeo a `tags` preserva las dimensiones específicas del CONTEXT (almacén, oficina, etc.) definidas en tu plan.
3. El frontend no se toca. Verifica que `NEXT_PUBLIC_TELEMETRY_ENDPOINT` sigue apuntando al mismo endpoint — solo cambia lo que pasa dentro del backend.
4. Sigue el orden: tabla en Supabase → endpoint real → verificación end-to-end.

---

## 💻 Lo Que Debes Hacer

### Fase 1 — Tabla de almacenamiento en Supabase

- [ ] Crea la tabla `telemetry_events` en Supabase con la siguiente estructura:

  | Columna      | Tipo                                   | Descripción                                             |
  | ------------ | -------------------------------------- | ------------------------------------------------------- |
  | `id`         | `uuid` PK, default `gen_random_uuid()` | Identificador único del registro                        |
  | `timestamp`  | `timestamptz` NOT NULL                 | Marca de tiempo del evento en ISO 8601                  |
  | `service`    | `text` NOT NULL                        | Origen del evento (`backoffice`, `api`)                 |
  | `event_type` | `text` NOT NULL                        | Tipo de evento en formato `entidad_acción`              |
  | `level`      | `text` default `'info'`                | Severidad: `info`, `warn`, `error`                      |
  | `value`      | `numeric` nullable                     | Valor numérico asociado al evento si aplica             |
  | `message`    | `text` nullable                        | Descripción legible del evento                          |
  | `tags`       | `jsonb` default `'{}'`                 | `properties` del envelope (solo claves de la allowlist) |

- [ ] Mapea cada `TelemetryEvent` de la API a una fila de tabla con este contrato:

  | Columna DB   | Origen                                           |
  | ------------ | ------------------------------------------------ |
  | `timestamp`  | `event.timestamp`                                |
  | `service`    | constante `backoffice` (o derivado del envelope) |
  | `event_type` | `event.event_type`                               |
  | `level`      | derivar del tipo de evento o default `info`      |
  | `value`      | numérico opcional desde `properties` si aplica   |
  | `message`    | resumen legible opcional                         |
  | `tags`       | `event.properties` (solo claves de la allowlist) |

  Los campos del envelope `eventId`, `sessionId`, `userId`, `schemaVersion` y `requestId` también pueden guardarse dentro de `tags` si tu plan los requiere para análisis — documenta el mapeo en `telemetry-plan.md` y aplícalo de forma consistente.

- [ ] Crea los tres índices que hacen la tabla consultable a escala: sobre `timestamp`, sobre `event_type`, y un índice GIN sobre `tags` para búsquedas dentro del JSONB.
- [ ] Confirma que la tabla no tiene lógica de UPDATE ni DELETE — los eventos de telemetría son inmutables una vez registrados.

### Fase 2 — Endpoint real en FastAPI

- [ ] Reemplaza el stub `POST /telemetry/events` por la implementación completa. El endpoint real debe:
  - Aceptar el mismo envelope que el stub: `{ "events": [...] }` — parsear la lista de forma laxa; **no** declarar `events: list[TelemetryEvent]` como tipo del body en FastAPI (ver validación parcial arriba)
  - Validar cada evento en bruto individualmente con `TelemetryEvent.model_validate(...)` dentro del handler — el mismo modelo de la fase anterior, sin modificarlo
  - Rechazar con error individual los eventos que no cumplan el contrato, **sin cancelar el batch** — los eventos válidos del mismo lote se persisten igualmente
  - Insertar los eventos válidos en `telemetry_events` en una sola operación de bulk insert
  - Devolver `{ "received": N, "stored": M, "rejected": R }` donde N es el total recibido, M los persistidos y R los rechazados
- [ ] Verifica que la respuesta del endpoint real es compatible con el frontend existente — el `TelemetryService` solo mira el código de estado HTTP, no el cuerpo de la respuesta.

### Fase 3 — Verificación end-to-end

- [ ] Con el endpoint real activo, usa el backoffice para generar eventos reales: registra al menos una orden de entrada y una de salida en el módulo de inventario.
- [ ] Consulta directamente la tabla `telemetry_events` en Supabase y confirma que los eventos aparecen con los campos correctos — especialmente `event_type`, `timestamp` y `tags`.
- [ ] Prueba el comportamiento de rechazo: envía manualmente (con curl o el cliente HTTP que prefieras) un batch que mezcle eventos válidos e inválidos y verifica que la respuesta refleja correctamente `stored` y `rejected`.

---

## ✅ Qué Evaluaremos

- [ ] La tabla `telemetry_events` existe en Supabase con las ocho columnas, los tres índices y sin lógica de UPDATE/DELETE
- [ ] El endpoint `POST /telemetry/events` hace bulk insert y devuelve `{ "received", "stored", "rejected" }`
- [ ] Los eventos inválidos se rechazan individualmente sin cancelar el batch — los válidos se persisten (parseo por evento con `model_validate`, no body tipado `list[TelemetryEvent]` que devolvería `422` para todo el lote)
- [ ] El modelo Pydantic `TelemetryEvent` no ha sido modificado respecto al proyecto anterior — se reutiliza tal cual
- [ ] El frontend no ha cambiado ninguna línea — la sustitución stub → real es completamente transparente
- [ ] Los eventos aparecen en `telemetry_events` con `event_type`, `timestamp` y `tags` correctamente poblados
- [ ] El JSON de `tags` guardado preserva las allowlists de propiedades y dimensiones específicas del CONTEXT documentadas en el `telemetry-plan.md` del estudiante
- [ ] El insert es una sola operación por batch, no un INSERT por evento

---

## 📦 Cómo Entregar

1. Asegúrate de que los cambios están en tu fork: tabla creada en Supabase y endpoint real en `services/`.
2. Crea un Pull Request contra la rama principal del monorepo con el título: `[W16D48] Telemetry Storage`.
3. En la descripción del PR, incluye:
   - Una captura de la tabla `telemetry_events` en Supabase con al menos 5 filas de eventos reales
   - La respuesta JSON de un batch que mezcle eventos válidos e inválidos (mostrando `received`, `stored` y `rejected`)
   - Confirmación explícita de que el frontend no cambió

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
