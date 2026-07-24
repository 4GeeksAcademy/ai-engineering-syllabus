# Maple Street Library — Migración a Agente LangGraph (Ejemplo de Clase)

> **Para instructores:** Escenario paralelo en aula para `ai-eng-langgraph-agent-base`. Misma columna vertebral (estado LangGraph mínimo, tres nodos de responsabilidad única, aristas condicionales, compilar + checkpoint, trace consultable, evals, `POST /agent/query` delgado), alcance distinto al monorepo de empresa. Asume que los estudiantes ya tienen el RAG de Maple Street del ejemplo de clase RAG previo — o tú entregas `retrieve`/`query` preconstruidos en `data/pipelines/`. Los estudiantes siguen el enunciado completo del monorepo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

El personal de mostrador de **Maple Street Library** usa el asistente RAG de la sesión anterior. Funciona, pero cada respuesta es una caja negra — nadie ve si la recuperación corrió antes de la generación ni qué decidió el flujo.

Objetivo del demo en vivo: envolver las funciones existentes `retrieve` y `query` en un **LangGraph compilado** para que cada pregunta de usuario produzca un **trace consultable**, sin reescribir el pipeline RAG.

### Nota de alcance

| Proyecto evaluable (`ai-eng-langgraph-agent-base`) | Este ejemplo de clase                               |
| -------------------------------------------------- | --------------------------------------------------- |
| Fork completo del monorepo + `CONTEXT-company.md`  | Mini `library-api` + corpus `maple_knowledge`       |
| LangSmith o tracing de producción                  | Lista de trace en memoria + export JSON opcional    |
| Checkpointing con almacén durable                  | Solo checkpointer `MemorySaver`                     |
| PR con captura de trace + salida de evals          | Demo local + `pytest tests/pipelines/`              |
| Convivir con endpoint RAG existente en monorepo    | Reemplazar o añadir junto a `POST /knowledge/query` |

---

## Prerrequisitos (del ejemplo de clase RAG)

- [ ] Qdrant corriendo con colección `maple_knowledge` indexada
- [ ] `data/pipelines/rag.py` expone `retrieve()` y `generate_answer()` (el paso de generación separado de `query()`) funcionales — **impórtalos; no copies lógica en los nodos, y no llames al `query()` monolítico dentro de un solo nodo**

---

## Qué construir

### 1. Estado del grafo (`services/agent/state.py`)

- [ ] TypedDict con: `question`, `retrieved_context`, `answer`, `trace_steps`, `error`
- [ ] Sin historial completo de chat — justifica verbalmente cualquier campo extra si lo añades

### 2. Nodos (`services/agent/nodes.py`)

| Nodo               | Llama a                              | Responsabilidad                                                                                                    |
| ------------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `receive_question` | —                                    | Validar pregunta no vacía; añadir paso al trace                                                                    |
| `retrieve_node`    | `data.pipelines.rag.retrieve`        | Obtener contexto; registrar conteo de chunks en trace                                                              |
| `query_node`       | `data.pipelines.rag.generate_answer` | Generar respuesta con voz de mostrador a partir del contexto recibido — **no** `query()`, que volvería a recuperar |

### 3. Grafo + checkpoint (`services/agent/graph.py`)

- [ ] Aristas condicionales: pregunta vacía → `END`; si no `receive` → `retrieve` → `query` → `END`
- [ ] `builder.compile(checkpointer=MemorySaver())` al arranque — no por petición
- [ ] Grafo roto (p. ej. nodo huérfano) debe fallar al compilar durante la preparación del demo

### 4. Tracing

- [ ] Cada nodo añade a `trace_steps`, p. ej. `{"node": "retrieve", "order": 2, "summary": "3 chunks"}`
- [ ] Tras una corrida, exporta o imprime JSON del trace para inspección

### 5. Endpoint

- [ ] `POST /agent/query` body `{ "question": "..." }` → `{ "answer": "...", "trace_id": "..." }`
- [ ] La ruta solo invoca el grafo compilado — sin lógica RAG en el router
- [ ] Fallo en nodo → `{ "detail": "..." }` sin stack trace crudo

### 6. Evals (`tests/pipelines/test_agent_evals.py`)

- [ ] **Eval 1:** el trace muestra `retrieve` antes de `query` para pregunta de política de préstamos
- [ ] **Eval 2:** pregunta vacía nunca llega al nodo `query` en el trace
- [ ] **Eval 3:** pipeline mockeado — campo `answer` poblado cuando retrieve devuelve fixtures

Ejecutar: `uv run pytest tests/pipelines/ -q`

---

## Verificar juntos

- [ ] Pregunta: _"¿Cuánto tiempo puedo tener una novela?"_ — inspecciona trace: `receive` → `retrieve` → `query`
- [ ] Pregunta con cadena vacía — el grafo termina pronto; la API devuelve error claro
- [ ] Rompe una arista a propósito — confirma que la compilación falla antes de servir
- [ ] Muestra historial de checkpoint de un `thread_id` tras dos preguntas

---

## Preguntas de discusión

1. ¿Por qué es más seguro un estado mínimo que pasar toda la conversación a cada nodo?
2. ¿Qué se rompe si compilas el grafo en cada petición HTTP en lugar de una vez al arranque?
3. ¿Cómo añadirías un cuarto nodo (p. ej. "escalar a humano") sin reescribir `retrieve` y `query`?
