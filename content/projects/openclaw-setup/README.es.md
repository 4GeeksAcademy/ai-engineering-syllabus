# Configurando tu Agente de IA Personal con OpenClaw

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/openclaw/openclaw/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de comenzar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Llevas tiempo usando herramientas de IA de terceros como los chats comerciales. Funcionan, pero nunca son del todo tuyas. Quieres un asistente de IA propio — autoalojado en un VPS, privado, configurable a tu gusto y que puedas adaptar según la tarea. Sin depender de plataformas externas. Tuyo.

La herramienta que vas a usar es **OpenClaw**. Tu objetivo es desplegar y configurar una instancia funcional en un VPS, conectarla a un modelo de IA a través de LiteLLM y verificar que responde correctamente en el chat local.

Este no es un proyecto de código — es una tarea de infraestructura y configuración. El resultado principal es un sistema funcionando, no un repositorio. Dicho esto, si en algún momento personalizas el código de OpenClaw, un repositorio es el lugar correcto para registrar esos cambios — los buenos ingenieros versionan su trabajo. Por ahora, usarás un repositorio para documentar tu configuración con una captura de pantalla y un archivo de configuración como evidencia de entrega.

> **Antes de empezar, asegúrate de entender:**
>
> - OpenClaw solo es útil si tiene un modelo conectado. Sin él, no hace nada. Parte de montar tu propio asistente es elegir qué modelo usar para cada tarea — no siempre el más potente, sino el más adecuado según el contexto, el coste y los requisitos de latencia.
> - OpenClaw **no** es un entorno multi-tenant. Cualquier persona con acceso a la URL de tu VPS puede usarlo. Nunca lo expongas públicamente sin autenticación.
> - Sigue siempre la guía de instalación de 4Geeks. El orden de los pasos de configuración importa — saltarlos o reordenarlos provoca errores difíciles de depurar.

Ponlo a correr.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no usa un repositorio de inicio — es un proyecto de configuración de servidor. Sigue estos pasos para comenzar:

1. Accede al VPS proporcionado por la plataforma (las credenciales se compartirán por la plataforma del curso).
2. Conéctate al VPS usando tu editor Codespaces o VS Code para poder recibir ayuda de Copilot si la necesitas. También puedes conectarte al VPS mediante SSH desde tu terminal:

   ```bash
   ssh tu_usuario@ip_de_tu_vps
   ```

3. Sigue la guía de instalación de OpenClaw de 4Geeks (lee la lección de "Configurando Tu Asistente AI Personal") paso a paso — no omitas ninguna fase.
4. Crea un **nuevo repositorio en GitHub** llamado `openclaw-setup-<tu_usuario_github>` para almacenar los archivos de entrega (captura de pantalla + configuración).

> Si vas a trabajar en local en lugar de en un VPS, confírmalo con tu instructor primero. Los pasos de instalación son diferentes.

---

## 💻 Qué debes hacer

### Acceso al VPS por SSH

- [ ] Conectarte exitosamente al VPS por SSH desde tu editor de código o tu terminal local.
- [ ] Confirmar el sistema operativo y los recursos disponibles del servidor antes de iniciar la instalación.

### Instalación de OpenClaw

- [ ] Instalar OpenClaw en el VPS siguiendo la guía de instalación de 4Geeks.

### Configuración básica (en orden)

- [ ] Configurar el **proveedor LiteLLM** como backend de modelo.
- [ ] Ingresar una **API Key** válida del proveedor de modelo elegido.
- [ ] Saltar el paso de configuración de Skills (se abordará en una sesión futura).
- [ ] Habilitar los **hooks** cuando se solicite durante la configuración.
- [ ] Saltar el paso de Channel Workflows (se abordará en una sesión futura).
- [ ] Abrir **Try Local Chat** y enviar un mensaje de prueba para confirmar que la instancia responde.

### Personalizando tu Asistente

