# Sistemas en Tiempo Real: Notificaciones SSE (Parte 1 de 2)

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/notification)** antes de escribir código — ahí se definen los eventos operativos, nombres de campos y restricciones específicas de tu empresa para esta parte.

---

## 🎯 Tu reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya tienes una API central funcionando, un pipeline de reporting que alimenta métricas de negocio, y el sistema multiagente de generación de RFPs con checkpointing que tu equipo entregó la semana pasada. Ese sistema registra cada nueva solicitud de propuesta (RFP) como un ticket que debe ser procesado — pero hoy, la única forma de enterarse de que llegó un ticket nuevo es recargando el dashboard manualmente. El equipo comercial abrió una **RFI**: quieren saber por qué nadie se entera de una RFP nueva hasta que alguien revisa la pantalla por curiosidad. Tu tech lead convirtió esa pregunta en un **ticket** para tu squad: reemplazar ese refresco manual con un flujo que empuje la notificación al frontend en cuanto el ticket de RFP se registra.

El encargo es concreto. Tu manager lo resume así:

> "Cada RFP que entra es plata sobre la mesa, y ahora mismo nadie se entera hasta que abre el dashboard por su cuenta. Necesito que en el momento en que se registra un ticket de RFP nuevo, la pantalla lo muestre sola, sin que nadie tenga que refrescar. Y si se cae la conexión de alguien, que se reconecte sin que tenga que recargar la página."

Algunos requisitos quedan implícitos en este encargo y tendrás que identificarlos con cuidado: la notificación debe distinguirse de otros tipos de evento que ya existan en tu dashboard (no es un evento más genérico), debe indicar al menos qué ticket de RFP llegó y que requiere procesamiento, y debe degradar con gracia si el cliente pierde la conexión — no simplemente dejar de notificar en silencio.

**Fuera de alcance en esta parte:** esta entrega no requiere ninguna llamada a un modelo o agente. Es una capa de comunicación, no una capa de IA — eso llega en la Parte 2.

---

## 🌱 Cómo Empezar el Proyecto

