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

Acabas de incorporarte como AI engineer en una consultora pequeña. Tu tech lead te asigna una tarea el primer día: el equipo necesita un asistente de IA autoalojado que corra en un VPS, que mantenga las conversaciones de clientes fuera de servidores de terceros y que pueda configurarse para usar distintos modelos de IA según el tipo de tarea.

"No podemos mandar todo a través de APIs comerciales", te explica. "Hay restricciones de cumplimiento normativo. Necesitamos nuestra propia instancia — privada, controlable, nuestra."

La herramienta que usa el equipo es **OpenClaw**. Tu trabajo es desplegar y configurar una instancia funcional de OpenClaw en un VPS, conectarla a un modelo de IA a través de LiteLLM y verificar que responde correctamente en el chat local.

Este no es un proyecto de código — es una tarea de infraestructura y configuración. El resultado principal es un sistema funcionando, no un repositorio. Dicho esto, si en algún momento personalizas el código de OpenClaw, un repositorio es el lugar correcto para registrar esos cambios — los buenos ingenieros versionan su trabajo. Por ahora, usarás un repositorio para documentar tu configuración con una captura de pantalla y un archivo de configuración como evidencia de entrega.

> **Antes de empezar, asegúrate de entender:**
>
> - OpenClaw solo es útil si tiene un modelo conectado. Sin él, no hace nada. Parte de tu trabajo como AI engineer es saber qué modelo usar para cada tarea — no siempre el más potente, sino el más adecuado según el contexto, el coste y los requisitos de latencia.
> - OpenClaw **no** es un entorno multi-tenant. Cualquier persona con acceso a la URL de tu VPS puede usarlo. Nunca lo expongas públicamente sin autenticación.
> - Sigue siempre la guía de instalación de 4Geeks. El orden de los pasos de configuración importa — saltarlos o reordenarlos provoca errores difíciles de depurar.

Tu tech lead espera una instancia funcional antes de que acabe el día. Ponla a correr.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no usa un repositorio de inicio — es un proyecto de configuración de servidor. Sigue estos pasos para comenzar:

1. Accede al VPS proporcionado por la plataforma (las credenciales se compartirán por la plataforma del curso).
2. Conéctate al VPS mediante SSH desde tu terminal:

   ```bash
   ssh tu_usuario@ip_de_tu_vps
   ```

3. Sigue la [guía de instalación de OpenClaw de 4Geeks](https://4geeks.com) paso a paso — no omitas ninguna fase.
4. Crea un **nuevo repositorio en GitHub** llamado `openclaw-setup-<tu_usuario_github>` para almacenar los archivos de entrega (captura de pantalla + configuración).

> Si vas a trabajar en local en lugar de en un VPS, confírmalo con tu instructor primero. Los pasos de instalación son diferentes.

---

## 💻 Qué debes hacer

### Acceso al VPS por SSH

- [ ] Conectarte exitosamente al VPS por SSH desde tu terminal local.
- [ ] Confirmar el sistema operativo y los recursos disponibles del servidor antes de iniciar la instalación.

### Instalación de OpenClaw

- [ ] Instalar OpenClaw en el VPS siguiendo la guía de instalación de 4Geeks.
- [ ] Utilizar el método de instalación indicado por tu instructor (1-click, Docker o manual).

### Configuración básica (en orden)

- [ ] Configurar el **proveedor LiteLLM** como backend de modelo.
- [ ] Ingresar una **API Key** válida del proveedor de modelo elegido.
- [ ] Saltar el paso de configuración de Skills (se abordará en una sesión futura).
- [ ] Habilitar los **hooks** cuando se solicite durante la configuración.
- [ ] Saltar el paso de Channel Workflows (se abordará en una sesión futura).
- [ ] Abrir **Try Local Chat** y enviar un mensaje de prueba para confirmar que la instancia responde.

### Archivo de configuración

- [ ] Localizar el archivo `openclaw.json` en el servidor.
- [ ] Revisar sus atributos principales y asegurarte de entender qué controla cada sección.
- [ ] Copiar el `openclaw.json` a tu máquina local e incluirlo en tu repositorio de entrega.

⚠️ **IMPORTANTE:** No publiques API Keys en tu repositorio. Antes de hacer commit del `openclaw.json`, elimina o reemplaza los valores reales de cualquier API Key con un placeholder (ej: `"api_key": "YOUR_KEY_HERE"`).

### Evidencia de entrega

- [ ] Tomar una captura de pantalla del chat local de OpenClaw que muestre una respuesta exitosa de la IA.
- [ ] Añadir la captura a tu repositorio de GitHub como `proof.png` (o `.jpg`).
- [ ] Añadir un `README.md` a tu repositorio con: el proveedor de VPS utilizado, el modelo elegido y una frase explicando por qué seleccionaste ese modelo para un asistente de propósito general.

---

## ✅ Qué vamos a evaluar

- [ ] OpenClaw está correctamente instalado y accesible en el VPS.
- [ ] El proveedor LiteLLM está configurado y conectado a un modelo de IA funcional.
- [ ] El chat local devuelve una respuesta válida de la IA (evidenciado por la captura de pantalla).
- [ ] El `openclaw.json` está presente en el repositorio con los valores de API Key eliminados.
- [ ] El `README.md` de entrega incluye los campos requeridos: proveedor de VPS, nombre del modelo y justificación de la elección del modelo.
- [ ] Se utilizó SSH para conectarse al VPS (no una consola web ni herramienta gráfica).
- [ ] Los pasos de configuración se siguieron en el orden correcto según la guía de 4Geeks.

> Nota: La corrección de los valores internos del `openclaw.json` será revisada por el instructor directamente en el servidor — el archivo en el repositorio es solo para referencia.

---

## 📦 Cómo entregar

Sube tu repositorio a GitHub (debe contener `proof.png` y `openclaw.json` con las keys saneadas) y comparte el enlace siguiendo las instrucciones de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
