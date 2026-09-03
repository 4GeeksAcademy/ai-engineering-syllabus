# Milestone — Sistemas en Tiempo Real: Observabilidad de Agentes (Parte 1 de 2)

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/agent-observability)** antes de escribir una sola línea de código — ahí se define qué agentes de tu empresa vas a observar, los nombres de eventos y los campos específicos para tu implementación.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya tienes agentes corriendo en producción: un asistente conversacional que resuelve preguntas del equipo, y un sistema multiagente que procesa flujos de trabajo completos con varios pasos y validaciones internas. El problema es que, ahora mismo, la única forma de saber qué está haciendo cualquiera de los dos en un momento dado es revisar logs manualmente.

Tu tech lead te traslada una **RFI** que llegó del equipo de operaciones y la convierte en un **ticket** para tu escuadra:

> **Contexto:** No tenemos visibilidad de lo que hacen nuestros agentes mientras están corriendo, ni un historial confiable de lo que ya hicieron. Cuando algo sale mal, nos enteramos por un usuario molesto, no por el sistema.
>
> **Qué necesito que construyan** — un panel con, al menos:
>
> - Un **listado de todos los agentes registrados**: identificador, nombre, en qué flujo(s) participa, su estado actual y si necesita intervención.
> - El **detalle de un agente**, incluyendo qué acciones estarían disponibles sobre él según su estado actual.
> - Dentro del detalle, los **últimos 5 flujos** en los que participó, con su estado en cada uno y, dentro de cada flujo, las tareas que ese agente ejecutó ahí.
> - Un **log rápido de las últimas 10 tareas** ejecutadas por ese agente, sin importar en qué flujo.
> - Una opción para ver **todo el historial paginado** de ejecuciones de todos los agentes, no solo las últimas.
> - Aparte del enfoque por agente, una **vista por flujo**: los flujos ejecutados, y al entrar en uno, el detalle de qué agentes participaron, su estado, y qué acciones realizó cada uno dentro de ese flujo.
>
> **Criterio de aceptación:** dado el identificador de cualquier tarea, cualquier persona del equipo debe poder reconstruir sin ambigüedad qué flujo la originó, qué la disparó, qué tareas se derivaron de ella, y cuál fue el paso anterior y el siguiente.
>
> — Tu tech lead

Algunos requisitos quedan implícitos y tendrás que identificarlos con cuidado: el esquema de datos debe servir para **más de un tipo de agente** (uno conversacional de un solo paso, y otro con múltiples nodos y sub-tareas); un agente puede participar en **varios flujos distintos** a lo largo del tiempo, así que "flujo" y "agente" son dos entidades relacionadas, no una sola; toda tarea debe conservar **de dónde vino** (qué la inició) y **qué generó** (tareas derivadas), formando una cadena trazable por identificadores; y el historial debe **sobrevivir después de que la ejecución termina** — no es solo una vista en vivo que desaparece al refrescar.

### 📚 Conocimiento complementario: observabilidad vs. control vs. aprobación de negocio

Es fácil confundir tres cosas distintas. **Observabilidad** es simplemente poder ver y reconstruir qué pasó — este proyecto, incluyendo mostrar qué acciones _estarían_ disponibles. **Control operativo** es poder _ejecutar_ esas acciones (pausar, reanudar, matar un agente) — eso es la [Parte 2](../ai-eng-milestone-real-time-agent-control). **Aprobación de negocio** es cuando un humano da el visto bueno a una decisión específica antes de que se ejecute — algo que tu sistema multiagente ya resuelve internamente con sus propios puntos de control. Esta parte del proyecto es solo la primera: **mirar y entender, no tocar todavía**.

**Fuera de alcance para esta parte:** puedes _mostrar_ qué acciones estarían disponibles según el estado del agente (por ejemplo, una etiqueta "pausa disponible" o "requiere aprobación"), pero no implementes que esas acciones realmente se ejecuten — eso es la [Parte 2](../ai-eng-milestone-real-time-agent-control). Tampoco toques la lógica interna de aprobación que ya existe en tu flujo multiagente; este panel la observa desde afuera, no la reemplaza.

