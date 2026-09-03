# Sistemas en Tiempo Real: Streaming de Chat por WebSocket (Parte 2 de 2)

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/communication)** antes de escribir código — ahí se define qué agente vas a conectar, los campos de la sesión de chat y el contrato de eventos WebSocket de esta parte. Los detalles SSE / notificación RFP de la Parte 1 viven en [`10-realtime/notification/`](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/notification), no en este CONTEXT.

---

## 🎯 Tu reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

En la Parte 1 resolviste la mitad del problema: el backend avisa al frontend cuando pasa algo, sin que nadie tenga que preguntar. Pero esa notificación va en una sola dirección. El agente de soporte de tu empresa hoy funciona igual: el usuario envía un mensaje, espera, y recibe la respuesta completa de una sola vez. Si el agente se está yendo por el camino equivocado, el usuario no tiene forma de decírselo hasta que termina de responder.

El equipo de soporte abrió un **RFI**: quieren saber por qué el chat no se siente como una conversación real. Tu tech lead lo convirtió en un **ticket** para tu squad:

> **Contexto:** el agente de soporte ya existe y funciona — no vas a tocar su lógica interna ni sus herramientas.
> **Qué necesito que construyas:** que la respuesta del agente llegue token por token en tiempo real, y que el usuario pueda interrumpirlo a mitad de una respuesta y redirigirlo, sin esperar a que termine.
> **Criterios de aceptación:** el canal debe ser bidireccional (el cliente también envía datos, no solo recibe), los tokens deben streamearse conforme se generan, y una interrupción debe **abortar** genuinamente la generación en curso — no solo ignorar la respuesta cuando llega.

Algunos requisitos quedan implícitos y tendrás que identificarlos con cuidado: SSE (lo que usaste en la Parte 1) ya no alcanza porque el cliente necesita hablar de vuelta mientras el servidor sigue enviando datos; el streaming de tokens y el abort deben convivir en el mismo canal sin pisarse; y la conexión debe recuperarse si se cae, igual que en la Parte 1, pero ahora en ambas direcciones — reenganchando el mismo hilo de chat.

**Fuera de alcance en esta parte:** no vas a construir un agente nuevo ni a cambiar sus herramientas o su memoria. El agente de soporte que ya tienes es el mismo — lo que cambia es cómo se comunica con el usuario.

---

## 🌱 Cómo Empezar el Proyecto