Ahora que OpenClaw está funcionando, es momento de hacerlo verdaderamente tuyo. En lugar de editar archivos de configuración manualmente, **conversarás con OpenClaw mismo** para personalizarlo.

- [ ] Abre la interfaz de chat local nuevamente.
- [ ] Pídele a OpenClaw que configure los siguientes atributos personales conversando con él:
  - **Name (Nombre):** El nombre de tu asistente (ej: "Name: Kai")
  - **Emoji:** El avatar que representa a tu agente (ej: "Emoji: 🤖")
  - **Greeting (Saludo):** El mensaje inicial al comenzar un chat (ej: "Greeting: ¡Hola!")

> **Consejo:** Puedes decir algo como: _"Quiero configurarte. Establece tu nombre como Kai, tu emoji como 🤖 y tu saludo como '¡Hola, soy Kai, ¿en qué puedo ayudarte hoy?'"_

- [ ] Una vez configurado, localiza el archivo `.openclaw/IDENTITY.md` en tu servidor.
- [ ] Revísalo para confirmar que tu personalización se aplicó correctamente.
- [ ] Copia el archivo `.openclaw/IDENTITY.md` a tu máquina local e inclúyelo en tu repositorio de entrega.

⚠️ **ADVERTENCIA DE SEGURIDAD:** Nunca subas a GitHub archivos que contengan API keys, tokens, credenciales o datos sensibles. El archivo `.openclaw/IDENTITY.md` es seguro para compartir porque solo contiene datos de personalización pública (Name, Emoji, Greeting). Sin embargo, **nunca subas** archivos como `openclaw.json`, `.env`, archivos de configuración con secretos, o cualquier archivo que contenga información sensible.

### Evidencia de entrega

- [ ] Tomar una captura de pantalla del chat local de OpenClaw que muestre una respuesta exitosa de la IA.
- [ ] Añadir la captura a tu repositorio de GitHub como `proof.png` (o `.jpg`).
- [ ] Añadir el archivo `.openclaw/IDENTITY.md` a tu repositorio (esto demuestra que personalizaste exitosamente tu asistente).
- [ ] Añadir un `README.md` a tu repositorio con: el proveedor de VPS utilizado, el modelo elegido y una frase explicando por qué seleccionaste ese modelo para un asistente de propósito general.

---

## ✅ Qué vamos a evaluar

- [ ] OpenClaw está correctamente instalado y accesible en el VPS.
- [ ] El proveedor LiteLLM está configurado y conectado a un modelo de IA funcional.
- [ ] El chat local devuelve una respuesta válida de la IA (evidenciado por la captura de pantalla).
- [ ] El archivo `.openclaw/IDENTITY.md` está presente en el repositorio mostrando Name, Emoji y Greeting personalizados.
- [ ] La personalización se realizó conversando con OpenClaw (no editando archivos manualmente).
- [ ] El `README.md` de entrega incluye los campos requeridos: proveedor de VPS, nombre del modelo y justificación de la elección del modelo.
- [ ] Se utilizó SSH para conectarse al VPS (no una consola web ni herramienta gráfica).
- [ ] Los pasos de configuración se siguieron en el orden correcto según la guía de 4Geeks.

> Nota: El instructor puede verificar la personalización del asistente directamente en el servidor para asegurar que la configuración se aplicó correctamente.

---

## 📦 Cómo entregar

Sube tu repositorio a GitHub (debe contener `proof.png`, `.openclaw/IDENTITY.md` y un `README.md` con la documentación de tu VPS/modelo) y comparte el enlace siguiendo las instrucciones de tu instructor.

⚠️ **ANTES DE HACER PUSH:** Verifica dos veces que NO estás subiendo ningún archivo con API keys, tokens, credenciales o configuración sensible. Solo sube:

- `proof.png` (captura de pantalla)
- `.openclaw/IDENTITY.md` (seguro - solo Name, Emoji, Greeting)
- `README.md` (tu documentación)

**Nunca subas:** `openclaw.json`, `.env`, archivos de credenciales, o cualquier configuración que contenga secretos.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
