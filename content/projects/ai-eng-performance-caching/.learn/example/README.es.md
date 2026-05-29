# Biblioteca del Barrio — Mini laboratorio de caching (Ejemplo en clase)

> **Para instructores:** Escenario paralelo para `ai-eng-application-caching`. Mismo esqueleto (lazy load, `useMemo`, caché TTL en FastAPI + invalidación, informe breve), dominio distinto. Los estudiantes siguen el enunciado completo del monorepo en el `README.md` de la raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Biblioteca Maple Street** usa un stack pequeño: web pública de catálogo (`catalog-site`, Next.js), mostrador de reservas del personal (`desk-app`, Next.js) y API FastAPI (`library-api`). La telemetría muestra llamadas idénticas repetidas a `GET /books` y un panel de filtros que se re-renderiza en cada tecla. En una sesión, demuestra **caching deliberado** en una superficie reducida — no el alcance completo del monorepo corporativo del proyecto evaluable.

### Nota de alcance

| Proyecto evaluable (`ai-eng-application-caching`) | Este ejemplo en clase                                  |
| ------------------------------------------------- | ------------------------------------------------------ |
| Web corporativa + backoffice (2 apps)             | Catálogo público + app de mostrador                    |
| ≥2 componentes/rutas con lazy loading             | 1 componente con carga diferida                        |
| ≥1 `useMemo` en cálculo no trivial                | 1 `useMemo` en filtro/ordenación de libros             |
| ≥2 endpoints cacheados + auditoría completa       | 1 `GET` cacheado + lista de por qué se omiten otros    |
| Rúbrica completa en `CACHING_REPORT.md`           | `CACHING_CLASS.md` breve (4 secciones)                 |
| Invalidación en todos los writes                  | Invalidación en un `POST` que afecta al `GET` cacheado |

---

## Qué construir

### 1. Frontend — una carga diferida

- [ ] Elegir **un** componente pesado (p. ej. `BookCoverGallery` o `LoanHistoryChart`) usado solo en ruta secundaria o bajo el pliegue.
- [ ] Cargarlo con `next/dynamic` (o `React.lazy` + `Suspense` si no usas App Router).
- [ ] Una frase en notas: por qué diferir este chunk mejora el TTI.

### 2. Frontend — un `useMemo`

- [ ] En la vista de listado del mostrador, memoizar una lista derivada **no trivial** (filtrar + ordenar ≥50 libros mock).
- [ ] Array de dependencias: `[books, searchQuery, sortKey]` (o equivalente).
- [ ] **No** memoizar formateo de cadenas trivial.

### 3. Backend — una caché TTL + invalidación

**Identifica candidatos primero.** La rúbrica completa (señales en logs → coste / frecuencia / estabilidad) está en el [README.es.md](../../README.es.md#cómo-identificar-candidatos-con-evidencia-no-por-intuición) del proyecto. En el mini-lab, añade esto a `main.py` de `library-api` antes de elegir `/books`:

```python
import time
import logging
from fastapi import Request

logger = logging.getLogger("api.timing")

@app.middleware("http")
async def timing_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration = (time.perf_counter() - start) * 1000
    logger.info(
        f"{request.method} {request.url.path} → {response.status_code} | {duration:.1f}ms"
    )
    return response
```

Navega el catálogo dos veces: `GET /books` debe repetirse y ser lento en el primer impacto — eso justifica la caché TTL de abajo.

Si el catálogo tiene pocos libros mock, los tiempos engañan. Haz **seed** de muchos títulos realistas antes (seeder o SQL con agente — autores, géneros y años variados; ver [README.es.md](../../README.es.md#carga-realista-en-la-base-de-datos)) y vuelve a mirar los logs.

| Endpoint          | ¿Caché? | TTL | Notas                                     |
| ----------------- | ------- | --- | ----------------------------------------- |
| `GET /books`      | Sí      | 45s | Catálogo público; estable entre préstamos |
| `GET /members/me` | No      | —   | Por usuario; clave compartida = fuga      |
| `POST /books`     | —       | —   | Debe invalidar caché de `GET /books`      |

- [ ] Implementar caché en proceso con diccionario (o `functools` + expiración) solo para `GET /books`.
- [ ] En `POST /books` (nuevo título), limpiar o invalidar por prefijo la caché del catálogo.
- [ ] Registrar o comentar por qué se rechazó `GET /members/me`.

### 4. Informe breve

- [ ] Crear `CACHING_CLASS.md` con:
  - **Frontend** (elección de lazy + memo)
  - **Backend** (TTL + invalidación de `/books`)
  - **Un intercambio** (p. ej. catálogo potencialmente desactualizado 45s vs. navegación más rápida)
  - **No cacheado** (al menos `/members/me` con motivo)

---

## Verificar juntos

- [ ] Los logs de timing listan cada petición (`GET /books → 200 | …ms`); el primer `/books` más lento que el segundo tras calentar la caché.
- [ ] El segundo `GET /books` es más rápido que el primero (o misma respuesta desde caché — demostrar con logs).
- [ ] Tras `POST /books`, el siguiente `GET /books` incluye el título nuevo.
- [ ] El chunk lazy aparece solo al entrar en la ruta que lo necesita (pestaña Network: JS separado).
- [ ] Al cambiar deps de `useMemo`, la lista se recalcula (cambiar orden en UI).
- [ ] Apps y API siguen arrancando (`docker compose up` o comandos locales de dev).

---

## Preguntas para debatir

1. ¿Por qué un TTL de 45s es aceptable para un listado público de libros pero no para “los libros que tengo prestados ahora”?
2. ¿Cuándo el lazy loading perjudica más la UX (spinners, layout shift) de lo que ayuda al tamaño del bundle?
3. ¿Cómo migrarías la caché en proceso a Redis sin cambiar la historia de invalidación?
