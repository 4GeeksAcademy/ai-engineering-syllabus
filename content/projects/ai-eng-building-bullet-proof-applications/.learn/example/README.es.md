# API de Gestión de Tareas — Suite de Tests (Ejemplo en Clase)

> **Nota para el instructor:** Este es un ejemplo simplificado en clase para el proyecto "Building Bullet-Proof Applications". Usa este escenario para introducir pytest, los planes de tests y la estructura de tres niveles (camino feliz / caso límite / modo de fallo) en 1–2 horas. El proyecto original aplica los mismos conceptos a una API de autenticación con requisitos de cobertura más altos.

---

## Escenario

Tu equipo construyó una pequeña **API de Gestión de Tareas** con FastAPI. Funcionaba bien en desarrollo, pero la semana pasada un compañero añadió una funcionalidad de "completar tarea" que ignoraba silenciosamente las tareas que no existían. Nadie lo notó hasta que un usuario lo reportó.

Tu tech lead abrió un ticket:

> *"Necesitamos una suite de tests. Cada endpoint debe tener al menos un test de camino feliz, un test de caso límite y un test de modo de fallo. Usa pytest. Apunta a un 70% de cobertura en el módulo de tareas."*

---

## La API a Testear

La API de Gestión de Tareas tiene estos endpoints:

| Método | Ruta | Descripción |
|--------|------|-------------|
| `GET` | `/tasks` | Devuelve todas las tareas |
| `POST` | `/tasks` | Crea una tarea (`title`, `description` opcional) |
| `PATCH` | `/tasks/{task_id}/complete` | Marca una tarea como completada |
| `DELETE` | `/tasks/{task_id}` | Elimina una tarea |

Cada tarea tiene: `id` (autogenerado), `title` (cadena, obligatorio), `description` (cadena, opcional), `completed` (bool, por defecto `False`).

---

## Lo que Debes Hacer

### Paso 1 — Escribe el plan de tests primero

- [ ] Crea `TESTING.md` en la raíz del proyecto.
- [ ] Antes de escribir ningún test, lista en `TESTING.md` los casos que planeas cubrir para cada endpoint: camino feliz, caso límite y modo de fallo.

Ejemplo para `POST /tasks`:

| Test | Tipo | Entrada | Resultado esperado |
|------|------|---------|-------------------|
| Crear tarea con título válido | Camino feliz | `{"title": "Comprar leche"}` | 201, tarea devuelta con `completed: false` |
| Crear tarea sin título | Caso límite | `{}` | 422, error de validación |
| Crear tarea con título vacío | Modo de fallo | `{"title": ""}` | 422 o 400, mensaje de error |

### Paso 2 — Escribe los tests

- [ ] Crea un directorio `tests/` en la raíz del proyecto.
- [ ] Crea un archivo de tests por grupo de endpoints:

```
tests/
├── test_list_tasks.py
├── test_create_task.py
├── test_complete_task.py
└── test_delete_task.py
```

- [ ] Para cada endpoint, implementa como mínimo:
  - [ ] **Un test de camino feliz** — entrada válida, respuesta exitosa esperada.
  - [ ] **Un test de caso límite** — entrada en el límite: título vacío, ID inexistente, tarea ya completada, etc.
  - [ ] **Un test de modo de fallo** — entrada inválida o mal formada que debe ser rechazada.

### Paso 3 — Ejecuta y verifica la cobertura

```bash
# Instalar dependencias
pip install pytest pytest-cov httpx

# Ejecutar todos los tests
pytest

# Ejecutar con informe de cobertura
pytest --cov=app --cov-report=term-missing
```

- [ ] Todos los tests pasan con `pytest`.
- [ ] La cobertura del módulo de tareas es igual o superior al **70%** (`pytest --cov`).
- [ ] Documenta el resultado de la cobertura en `TESTING.md`.

---

## Ejemplo de Estructura de Test

```python
# tests/test_create_task.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task_happy_path():
    response = client.post("/tasks", json={"title": "Comprar leche"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Comprar leche"
    assert data["completed"] is False

def test_create_task_missing_title():
    # Caso límite: falta el campo obligatorio
    response = client.post("/tasks", json={})
    assert response.status_code == 422

def test_create_task_empty_title():
    # Modo de fallo: el título está presente pero es inválido
    response = client.post("/tasks", json={"title": ""})
    assert response.status_code in (400, 422)
```

> **Importante:** No testees la serialización HTTP ni los internos del framework. Cada test debe verificar algo sobre la **lógica de negocio** — lo que el endpoint *decide*, no cómo FastAPI formatea la respuesta.

---

## Casos de Test a Cubrir (Lista de Partida)

Usa esto como punto de partida. Añade más casos a medida que se te ocurran.

| Endpoint | Camino feliz | Caso límite | Modo de fallo |
|----------|-------------|-------------|---------------|
| `GET /tasks` | Devuelve lista (puede estar vacía) | Devuelve lista con varias tareas | — |
| `POST /tasks` | Crea tarea con título + descripción | Crea tarea solo con título (sin descripción) | Título vacío |
| `PATCH /tasks/{id}/complete` | Marca tarea existente como completada | Tarea ya marcada como completada | ID de tarea inexistente |
| `DELETE /tasks/{id}` | Elimina tarea existente | — | ID de tarea inexistente |

---

## Flujo de Trabajo con Ayuda de IA

- [ ] Pega la lógica de tu endpoint en tu agente de código IA y pregunta: *"¿Qué casos límite me estoy perdiendo para este endpoint?"*
- [ ] Revisa cada caso de test sugerido antes de añadirlo — tú eres quien toma las decisiones sobre qué testear.
- [ ] Si un test revela un bug en el código existente, corrige el bug y anótalo en `TESTING.md` en una sección "Bugs Encontrados".

---

## Preguntas para Debatir

1. ¿Cuál es la diferencia entre un test de caso límite y uno de modo de fallo? Da un ejemplo de cada uno para `DELETE /tasks/{id}`.
2. ¿Por qué el 70% de cobertura es un objetivo y no el 100%? ¿Cómo sería una suite de tests centrada únicamente en alcanzar el 100%, y qué dejaría de lado?
3. Tu agente de IA sugirió testear que el cuerpo de la respuesta contiene un campo `id` al crear una tarea. ¿Esto testa lógica de negocio o serialización HTTP? Justifica tu respuesta.
