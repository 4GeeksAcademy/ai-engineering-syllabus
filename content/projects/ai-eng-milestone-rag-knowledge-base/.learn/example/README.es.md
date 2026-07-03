# Maple Street Library — Base de Conocimiento RAG (Ejemplo de Clase)

> **Para instructores:** Escenario paralelo en aula para `ai-eng-milestone-rag-knowledge-base`. Misma columna vertebral (cuatro funciones, Qdrant, umbral de similitud, respuestas generadas por modelo, endpoint FastAPI, UI mínima), dominio distinto. Los estudiantes siguen el enunciado completo del monorepo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

El personal de mostrador de **Maple Street Library** responde a diario las mismas preguntas de usuarios — plazos de préstamo, multas, reserva de salas — enterradas en documentos Markdown internos. Construye un asistente con voz de **mostrador**: respuestas en lenguaje natural desde políticas indexadas, nunca hits de búsqueda crudos.

### Nota de alcance

| Proyecto evaluable (`ai-eng-milestone-rag-knowledge-base`) | Este ejemplo de clase              |
| ---------------------------------------------------------- | ---------------------------------- |
| Monorepo completo + documentos de `CONTEXT-company.md`     | Mini `library-api` + 3 archivos MD |
| Nombre de colección específico de empresa                  | `maple_knowledge`                  |
| Integración UI en backoffice                               | Página única bajo `uis/`           |
| PR al fork del estudiante                                  | Qdrant local vía Docker            |

---

## Documentos fuente (corpus mini)

Colocar bajo `data/raw/knowledge/`:

| Archivo                | Contenido indicativo                  |
| ---------------------- | ------------------------------------- |
| `loan-policy.md`       | Plazos, renovaciones, multas          |
| `room-reservations.md` | Reglas de reserva de salas de estudio |
| `membership-faq.md`    | Tipos de carnet, invitados, pérdidas  |

Fragmentar por encabezados `##` — cada sección genera uno o más chunks con metadatos `document` + `section`.

---

## Qué construir

### 1. `data/process/rag.py`

- [ ] `setup()` — parsea los tres archivos, fragmenta por sección, upsert en colección Qdrant `maple_knowledge`
- [ ] `embed(text)` — mismo modelo para chunks y consultas (p. ej. `sentence-transformers` o embeddings por API)

### 2. `data/pipelines/rag.py`

- [ ] `retrieve(query, k=5, min_score=0.72)` — filtra por debajo del umbral
- [ ] `query(question)` — prompt con voz de mostrador + LLM de generación; nunca devolver lista de chunks

### 3. API + UI

- [ ] `POST /knowledge/query` → `{ "answer": "..." }`
- [ ] Página mínima: input, enviar, área de respuesta, estados carga/error

### 4. Pruebas

- [ ] `tests/pipelines/test_rag.py` — mock Qdrant + LLM para `retrieve()` y `query()`

---

## Verificar juntos

- [ ] Pregunta: _"¿Cuánto tiempo puedo tener una novela?"_ → respuesta cita política de préstamos, no JSON crudo
- [ ] Pregunta sin sentido: _"¿Qué tiempo hace en Marte?"_ → respuesta honesta de "no está en la base"
- [ ] `retrieve()` con puntuaciones bajas simuladas devuelve menos de k hits
- [ ] UI de Qdrant muestra payloads con `document` y `section`

---

## Fragmento Docker (Qdrant)

```yaml
qdrant:
  image: qdrant/qdrant:latest
  ports:
    - "6333:6333"
```

Ejecuta `setup()` una vez con Qdrant levantado; confirma que el conteo de puntos coincide con el de chunks.