Sigue trabajando en el fork del monorepo de tu empresa que has usado a lo largo del programa. Si por alguna razón aún no tienes tu fork, créalo ahora desde el [monorepo base](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Crea una rama nueva desde tu rama principal: `feature/sse-notifications`.
2. Ubica el servicio y la vista de dashboard que hoy dependen de polling — vas a extender esas rutas, no crear una app paralela ni una carpeta de entrega.
3. Revisa tu `CONTEXT-company.md` para confirmar cómo se representa un ticket de RFP (campos, estado inicial) — eso define qué debe llevar la notificación en tiempo real.
4. Añade dependencias nuevas con `uv add` (backend) / el gestor de paquetes que ya uses en el monorepo para la UI — nunca con `pip install` ni `pipenv`.
5. Implementa en el layout existente: SSE en `services/`, UI consumidora en `uis/`, pruebas en `tests/`.

Si necesitas un repaso de cómo montar un proyecto, mira [cómo empezar un proyecto de código](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 Qué Debes Hacer

**Backend (`services/`)**

- [ ] Implementa un endpoint SSE que emita un evento cada vez que se registra un nuevo ticket de RFP en el sistema
- [ ] Define un nombre de evento explícito (p. ej. `rfp_ticket_created`) y un payload consistente con al menos el identificador del ticket y su estado inicial (evita un evento genérico tipo "message")
- [ ] Configura correctamente los headers y el keep-alive de la conexión SSE para que no se cierre prematuramente (`Content-Type: text/event-stream`, y frames de comentario keep-alive cuando haga falta)
- [ ] Protege el stream con el **mismo JWT** que usa la API del backoffice — clientes sin autenticación no deben recibir eventos

⚠️ **IMPORTANTE:** los nombres de campos, entidades y valores del dominio en tu implementación deben coincidir con lo especificado en tu CONTEXT.md. Una implementación genérica que ignore el contexto no será aceptada.

**Frontend (`uis/`)**

- [ ] Refactoriza la vista de dashboard existente que hoy requiere recarga manual para que muestre la llegada de un ticket de RFP en tiempo real, consumiendo el stream SSE
- [ ] Consume el stream usando `fetch` + `ReadableStream` (o el mecanismo equivalente de tu stack), enviando el JWT (p. ej. `Authorization: Bearer …`). **No** te bases solo en `EventSource` — no permite headers de auth personalizados de forma limpia; por eso aquí se exige `fetch`
- [ ] Implementa reconexión con backoff progresivo cuando la conexión se interrumpe
- [ ] Implementa al menos una **estrategia de recuperación** para que los eventos registrados mientras estabas desconectado no se pierdan en silencio. Opciones aceptables (elige una y documéntala): `Last-Event-ID` / replay corto en servidor; al reconectar, refetch de la lista de tickets y SSE solo para eventos posteriores; o un enfoque equivalente. Deduplica para que el mismo ticket no aparezca dos veces en la UI
- [ ] La notificación de un ticket de RFP nuevo es visualmente distinguible de otros datos del dashboard y no requiere recargar la página ni volver a pedir todos los datos en cada evento

**Pruebas (`tests/`)**

- [ ] Prueba el endpoint SSE en sí: afirma que los headers de respuesta incluyen `text/event-stream`, que el wire usa un `event:` nombrado (p. ej. `rfp_ticket_created`), y que `data:` es JSON con la forma de payload / campos del CONTEXT exigidos — no solo un test unitario abstracto de un dict desligado del framing SSE
- [ ] Prueba o verificación manual documentada de reconexión + recuperación tras una caída (el backoff dispara, los tickets perdidos se recuperan o se manejan de forma explícita, sin duplicar UI para el mismo `ticket_id`)

---

## 🎁 Opcional: Otro Caso de Notificación en Tiempo Real

El ticket de RFP es tu entrega obligatoria. Si quieres práctica adicional (esto no es requisito para aprobar la parte), puedes implementar **un segundo tipo de notificación push**, reutilizando el mismo endpoint SSE con un nuevo nombre de evento. Elige como máximo una de estas opciones, la que mejor encaje con lo que ya construiste y con tu CONTEXT:

- **Alerta de umbral de negocio** — notifica cuando una métrica de tu pipeline de reporting cruza el umbral crítico que tu CONTEXT define para tu empresa (por ejemplo, una caída de ventas, una tasa de inasistencia, o una tasa de rechazo de facturación, según corresponda).
- **Escalamiento de agente** — notifica cuando una conversación es escalada de agente a humano, para que quien supervisa lo vea aparecer en el dashboard sin recargar.
- **Alerta por inactividad operativa** — notifica cuando un proceso o ubicación no registra la actividad esperada durante un período definido (por ejemplo, sin ventas registradas en un rango de horas, o una vacante sin cubrir más allá del plazo esperado).

Si decides implementar una de estas, debe cumplir el mismo estándar técnico que la notificación de RFP: evento nombrado, payload estructurado, y compatible con la reconexión ya implementada.

---

## 🤔 Preguntas de Diseño

Antes de dar por cerrada la implementación, piensa y documenta tu respuesta a estas preguntas en tu PR:

- Si dos personas del equipo comercial abren el dashboard al mismo tiempo, ¿cada conexión SSE debería ser independiente o deberían compartir alguna capa intermedia? ¿Qué pasaría si 50 personas lo abren a la vez?
- ¿Qué estrategia de recuperación elegiste para tickets registrados mientras estabas desconectado (`Last-Event-ID` / replay corto, refetch-luego-SSE, o equivalente), y cómo evitas duplicados tras reconectar?
- ¿Por qué SSE es la herramienta correcta para notificar la llegada de un ticket y no WebSockets? ¿En qué momento dejaría de serlo — por ejemplo, si quisieras que alguien pudiera reaccionar al ticket desde el mismo canal?

---

## ✅ Qué Evaluaremos

- [ ] El dashboard muestra la notificación de un ticket de RFP nuevo automáticamente, sin acción manual del usuario
- [ ] Cortar y restablecer la conexión de red dispara una reconexión dentro del esquema de backoff, aplica la estrategia de recuperación documentada, y no duplica notificaciones ya recibidas
- [ ] El endpoint SSE exige el mismo JWT que el backoffice; el cliente lo envía vía `fetch` (no `EventSource` a pelo)
- [ ] El endpoint SSE usa un evento nombrado y con payload estructurado para el ticket de RFP, no un único tipo de mensaje genérico; las pruebas cubren `text/event-stream`, nombre de evento y forma del JSON en `data`
- [ ] No existe ninguna llamada a un modelo o agente en la implementación de esta parte
- [ ] Los nombres de campos y entidades coinciden con los definidos en el CONTEXT.md de tu empresa

---

## 📦 Cómo Entregar Este Proyecto

Esta es la Parte 1 de 2. Entrégala con su propio Pull Request contra tu rama principal — no esperes a tener la Parte 2 lista.

1. Haz commit y push de tu rama `feature/sse-notifications` (el código vive en `services/`, `uis/` y `tests/` — **no** crees una carpeta de entrega aparte)
2. Abre un Pull Request describiendo qué implementaste y cómo probar el stream SSE
3. Incluye en la descripción del PR tus respuestas a las Preguntas de Diseño
4. Solicita revisión a tu tech lead

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