---

## 🌱 Cómo Empezar el Proyecto

Continúa sobre el fork del monorepo de tu empresa que has usado desde el inicio del curso. Si por alguna razón no tienes tu fork, créalo ahora desde el [monorepo base](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Crea una rama nueva desde tu rama principal: `feature/agent-observability-sse`.
2. Antes de escribir código, dibuja (aunque sea en papel) el modelo de datos: qué es un **agente**, qué es un **flujo/ejecución**, qué es una **tarea/paso**, y cómo se relacionan entre sí. La mayoría de los errores en este proyecto vienen de no separar bien estas tres entidades.
3. Ubica los puntos de tu backend donde tus agentes ya emiten pasos, tool calls o cambios de estado — vas a extender esos puntos, no vas a reescribir la lógica de los agentes.
4. Revisa tu `CONTEXT-company.md` en `content/contexts/10-realtime/agent-observability/` para confirmar qué agentes y flujos debes observar.
5. Agrega nuevas dependencias con `uv add` — nunca con `pip install` o `pipenv`.
6. Implementa bajo la estructura existente: SSE + persistencia en `services/`, panel en `uis/backoffice`, tests en `tests/`.

---

## 💻 Qué Debes Hacer

**Modelo de datos (`services/`)**

- [ ] Define una entidad **Agente**: identificador, nombre, flujo(s) en los que puede participar, estado actual, indicador de si necesita intervención
- [ ] Define una entidad **Flujo/Ejecución**: identificador, tipo de flujo, estado, qué la disparó (`triggered_by`), agentes participantes
- [ ] Define una entidad **Tarea/Paso**: identificador, a qué flujo y agente pertenece, `action_type` (`query`, `write`, `draft_start`, `tool_call`, `deliver`, u otro definido en tu CONTEXT), qué la inició (`trigger` — tarea anterior o evento externo), tareas derivadas de ella, referencia al paso anterior y al paso siguiente
- [ ] Toda tarea debe quedar **persistida** de forma que su cadena completa (disparador → tarea → derivadas → siguiente paso) sea reconstruible después de que el flujo terminó

**Backend — API y stream (`services/`)**

- [ ] Endpoint SSE que emita un evento por cada cambio de paso o estado de un agente activo (`agent_step`, `agent_status_changed`), con `action_type` incluido
- [ ] Endpoint: **listado de agentes registrados** (id, nombre, flujo(s), estado, `needs_intervention`)
- [ ] Endpoint: **detalle de un agente**, incluyendo qué acciones estarían disponibles según su estado actual
- [ ] Endpoint: **últimos 5 flujos** de un agente, con estado por flujo y las tareas de ese agente dentro de cada uno
- [ ] Endpoint: **últimas 10 tareas** de un agente (log rápido, sin agrupar por flujo)
- [ ] Endpoint: **log paginado completo** de ejecuciones de todos los agentes
- [ ] Endpoint: **listado de flujos ejecutados**, y detalle de un flujo con sus agentes participantes, estado de cada uno y acciones realizadas
- [ ] Protege todos los endpoints y el stream con el mismo JWT que usa el backoffice

⚠️ **IMPORTANTE:** los nombres de eventos, agentes, `action_type` y campos deben coincidir con lo especificado en tu `CONTEXT-company.md`. Una implementación genérica que ignore el contexto no será aceptada.

**Frontend (`uis/backoffice`)**

- [ ] Vista de **listado de agentes**: id, nombre, flujo(s), estado, indicador visual de "necesita intervención"
- [ ] Vista de **detalle de agente**: estado actual, acciones disponibles (informativas, no ejecutables aún), últimos 5 flujos con su estado y tareas del agente en cada uno, últimas 10 tareas en modo log
- [ ] Vista de **log completo paginado**, filtrable al menos por agente o por flujo
- [ ] Vista de **listado de flujos** y **detalle de flujo**: agentes participantes, estado de cada uno, acciones realizadas
- [ ] En cualquier tarea individual, debe poder verse claramente: qué la disparó, qué tareas derivó, y cuál es el paso anterior/siguiente en la cadena
- [ ] El listado de agentes y el detalle de agente se actualizan en tiempo real vía SSE; las vistas de log e historial pueden ser bajo demanda (no necesitan ser streaming)
- [ ] Consume el stream con `fetch` + `ReadableStream` (o el equivalente de tu stack), enviando el JWT (p. ej. `Authorization: Bearer …`). **No** dependas solo de `EventSource` — no puede fijar cabeceras de auth personalizadas de forma limpia
- [ ] Reconexión con backoff progresivo y recuperación de eventos perdidos

**Bonus (opcional, no bloquea la aceptación)**

- [ ] Representa un flujo como un **grafo visual**: nodos = tareas o agentes, aristas = disparador → derivada / paso anterior → siguiente. No hace falta una librería sofisticada; incluso un diagrama generado a partir de la cadena de identificadores cuenta.

**Testing (`tests/`)**

- [ ] Test del endpoint SSE: headers, nombre de evento, forma del `data` JSON
- [ ] Test de los endpoints de listado y detalle de agente
- [ ] Test del endpoint de flujo: dado un `flow_id`, devuelve correctamente todos sus agentes participantes y tareas en orden
- [ ] Test de trazabilidad: dado un `task_id` cualquiera, se puede obtener su disparador, sus derivadas y sus pasos anterior/siguiente sin ambigüedad
- [ ] Test del log paginado: verifica orden cronológico y que la paginación no duplica ni omite registros

---

## 🤔 Preguntas de Diseño

- ¿Cómo modelaste la relación entre Agente, Flujo y Tarea? ¿Por qué esa cardinalidad y no otra?
- ¿Cómo representaste "qué disparó esta tarea"? ¿Es siempre otra tarea, o también puede ser un evento externo (por ejemplo, la llegada de un ticket)?
- Si un agente participa en dos flujos distintos al mismo tiempo, ¿cómo evita tu panel mezclar sus tareas?
- ¿Qué decisión tomaste para que el listado de acciones disponibles sea informativo ahora, pero fácil de conectar a ejecución real en la Parte 2?

---

## ✅ Qué Vamos a Evaluar

- [ ] Existen y funcionan las tres entidades (Agente, Flujo, Tarea) con sus relaciones correctamente modeladas
- [ ] El listado de agentes muestra id, nombre, flujo(s), estado y `needs_intervention`, actualizado en tiempo real
- [ ] El detalle de agente muestra correctamente acciones disponibles según estado, últimos 5 flujos con tareas anidadas, y últimas 10 tareas en log
- [ ] El log completo paginado funciona sin duplicar ni omitir registros
- [ ] La vista por flujo muestra correctamente los agentes participantes, su estado y sus acciones dentro de ese flujo
- [ ] Dado cualquier `task_id`, se puede reconstruir su disparador, sus tareas derivadas y sus pasos anterior/siguiente
- [ ] El esquema funciona para al menos dos agentes con arquitecturas distintas (conversacional simple y multiagente)
- [ ] Todos los endpoints y el stream requieren el mismo JWT que el resto del backoffice
- [ ] No se implementó ejecución real de ninguna acción de control en esta parte — solo se muestra qué estaría disponible
- [ ] Nombres de eventos, agentes, flujos y `action_type` coinciden con `CONTEXT-company.md`

---

## 📦 Cómo Entregar

Esta es la Parte 1 de 2 del Milestone. Entrégala con su propio Pull Request contra tu rama principal — no esperes a que la Parte 2 esté lista.

1. Haz commit y push de tu rama `feature/agent-observability-sse`
2. Abre un Pull Request describiendo qué implementaste y cómo probarlo
3. Incluye tus respuestas a las Preguntas de Diseño en la descripción del PR
4. Solicita revisión a tu tech lead

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
