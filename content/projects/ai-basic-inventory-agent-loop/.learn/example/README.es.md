# Agente de Stock para Librería — Ejemplo en Clase

> **Nota para el instructor:** Este es un ejemplo simplificado en clase para el proyecto "AI Basic Inventory Agent Loop". Usa este escenario para demostrar el bucle del agente (Observar → Pensar → Actuar → Actualizar) y el uso de tools con un backend FastAPI en 1–2 horas. El proyecto original cubre los mismos patrones técnicos en el contexto de suministros para una cafetería.

---

## Escenario

**PageTurner Books** es una pequeña librería independiente. La dueña, Mia, quiere dejar de revisar hojas de cálculo y empezar a hacer preguntas en lenguaje natural: *"¿Cuántas copias de Dune tenemos?"* o *"Acaban de llegarnos 20 ejemplares de La Biblioteca de Medianoche."*

Tu trabajo es construir un sistema de dos partes:

1. **Una API REST con FastAPI** que gestione el stock de la librería en un archivo CSV.
2. **Un agente de IA** (`agent.py`) que se conecte a un LLM, use la API como conjunto de tools y mantenga un bucle de conversación con Mia.

---

## Arquitectura del Sistema

```
Mia escribe un mensaje
    → agent.py lo envía al LLM (con las definiciones de tools)
        → El LLM selecciona una tool y sus parámetros
            → agent.py llama al endpoint correspondiente de la API
                → El resultado de la API se inyecta de vuelta en el contexto del LLM
                    → El LLM genera una respuesta final para Mia
```

Este ciclo es el **bucle del agente**: Observar → Pensar → Actuar → Actualizar → Repetir.

---

## Lo que Debes Hacer

### Parte 1 — FastAPI (`api/app.py`)

Construye una aplicación FastAPI que almacene los datos de libros en `books.csv` con estos campos: `id`, `title`, `author`, `quantity`.

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/books` | `GET` | Devuelve la lista completa de libros |
| `/books` | `POST` | Añade un nuevo libro (`title`, `author`, `quantity`) |
| `/books/{book_id}` | `PATCH` | Actualiza el stock — acepta un `delta` (positivo = reposición, negativo = venta) |
| `/books/alerts` | `GET` | Devuelve los libros con cantidad por debajo del umbral (por defecto: 5) |

- [ ] `books.csv` se crea automáticamente si no existe.
- [ ] Todos los endpoints devuelven los códigos HTTP apropiados.
- [ ] `PATCH` rechaza peticiones que dejarían la cantidad por debajo de 0.

### Parte 2 — Agente de IA (`agent.py`)

- [ ] Define los cuatro endpoints de la API como **tools** para el LLM. Cada tool necesita:
  - `name` — un identificador corto
  - `description` — explicación en lenguaje natural de lo que hace
  - `parameters` — esquema JSON tipado para sus entradas

- [ ] Implementa el **bucle del agente**:

```python
while True:
    # 1. Observar: leer la entrada del usuario
    # 2. Pensar: enviar mensajes + definiciones de tools al LLM
    # 3. Actuar: si el LLM eligió una tool, llamar a la API
    # 4. Actualizar: inyectar el resultado de la tool en el historial de mensajes
    # 5. Repetir hasta que el LLM dé una respuesta final (sin llamada a tool)
```

- [ ] Mantén el **historial completo de la conversación** en memoria durante la sesión.
- [ ] Expón una interfaz CLI simple: muestra el prompt `Tú:` e imprime la respuesta del agente.

### Parte 3 — Log de Conversación (`conversation_log.csv`)

Cada evento del bucle debe añadirse a `conversation_log.csv`:

| Campo | Descripción |
|-------|-------------|
| `actor` | `user`, `agent` o `tool` |
| `message` | Texto o contenido del resultado |
| `tool_call` | Nombre de la tool llamada (vacío si no aplica) |
| `timestamp` | Fecha y hora en formato ISO 8601 |

- [ ] El archivo es **solo de adición** — nunca se sobreescribe entre sesiones.

---

## Ejemplo Mínimo de Definición de Tool

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_books",
            "description": "Devuelve la lista actual de todos los libros y sus cantidades en stock.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_stock",
            "description": "Actualiza el stock de un libro por un valor delta. Usa valores positivos para reposición y negativos para ventas.",
            "parameters": {
                "type": "object",
                "properties": {
                    "book_id": {"type": "string", "description": "El ID del libro"},
                    "delta": {"type": "integer", "description": "Cantidad a añadir (positivo) o restar (negativo)"}
                },
                "required": ["book_id", "delta"]
            }
        }
    }
]
```

---

## Cómo Ejecutar

```bash
# Terminal 1 — iniciar la API
uvicorn api.app:app --reload

# Terminal 2 — iniciar el agente
python agent.py
```

Crea un archivo `.env` con tu clave de API antes de empezar:

```
GROQ_API_KEY=tu_clave_aquí
```

> **Importante:** No uses ningún framework de agentes (LangChain, AutoGen, etc.). El bucle debe implementarse manualmente en Python puro.

---

## Conversación de Prueba

```
Tú: ¿Qué libros tenemos?
Agente: Aquí está la lista de libros en stock: ...

Tú: Acabamos de recibir 15 ejemplares de Dune.
Agente: ¡Hecho! He añadido 15 copias al stock de Dune. Cantidad actual: ...

Tú: ¿Qué libros están por agotarse?
Agente: Los siguientes libros están por debajo del umbral mínimo: ...
```

---

## Preguntas para Debatir

1. ¿Qué pasaría si eliminaras el resultado de la tool del historial de mensajes antes de la siguiente llamada al LLM? ¿Cómo afectaría esto al comportamiento del agente?
2. ¿Por qué `conversation_log.csv` es de solo adición? ¿Qué problema causaría sobrescribirlo?
3. El LLM elige qué tool llamar basándose en tus descripciones. Escribe una descripción mejorada para la tool `update_stock` que ayude al modelo a distinguir entre una venta y una reposición.
