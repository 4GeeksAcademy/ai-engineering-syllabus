# Ejemplo en Clase: API de Diario de Notas por Voz

> **Nota para el instructor:** Este es un ejemplo en vivo para clase que enseña los conceptos del proyecto `voice-to-do-list-api`. Usa este escenario para demostrar endpoints CRUD con FastAPI, almacenamiento en memoria, integración con la API de Groq e ingeniería de prompts para extracción de intención. **No lo asignes como tarea — es un ejercicio guiado en el aula.**

---

## El Escenario

Una periodista usa una aplicación de voz para capturar notas rápidas mientras trabaja en el campo. El frontend del navegador ya graba su voz, la transcribe con la Web Speech API y envía el texto a un backend. Tu trabajo es construir ese backend.

Los usuarios dicen cosas como:
- _"Guarda que la reunión del consejo municipal es el viernes a las 7 de la tarde"_
- _"Muéstrame todas mis notas"_
- _"Elimina la nota 3"_
- _"Actualiza la nota 2 para decir que la reunión fue aplazada"_

**Qué vas a aprender:**
- Cómo construir una API RESTful con FastAPI y almacenamiento en memoria
- Cómo implementar los cinco métodos HTTP (GET, POST, PUT, PATCH, DELETE) para un recurso
- Cómo llamar a la API de Groq desde un endpoint de FastAPI
- Cómo escribir un system prompt que fuerce a un LLM a devolver JSON estructurado (extracción de intención)
- Por qué importa la ingeniería de prompts: el LLM es tu capa de enrutamiento

---

## Modelo de Datos

Cada nota se almacena como un diccionario de Python:

```python
{ "id": 1, "content": "Reunión del consejo municipal el viernes a las 7 pm", "archived": False }
```

El almacenamiento es una lista a nivel de módulo — sin base de datos, sin sistema de archivos:

```python
notes: list[dict] = []
```

---

## Especificación de la API

### Endpoints de notas

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/notes` | Devuelve todas las notas como un array JSON |
| `POST` | `/notes` | Crea una nueva nota (`content` obligatorio, `archived` por defecto `False`) |
| `PUT` | `/notes/{note_id}` | Reemplaza la nota completa (nuevo `content` obligatorio) |
| `PATCH` | `/notes/{note_id}` | Actualización parcial: cambiar `content` y/o establecer `archived: true` |
| `DELETE` | `/notes/{note_id}` | Elimina la nota por ID; devuelve un mensaje de confirmación |

### Endpoint de instrucción

| Método | Ruta | Descripción |
|---|---|---|
| `POST` | `/instruction` | Recibe `{ "transcription": "..." }`, llama a Groq y devuelve el JSON de enrutamiento |

El endpoint `/instruction` llama a Groq con un system prompt que fuerza al LLM a responder **únicamente** con:

```json
{
  "endpoint": "/notes",
  "method": "POST",
  "params": { "content": "Reunión del consejo municipal el viernes a las 7 pm" }
}
```

---

## Tareas

### Configuración

- [ ] Crea un entorno virtual e instala `fastapi`, `uvicorn` y `groq`
- [ ] Guarda tu API key de Groq en un archivo `.env` (añádelo al `.gitignore`)
- [ ] Configura CORS para permitir peticiones desde `localhost`

### Almacenamiento en memoria

- [ ] Declara `notes: list[dict] = []` a nivel de módulo
- [ ] Cada nota tiene `id` (int, auto-incremental), `content` (str) y `archived` (bool, por defecto `False`)

### Endpoints de notas

- [ ] Implementa los cinco endpoints de la especificación anterior
- [ ] Los IDs deben ser únicos incluso después de eliminar notas (usa `max(n["id"] for n in notes) + 1` o un contador)
- [ ] Devuelve `404` con un mensaje si el ID de la nota no existe

### Endpoint de instrucción

- [ ] Implementa `POST /instruction` que lee el campo `transcription`
- [ ] Escribe un system prompt que instruya al LLM a devolver **solo** un objeto JSON con `endpoint`, `method` y `params`
- [ ] Llama a la API de Groq (modelo: `llama3-8b-8192` o similar) y devuelve la respuesta JSON

> ⚠️ **No** escribas lógica de detección de intención de forma manual (sin `if "guarda" in transcription`). Toda la lógica de enrutamiento debe provenir de la respuesta del LLM.

### Verificación de extremo a extremo

- [ ] Prueba estos comandos hablados manualmente (usando Postman, curl o el frontend si está disponible):

  | Frase hablada | Enrutamiento esperado del LLM |
  |---|---|
  | "Guarda que necesito llamar a la oficina del alcalde" | `POST /notes` |
  | "Muéstrame todas mis notas" | `GET /notes` |
  | "Archiva la nota 2" | `PATCH /notes/2` con `archived: true` |
  | "Elimina la nota 1" | `DELETE /notes/1` |

---

## Plantilla de System Prompt (punto de partida)

```
Eres un extractor de intenciones para una API de notas de voz.
Dada una transcripción hablada, responde ÚNICAMENTE con un objeto JSON en este formato exacto:
{
  "endpoint": "<ruta>",
  "method": "<método HTTP en mayúsculas>",
  "params": { ... }
}
Endpoints disponibles: GET /notes, POST /notes, PUT /notes/{id}, PATCH /notes/{id}, DELETE /notes/{id}.
Nunca devuelvas explicaciones. Nunca devuelvas texto libre. Solo JSON.
```

---

## Preguntas de Discusión

1. ¿Qué ocurre si el LLM devuelve texto libre en lugar de JSON? ¿Cómo harías que tu endpoint `/instruction` manejara eso correctamente?
2. El system prompt define todos los endpoints disponibles. ¿Qué tendrías que cambiar en el prompt si añadieras un endpoint `GET /notes/{id}` para recuperar una nota individual?
3. Ahora mismo, la lista de notas se reinicia cada vez que el servidor se reinicia. ¿Qué tendrías que cambiar para persistir las notas entre reinicios — y qué añadiría eso en términos de complejidad?
