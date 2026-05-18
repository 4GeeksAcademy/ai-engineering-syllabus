# Ejemplo en Clase: Conecta tu Agente a Discord y Notion

> **Nota para el instructor:** Este es un ejemplo en vivo para clase que enseña los conceptos del proyecto `openclaw-connection`. Usa este escenario en clase para guiar a los estudiantes por la configuración de canales de un agente y la integración con servicios externos mediante MCP. **No lo asignes como tarea — es un ejercicio guiado en el aula.**

_These instructions are also available in [English](./README.md)._

---

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


Un grupo de estudio de un bootcamp usa **Discord** como canal de comunicación principal y **Notion** para mantener apuntes compartidos. Quieren que su asistente OpenClaw viva dentro de Discord para que los miembros puedan hacerle preguntas y que automáticamente cree páginas en Notion con resúmenes de las sesiones de estudio.

Tu tarea: conectar una instancia existente de OpenClaw a Discord y a Notion (mediante el MCP de Zapier), y verificar que el flujo completo funciona de extremo a extremo.

**Qué vas a aprender:**
- Cómo crear un token de bot y registrarlo en una plataforma de mensajería externa
- Qué hace un servidor MCP (Model Context Protocol) y cómo actúa como puente de habilidades
- Cómo el MCP de Zapier expone integraciones de servicios preconstruidas como habilidades invocables
- Cómo verificar una integración de agente de extremo a extremo sin escribir código de aplicación

---

## Requisitos previos

- Una instancia de OpenClaw en funcionamiento (del ejercicio `openclaw-setup`)
- Una cuenta personal de Discord
- Una cuenta gratuita en Zapier
- Una cuenta gratuita en Notion (usa un espacio de trabajo de prueba, no el personal)

---

## Tareas Paso a Paso

### 1. Crear el Bot de Discord

- [ ] Ve a [https://discord.com/developers/applications](https://discord.com/developers/applications) y crea una nueva aplicación
- [ ] Ve a la pestaña **Bot**, habilita el bot y copia su **token**
- [ ] En **OAuth2 → URL Generator**, selecciona el scope `bot` con permiso `Send Messages` e invita el bot a un servidor de Discord de prueba que seas el/la dueño/a
- [ ] En OpenClaw, añade Discord como canal de mensajería del agente usando el token del bot
- [ ] Envía un mensaje de prueba en Discord y confirma que el agente responde

### 2. Configurar el MCP de Zapier

- [ ] Crea una cuenta gratuita en Zapier en [https://zapier.com](https://zapier.com)
- [ ] Navega a la configuración de MCP de Zapier y genera una URL de endpoint MCP
- [ ] En OpenClaw, añade el MCP de Zapier usando esa URL de endpoint
- [ ] Confirma que el MCP aparece como proveedor activo de habilidades en la configuración del agente

### 3. Conectar Notion mediante Zapier

- [ ] En Zapier, conecta tu cuenta de Notion (espacio de trabajo de prueba)
- [ ] Habilita la acción "Create Notion page" (crear página en Notion) a través del MCP de Zapier
- [ ] Verifica que el agente liste "crear página en Notion" como una habilidad disponible

### 4. Prueba de Extremo a Extremo

- [ ] En Discord, envía al agente un mensaje como: _"Crea una página en Notion con el título 'React Hooks — Resumen de Clase' y una nota que diga que cubrimos useState y useEffect"_
- [ ] Si el agente pide aclaraciones, responde y continúa
- [ ] Confirma que aparece una nueva página en el espacio de trabajo de Notion conectado
- [ ] Confirma que el agente responde en Discord indicando que la página fue creada

### 5. Evidencia en Capturas de Pantalla

- [ ] Canal de Discord mostrando la conversación (solicitud → respuesta del agente)
- [ ] Configuración de OpenClaw mostrando Discord conectado
- [ ] Configuración de OpenClaw mostrando el MCP de Zapier activo
- [ ] Página de Notion que fue creada

---

## Preguntas de Discusión

1. ¿Cuál es la diferencia entre conectar un **canal de mensajería** (Discord) y conectar un **proveedor de habilidades MCP** (Zapier)? ¿Por qué se configuran por separado?
2. El agente usa el MCP de Zapier para crear páginas en Notion sin que hayas escrito ningún código de la API de Notion. ¿Cuáles son las ventajas y desventajas de usar un conector genérico como Zapier frente a construir una integración directa?
3. Si el mensaje del usuario es ambiguo (por ejemplo, "guarda lo que acabamos de hablar"), ¿qué debería ocurrir? ¿Cómo diseñarías el system prompt o el comportamiento del agente para manejar esto correctamente?
