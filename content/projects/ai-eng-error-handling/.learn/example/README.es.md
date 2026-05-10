# Ejemplo de clase: Auditoría de gestión de errores — App de recetas

> **Nota para el instructor:** Este es un ejemplo de clase para introducir los conceptos del proyecto *Gestión de Errores* usando un dominio más sencillo. Cubre los mismos patrones (UI de tres estados, try/catch acotado, sin stack traces al cliente, códigos de salida en scripts, optional chaining, bloques finally) aplicados a una pequeña app de recetas ya construida. Úsalo para demostrar el flujo de auditoría antes de que los estudiantes lo apliquen a su propio monorepo. NO compartir este archivo con los estudiantes antes de que intenten el proyecto principal.

---

## El escenario

Un equipo pequeño construyó la semana pasada una app de descubrimiento de recetas. Funciona la mayoría del tiempo, pero cuando algo falla, la experiencia se rompe de forma grave. Los usuarios ven mensajes de error técnicos en crudo, las páginas quedan en blanco y los scripts se caen sin dejar rastro útil.

Tu tarea es auditar el repositorio y aplicar una estrategia de gestión de errores consistente en las tres capas: el frontend Next.js, el backend FastAPI y el script Python de importación de datos.

> **Del ticket de revisión del tech lead:**
>
> - Ningún error debe romper la app ni dejar al usuario en un estado indefinido.
> - Toda operación asíncrona debe tener tres estados visibles: cargando, éxito y error.
> - Los mensajes de error que ve el usuario deben ser legibles — nunca un código de estado, un stack trace o un error de parseo de JSON en crudo.
> - Todo estado de error debe ofrecer una salida clara: un botón de reintentar, un enlace atrás o un prompt para contactar soporte.
> - En el backend, las excepciones deben capturarse en el ámbito correcto — no con un único try/except gigante.
> - Los scripts deben terminar con código distinto de cero en un fallo crítico e imprimir los errores en `stderr`.

---

## Visión general del repositorio

La app tiene tres capas:

```text
frontend/          Next.js + TypeScript
  pages/
    index.tsx      Página de listado de recetas — carga desde la API al montar
    [id].tsx       Página de detalle de receta — carga una sola receta
    submit.tsx     Formulario de envío de recetas — hace POST a la API
backend/           FastAPI
  main.py          Rutas: GET /recipes, GET /recipes/{id}, POST /recipes
scripts/
  import_recipes.py  Lee un fichero JSON e inserta recetas en la BD en bloque
```

---

## Checklist de auditoría

### Frontend (Next.js / TypeScript)

**`pages/index.tsx` — Listado de recetas**

- [ ] El `useEffect` carga las recetas pero no tiene `try/catch` — si la petición falla, el componente se rompe en silencio.
- [ ] No hay estado de carga: la página renderiza una lista vacía mientras se obtienen los datos.
- [ ] Si el fetch falla, no se muestra nada — ni mensaje ni opción de reintentar.
- [ ] **Corrección:** Implementa el patrón de tres estados con `isLoading`, `error` y `data`. Muestra un spinner mientras carga, un mensaje de error con botón "Intentar de nuevo" en caso de fallo, y la lista en caso de éxito.

**`pages/[id].tsx` — Detalle de receta**

- [ ] `recipe.ingredients.map(...)` lanzará una excepción si `ingredients` es `undefined` o `null`.
- [ ] Un `404` de la API renderiza una página en blanco.
- [ ] **Corrección:** Añade `optional chaining` (`recipe.ingredients?.map(...)`), un fallback para campos que falten, y una página amigable de "Receta no encontrada" para respuestas `404`.

**`pages/submit.tsx` — Formulario de envío**

