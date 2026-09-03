# Milestone — Sistemas en Tiempo Real: Control de Agentes (Parte 2 de 2)

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/agent-control)** antes de escribir una sola línea de código — ahí se define qué acciones de control aplican a cada agente de tu empresa y qué campos espera tu implementación. Las entidades e ids de agente de la Parte 1 viven en [`agent-observability/`](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/agent-observability); este CONTEXT solo añade semántica de control encima.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya construiste el panel que **muestra** el estado de tus agentes y qué acciones estarían disponibles según ese estado. El problema ahora es que "disponible" es solo una etiqueta: si un agente entra en un bucle o se atasca, la única forma real de detenerlo hoy es reiniciar todo el servicio — lo cual también mata a cualquier otro agente que esté trabajando bien en ese momento.

Tu tech lead convierte esto en un **ticket** de seguimiento directo al anterior:

> **Contexto:** El panel ya nos dice cuándo un agente necesita intervención, pero no podemos hacer nada al respecto sin afectar a todo el sistema.
>
> **Qué necesito que construyan:**
>
> - Que las acciones que el panel ya muestra como "disponibles" se puedan **ejecutar de verdad**: pausar, reanudar y cancelar un agente específico, sin tocar a los demás.
> - Que pausar un agente en medio de un flujo con varios pasos **no pierda su progreso** — debe poder reanudarse después desde donde quedó, no desde cero.
> - Que cancelar sea claramente distinto de pausar: cancelar es definitivo, no se puede reanudar.
> - Que cualquier persona del equipo con el panel abierto vea el resultado de la acción **en el momento**, sin refrescar — incluso si hay varias personas mirando el mismo agente a la vez.
> - Que quede registrado **quién** ejecutó cada acción y cuándo, como parte del historial de esa tarea.
>
> **Criterio de aceptación:** un agente atascado se puede pausar sin afectar al resto del sistema, y su historial de tareas (el que ya construiste) refleja con claridad que fue pausado, por quién, y si luego se reanudó o se canceló.
>
> — Tu tech lead

Algunos requisitos quedan implícitos: pausar y cancelar **no son la misma acción disfrazada** — tienen garantías distintas, y tu modelo de datos de la Parte 1 debe poder representar ambas sin ambigüedad; la ejecución de una acción de control debe **notificarse a todos los clientes conectados**, no solo a quien la ejecutó, porque varias personas del equipo pueden estar mirando el mismo panel; y esto es control operativo — un kill switch — no reemplaza ni interfiere con los puntos de aprobación de negocio que tu flujo multiagente ya tiene internamente.

### 📚 Conocimiento complementario: kill switch vs. aprobación de negocio

Ya viste esta distinción en la Parte 1, pero ahora es donde realmente importa: el control que vas a implementar aquí es de nivel **operativo** — cualquier persona del equipo técnico con permisos puede pausar o cancelar un agente porque algo se ve mal en su ejecución, sin necesidad de entender qué decisión de negocio estaba tomando. Es un **kill switch**, no una aprobación. La **aprobación de negocio** que tu flujo multiagente ya implementa es distinta: la ejecuta la persona dueña de esa decisión específica, y responde a "¿esto que va a salir está bien?", no a "¿este proceso está funcionando bien?". Ambas pueden coexistir sobre la misma ejecución: un agente puede estar correctamente esperando una aprobación de negocio (eso no es una falla) y, aun así, un operador puede decidir cancelarlo si, por ejemplo, lleva demasiado tiempo esperando.

**Fuera de alcance para esta parte:** no dupliques ni reemplaces la lógica de aprobación de negocio que ya existe en tu flujo multiagente — tus nuevas acciones de control conviven con ella, no la sustituyen.

---

## 🌱 Cómo Empezar el Proyecto

Continúa sobre la misma rama de trabajo del monorepo de tu empresa. La Parte 1 ([Observabilidad de Agentes](../ai-eng-milestone-real-time-agent-observability)) debe estar ya mergeada o disponible en tu rama — extiendes ese panel, no lo reconstruyes.

1. Crea una rama nueva desde tu rama principal: `feature/agent-control-websocket`.
2. Antes de escribir código, decide cómo tu entidad **Agente** de la Parte 1 va a representar la diferencia entre "pausado" (reanudable) y "cancelado" (terminal) — no los mezcles en un mismo campo de estado sin distinción.
3. Identifica dónde tu sistema multiagente ya usa checkpointing para retomar ejecuciones — vas a **reutilizar ese mecanismo** para que pausar/reanudar funcione de verdad, no vas a construir uno nuevo desde cero.
4. Revisa tu `CONTEXT-company.md` en `content/contexts/10-realtime/agent-control/` para confirmar qué acciones de control aplican a cada agente de tu empresa.
5. Agrega nuevas dependencias con `uv add` — nunca con `pip install` o `pipenv`.
6. Implementa bajo la estructura existente: WebSocket + lógica de control en `services/`, panel en `uis/backoffice`, tests en `tests/`.

---

## 💻 Qué Debes Hacer

**Modelo de datos (`services/`)**

- [ ] Extiende tu entidad **Agente** para representar sin ambigüedad los estados `paused` (reanudable) y `cancelled` (terminal), distintos entre sí y distintos de `running`/`failed`/`completed`
- [ ] Cada acción de control ejecutada queda registrada en el historial de **Tarea** de la Parte 1: qué acción, quién la ejecutó (`actor_id`), timestamp
- [ ] Un flujo que contiene un agente cancelado refleja ese estado también a nivel de **Flujo**, no solo a nivel de agente individual

