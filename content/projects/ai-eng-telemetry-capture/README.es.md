# Telemetría – Captura en el frontend

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Necesitas el `telemetry-plan.md` y el `event-schemas.json` aprobados de la Fase 1 — son el contrato que implementarás hoy. Si no están aprobados, resuélvelo antes de escribir código.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

El plan de telemetría está aprobado. Hoy implementas la mitad que el usuario nunca ve pero que lo hace todo posible: el sistema de captura en el frontend.

Cada evento que diseñaste en la Fase 1 debe capturarse en el momento exacto en que ocurre en el backoffice, acumularse en una cola local y enviarse al backend en lotes — nunca uno a uno. Para poder verificar que los eventos llegan correctamente, crearás también un endpoint receptor mínimo en FastAPI: no persiste nada todavía, solo valida el formato y responde 200. La persistencia real en base de datos es el trabajo de la Fase 3.

> Tu tech lead te ha enviado este mensaje:
>
> > "Quiero ver los eventos fluyendo antes de construir el almacenamiento. Crea el `TelemetryService` en el backoffice e instrumenta el flujo de inventario con los eventos del plan. Para que puedas probar que el payload llega bien, añade un endpoint stub en el backend — que valide el formato y devuelva 200, sin escribir en base de datos todavía.
> >
> > Una cosa importante: configura la URL del endpoint como variable de entorno desde el principio. En la siguiente fase reemplazaremos el stub por la implementación real y el frontend no debería tener que cambiar nada.
> >
> > No quiero tracking disperso por todos los componentes. Todo pasa por una sola función `track()` — nada más."

---

### 📚 Conocimiento complementario — Cómo funciona el sistema de captura

El servicio de captura en el frontend no dispara una llamada HTTP por cada evento — eso generaría cientos de requests por minuto en una aplicación activa y saturaría el backend. El patrón correcto tiene tres mecanismos trabajando juntos:

**Cola local + batch:** los eventos se acumulan en memoria como array. Cada N segundos, o cuando la cola alcanza un tamaño máximo, el servicio envía el lote completo en una sola request (`events: []`). El timestamp de cada evento es el momento de captura, no el de envío.

**Flush fiable con `sendBeacon`:** cuando el usuario cierra la pestaña o navega fuera, el browser cancela las requests HTTP en vuelo. `navigator.sendBeacon` resuelve esto — envía el lote pendiente de forma asíncrona y garantizada incluso cuando la página está destruyéndose.

**Retry con backoff:** si la red falla, el servicio reintenta con espera exponencial. Si después de N intentos sigue fallando, descarta el lote — los datos de telemetría no son críticos y no deben bloquear la aplicación.

**El endpoint como variable de entorno:** en entornos reales los equipos de frontend y backend trabajan en paralelo. El frontend apunta a `NEXT_PUBLIC_TELEMETRY_ENDPOINT` — hoy esa variable apunta al stub; mañana apuntará al endpoint real con persistencia. El frontend no cambia.

**La separación perfil/uso:** los datos de usuario (nombre, rol, preferencias) son estado persistente que vive en la base de datos principal. Los datos de uso son eventos `append-only` que van a telemetría. Nunca mezcles los dos.

---

## 🌱 Cómo Empezar el Proyecto

1. Abre tu fork del monorepo y localiza `uis/backoffice/` (frontend) y `services/` (backend FastAPI).
2. Recupera tu `docs/telemetry/event-schemas.json` — es el contrato que guiará toda la implementación.
3. Añade `NEXT_PUBLIC_TELEMETRY_ENDPOINT` a tu `.env.local` apuntando al endpoint stub que crearás: `http://localhost:8000/telemetry/events`.
4. Sigue el orden de las fases: stub → servicio → instrumentación. No instrumentes antes de tener el servicio.

---

## 💻 Lo Que Debes Hacer

### Fase 1 — Endpoint stub en FastAPI

> ⚠️ Este endpoint es **temporal y de verificación**. Su único propósito es que puedas comprobar que el payload llega con el formato correcto. En la Fase 3 (próximo proyecto) lo reemplazarás por la implementación real con validación completa y persistencia en Supabase.

- [ ] Crea el endpoint `POST /telemetry/events` en el backend, en un router propio dentro de `services/`. Por ahora debe:
  - Aceptar un body con la forma `{ "events": [...] }`
  - Hacer un log del número de eventos recibidos y del `event_type` de cada uno
  - Devolver `200 OK` con `{ "received": N }` donde N es el número de eventos del batch
