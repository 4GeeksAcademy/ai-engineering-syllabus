# Hito 7 — RAG y Base de Conocimiento

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/07-trainning-rag)** antes de escribir código — define los datos específicos de tu empresa, los campos, los documentos fuente y las restricciones de tu implementación.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya tienes una API central funcionando y un pipeline de datos que alimenta dashboards en tiempo real. Ahora tu empresa necesita algo distinto: que cualquier persona del equipo comercial pueda hacer una pregunta en lenguaje natural y obtener una respuesta confiable, sin tener que buscarla manualmente en documentos dispersos.

El equipo de ventas pierde tiempo respondiendo preguntas de prospectos y clientes que ya están contestadas en algún documento interno — políticas, catálogos, procedimientos — pero nadie las encuentra a tiempo. Tu tech lead te traslada un **ticket** con el **brief** que dejó el equipo comercial: necesitan un asistente que responda **desde la perspectiva de un vendedor**, con la voz y las prioridades del negocio, no un buscador que devuelva fragmentos crudos de la base de datos.

El **ticket** deja claro el criterio de aceptación central: la respuesta final siempre debe ser generada por un modelo a partir del contexto recuperado — nunca se debe devolver directamente el resultado de la búsqueda en la base de datos vectorial. Además, la solución debe estar modularizada: cada responsabilidad (preparar los datos, guardar los vectores, buscar, generar la respuesta) debe vivir en su propia función, de forma que el equipo técnico pueda reemplazar cualquier pieza sin tocar las demás.

<details>
<summary>📚 Conocimiento complementario — RAG no es Memoria</summary>

Un RAG no almacena "recuerdos" de una conversación — es una **base de conocimiento** que tu sistema consulta antes de responder. Cada vez que llega una pregunta, el sistema busca los fragmentos más relevantes de tus documentos y se los entrega al modelo como contexto para que redacte la respuesta. Esto es distinto de la memoria conversacional (lo que el agente recuerda de turnos anteriores), y ambos conceptos pueden convivir en un mismo sistema pero resuelven problemas diferentes.

Para este hito trabajarás directo con el SDK de Qdrant y FastAPI — sin frameworks de orquestación (LangChain, LlamaIndex, etc.). Eso significa que las cuatro funciones mínimas (`setup`, `embed`, `retrieve`, `query`) las escribes tú, lo cual te obliga a entender qué hace cada pieza en lugar de delegarlo a una abstracción.

</details>

<details>
<summary>📚 Conocimiento complementario — Chunking y umbrales de similitud</summary>

El **chunking** determina qué puede encontrar el recuperador. Un fragmento que corta una política por la mitad produce trozos sin la condición de la que dependen — el modelo alucinará o se negará a responder. Fragmenta por unidades semánticas: una sección, un bloque de producto, un grupo de pasos de un procedimiento — no solo por un número fijo de caracteres.

El **umbral de similitud** es la barrera contra contexto irrelevante. `top-k` solo siempre devuelve k fragmentos aunque ninguno encaje bien. Aplica una puntuación mínima (similitud coseno o la métrica de tu modelo de embeddings) y devuelve **menos de k** — o cero — cuando nada la supera. Forzar contexto malo al prompt es peor que admitir que no encontraste nada.

**Dos modelos, dos trabajos:** el modelo de embeddings convierte texto en vectores para buscar; el LLM de generación convierte contexto recuperado + pregunta en una respuesta natural. **Debes** usar un **modelo de embeddings** dedicado en `embed()` — nunca el mismo modelo que llamas para generación en `query()`. Tienen APIs, formas de salida, latencia, coste y modos de fallo distintos.

Como estudiante de AI Engineering, usa los **modelos que proporciona 4Geeks** (incluidos en tu acceso LLM de estudiante) tanto para embeddings como para generación — no necesitas claves de API personales de pago para este hito.

</details>

---

## 🌱 Cómo Empezar

1. Asegúrate de tener actualizado tu fork del monorepo de tu empresa con el trabajo de los hitos anteriores.
2. Crea una rama nueva para este hito.
3. Añade Qdrant a `docker-compose.yml` (o usa Qdrant Cloud) y confirma la conectividad desde tu entorno Python.
4. Instala las dependencias con `uv add` — cliente de Qdrant, librería de embeddings, SDK del LLM de generación, `fastapi`, etc. Nunca uses `pip install` ni `pipenv`. Configura el modelo de embeddings y el de generación **proporcionados por 4Geeks** como IDs de modelo separados (y claves / URLs base en `.env` si aplica) — nunca reutilices el modelo de generación para embeddings.
5. Revisa `CONTEXT-company.md`, copia los documentos fuente de la empresa que debes indexar (políticas, catálogos, procedimientos — los nombres de archivo son específicos de cada empresa) en `docs/company-knowledge-base/` de tu monorepo, y apunta `setup()` a esa carpeta.
6. Implementa las cuatro funciones en este orden: `setup` → `embed` → `retrieve` → `query` → API → UI → tests.