Sigue trabajando en el fork del monorepo de tu empresa que has usado a lo largo del programa (y la Parte 1 de este proyecto). Si por alguna razón aún no tienes tu fork, créalo ahora desde el [monorepo base](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Crea una rama nueva desde tu rama principal: `feature/websocket-chat`.
2. Ubica el endpoint o función que hoy invoca a tu agente de soporte con un patrón de petición/respuesta tradicional — extiende esa ruta; no crees una app paralela ni una carpeta de entrega.
3. Revisa tu `CONTEXT-company.md` (en `10-realtime/communication/`) para confirmar qué agente vas a conectar y los nombres de sesión / eventos de esta parte — reutiliza la _disciplina_ de nombres de la Parte 1, no los esquemas RFP/SSE de la Parte 1.
4. Repasa cómo tu agente expone el streaming (modos `messages`, `values`, `updates` o `custom` de LangGraph) antes de decidir cuál necesitas para transmitir tokens.
5. Implementa en el layout existente: WebSocket en `services/`, UI de chat en `uis/`, pruebas en `tests/`.

Si necesitas un repaso de cómo montar un proyecto, mira [cómo empezar un proyecto de código](https://4geeks.com/lesson/how-to-start-a-project).

---

## 💻 Qué Debes Hacer

**Backend (`services/`)**

- [ ] Implementa un endpoint WebSocket que acepte una conexión persistente por sesión de chat
- [ ] Protege el socket con el **mismo JWT** que usa la API del backoffice (y el SSE de la Parte 1). Pasa el token al conectar vía query string (p. ej. `?token=…`) y/o un primer frame de auth del cliente — los navegadores no pueden poner `Authorization` limpio en el handshake WebSocket. Rechaza conexiones sin autenticación antes de cualquier evento de chat
- [ ] Exige `session_id` (y/o LangGraph `thread_id`) en el handshake / URL para que el socket quede ligado a un hilo de conversación existente
- [ ] Transmite la respuesta del agente token por token a través de esa conexión, usando el modo de streaming de LangGraph que corresponda
- [ ] Ante una interrupción del cliente: **aborta el stream en curso** para que no se produzcan más eventos `token_chunk` de esa generación (cancela la tarea / detén el stream del modelo). **No** uses LangGraph `interrupt()` HITL como sustituto del abort del stream — usa `interrupt()` solo si además necesitas una pausa de grafo aparte
- [ ] Tras el abort: marca el mensaje parcial del asistente como `interrupted` (conserva los tokens ya mostrados), acepta la nueva entrada del usuario y arranca un **turno nuevo** del asistente — no borres ni sobrescribas en el sitio el mensaje interrumpido
- [ ] Desacopla la producción de eventos del agente de las conexiones WebSocket que los consumen usando un patrón pub/sub — no es obligatorio un backplane externo como Redis para esta entrega, pero el patrón productor/consumidor sí es evaluado

⚠️ **IMPORTANTE:** los nombres de campos y entidades del chat deben coincidir con tu CONTEXT de la Parte 2. Una implementación genérica que ignore el contexto no será aceptada. No mezcles los payloads de notificación RFP de la Parte 1 en este contrato WebSocket.

**Frontend (`uis/`)**

- [ ] Conecta la interfaz de chat existente por WebSocket en lugar de una llamada de petición/respuesta única
- [ ] Renderiza la respuesta del agente a medida que llegan los tokens (efecto de escritura en vivo, no un reemplazo del mensaje completo al final)
- [ ] Agrega un control de interrupción (por ejemplo, poder enviar un nuevo mensaje mientras el agente todavía está respondiendo) que dispare la señal de abort al backend; deja visible el mensaje parcial marcado como interrumpido; muestra la respuesta redirigida como un mensaje nuevo
- [ ] Implementa reconexión con backoff progresivo: al reconectar, envía el mismo `session_id` / `thread_id` y **rehidrata** la conversación desde checkpoint y/o historial de mensajes antes de aceptar tokens nuevos — “sin perder el hilo” significa restaurar contexto, no solo reabrir un socket

**Pruebas (`tests/`)**

- [ ] Prueba(s) unitaria(s) que verifiquen el contrato de eventos del WebSocket (`token_chunk`, interrupt / `generation_interrupted`, `generation_completed`)
- [ ] Prueba o verificación manual documentada de que una interrupción a mitad de respuesta detiene más tokens de la generación original, deja el mensaje parcial marcado como `interrupted`, y que la siguiente respuesta es un turno nuevo que refleja `new_input`
- [ ] Prueba o verificación manual documentada de que reconectar con el mismo `session_id` restaura el hilo de conversación (historial / checkpoint), no un chat vacío

---

## 🤔 Preguntas de Diseño

Antes de dar por cerrada la implementación, piensa y documenta tu respuesta a estas preguntas en tu PR:

- ¿Por qué esta funcionalidad necesita WebSockets y no te alcanza con lo que construiste en la Parte 1? ¿Qué parte del requisito obliga específicamente a un canal bidireccional?
- Si más de un cliente está suscrito a la misma sesión de chat (por ejemplo, un supervisor observando la conversación en vivo), ¿cómo te aseguras de que todos reciban los mismos eventos sin duplicar las llamadas al agente?
- ¿Cómo separaste el **abort del stream** (parar tokens) de LangGraph HITL `interrupt()` (pausa de grafo), si usaste lo segundo? ¿Qué pasa con el mensaje parcial del asistente y con el siguiente turno?

---

## ✅ Qué Evaluaremos

- [ ] La interfaz de chat muestra los tokens de la respuesta conforme se generan, no la respuesta completa de una sola vez
- [ ] El WebSocket exige el mismo JWT que el backoffice (query param y/o primer frame de auth); se rechazan clientes sin autenticación
- [ ] El WebSocket queda ligado a una conversación existente vía `session_id` y/o LangGraph `thread_id` en el handshake o la URL
- [ ] Enviar una interrupción a mitad de una respuesta aborta de forma medible la generación original (sin más tokens), conserva el mensaje parcial marcado como `interrupted`, y la siguiente respuesta del agente es un turno nuevo que refleja la nueva entrada
- [ ] El WebSocket se reconecta tras una caída con el mismo `session_id` / `thread_id` y rehidrata desde checkpoint o historial — el hilo de conversación no se pierde
- [ ] La producción de eventos del agente está desacoplada de los consumidores WebSocket vía un patrón pub/sub (o productor/consumidor equivalente); los eventos están nombrados y estructurados, no son un único tipo de mensaje genérico
- [ ] Los nombres de campos y entidades coinciden con los definidos en el CONTEXT.md de la Parte 2 de tu empresa

---

## 📦 Cómo Entregar Este Proyecto

Esta es la Parte 2 de 2. Entrégala con su propio Pull Request contra tu rama principal — independiente de la Parte 1.

1. Haz commit y push de tu rama `feature/websocket-chat` (el código vive en `services/`, `uis/` y `tests/` — **no** crees una carpeta de entrega aparte)
2. Abre un Pull Request describiendo qué implementaste y cómo probar el streaming de tokens y la interrupción
3. Incluye en la descripción del PR tus respuestas a las Preguntas de Diseño
4. Solicita revisión a tu tech lead

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