- [ ] El manejador del envío no tiene `try/catch` — un error de red provoca una promesa rechazada sin gestionar.
- [ ] El botón permanece habilitado mientras la petición está en vuelo — el usuario puede enviar dos veces.
- [ ] En caso de error de la API, el JSON crudo del servidor se renderiza directamente dentro de una etiqueta `<p>`.
- [ ] No hay bloque `finally`, por lo que `isLoading` nunca vuelve a `false` si la petición lanza una excepción.
- [ ] **Corrección:** Envuelve el fetch en `try/catch/finally`, deshabilita el botón durante la petición, traduce los errores de la API en mensajes legibles para el usuario y reinicia siempre `isLoading` en `finally`.

---

### Backend (FastAPI)

**`GET /recipes` y `GET /recipes/{id}`**

- [ ] Un error de conexión a la base de datos hace que FastAPI devuelva un traceback de Python en crudo como cuerpo de la respuesta.
- [ ] `GET /recipes/{id}` con un `id` no entero (p. ej. `/recipes/abc`) se rompe con un `ValueError` sin gestionar.
- [ ] **Corrección:** Añade un manejador de excepciones global que devuelva `{"error": "Algo ha fallado"}` para excepciones no capturadas. Gestiona `ValueError` con una respuesta `400`.

**`POST /recipes`**

- [ ] El handler de la ruta tiene un único `try/except Exception` grande que engulle todos los errores y siempre devuelve `200`.
- [ ] Los errores de validación (falta `title`, `ingredients` vacío) devuelven la representación interna del objeto Python, no un mensaje JSON limpio.
- [ ] **Corrección:** Divide el catch genérico en catches específicos y acotados. Devuelve `400` para errores de validación con un cuerpo JSON a nivel de campo. Reserva el handler genérico `500` para errores verdaderamente inesperados.

**Datos sensibles:**

- [ ] La cadena de conexión a la base de datos aparece en los logs de error que se devuelven al cliente.
- [ ] **Corrección:** Registra el error completo en el servidor; devuelve al cliente únicamente un mensaje genérico seguro.

---

### Script (`scripts/import_recipes.py`)

- [ ] El script abre el fichero JSON sin `try/except` — si el fichero falta o está mal formado, se rompe con un traceback de Python impreso en `stdout`.
- [ ] Cuando falla la inserción de una receta, el script continúa en silencio — el usuario nunca sabe que se omitieron registros.
- [ ] El script siempre termina con código `0`, incluso ante un fallo crítico.
- [ ] **Corrección:** Envuelve la lectura de fichero y el parseo de JSON en `try/except` con mensajes informativos impresos en `stderr`. Recopila e informa los registros omitidos al final. Llama a `sys.exit(1)` si el fichero no se puede abrir.

---

## Qué evaluaremos

- [ ] Las tres páginas del frontend implementan el patrón de tres estados: cargando / éxito / error.
- [ ] Los bloques `try/catch` están acotados a operaciones específicas, no envuelven funciones enteras.
- [ ] Los bloques `finally` se usan para resetear el estado de carga en todos los formularios de envío.
- [ ] El `optional chaining` y los fallbacks evitan errores de renderizado por datos `undefined`.
- [ ] Las rutas del backend devuelven respuestas JSON de error estructuradas con los códigos HTTP correctos.
- [ ] Ningún traceback de Python ni cadena de conexión a la BD llega al cliente.
- [ ] El script de importación gestiona errores de fichero, reporta registros omitidos y termina con `sys.exit(1)` ante un fallo crítico.

---

## Preguntas de discusión

1. La ruta del backend tiene un único `try/except Exception` que lo captura todo. ¿Por qué se considera mala práctica? ¿Qué tipos de errores quedan ocultos tras él, y cómo mejora la visibilidad una gestión de errores acotada?
2. El botón de envío del frontend no usa bloque `finally` para resetear el estado de carga. Describe un escenario concreto en el que omitir `finally` deja la UI permanentemente rota, incluso después de que la red del usuario se recupere.
3. El script termina con código `0` aunque falle. ¿Por qué importa el código de salida en un pipeline de CI/CD o en un flujo automatizado? ¿Qué podría fallar silenciosamente más adelante?
