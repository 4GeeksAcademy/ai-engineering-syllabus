# Ejemplo en Clase: Despliega OpenClaw como Asistente de Soporte al Cliente

> **Nota para el instructor:** Este es un ejemplo en vivo para clase que enseña los conceptos del proyecto `openclaw-setup`. Usa este escenario en clase para guiar a los estudiantes por el acceso a un VPS mediante SSH, la instalación de OpenClaw y la configuración de LiteLLM. **No lo asignes como tarea — es un ejercicio guiado en el aula.**

_These instructions are also available in [English](./README.md)._

---

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


Una pequeña librería online quiere desplegar un asistente de IA autoalojado para responder las preguntas más comunes de sus clientes (estado de pedidos, política de devoluciones, recomendaciones de libros). No quieren pagar una suscripción a un chatbot SaaS y prefieren mantener sus datos en su propio servidor.

Tu tarea: desplegar y configurar OpenClaw en un VPS, conectarlo a un modelo de IA a través de LiteLLM, y verificar que puede responder a una pregunta de cliente en el chat local.

**Qué vas a aprender:**
- Cómo conectarse de forma segura a un servidor remoto mediante SSH
- Qué hace LiteLLM y por qué se usa como proxy de modelos
- Cómo el archivo de configuración de OpenClaw controla la identidad del agente y el modelo
- Cómo verificar un servicio de IA en funcionamiento antes de compartirlo con otros

---

## Requisitos previos

- Credenciales de VPS proporcionadas por el instructor
- Un terminal o VS Code con la extensión SSH
- Una API key para un proveedor de modelos (por ejemplo, OpenAI, Groq o Mistral — usa la que se indique en clase)

---

## Tareas Paso a Paso

### 1. Conectarse al VPS por SSH

- [ ] Abre tu terminal y ejecuta:

  ```bash
  ssh tu_usuario@ip_de_tu_vps
  ```

- [ ] Confirma que has iniciado sesión y comprueba el espacio en disco y la memoria disponibles:

  ```bash
  df -h && free -h
  ```

### 2. Instalar OpenClaw

- [ ] Sigue la guía de instalación de OpenClaw de 4Geeks paso a paso
- [ ] No omitas ni reordenes ninguna fase

### 3. Configurar el Agente

Sigue este orden de configuración — no te saltes ningún paso:

- [ ] Configura el **proveedor LiteLLM** como backend de modelo
- [ ] Introduce una **API key** válida del proveedor de modelo elegido
- [ ] Salta el paso de Skills (no es necesario para este ejercicio)
- [ ] Habilita los **hooks** cuando se solicite
- [ ] Salta el paso de Channel Workflows (no es necesario para este ejercicio)
- [ ] Dale al agente un nombre de persona y un system prompt breve, por ejemplo:
  > "Eres un asistente de ayuda para una pequeña librería online. Responde las preguntas de los clientes sobre pedidos, devoluciones y recomendaciones de libros de forma amable y concisa."

### 4. Verificar que el Agente Responde

- [ ] Abre **Try Local Chat** en la interfaz de OpenClaw
- [ ] Envía un mensaje de prueba estilo cliente, por ejemplo: _"¿Cuál es vuestra política de devoluciones para libros dañados?"_
- [ ] Confirma que el agente responde en el personaje configurado

### 5. Revisar el Archivo de Configuración

- [ ] Localiza `openclaw.json` en el servidor
- [ ] Lee el archivo e identifica qué campos controlan: el proveedor de modelo, la API key y el system prompt
- [ ] Copia el archivo a tu máquina local

> ⚠️ Antes de guardar `openclaw.json` en ningún sitio, reemplaza cualquier API key real con un marcador de posición: `"api_key": "YOUR_KEY_HERE"`

---

## Referencia de Configuración

| Campo | Qué controla |
|---|---|
| `model_provider` | Qué backend de LiteLLM se usa |
| `api_key` | Credencial para el proveedor de modelos |
| `system_prompt` | La personalidad e instrucciones del agente |
| `hooks_enabled` | Si OpenClaw ejecuta hooks de ciclo de vida |

---

## Preguntas de Discusión

1. ¿Por qué es importante establecer un system prompt al desplegar un asistente de IA para un negocio específico? ¿Qué ocurre si lo dejas vacío?
2. OpenClaw no es un sistema multi-tenant — cualquier persona con la URL del VPS puede usarlo. ¿Qué opciones de autenticación añadirías antes de exponerlo a clientes reales?
3. Has elegido un modelo de IA específico para este asistente. ¿Qué criterios usarías para decidir entre un modelo rápido y barato y uno más capaz pero costoso para un caso de uso de soporte al cliente?
