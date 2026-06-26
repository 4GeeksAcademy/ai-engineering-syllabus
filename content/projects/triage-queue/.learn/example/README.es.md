# Ejemplo en clase: Cola de trabajos de imprenta — Cola de prioridad (Ejemplo para clase)

> **Para instructores:** Escenario paralelo en aula para `triage-queue`. Misma columna vertebral (cola de prioridad con FIFO dentro del nivel, cinco operaciones núcleo, menú CLI, estructuras solo con stdlib, debate de diseño sobre concurrencia), dominio distinto. Los estudiantes siguen el enunciado completo del hospital en el `README.md` de la raíz del proyecto.

_Estas instrucciones también están disponibles en [inglés](./README.md)._

---

## El reto

Una imprenta de barrio sigue anotando pedidos en un bloc de papel. Los programas de boda urgentes se cuelan delante de los folletos estándar, y dos empleados que actualizan el bloc a la vez se borran entradas. Tu demo en vivo modela un **gestor de cola en terminal** — sin interfaz gráfica — listo para integrarse después en una app real.

> **La especificación del encargado dice:**
>
> - Cada trabajo recibe un **nivel de prioridad** (1 = urgente, 2 = mismo día, 3 = estándar).
> - Registrar nombre del cliente, hora de llegada y nivel de prioridad.
> - Nivel 1 siempre antes que 2, nivel 2 antes que 3; **FIFO dentro del mismo nivel**.
> - Operaciones: encolar, desencolar, peek, listar cola, stats.

### Nota de alcance

Pensado para **una sesión en vivo (~60–90 min)**. Mismos patrones que el proyecto estudiantil, pero:

- Dominio de **imprenta**, no hospital.
- Un solo archivo `print_queue.py` — sin repositorio plantilla.
- `DESIGN.md` es **verbal en clase**; los estudiantes lo escriben en el proyecto real.
- Menú CLI de cinco opciones como tarea si falta tiempo; en vivo basta con añadir / llamar siguiente / ver cola.

---

## Qué construir

### Modelo de datos

- [ ] Dataclass `Job`: `customer_name`, `priority_level` (int 1–3), `arrived_at` (`datetime`).
- [ ] Clase `PrintQueue` que posea la estructura interna de prioridad.

### Operaciones de cola

- [ ] `enqueue(job)` — insertar respetando prioridad + orden de llegada.
- [ ] `dequeue()` — extraer y devolver el siguiente trabajo; error claro si está vacía.
- [ ] `peek()` — siguiente trabajo sin extraer.
- [ ] `list_queue()` — todos los trabajos en espera en orden de atención.
- [ ] `stats()` — diccionario con conteos por nivel de prioridad.

| Método       | Comportamiento esperado                                         |
| ------------ | --------------------------------------------------------------- |
| `enqueue`    | Trabajo urgente queda delante de mismo día y estándar en espera |
| `dequeue`    | Siempre saca del nivel no vacío más bajo (1 → 2 → 3)            |
| `peek`       | Mismo objetivo que `dequeue` sin mutar                          |
| `list_queue` | `[todos nivel 1 FIFO] + [nivel 2 FIFO] + [nivel 3 FIFO]`        |
| `stats`      | p. ej. `{1: 0, 2: 2, 3: 1}`                                     |

### CLI (mínimo para demo en vivo)

- [ ] Bucle de menú de texto:
  - Añadir trabajo (nombre + prioridad).
  - Llamar siguiente (`dequeue`).
  - Ver cola (`list_queue`).
  - _(Tarea si hace falta: stats + salida pulida)_

### Correctitud (demostrar en clase)

- [ ] Trabajo urgente que llega con mismo día y estándar en espera → va al frente.
- [ ] Dos trabajos mismo día → orden estricto de llegada.
- [ ] `dequeue()` / `peek()` en cola vacía → capturado en CLI, sin romper el programa.

⚠️ **Solo stdlib:** `collections.deque`, `heapq`, `datetime`.

---

## Verificar juntos

- [ ] Añadir trabajo estándar, luego urgente → el urgente sale primero al "llamar siguiente".
- [ ] Añadir dos trabajos mismo día con 30 s de diferencia → primero el que llegó antes.
- [ ] Orden de `list_queue` coincide con el orden de atención esperado tras inserciones mixtas.
- [ ] Conteos de `stats()` coinciden con la cola visible.
- [ ] `dequeue()` en cola vacía muestra mensaje amable y el programa continúa.
- [ ] Prioridad inválida (p. ej. `4`) rechazada sin romper el programa.

---

## Preguntas de debate

1. ¿Por qué una sola `deque` no basta para esta especificación? ¿Qué falla si solo haces append y pop por un extremo?
2. Tres `deque` separadas (una por nivel) frente a un `heapq` con tuplas `(prioridad, contador, job)` — ¿qué compromisos importan en complejidad de encolar/desencolar y claridad del código?
3. Si dos empleados comparten un mismo objeto cola, ¿qué orden de mutación en `dequeue` + `enqueue` evita procesar el mismo trabajo dos veces?
