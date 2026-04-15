# Habla con la Máquina — Construyendo una Interfaz de Chat con una API de IA Real

<!-- hide -->

Por [@4GeeksAcademy](https://github.com/4GeeksAcademy) y [otros colaboradores](https://github.com/4GeeksAcademy/talking-to-apis-project/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en inglés](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/how-to-start-a-coding-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Una pequeña consultora digital ha sido contratada por un cliente que quiere explorar interfaces con IA para uso interno. Antes de comprometerse con un producto completo, el tech lead del equipo te ha pedido que construyas un **prototipo de interfaz de chat** que se comunique con un modelo de lenguaje real a través de una API externa.

El objetivo no es solo conseguir que el modelo responda — es hacer que los datos de la conversación sean **visibles y medibles**. El cliente quiere entender qué ocurre por dentro: cuántos tokens está consumiendo, cómo se acumula el uso a lo largo de una sesión y qué otras métricas ofrece el modelo. Esta visibilidad es algo que cualquier integración de IA seria necesita desde el primer día.

Vas a usar [Groq](https://groq.com/), una plataforma que ofrece inferencia ultrarrápida para modelos de lenguaje de código abierto y devuelve metadatos detallados con cada respuesta. Tu trabajo es construir un **frontend en React/Next.js** que se integre con la API de Groq — gestionando correctamente el flujo de datos asíncrono, el estado de la interfaz y la persistencia de la sesión.

> Tu tech lead ha compartido el siguiente brief:
>
> #### Lo que necesitamos
>
> - Una interfaz de chat donde el usuario pueda escribir mensajes y recibir respuestas de la IA
> - Una cuenta en [Groq](https://console.groq.com/) con una API Key almacenada como variable de entorno
> - Usar el **modelo Llama 3 de Meta** disponible en el plan gratuito de Groq
> - Cada respuesta de Groq incluye un objeto `usage` — registra y muestra el consumo de tokens (tokens de prompt, tokens de completado y totales acumulados) para toda la sesión
> - Al menos una métrica adicional de la respuesta debe aparecer en la interfaz: nombre del modelo, tiempo de respuesta o tokens por segundo son opciones válidas
> - El historial de la conversación debe sobrevivir una recarga de página — el usuario no debería perder su sesión por haber cerrado accidentalmente la pestaña

El tech lead también mencionó que esto es un prototipo, así que la interfaz no tiene que ser perfecta visualmente — pero los datos deben ser precisos y siempre actualizados.

### Una nota sobre la autenticación con una API externa

Cuando llamas a una API externa como usuario registrado de ese servicio, estableces tu identidad usando un **Bearer Token** — una credencial que obtuviste al registrarte, que se envía en la cabecera `Authorization` de cada petición:

```text
Authorization: Bearer TU_API_KEY_AQUÍ
```

Piensa en él como el pase de sesión que te da acceso. Sin él, el servidor de la API no sabe quién eres y rechazará tu petición con un error `401 Unauthorized`. En este proyecto, tu Bearer Token es la API Key que generarás en tu cuenta de Groq. Es lo que abre la sesión entre tu aplicación y la API — y debe almacenarse siempre en un archivo `.env`, nunca escrita directamente en el código ni subida a GitHub.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto parte de cero — generarás la interfaz inicial usando [v0.dev](https://v0.dev/), el generador de componentes de Vercel basado en IA.

1. Ve a [https://v0.dev](https://v0.dev) y describe la interfaz que necesitas — por ejemplo: _"una interfaz de chat con un panel de historial de mensajes y una barra lateral con estadísticas de consumo de tokens"_
2. Crea tu propio repositorio público en GitHub y ábrelo en Codespaces
3. Exporta o copia el código del componente React/Next generado en V0 y pégalo en tu proyecto

> 💡 v0 te dará un punto de partida — no un producto terminado. Tendrás que conectar las llamadas a la API, la gestión del estado y la persistencia tú mismo. Ese es el trabajo real.

---

## 💻 Qué debes hacer

### Cuenta y configuración

- [ ] Crea una cuenta gratuita en [https://console.groq.com/](https://console.groq.com/)
- [ ] Genera una API Key y guárdala en un archivo `.env` (por ejemplo, `NEXT_PUBLIC_GROQ_API_KEY`)
- [ ] Confirma que la clave funciona haciendo una llamada `fetch` de prueba a `https://api.groq.com/openai/v1/chat/completions` con el Bearer token en la cabecera `Authorization`

### Interfaz de chat

- [ ] Genera el layout inicial de la interfaz con v0.dev y expórtalo a tu proyecto Next.js
- [ ] Construye un campo de texto y un botón de envío que disparen la llamada a la API
- [ ] Muestra el historial completo de la conversación — mensajes del usuario y respuestas de la IA visualmente diferenciados
- [ ] Usa `useState` para gestionar la lista de mensajes y el valor del campo de texto
- [ ] Cada vez que el usuario envíe un mensaje, agrégalo al estado y envía el **historial completo de la conversación** (todos los turnos anteriores) a la API de Groq — usa el modelo Llama 3 de Meta disponible en Groq

⚠️ **IMPORTANTE:** La API debe llamarse usando `fetch` — sin SDK de terceros ni librerías de envoltorio. Debes configurar manualmente las cabeceras `Authorization: Bearer <tu_clave>` y `Content-Type: application/json` en cada petición.

### Promesas y flujo asíncrono

- [ ] Gestiona la llamada `fetch` usando `async/await`
- [ ] Mientras la API procesa la petición, muestra un indicador de carga o un estado "pensando…" en la interfaz — usa `useState` para controlarlo
- [ ] Si la API devuelve un error (código de estado no 2xx), captúralo y muestra al usuario un mensaje claro y legible en lugar de dejar que la aplicación falle

### Panel de uso de tokens y métricas

- [ ] Tras cada respuesta, lee el objeto `usage` de la respuesta de la API de Groq
- [ ] Acumula y muestra el total acumulado de **tokens de prompt enviados** durante toda la sesión
- [ ] Acumula y muestra el total acumulado de **tokens de completado recibidos** durante toda la sesión
- [ ] Muestra el **total combinado de tokens** consumidos hasta el momento en la sesión
- [ ] Muestra al menos una métrica adicional de la respuesta de Groq: nombre del modelo, tiempo de respuesta o tokens por segundo

### Persistencia de sesión

- [ ] Usa `useEffect` para cargar el historial de la conversación desde `localStorage` cuando el componente se monte
- [ ] Guarda el historial de la conversación en `localStorage` después de cada nuevo mensaje para que la sesión sobreviva una recarga de página
- [ ] Incluye un botón "Borrar conversación" que reinicie el estado de mensajes y limpie el `localStorage`

---

## ✅ Qué vamos a evaluar

- [ ] La API de Groq se llama correctamente con `fetch` incluyendo las cabeceras `Authorization: Bearer` y `Content-Type: application/json` en cada petición
- [ ] El historial completo de la conversación se envía en cada llamada a la API (comunicación stateless gestionada correctamente en el cliente)
- [ ] La promesa se gestiona con `async/await` y se muestra un estado de carga mientras se espera la respuesta
- [ ] Los errores de la API se capturan y se muestran al usuario como mensajes comprensibles — sin fallos silenciosos ni errores técnicos en pantalla
- [ ] `useState` gestiona correctamente los mensajes, el estado de carga y las métricas
- [ ] `useEffect` se usa para cargar y sincronizar el historial de la conversación desde `localStorage`
- [ ] Los datos de tokens del objeto `usage` se acumulan y muestran correctamente a lo largo de toda la sesión
- [ ] La conversación persiste tras una recarga de página y puede borrarse manualmente
- [ ] Al menos una métrica adicional más allá del conteo de tokens es visible en la interfaz

> **Nota:** El diseño visual no se evalúa. Un layout funcional y legible es suficiente.

---

## 📦 Cómo entregar

Sube tu proyecto a tu repositorio de GitHub y comparte el enlace siguiendo las instrucciones de entrega de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