Distribución de archivos sugerida (los nombres pueden variar; las responsabilidades no):

| Responsabilidad           | Ubicación (indicativa)                |
| ------------------------- | ------------------------------------- |
| Corpus de conocimiento    | `docs/company-knowledge-base/`        |
| Chunking + indexación     | `data/process/rag.py`                 |
| Recuperación + generación | `data/pipelines/rag.py`               |
| Endpoint HTTP             | `services/routers/` o `services/api/` |
| UI de consulta            | `uis/`                                |
| Pruebas unitarias         | `tests/pipelines/test_rag.py`         |
| Documento de diseño RAG   | `docs/rag/rag-design.md`              |

---

## 💻 Lo Que Debes Hacer

### Fase 1 — Preparación de datos e indexación (`data/process/`)

- [ ] Implementar `setup()`: lee los documentos fuente desde `docs/company-knowledge-base/` (el corpus listado en tu `CONTEXT-company.md`), los parsea (Markdown, texto plano o el formato indicado en el contexto) y los divide en chunks semánticos coherentes. Cada chunk debe ser una unidad autocontenida — sin cortar frases ni reglas por la mitad.
- [ ] Implementar `embed(text: str) -> list[float]`: genera un vector para un texto usando un **modelo de embeddings** dedicado — **no** el mismo modelo usado para generación en `query()`. Prefiere el modelo de embeddings gratuito proporcionado por 4Geeks para estudiantes de AI Engineering. La misma función `embed()` se usa para los chunks al indexar y para la pregunta del usuario al consultar.
- [ ] Crear o recrear la colección de Qdrant de tu empresa (nombre de colección desde `CONTEXT-company.md`). Inserta todos los chunks con:
  - `vector`: salida de `embed(chunk_text)`
  - `payload`: como mínimo `source_document`, `section`, `company`, `language`, `chunk_index` y `text` (cuerpo del chunk para el prompt) — nombres de campo desde `CONTEXT-company.md`
- [ ] `setup()` debe ser idempotente en desarrollo: volver a ejecutarlo no debe duplicar puntos (usa IDs deterministas o estrategia de limpiar-y-recargar — documenta cuál elegiste).

### Fase 2 — Pipeline de recuperación y generación (`data/pipelines/`)

- [ ] Implementar `retrieve(query: str, *, k: int = 5, min_score: float) -> list[dict]`: embebe la consulta, busca en Qdrant los k vecinos más cercanos, **filtra** los que queden por debajo de `min_score`, y devuelve los payloads supervivientes (no objetos crudos del SDK de Qdrant).
- [ ] Implementar `query(question: str) -> str`: la **única** función que deben llamar consumidores externos. Orquesta `retrieve()` → armado del prompt → llamada al LLM de **generación** (modelo de chat/completion — no el de embeddings) → devuelve la respuesta final como string. Prefiere el modelo de generación gratuito proporcionado por 4Geeks para estudiantes de AI Engineering. Si `retrieve()` no devuelve nada por encima del umbral, el modelo debe responder con honestidad (p. ej. que la base de conocimiento no tiene información relevante) — nunca inventar datos de la empresa.
- [ ] El prompt de generación debe instruir al modelo a responder desde la **perspectiva de un vendedor** usando solo el contexto recuperado, según el brief comercial del ticket.

⚠️ **IMPORTANTE:** Los nombres de campos, nombres de colección, rutas de documentos, IDs de entidad y valores específicos del dominio deben coincidir con `CONTEXT-company.md`. Una implementación genérica que ignore el contexto no será aceptada.

### Fase 3 — Endpoint de consulta (`services/`)

- [ ] Exponer `POST /knowledge/query` (o la ruta indicada en tu contexto) vía FastAPI. Cuerpo de petición: `{ "question": "..." }`. Cuerpo de respuesta: `{ "answer": "..." }` — solo el string generado por el modelo.
- [ ] El endpoint importa y llama a `query()` desde `data/pipelines/` — **sin** lógica duplicada de recuperación o generación en el router.
- [ ] El endpoint **nunca** debe devolver al cliente resultados crudos de Qdrant, listas de chunks ni puntuaciones de similitud (pueden registrarse en servidor para depuración).

### Fase 4 — Interfaz de consulta (`uis/`)

