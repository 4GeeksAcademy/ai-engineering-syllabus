# Conecta tu Agente: Telegram, Google Drive y Calendario

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/openclaw-integrations/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto.

<!-- endhide -->

---

## 🎯 Tu reto

La pequeña consultora donde configuraste OpenClaw como asistente de IA interno está lista para el siguiente paso. El team lead quedó satisfecho con la configuración básica — el agente funciona, responde, tiene personalidad. Ahora quieren que haga cosas.

Esta mañana llegó el pedido: conectar el agente a las herramientas que el equipo ya usa para que cualquier miembro pueda delegar tareas simples directamente desde su teléfono. Sin dashboards, sin interfaces complejas — solo un mensaje por **Telegram** y el agente se encarga del resto.

> El team lead envió este mensaje por Slack:
>
> > "El agente está funcionando muy bien como asistente básico. Ahora hagámoslo útil. Conéctalo a Google Drive y Google Calendar, y conéctalo a Telegram para que podamos hablarle desde cualquier lugar. Quiero probarlo yo mismo: le voy a mandar un mensaje pidiéndole que cree un documento, y espero que cree el doc, bloquee tiempo en mi calendario para revisarlo y me confirme en Telegram que ya está hecho. Nada complicado, solo un flujo que funcione de punta a punta."

Para integrar Google Drive y Google Calendar rápidamente sin construir conectores propios, usarás el **MCP de Zapier** — un puente que expone las acciones preconstruidas de Zapier como skills que tu agente puede invocar directamente. No es la única forma de conectar estos servicios, pero es el camino más rápido hacia un prototipo funcional.

Este proyecto es de **configuración, no de código**. Estás ensamblando un agente funcional a partir de servicios y conectores ya existentes. Piensa en cómo cada integración convierte una API de terceros en una habilidad que tu agente puede usar — porque eso es exactamente lo que estás haciendo.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no requiere hacer fork de un repositorio de código. En su lugar, vas a configurar un agente en OpenClaw y conectarlo con servicios externos.

1. Asegúrate de tener una instancia activa de **OpenClaw** en funcionamiento (configurada en el [proyecto openclaw-setup](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/projects/openclaw-setup)).
2. Crea un **bot de Telegram** con BotFather si aún no lo tienes.
3. Crea una cuenta en **Zapier** (el plan gratuito es suficiente) y configura la conexión MCP.
4. Conecta **Google Drive** y **Google Calendar** mediante las integraciones preconstruidas de Zapier.
5. Documenta los pasos de tu configuración y toma capturas de pantalla como evidencia de cada conexión.

> ⚠️ **IMPORTANTE:** No conectes cuentas personales con información sensible o privada a OpenClaw en este ejercicio. Usa una cuenta de prueba para Google Drive y Google Calendar. Nunca expongas tokens o claves de API en capturas de pantalla ni en archivos enviados.

---

## 💻 Qué debes hacer

### Conexión con Telegram

- [ ] Crear un bot de Telegram usando BotFather y obtener su token
- [ ] Configurar OpenClaw para usar Telegram como canal de mensajería
- [ ] Validar la conexión: enviar un mensaje de prueba y confirmar que el agente responde

### Configuración del MCP de Zapier

- [ ] Crear una cuenta en Zapier y localizar la opción de configuración del MCP
- [ ] Agregar el MCP de Zapier al agente en OpenClaw
- [ ] Conectar Google Drive a través de Zapier y verificar que el agente puede crear documentos
- [ ] Conectar Google Calendar a través de Zapier y verificar que el agente puede crear eventos

### Flujo completo de punta a punta

- [ ] Enviar un mensaje por Telegram pidiendo al agente que cree un documento (especificar título o tema)
- [ ] Si el agente necesita información adicional para completar la tarea, verificar que la solicita antes de continuar
- [ ] Verificar que se crea un nuevo documento en Google Drive
- [ ] Verificar que se crea un evento en el calendario para reservar tiempo para revisar el documento
- [ ] Confirmar que el agente envía un mensaje por Telegram reportando que la tarea se completó

### Evidencias y entrega

- [ ] Captura de pantalla de cada integración conectada correctamente en OpenClaw
- [ ] Captura de pantalla de la conversación completa en Telegram (solicitud → preguntas del agente si las hay → confirmación)
- [ ] Captura de pantalla del documento creado en Google Drive
- [ ] Captura de pantalla del evento creado en el calendario

> ⚠️ **IMPORTANTE:** Difumina o recorta cualquier información personal (nombres completos, direcciones de correo) en tus capturas antes de enviarlas.

---

## ✅ Qué vamos a evaluar

- [ ] El bot de Telegram está correctamente creado y conectado a OpenClaw
- [ ] El MCP de Zapier está agregado y activo en la configuración del agente
- [ ] La integración con Google Drive funciona: el agente crea un documento en respuesta a la solicitud del usuario
- [ ] La integración con Google Calendar funciona: el agente crea un evento vinculado a la revisión del documento
- [ ] El agente confirma la finalización de la tarea por Telegram
- [ ] El agente solicita información faltante cuando el mensaje del usuario no es suficientemente específico
- [ ] Las capturas de pantalla documentan cada integración y la conversación completa de punta a punta
- [ ] No se exponen credenciales ni datos personales en los materiales entregados

> Nota: La calidad o el tono de las respuestas del agente no se evalúan. Lo que importa es que el flujo se ejecute correctamente de punta a punta.

---

## 📦 Cómo entregar

Crea una carpeta llamada `openclaw-connection` que contenga:

- Todas las capturas de pantalla (nombradas con claridad, p.ej. `01-telegram-conectado.png`, `02-zapier-mcp.png`, etc.)
- Un archivo corto `notes.md` (5–10 líneas) describiendo las decisiones de configuración que tomaste o los problemas que encontraste

Comparte la carpeta como archivo ZIP o enlace a un repositorio de GitHub según las instrucciones de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