**Backend — WebSocket y control (`services/`)**

- [ ] Implementa un canal WebSocket para enviar comandos de control (`pause`, `resume`, `cancel`) dirigidos a un agente/ejecución específica
- [ ] `pause` debe usar el checkpointing existente de tu sistema multiagente para persistir el punto exacto de ejecución; `resume` retoma desde ahí, no desde el inicio
- [ ] `cancel` es terminal: una vez cancelado, un agente no puede reanudarse — solo puede iniciarse una nueva ejecución
- [ ] Usa un patrón **pub/sub**: cuando se ejecuta una acción sobre un agente, todos los clientes suscritos a ese agente (o a ese flujo) reciben la actualización, no solo quien envió el comando
- [ ] Valida que la acción solicitada sea válida para el estado actual del agente (por ejemplo, no se puede "reanudar" un agente que nunca fue pausado) y responde con un error claro si no lo es
- [ ] Protege el canal WebSocket con el mismo JWT que el resto del backoffice, y registra el `actor_id` a partir de esa identidad — no confíes en un campo enviado por el cliente

⚠️ **IMPORTANTE:** los nombres de acciones, estados y campos deben coincidir con lo especificado en tu `CONTEXT-company.md`. Una implementación genérica que ignore el contexto no será aceptada.

**Frontend (`uis/backoffice`)**

- [ ] En la vista de detalle de agente (de la Parte 1), las acciones que antes eran solo informativas ahora son **botones funcionales**: pausar, reanudar, cancelar, habilitados/deshabilitados según el estado actual
- [ ] Al ejecutar una acción, el panel refleja el resultado en tiempo real vía WebSocket — sin recargar la página
- [ ] Si hay más de un cliente/pestaña con el mismo agente abierto, ambos deben verse actualizados cuando cualquiera de los dos ejecuta una acción
- [ ] El historial de tareas del agente (de la Parte 1) muestra claramente cuándo una tarea fue interrumpida por una pausa o cancelación, y quién la ejecutó
- [ ] Reconexión del WebSocket con recuperación de estado — si el cliente se desconecta y reconecta, debe poder recuperar el estado actual del agente, no quedar desincronizado

**Testing (`tests/`)**

- [ ] Test de `pause`: verifica que el checkpoint se persiste y que el estado del agente cambia a `paused`
- [ ] Test de `resume`: verifica que la ejecución retoma desde el checkpoint correcto, no desde el inicio
- [ ] Test de `cancel`: verifica que el agente queda en estado terminal y que un intento posterior de `resume` es rechazado
- [ ] Test de validación de transición de estado: acciones inválidas para el estado actual devuelven error, no se ejecutan silenciosamente
- [ ] Test de pub/sub: verifica que una acción ejecutada por un cliente se propaga a otros clientes suscritos al mismo agente
- [ ] Test de auditoría: cada acción de control queda registrada con `actor_id` y timestamp en el historial de la tarea correspondiente

---

## 🤔 Preguntas de Diseño

- ¿Por qué `pause` y `cancel` necesitan garantías distintas en tu sistema? ¿Qué se rompería si los tratabas como la misma acción con dos nombres?
- ¿Cómo evitaste que dos comandos de control simultáneos sobre el mismo agente (por ejemplo, dos personas pausando y reanudando casi al mismo tiempo) dejen el estado inconsistente?
- Un agente puede estar esperando una aprobación de negocio y, al mismo tiempo, ser candidato a una acción de control operativo — ¿cómo se distingue en tu panel cuál de las dos cosas está pasando?
- ¿Qué decidiste hacer con los agentes/tareas hijas de un flujo cuando el agente padre se cancela?

---

## ✅ Qué Vamos a Evaluar

- [ ] `pause`, `resume` y `cancel` funcionan de verdad sobre un agente específico, sin afectar a otros agentes en ejecución
- [ ] `pause` reutiliza el checkpointing existente y `resume` retoma correctamente desde ese punto, no desde cero
- [ ] `cancel` es terminal y un intento posterior de `resume` es rechazado con un error claro
- [ ] Las acciones se transmiten por pub/sub: todos los clientes suscritos al agente/flujo ven el cambio en tiempo real, no solo quien ejecutó la acción
- [ ] Las transiciones de estado inválidas son rechazadas explícitamente, no ignoradas silenciosamente
- [ ] Cada acción de control queda auditada en el historial de tareas: qué acción, quién (`actor_id` derivado del JWT, no del cliente), cuándo
- [ ] El estado de un flujo refleja correctamente cuando uno de sus agentes fue cancelado
- [ ] El canal WebSocket requiere el mismo JWT que el resto del backoffice
- [ ] La reconexión del WebSocket recupera el estado real del agente, sin desincronización
- [ ] La lógica de aprobación de negocio existente no fue duplicada ni alterada
- [ ] Nombres de acciones, estados y campos coinciden con `CONTEXT-company.md`

---

## 📦 Cómo Entregar

Esta es la Parte 2 de 2 del Milestone. Entrégala con su propio Pull Request contra tu rama principal.

1. Haz commit y push de tu rama `feature/agent-control-websocket`
2. Abre un Pull Request describiendo qué implementaste y cómo probarlo
3. Incluye tus respuestas a las Preguntas de Diseño en la descripción del PR
4. Solicita revisión a tu tech lead

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