- [ ] Construir una UI mínima (página Next.js en el backoffice, o página pequeña bajo `uis/`) donde el usuario escriba una pregunta, la envíe y vea la respuesta del endpoint.
- [ ] Manejar estados de carga y error — una llamada fallida a la API no debe parecer una respuesta vacía.
- [ ] Soportar modo claro y oscuro si usas el design system existente del backoffice.

### Fase 5 — Pruebas unitarias (`tests/pipelines/`)

- [ ] Crear `tests/pipelines/test_rag.py` (o equivalente) con pruebas unitarias para `retrieve()` y `query()`.
- [ ] Las pruebas de `retrieve()` deben usar un cliente Qdrant simulado o stub en memoria — sin Qdrant en vivo en CI. Verificar: se excluyen resultados por debajo de `min_score`; pueden devolverse menos de k resultados.
- [ ] Las pruebas de `query()` deben simular `retrieve()` y el LLM de generación. Verificar: la función devuelve la salida del modelo; no devuelve texto crudo de chunks sin pasar por generación.
- [ ] Las pruebas pasan con `python -m pytest tests/pipelines/test_rag.py`.

### Fase 6 — Documento de diseño RAG (`docs/rag/`)

- [ ] Crear `docs/rag/rag-design.md` en tu monorepo. Otro desarrollador debe poder leerlo y entender tu stack RAG sin revisar el código.
- [ ] **Proceso RAG:** describe el flujo de extremo a extremo en tu implementación — desde los documentos fuente en `docs/company-knowledge-base/` pasando por `setup()` → indexación en Qdrant → `retrieve()` al consultar → armado del prompt → LLM de generación → respuesta final. Incluye un diagrama simple o un flujo numerado si ayuda.
- [ ] **Estrategia de chunking:** documenta cómo fragmentaste los documentos fuente de tu empresa (p. ej. por nivel de encabezado, sección semántica, tamaño fijo con solapamiento o híbrido). Explica _por qué_ esa estrategia encaja con tu corpus — qué unidades semánticas preservaste, cómo evitaste cortar reglas o condiciones por la mitad, y tamaño aproximado o conteo de chunks por documento.
- [ ] **Prácticas de embeddings:** indica el **modelo de embeddings** y el **modelo de generación** que usaste (deben ser IDs de modelo distintos), confirma que usaste modelos proporcionados por 4Geeks cuando aplique, y explica cómo usas `embed()` de forma consistente al indexar y al consultar. Anota la dimensión del vector, la métrica de distancia en Qdrant, tu umbral `min_score` y cómo lo afinaste, y cualquier normalización o preprocesado del texto antes de embeber.

---

## ✅ Lo Que Evaluaremos

- [ ] Las cuatro funciones mínimas (`setup`, `embed`, `retrieve`, `query`) existen, están separadas y cada una tiene una única responsabilidad.
- [ ] Los documentos fuente viven en `docs/company-knowledge-base/` y son lo que `setup()` indexa.
- [ ] El chunking respeta unidades semánticas del contenido (no corta a mitad de una idea).
- [ ] Cada chunk almacenado en Qdrant conserva metadatos de origen recuperables (`source_document`, `section` como mínimo).
- [ ] `embed()` usa un modelo de embeddings dedicado distinto del modelo de generación usado en `query()`.
- [ ] `retrieve()` aplica un umbral mínimo de similitud y no siempre fuerza k resultados.
- [ ] La respuesta final del endpoint es generada por un modelo a partir del contexto recuperado — no es el resultado crudo de la base vectorial.
- [ ] El endpoint reutiliza la lógica de `data/pipelines/` sin duplicarla.
- [ ] La interfaz permite ingresar una consulta y muestra la respuesta obtenida del endpoint.
- [ ] Las pruebas unitarias cubren `retrieve()` y `query()` con mocks; pasan en local.
- [ ] Los valores específicos de la empresa usados en la implementación coinciden con el `CONTEXT-company.md` asignado.
- [ ] `docs/rag/rag-design.md` explica el proceso RAG, la estrategia de chunking y las prácticas de embeddings aplicadas — con decisiones justificadas para los documentos de tu empresa.

---

## 📦 Cómo Entregar

1. Haz commit y push de tus cambios a tu fork.
2. Abre un Pull Request hacia la rama principal del monorepo con el título: `[W18D51] RAG Knowledge Base`.
3. En la descripción del PR, incluye:
   - Una pregunta de ejemplo que haría un vendedor
   - La respuesta que generó tu sistema
   - El nombre de la colección Qdrant y el conteo de chunks tras `setup()`
   - Un enlace a `docs/rag/rag-design.md` y un resumen de una línea de tu estrategia de chunking
4. Espera el **sign-off** de tu tech lead antes de considerar el hito cerrado.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
