# Hito 10 — Sistemas en Tiempo Real (Parte 2 de 2): Streaming de Chat por WebSocket

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/10-realtime/communication)** antes de escribir código — ahí se define qué agente vas a conectar y qué convenciones de eventos ya usaste en la Parte 1.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

En la Parte 1 resolviste la mitad del problema: el backend avisa al frontend cuando pasa algo, sin que nadie tenga que preguntar. Pero esa notificación va en una sola dirección. El agente de soporte de tu empresa hoy funciona igual: el usuario envía un mensaje, espera, y recibe la respuesta completa de una sola vez. Si el agente se está yendo por el camino equivocado, el usuario no tiene forma de decírselo hasta que termina de responder.

El equipo de soporte abrió un **RFI**: quieren saber por qué el chat no se siente como una conversación real. Tu tech lead lo convirtió en un **ticket** para tu squad:

> **Contexto:** el agente de soporte ya existe y funciona — no vas a tocar su lógica interna ni sus herramientas.
> **Qué necesito que construyas:** que la respuesta del agente llegue token por token en tiempo real, y que el usuario pueda interrumpirlo a mitad de una respuesta y redirigirlo, sin esperar a que termine.
> **Acceptance criteria:** el canal debe ser bidireccional (el cliente también envía datos, no solo recibe), los tokens deben streamearse conforme se generan, y una interrupción debe detener genuinamente la generación en curso — no solo ignorar la respuesta cuando llega.

Algunos requisitos quedan implícitos y tendrás que identificarlos con cuidado: SSE (lo que usaste en la Parte 1) ya no alcanza porque el cliente necesita hablar de vuelta mientras el servidor sigue enviando datos; el streaming de tokens y el manejo de la interrupción deben convivir en el mismo canal sin pisarse; y la conexión debe recuperarse si se cae, igual que en la Parte 1, pero ahora en ambas direcciones.

**Fuera de alcance en esta parte:** no vas a construir un agente nuevo ni a cambiar sus herramientas o su memoria. El agente de soporte que ya tienes es el mismo — lo que cambia es cómo se comunica con el usuario.

---

## 🌱 Cómo Empezar

1. Ubica el endpoint o función que hoy invoca a tu agente de soporte con un patrón de petición/respuesta tradicional.
2. Revisa tu `CONTEXT-company.md` para confirmar qué agente vas a conectar y qué eventos ya definiste en la Parte 1 — reutiliza esa convención de nombres, no la reinventes.
3. Repasa cómo tu agente expone el streaming (modos `messages`, `values`, `updates` o `custom` de LangGraph) antes de decidir cuál necesitas para transmitir tokens.
4. Crea una rama de trabajo para esta parte.

---

## 💻 Qué Debes Hacer

**Backend (`services/`)**

- [ ] Implementa un endpoint WebSocket que acepte una conexión persistente por sesión de chat
- [ ] Transmite la respuesta del agente token por token a través de esa conexión, usando el modo de streaming de LangGraph que corresponda
- [ ] Implementa la recepción de un mensaje de interrupción desde el cliente: al llegar, debe pausar la generación en curso (usando `interrupt()` y el checkpointing que ya conoces) y aceptar una nueva entrada para retomar el flujo
- [ ] Desacopla la producción de eventos del agente de las conexiones WebSocket que los consumen usando un patrón pub/sub — no es obligatorio un backplane externo como Redis para esta entrega, pero el patrón productor/consumidor sí es evaluado

⚠️ **IMPORTANTE:** reutiliza los mismos nombres de evento y convenciones de payload que definiste en la Parte 1 cuando apliquen (por ejemplo, si necesitas identificar la sesión o el ticket relacionado). No inventes un esquema paralelo.

**Frontend (`uis/`)**

- [ ] Conecta la interfaz de chat existente por WebSocket en lugar de una llamada de petición/respuesta única
- [ ] Renderiza la respuesta del agente a medida que llegan los tokens (efecto de escritura en vivo, no un reemplazo del mensaje completo al final)
- [ ] Agrega un control de interrupción (por ejemplo, poder enviar un nuevo mensaje mientras el agente todavía está respondiendo) que dispare la señal de interrupción hacia el backend
- [ ] Implementa reconexión si la conexión WebSocket se cae, con la misma disciplina de backoff que usaste en la Parte 1

**Pruebas (`tests/`)**

- [ ] Prueba(s) unitaria(s) que verifiquen el contrato de eventos del WebSocket (evento de token, evento de interrupción, evento de finalización)
- [ ] Prueba o verificación manual documentada de que una interrupción enviada a mitad de una respuesta efectivamente detiene la generación original y el agente responde a la nueva entrada

---

## 🤔 Preguntas de Diseño

Antes de dar por cerrada la implementación, piensa y documenta tu respuesta a estas preguntas en tu PR:

- ¿Por qué esta funcionalidad necesita WebSockets y no te alcanza con lo que construiste en la Parte 1? ¿Qué parte del requisito obliga específicamente a un canal bidireccional?
- Si más de un cliente está suscrito a la misma sesión de chat (por ejemplo, un supervisor observando la conversación en vivo), ¿cómo te aseguras de que todos reciban los mismos eventos sin duplicar las llamadas al agente?
- ¿Qué pasa con el trabajo que el agente ya había generado cuando llega una interrupción? ¿Se descarta, se guarda, o se reutiliza parcialmente en el siguiente turno? ¿Qué decidiste y por qué?

---

## ✅ Qué Evaluaremos

- [ ] La interfaz de chat muestra los tokens de la respuesta conforme se generan, no la respuesta completa de una sola vez
- [ ] Enviar una interrupción a mitad de una respuesta detiene de forma medible la generación original, y la siguiente respuesta del agente refleja la nueva entrada
- [ ] La conexión WebSocket se reconecta tras una caída sin perder el hilo de la conversación
- [ ] Los eventos entre el agente, la capa pub/sub y los clientes WebSocket están nombrados y estructurados, no son un único tipo de mensaje genérico
- [ ] Los nombres de campos y entidades coinciden con los definidos en el CONTEXT.md de tu empresa y son consistentes con lo que usaste en la Parte 1

---

## 📦 Cómo Entregar

1. Haz commit y push de tu trabajo a tu fork del monorepo, dentro de la carpeta correspondiente a este proyecto (`parte-2-realtime-ws/`).
2. Abre un Pull Request contra tu propia rama principal, independiente del de la Parte 1.
3. Incluye en la descripción del PR tus respuestas a las Preguntas de Diseño.
4. Solicita revisión a tu tech lead.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
