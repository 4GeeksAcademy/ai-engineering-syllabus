# Ejemplo de clase: Tablero de despensa (SDD)

> **Nota para el instructor:** Ejemplo de aula para _Backoffice de Operaciones – Gestor de Inventario_. Mismo bucle (`specify → plan → tasks → implement → verify`) en un dominio mínimo de despensa. Pensado para una sesión en vivo de 1–2 horas. NO compartir con estudiantes antes de que intenten el proyecto principal.

_These instructions are also available in [English](./README.md)._

---

## El escenario

### Nota de alcance

Solo para sesión en vivo. Mismos patrones SDD que el proyecto oficial; catálogos CONTEXT y profundidad del monorepo reducidos. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.

Una cocina de coworking controla café, leche y snacks. Antes editaban un número `stock` en una hoja. Ops quiere un tablero mínimo: alta de artículos, movimientos, nunca tocar stock directo — y marcar lo que esté bajo el punto de reorden.

Asume que ya existen `.agents/rules` y un `memory-bank/` pequeño de un ejercicio previo.

---

## Fase 1 — Spec (20 min)

Crea `specs/pantry/spec.md` con ≥4 criterios EARS, incluyendo:

| Id        | Intención                                      |
| --------- | ---------------------------------------------- |
| `PAN-001` | Stock derivado solo de movimientos             |
| `PAN-002` | Rechazar salida que dejaría stock negativo     |
| `PAN-003` | Rechazar movimiento sobre artículo inexistente |
| `PAN-004` | Señalar cuando stock &lt; reorder_point        |

Sin arquitectura ni lista de tareas en este fichero.

---

## Fase 2 — Plan + tareas (15 min)

- [ ] `plan.md` — dónde vive el cálculo (p. ej. función de servicio que suma movimientos); justifica por qué no hay columna `stock` escribible.
- [ ] `tasks.md` — una tarea por id de criterio; p. ej. `T-001` → `PAN-001`.

---

## Fase 3 — Implementar + verificar (40–50 min)

### Modelo mínimo

| Entidad  | Campos                                                                              |
| -------- | ----------------------------------------------------------------------------------- |
| Item     | `name`, `unit` (`kg`\|`unit`), `reorder_point`                                      |
| Movement | `item_id`, `kind` (`inbound`\|`outbound`\|`adjustment`), `quantity`, `reason`, `at` |

### Debe demo

- [ ] Alta/listado de artículos
- [ ] Entrada y luego salida; stock mostrado = suma
- [ ] No existe (o se rechaza) ruta de edición directa de stock
- [ ] Salida negativa rechazada; stock sin cambio
- [ ] Señal visual de bajo reorden
- [ ] Al menos un test por `PAN-00x`

### Cambio a mitad de sesión (opcional 10 min)

El instructor añade: "Quedan prohibidos los ajustes que fijen stock absoluto; solo ajustes por delta." Los estudiantes editan `spec.md` primero, regeneran solo tareas afectadas, luego código.

---

## Preguntas de discusión

1. ¿Por qué un campo `stock` editable es el fallo por defecto del agente?
2. ¿Qué va en `plan.md` y **no** debe aparecer en `spec.md`?
3. ¿Por qué regenerar solo las tareas afectadas tras un cambio de requisito?

---

## Checklist del instructor

- [ ] Spec usa EARS + ids; invariante explícito
- [ ] Capas no mezcladas en un solo doc
- [ ] Tests mapean a ids de criterio
- [ ] Si hubo demo de cambio: evidencia de edición spec-first
