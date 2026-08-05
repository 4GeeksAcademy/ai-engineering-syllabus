# Maple Street Library — Aprobación y Documento Final (Ejemplo de clase)

> **Para instructores:** Escenario paralelo de aula para `ai-eng-milestone-agentic-workflows-produce`. Misma columna vertebral (`interrupt`/`resume` acotados, checkpointer, aprobación por departamento, arbitraje, ultimate synthesizer → Ventas). Continúa el mostrador de subvenciones Maple Street de los ejemplos de las Partes 1–2. El alumnado sigue el brief completo del `README.md` en la raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

Las Partes 1–2 ya redactaron y autoevaluaron las secciones Programs / Facilities / Finance. Ahora: **humanos** deben aprobar cada ticket de departamento antes de que el **ultimate document synthesizer** envíe una respuesta final de subvención al mostrador (análogo de Ventas).

Pausa solo la rama que espera. Persiste con checkpointer. Reanuda sin reiniciar. Arbitra contradicciones. Traza cada nodo.

### Nota de alcance

| Proyecto evaluado (`ai-eng-milestone-agentic-workflows-produce`) | Este ejemplo de clase                     |
| ---------------------------------------------------------------- | ----------------------------------------- |
| Monorepo de empresa + aprobadores CONTEXT / arbitraje §7         | Solo mostrador Maple Street               |
| Pipeline completo Partes 1–2                                     | Fixtures de tickets de asignación Parte 2 |
| Checkpointer SQLite/Postgres                                     | Checkpointer SQLite en archivo            |
| UI completa de aprobación en `uis/backoffice`                    | CLI approve/reject + ticket JSON          |
| E2E reproducible + test de paralelo bajo interrupt               | Mini E2E con fixtures + 6 tests           |

---

## Columna vertebral (debe cubrirse en vivo)

1. **Ticket de asignación** por departamento esperando aprobación humana
2. **`interrupt` acotado** — solo pausa esa rama
3. **Checkpointer** + `thread_id` con namespace (p. ej. `grant-{ticket_id}`)
4. **`resume` explícito** con payload validado: approve / reject / request_changes
5. **Nodo de arbitraje** con triggers concretos (Programs vs Finance presupuesto) → árbitro fijo: lead del mostrador (tabla de reglas, no voto LLM)
6. Límite de iteraciones en bucles post-rechazo
7. Cuando todos aprueban → **ultimate synthesizer** → documento final → mostrador
8. Trace por nodo: agente, input, output, timestamp
9. **Demo obligatoria:** aprobar Finance mientras Programs sigue interrumpido

![Tickets de aprobación → synthesizer → documento final](../approval-document-completion.jpg)

---

## Qué construir

### 1. Human-in-the-loop

- [ ] Interrupt antes de cada aprobación de departamento
- [ ] Resume valida la decisión humana
- [ ] Reject / request_changes vuelve hacia el generador de Parte 2 (o ruta documentada)

### 2. Control

- [ ] Nodo de arbitraje ante contradicción de presupuesto Programs vs Finance → árbitro por regla del mostrador (no LLM)
- [ ] `max_iterations` en bucles restantes entre departamentos
- [ ] Trace append-only en el estado
- [ ] `thread_id` = `grant-{ticket_id}` (obligatorio)

### 3. Produce

- [ ] Ultimate synthesizer solo si todos los tickets están aprobados
- [ ] Estado del ticket → `terminado`; ruta del `.md`/`.pdf` final guardada

### 4. Tests (`tests/test_grant_produce.py`)

| #   | Escenario                                                | Esperado                                  |
| --- | -------------------------------------------------------- | ----------------------------------------- |
| 1   | Aprobar los tres                                         | Documento final; ticket `terminado`       |
| 2   | Interrupt + resume Finance                               | Reanuda; Programs no reinicia             |
| 3   | **Aprobar Finance mientras Programs sigue interrumpido** | Finance completa; Programs sigue en pausa |
| 4   | Reject Facilities                                        | Sin synthesizer; sección a revisión       |
| 5   | Contradicción Programs vs Finance                        | Dispara arbitraje + regla fija            |
| 6   | Límite de iteraciones                                    | Para el bucle; trace muestra el límite    |

---

## Verificar juntos

- [ ] Un departamento esperando no congela a los demás (test #3)
- [ ] Resume ≠ reinicio completo
- [ ] Synthesizer nunca corre con una aprobación pendiente
- [ ] Trace lista agentes en orden para la ejecución
- [ ] E2E con fixtures corre sin clicks manuales en UI

---

## Preguntas de discusión

1. Guardrail vs interrupt — ¿qué casos nunca necesitan humano?
2. ¿Por qué el `thread_id` debe ir namespaced por ticket de subvención?
3. ¿Campos mínimos de UI para aprobar con confianza sin releer todo el borrador?
4. ¿Por qué el arbitraje usa regla/humano fijo, no consenso LLM?
