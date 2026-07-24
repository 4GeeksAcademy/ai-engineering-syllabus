# Hito 10 — Sistemas en Tiempo Real (Parte 1 de 2): Notificaciones SSE

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/notification)** antes de escribir código — ahí se definen los eventos operativos, nombres de campos y restricciones específicas de tu empresa para esta parte.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya tienes una API central funcionando, un pipeline de reporting que alimenta métricas de negocio, y el sistema multiagente de generación de RFPs con checkpointing que tu equipo entregó la semana pasada. Ese sistema registra cada nueva solicitud de propuesta (RFP) como un ticket que debe ser procesado — pero hoy, la única forma de enterarse de que llegó un ticket nuevo es recargando el dashboard manualmente. El equipo comercial abrió una **RFI**: quieren saber por qué nadie se entera de una RFP nueva hasta que alguien revisa la pantalla por curiosidad. Tu tech lead convirtió esa pregunta en un **ticket** para tu squad: reemplazar ese refresco manual con un flujo que empuje la notificación al frontend en cuanto el ticket de RFP se registra.

El encargo es concreto. Tu manager lo resume así:

> "Cada RFP que entra es plata sobre la mesa, y ahora mismo nadie se entera hasta que abre el dashboard por su cuenta. Necesito que en el momento en que se registra un ticket de RFP nuevo, la pantalla lo muestre sola, sin que nadie tenga que refrescar. Y si se cae la conexión de alguien, que se reconecte sin que tenga que recargar la página."

Algunos requisitos quedan implícitos en este encargo y tendrás que identificarlos con cuidado: la notificación debe distinguirse de otros tipos de evento que ya existan en tu dashboard (no es un evento más genérico), debe indicar al menos qué ticket de RFP llegó y que requiere procesamiento, y debe degradar con gracia si el cliente pierde la conexión — no simplemente dejar de notificar en silencio.

**Fuera de alcance en esta parte:** esta entrega no requiere ninguna llamada a un modelo o agente. Es una capa de comunicación, no una capa de IA — eso llega en la Parte 2.

---

## 🌱 Cómo Empezar

1. Ubica el servicio y la vista de dashboard que hoy dependen de polling en tu copia del monorepo.
2. Si todavía no tienes un fork del monorepo de tu empresa, créalo ahora desde [el repositorio base](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) antes de continuar.
3. Revisa tu `CONTEXT-company.md` para confirmar cómo se representa hoy un ticket de RFP en tu sistema (campos, estado inicial) — eso define qué información debe llevar la notificación en tiempo real.
4. Crea una rama de trabajo para esta parte.

---

## 💻 Qué Debes Hacer

**Backend (`services/`)**

- [ ] Implementa un endpoint SSE que emita un evento cada vez que se registra un nuevo ticket de RFP en el sistema
- [ ] Define un nombre de evento explícito (p. ej. `rfp_ticket_created`) y un payload consistente con al menos el identificador del ticket y su estado inicial (evita un evento genérico tipo "message")
- [ ] Configura correctamente los headers y el keep-alive de la conexión SSE para que no se cierre prematuramente

⚠️ **IMPORTANTE:** los nombres de campos, entidades y valores del dominio en tu implementación deben coincidir con lo especificado en tu CONTEXT.md. Una implementación genérica que ignore el contexto no será aceptada.

**Frontend (`uis/`)**

- [ ] Refactoriza la vista de dashboard existente que hoy requiere recarga manual para que muestre la llegada de un ticket de RFP en tiempo real, consumiendo el stream SSE
- [ ] Consume el stream usando `fetch` + `ReadableStream` (o el mecanismo equivalente de tu stack)
- [ ] Implementa reconexión con backoff progresivo cuando la conexión se interrumpe
- [ ] La notificación de un ticket de RFP nuevo es visualmente distinguible de otros datos del dashboard y no requiere recargar la página ni volver a pedir todos los datos

**Pruebas (`tests/`)**

- [ ] Prueba(s) unitaria(s) que verifiquen la estructura del payload emitido por el endpoint SSE
- [ ] Prueba o verificación manual documentada del comportamiento de reconexión tras una caída de conexión

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
- ¿Qué pasa si un ticket de RFP se registra mientras un usuario está desconectado? ¿Se pierde la notificación, o hay alguna forma de recuperarla al reconectar?
- ¿Por qué SSE es la herramienta correcta para notificar la llegada de un ticket y no WebSockets? ¿En qué momento dejaría de serlo — por ejemplo, si quisieras que alguien pudiera reaccionar al ticket desde el mismo canal?

---

## ✅ Qué Evaluaremos

- [ ] El dashboard muestra la notificación de un ticket de RFP nuevo automáticamente, sin acción manual del usuario
- [ ] Cortar y restablecer la conexión de red dispara una reconexión dentro del esquema de backoff implementado, sin duplicar notificaciones ya recibidas
- [ ] El endpoint SSE usa un evento nombrado y con payload estructurado para el ticket de RFP, no un único tipo de mensaje genérico
- [ ] No existe ninguna llamada a un modelo o agente en la implementación de esta parte
- [ ] Los nombres de campos y entidades coinciden con los definidos en el CONTEXT.md de tu empresa

---

## 📦 Cómo Entregar

1. Haz commit y push de tu trabajo a tu fork del monorepo, dentro de la carpeta correspondiente a este proyecto (`parte-1-realtime-sse/`).
2. Abre un Pull Request contra tu propia rama principal (no esperes a tener la Parte 2 lista — esta parte se entrega de forma independiente).
3. Incluye en la descripción del PR tus respuestas a las Preguntas de Diseño.
4. Solicita revisión a tu tech lead.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