- [ ] Define el modelo Pydantic `TelemetryEvent` con los campos del envelope estándar de tu plan (`eventId`, `timestamp`, `sessionId`, `userId`, `event_type`, `schemaVersion`, `properties`). Este modelo será reutilizado y ampliado en la Fase 3 — defínelo bien desde ahora.
- [ ] Lee la URL del endpoint desde la variable de entorno `TELEMETRY_ENDPOINT` en el backend, aunque de momento no la uses para redirigir tráfico. Establece el patrón desde el principio.

### Fase 2 — TelemetryService en el frontend

- [ ] Crea `uis/backoffice/src/services/telemetry.ts` (o equivalente) con las siguientes responsabilidades:
  - **Cola local:** acumular eventos en memoria como array interno
  - **Batch + debounce:** enviar la cola a `NEXT_PUBLIC_TELEMETRY_ENDPOINT` cada 10 segundos o cuando la cola alcance 20 eventos, lo que ocurra primero
  - **Flush fiable:** usar `navigator.sendBeacon` en el evento `visibilitychange` para garantizar que los eventos pendientes se envíen al cerrar o cambiar de pestaña
  - **Retry con backoff:** si el envío falla, reintentar hasta 3 veces con espera exponencial antes de descartar el lote
- [ ] El servicio debe añadir automáticamente a cada evento: `sessionId` (generado al iniciar sesión y almacenado en memoria de la sesión), `timestamp` en ISO 8601 en el momento de captura, y `schemaVersion` desde una constante compartida.
- [ ] Expón una única función pública `track(eventType: string, properties: Record<string, unknown>): void`. Todo el tracking del backoffice pasa por esta función — nunca por `fetch` o `axios` directo.

### Fase 3 — Instrumentación del flujo de inventario

- [ ] Instrumenta en el backoffice los eventos definidos en tu plan para el módulo de inventario. Como mínimo deben estar cubiertos:
  - Creación de una orden de entrada completada con éxito
  - Creación de una orden de salida completada con éxito
  - Intento fallido de cualquier orden (error de validación o stock insuficiente)
  - Visualización del listado de productos/stock
- [ ] Cada llamada a `track()` debe incluir solo las propiedades de la **allowlist** definida para ese evento en tu `event-schemas.json`. No añadas propiedades extra "por si acaso".
- [ ] Verifica en las DevTools de red (pestaña Network) que los batches llegan al endpoint stub con el formato correcto y que el backend responde 200.

### 🔵 Actividad adicional — Instrumentación del flujo de autenticación

- [ ] Instrumenta los eventos de autenticación definidos en tu plan: login exitoso, login fallido y sesión expirada. Captúralos en los hooks o componentes de autenticación — no en cada página individualmente.
- [ ] El evento de login fallido debe incluir en `properties` el motivo del fallo (`invalid_credentials`, `session_expired`, `network_error`) pero **nunca** el valor introducido por el usuario como contraseña o email.

---

## ✅ Qué Evaluaremos

- [ ] El endpoint stub `POST /telemetry/events` existe, acepta arrays con el modelo `TelemetryEvent` y devuelve `{ "received": N }`
- [ ] El modelo Pydantic `TelemetryEvent` refleja el envelope estándar del plan de la Fase 1 con todos sus campos
- [ ] La URL del endpoint se lee de `NEXT_PUBLIC_TELEMETRY_ENDPOINT` — no está hardcoded en el código
- [ ] El backend declara `TELEMETRY_ENDPOINT` en su configuración de entorno para establecer el patrón desde el inicio
- [ ] El `TelemetryService` implementa cola local, batch+debounce (10s / 20 eventos), flush con `sendBeacon` y retry con backoff
- [ ] El servicio genera `sessionId` y `timestamp` automáticamente — el componente que llama a `track()` no los pasa manualmente
- [ ] No hay llamadas directas a `fetch`/`axios` para telemetría fuera del `TelemetryService`
- [ ] Los eventos del flujo de inventario están instrumentados respetando la allowlist de propiedades de cada evento
- [ ] Los intentos fallidos de pedido (error de validación o stock insuficiente) se rastrean desde los bloques `catch`
- [ ] La visualización de la lista de productos/stock se rastrea cuando la página de productos carga
- [ ] No hay PII (email, nombre, contraseña) en ningún evento enviado
- [ ] Las DevTools de red muestran batches llegando al endpoint con el formato correcto

---

## 📦 Cómo Entregar

1. Asegúrate de que los cambios están en tu fork: endpoint stub en `services/` y `TelemetryService` + instrumentación en `uis/backoffice/`.
2. Crea un Pull Request contra la rama principal del monorepo con el título: `[W16D47] Telemetry Frontend`.
3. En la descripción del PR, incluye:
   - El listado de eventos instrumentados y en qué componente o hook se captura cada uno
   - Una captura de las DevTools mostrando un batch de eventos llegando al stub con respuesta 200
   - Si implementaste la actividad adicional de autenticación, indícalo

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
