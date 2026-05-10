# Ejemplo en Clase: Chatbot de Sugerencias de Recetas

> **Nota para el instructor:** Este es un ejemplo en clase diseñado para introducir los conceptos técnicos clave del proyecto principal en una sesión de programación en vivo de 60–90 minutos. El dominio es un asistente de cocina en lugar de una interfaz de chat para consultoría — mismos patrones técnicos, alcance mucho más reducido.

## El Escenario

Una pequeña escuela de cocina quiere un asistente con IA donde los estudiantes puedan escribir preguntas y recibir sugerencias de recetas o consejos culinarios. Construirás una página React/Next.js que se comunica con la API de Groq, registra el consumo de tokens por sesión y mantiene la conversación activa después de recargar la página.

---

## Conceptos Cubiertos

| Concepto | Dónde aparece |
|---|---|
| `fetch` con Bearer token | Cada llamada a la API de Groq |
| `async/await` | Gestión de la respuesta asíncrona |
| `useState` | Lista de mensajes, valor del input, flag de carga |
| `useEffect` | Cargar/guardar conversación en `localStorage` |
| Seguimiento de tokens | Leyendo `response.usage` tras cada respuesta |
| Persistencia de sesión | `localStorage`: lectura al montar, escritura al enviar |

---

## Qué Construir

### Configuración

- [ ] Crea una cuenta gratuita en [console.groq.com](https://console.groq.com) y genera una API Key
- [ ] Guárdala como `NEXT_PUBLIC_GROQ_API_KEY` en un archivo `.env.local` — nunca la escribas directamente en el código
- [ ] Crea un proyecto Next.js (o genera el diseño con [v0.dev](https://v0.dev))

### Interfaz de chat

- [ ] Un campo de texto y un botón "Enviar"
- [ ] Una lista de mensajes mostrando preguntas del usuario y respuestas de la IA, diferenciados visualmente (por ejemplo, con colores de fondo distintos)
- [ ] Usa `useState` para el array `messages` y el string `currentInput`

### Flujo asíncrono

- [ ] Llama al endpoint de Groq usando `fetch` — sin wrappers ni SDKs:
  - URL: `https://api.groq.com/openai/v1/chat/completions`
  - Headers: `Authorization: Bearer <clave>` y `Content-Type: application/json`
  - Modelo: `llama3-8b-8192`
- [ ] Muestra un indicador "Pensando…" mientras se espera la respuesta (estado `loading` con `useState`)
- [ ] Captura los errores y muestra un mensaje comprensible en lugar de dejar que la app falle

### Seguimiento de tokens

- [ ] Tras cada respuesta, lee `data.usage.prompt_tokens` y `data.usage.completion_tokens`
- [ ] Acumula y muestra los totales para la sesión (tokens de prompt, de completado y combinado)

### Persistencia de sesión

- [ ] Al montar el componente (`useEffect`), carga el historial de mensajes desde `localStorage`
- [ ] Después de cada nuevo mensaje, guarda el historial actualizado en `localStorage`
- [ ] Añade un botón "Borrar chat" que reinicia el estado y elimina la entrada de `localStorage`

---

## Ejemplo Mínimo de Llamada a la API

```js
const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.NEXT_PUBLIC_GROQ_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "llama3-8b-8192",
    messages: conversationHistory, // array completo de { role, content }
  }),
});
const data = await response.json();
// data.choices[0].message.content → respuesta de la IA
// data.usage.prompt_tokens, data.usage.completion_tokens → conteo de tokens
```

> **Importante:** Envía siempre el array completo `conversationHistory`, no solo el último mensaje. La API es sin estado — necesita todo el contexto en cada petición.

---

## Diseño de Interfaz Sugerido

```
┌────────────────────────────────────────────────┐
│  🍳 Asistente de Recetas                       │
├─────────────────────────────┬──────────────────┤
│  [historial de mensajes]    │  Stats sesión:   │
│                             │  Prompt: 312 tok │
│                             │  Respuesta: 145  │
│                             │  Total: 457 tok  │
├─────────────────────────────┴──────────────────┤
│  [campo de texto]                   [Enviar]   │
│                            [Borrar chat]       │
└────────────────────────────────────────────────┘
```

---

## Preguntas para Discusión

1. ¿Por qué enviamos el historial completo de la conversación en cada petición a la API, en lugar de solo el último mensaje?
2. ¿Qué riesgo de seguridad habría si almacenáramos la API Key directamente en el componente React en lugar de en `.env.local`?
3. ¿Cómo cambiaría el conteo de tokens si el system prompt describiera al asistente como un experto culinario muy detallado con instrucciones largas?
