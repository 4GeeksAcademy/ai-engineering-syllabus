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
2. Conéctate al VPS usando tu editor VS Code para poder recibir ayuda de Copilot si la necesitas. También puedes conectarte al VPS mediante SSH desde tu terminal:

   ```bash
   ssh tu_usuario@ip_de_tu_vps
   ```

3. Sigue la guía de instalación de OpenClaw de 4Geeks (lee la lección de "Configurando Tu Asistente AI Personal") paso a paso — no omitas ninguna fase.

> Si vas a trabajar en local en lugar de en un VPS, confírmalo con tu instructor primero. Los pasos de instalación son diferentes.

---

## 💻 Qué debes hacer

### Acceso al VPS por SSH

- [ ] Conectarte exitosamente al VPS por SSH desde tu editor de código o tu terminal local.
- [ ] Confirmar el sistema operativo y los recursos disponibles del servidor antes de iniciar la instalación.

### Instalación de OpenClaw

- [ ] Instalar OpenClaw en el VPS siguiendo la guía de instalación de 4Geeks.

### Configuración básica (en orden)

- [ ] Configurar el **proveedor LiteLLM** como proveedor de modelo.
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

- [ ] Una vez configurado, verifica que tu personalización se aplicó correctamente revisando el saludo en la interfaz de chat.

### Configurando el Respaldo en GitHub

OpenClaw crea una carpeta workspace en `~/.openclaw/workspace` donde almacena la configuración de tu asistente y el historial de chats. Subirás este workspace a GitHub como tu entrega del proyecto.

#### Paso 1: Crear SSH Key en el Servidor

> **Guía de GitHub:** Para el tutorial oficial (generación de la clave, frase de contraseña y añadir la clave al `ssh-agent` en Linux), consulta [Generación de una nueva clave SSH y adición al agente SSH](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

- [ ] Genera una clave SSH en tu VPS:

  ```bash
  ssh-keygen -t ed25519 -C "tu_email_en_github@example.com"
  ```

- [ ] Presiona Enter para aceptar la ubicación por defecto.
- [ ] Presiona Enter dos veces para omitir la contraseña (opcional, pero recomendado para automatización).
- [ ] Muestra tu clave pública:

  ```bash
  cat ~/.ssh/id_ed25519.pub
  ```

- [ ] Copia toda la salida (comienza con `ssh-ed25519`).

#### Paso 2: Añadir SSH Key a GitHub

- [ ] Ve a [Configuración SSH de GitHub](https://github.com/settings/keys).
- [ ] Haz clic en **"New SSH key"**.
- [ ] Dale un título (ej: "OpenClaw VPS").
- [ ] Pega tu clave pública en el campo "Key".
- [ ] Haz clic en **"Add SSH key"**.

#### Paso 3: Crear Repositorio en GitHub

- [ ] Ve a [GitHub](https://github.com/new) y crea un **nuevo repositorio**.
- [ ] Nómbralo: `openclaw-<tu_usuario_github>` (reemplaza con tu usuario real).
- [ ] Hazlo **Público** o **Privado** (a tu elección).
- [ ] **NO** inicialices con README, .gitignore, o licencia.
- [ ] Haz clic en **"Create repository"**.

#### Paso 4: Conectar Workspace a GitHub

- [ ] En tu VPS, navega al workspace de OpenClaw:

  ```bash
  cd ~/.openclaw/workspace
  ```

- [ ] Inicializa git si no está ya inicializado:

  ```bash
  git init
  git branch -M main
  ```

- [ ] Añade el remote de GitHub (reemplaza con la URL de tu repositorio):

  ```bash
  git remote add origin git@github.com:tu_usuario/openclaw-tu_usuario.git
  ```

- [ ] Añade todos los archivos:

  ```bash
  git add .
  ```

- [ ] Haz commit de tus cambios:

  ```bash
  git commit -m "Configuración inicial de OpenClaw con identidad personalizada"
  ```

- [ ] Sube a GitHub:

  ```bash
  git push -u origin main
  ```

#### Paso 5: Verificar la Subida

- [ ] Ve a `https://github.com/tu_usuario/openclaw-tu_usuario` en tu navegador.
- [ ] Confirma que los archivos de tu workspace son visibles, incluyendo `.openclaw/workspace/IDENTITY.md`.
- [ ] Toma una captura de pantalla de tu página de repositorio en GitHub mostrando el workspace subido.

⚠️ **ADVERTENCIA DE SEGURIDAD:** La carpeta workspace debería **solo** contener archivos seguros creados por OpenClaw (como `IDENTITY.md` y logs de chat). Sin embargo, **antes de hacer push**, verifica que no haya archivos sensibles accidentalmente en el workspace:

```bash
cd ~/.openclaw/workspace
ls -la
cat .gitignore  # Verifica qué se está ignorando
```

Si ves archivos como `openclaw.json`, `.env`, o cualquier configuración con API keys en el workspace, **NO hagas push**. Contacta a tu instructor primero.

---

## ✅ Qué vamos a evaluar

- [ ] OpenClaw está correctamente instalado y accesible en el VPS.
- [ ] El proveedor LiteLLM está configurado y conectado a un modelo de IA funcional.
- [ ] El chat local devuelve una respuesta válida de la IA (verificado en el servidor o por captura de pantalla).
- [ ] El repositorio de GitHub `openclaw-<tu_usuario>` existe y es accesible.
- [ ] La carpeta workspace (`~/.openclaw/workspace`) se ha subido exitosamente a GitHub.
- [ ] El archivo `.openclaw/workspace/IDENTITY.md` está presente en el repositorio mostrando Name, Emoji y Greeting personalizados.
- [ ] La personalización se realizó conversando con OpenClaw (no editando archivos manualmente).
- [ ] La clave SSH se configuró correctamente para permitir git push desde el VPS.
- [ ] El historial de commits de Git muestra al menos un commit con el contenido del workspace.
- [ ] No se subieron archivos sensibles (API keys, tokens, credenciales) al repositorio.
- [ ] Se utilizó SSH para conectarse al VPS (no una consola web ni herramienta gráfica).
- [ ] Los pasos de configuración se siguieron en el orden correcto según la guía de 4Geeks.

> Nota: El instructor puede verificar la configuración del asistente directamente en el servidor y revisar tu historial de commits de Git para asegurar que se siguió el flujo de trabajo correcto.

---

## 📦 Cómo entregar

Tu entrega es toda la carpeta `~/.openclaw/workspace` subida a GitHub desde tu VPS. Comparte la URL de tu repositorio siguiendo las instrucciones de tu instructor.

**Tu repositorio debe contener:**

- `.openclaw/workspace/IDENTITY.md` (la identidad personalizada de tu asistente)
- Cualquier log de chat o archivo del workspace creado por OpenClaw
- Historial de commits de Git mostrando la subida desde el VPS

**Formato de entrega:** `https://github.com/tu_usuario/openclaw-tu_usuario`

⚠️ **VERIFICACIÓN FINAL DE SEGURIDAD:** Antes de entregar, verifica que tu workspace NO contiene:

- `openclaw.json` (archivo de configuración principal - contiene secretos)
- Archivos `.env`
- API keys o tokens
- Cualquier archivo de credenciales

Si accidentalmente subiste archivos sensibles, **inmediatamente**:

1. Elimina el repositorio en GitHub
2. Remueve los archivos sensibles del workspace
3. Crea un nuevo repositorio y vuelve a subir
4. Contacta a tu instructor para orientación

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
