# Habla con la Máquina — Construyendo una Interfaz de Chat con una API de IA Real

<!-- hide -->

Por [@4GeeksAcademy](https://github.com/4GeeksAcademy) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en inglés](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/how-to-start-a-coding-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Una pequeña consultora digital ha sido contratada por un cliente que quiere explorar interfaces con IA para uso interno. Antes de comprometerse con un producto completo, el tech lead del equipo te ha pedido que construyas un **prototipo de interfaz de chat** que se comunique con un modelo de lenguaje real a través de una API externa.

El objetivo no es solo conseguir que el modelo responda — es hacer que los datos de la conversación sean **visibles y medibles**. El cliente quiere entender qué ocurre por dentro: cuántos tokens está consumiendo, cómo evoluciona el uso a lo largo de una sesión, y qué otras métricas ofrece el modelo. Esta visibilidad es algo que cualquier integración de IA seria necesita desde el primer día.

Vas a usar [Groq](https://groq.com/), una plataforma que ofrece inferencia ultrarrápida para modelos de lenguaje de código abierto y devuelve metadatos detallados con cada respuesta. Tu trabajo es construir un frontend que se integre directamente con la API de Groq — sin backend, sin proxy, solo el navegador comunicándose con un endpoint de IA real.

> Tu tech lead ha compartido el siguiente brief:
>
> #### Lo que necesitamos
>
> - Una interfaz de chat donde el usuario pueda escribir mensajes y recibir respuestas del modelo
> - Una cuenta en [Groq](https://console.groq.com/) con una API Key configurada en el proyecto
> - La API debe ser llamada directamente desde el frontend usando `fetch` — el modelo a usar es la variante de `llama3` (META) que ofrece Groq.
> - Cada respuesta de Groq incluye un objeto `usage`. La interfaz debe usarlo para registrar y mostrar el consumo de tokens (tokens de prompt, tokens de completado y totales acumulados de la conversación entera)
> - Al menos una métrica adicional de la respuesta de Groq debe mostrarse en la interfaz (tiempo de respuesta, tokens por segundo o nombre del modelo son opciones válidas)

El tech lead recordó que esto es un prototipo — la UI no tiene que ser compleja, pero los datos deben ser precisos y actualizarse en tiempo real tras cada intercambio de mensajes.

---

## 🌱 Cómo iniciar el proyecto

Haz un fork del boilerplate desde el siguiente repositorio y sigue las instrucciones en el README:

[https://github.com/4GeeksAcademy/html-hello](https://github.com/4GeeksAcademy/html-hello)

Puedes trabajar en Codespaces (recomendado) o clonarlo localmente. En cualquier caso, crea tu propio repositorio público en GitHub y actualiza la URL remota para que tu trabajo se suba a tu cuenta.

> 💡 Vas a llamar a la API de Groq directamente desde el navegador. Guarda tu API Key de forma que sea fácil de configurar — pero ten cuidado: nunca subas secretos a un repositorio público. Para este proyecto, un archivo `.env` o una constante con nombre claro al inicio de tu script es suficiente.

---

## 💻 Qué debes hacer

### Cuenta y configuración

- [ ] Crea una cuenta gratuita en [https://console.groq.com/](https://console.groq.com/)
- [ ] Genera una API Key desde el panel de Groq
- [ ] Confirma que puedes alcanzar el endpoint de la API de Groq (`https://api.groq.com/openai/v1/chat/completions`) con una petición de prueba usando tu clave

### Interfaz de chat

- [ ] Construye una UI de chat con un campo de texto y un botón de envío
- [ ] Muestra el historial de la conversación como una lista de mensajes — con los mensajes del usuario y las respuestas de la IA visualmente diferenciados
- [ ] Cada vez que el usuario envíe un mensaje, agrégalo a la conversación y envía el **historial completo** (todos los mensajes anteriores) a la API de Groq
- [ ] Muestra la respuesta de la IA en el chat en cuanto se reciba
- [ ] Usa el modelo `llama3-8b-8192` en todas las llamadas a la API

⚠️ **IMPORTANTE:** La API debe llamarse usando `fetch` — sin SDK de terceros ni librerías de envoltorio. Esta es la habilidad central que se practica.

### Panel de uso de tokens y métricas

- [ ] Tras cada respuesta, lee el objeto `usage` de la respuesta de la API de Groq
- [ ] Muestra un total acumulado de **tokens de prompt enviados** durante toda la sesión
- [ ] Muestra un total acumulado de **tokens de completado recibidos** durante toda la sesión
- [ ] Muestra el **total combinado de tokens** consumidos hasta el momento
- [ ] Muestra al menos una métrica adicional de la respuesta de Groq: nombre del modelo, tiempo de respuesta (cabecera `x-groq-request-time` o cualquier medición de tiempo que puedas capturar), o tokens por segundo

> El panel de métricas debe actualizarse automáticamente tras cada mensaje — los datos deben reflejar siempre la conversación completa hasta ese punto, no solo el último intercambio.

---

## ✅ Qué vamos a evaluar

- [ ] La API de Groq se llama correctamente usando `fetch` con las cabeceras correctas (`Authorization: Bearer`, `Content-Type: application/json`) y un cuerpo de petición válido
- [ ] El historial completo de la conversación se envía en cada petición (no solo el último mensaje)
- [ ] La respuesta se muestra en la UI sin necesidad de recargar la página
- [ ] Los datos de tokens del objeto `usage` se leen correctamente y se acumulan a lo largo de la sesión
- [ ] El panel de métricas se actualiza tras cada intercambio de mensajes y muestra totales acumulados correctos
- [ ] Se muestra al menos una métrica adicional más allá del conteo de tokens
- [ ] Los códigos de estado HTTP de la respuesta se gestionan correctamente — si la API devuelve un error, el usuario ve un mensaje comprensible en lugar de un fallo silencioso

> **Nota:** El diseño visual no se evalúa. Un layout funcional y legible es suficiente.

---

## 📦 Cómo entregar

Sube tu proyecto a tu repositorio de GitHub y comparte el enlace siguiendo las instrucciones de entrega de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
