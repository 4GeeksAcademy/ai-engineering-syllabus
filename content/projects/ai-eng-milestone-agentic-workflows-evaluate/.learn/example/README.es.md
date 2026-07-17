# Maple Street Library — Generación y Evaluación de Respuestas (Ejemplo de clase)

> **Para instructores:** Escenario paralelo de aula para `ai-eng-milestone-agentic-workflows-evaluate`. Misma columna vertebral (generadores por departamento, evaluadores en paralelo, ciclo generador-evaluador acotado, estado del ticket). Continúa el mostrador de subvenciones Maple Street del ejemplo de la Parte 1. El alumnado sigue el brief completo del `README.md` en la raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

La Parte 1 ya le dijo al mostrador de subvenciones **qué** deben responder Programs, Facilities y Finance. Ahora: redactar cada sección automáticamente y **autoevaluarla** (legibilidad, pertinencia, lineamientos de la biblioteca) antes de que la vea un humano. Los fallos vuelven al generador con feedback concreto — hasta un límite duro de iteraciones.

### Nota de alcance

| Proyecto evaluado (`ai-eng-milestone-agentic-workflows-evaluate`) | Este ejemplo de clase                        |
| ----------------------------------------------------------------- | -------------------------------------------- |
| Monorepo de empresa + reglas de lineamientos del CONTEXT          | Solo mostrador Maple Street                  |
| Reuso completo del pipeline de la Parte 1                         | JSON fixture del synthesizer de Parte 1      |
| Evaluadores paralelos legibilidad / pertinencia / lineamientos    | Tres evaluadores stub + lista fija de reglas |
| Actualizaciones completas de UI de tickets                        | Transiciones de estado en JSON               |
| PR de empresa con ejemplos pass + fail                            | Demo en vivo + 5 tests automatizados         |

---

## Columna vertebral (debe cubrirse en vivo)

1. **Assignment orchestrator** mapea workstreams de Parte 1 → generadores por departamento
2. **Un generador por departamento** redacta su sección
3. **Evaluadores en paralelo** sobre cada borrador: legibilidad, pertinencia, lineamientos
4. **Fallo → regenerar** con feedback estructurado (no vibes libres)
5. **Límite de iteraciones** — el ticket sigue vivo; sección `needs_human_review` si se agota
6. **Synthesizer / handoff** empaqueta contenido + resultados de eval por departamento
7. Estados del ticket: `drafting` → `under_evaluation` → listo para Parte 3

![Mapeo departamental y finalización del entregable](../departmental-mapping-deliverable-finalization.jpg)

---

## Lineamientos semilla (indicativo — no es CONTEXT)

```text
[G1] Toda sección debe nombrar un importe en dólares o "TBD with Finance".
[G2] Sin promesas de apertura en domingo sin OK de Facilities.
[G3] Tono: lenguaje claro; grado Flesch ≤ 10 en secciones públicas.
[G4] Debe responder lo que pide el solicitante (story hours / sala / fondos).
```

---

## Qué construir

### 1. Generadores

- [ ] Generadores Programs / Facilities / Finance; input = resumen de workstream Parte 1
- [ ] Salida estructurada de borrador por departamento

### 2. Evaluadores (paralelo)

- [ ] Legibilidad → pass/fail + score
- [ ] Pertinencia → pass/fail + asks faltantes
- [ ] Lineamientos → pass/fail + ids de reglas fallidas (`G1`…)

### 3. Ciclo

- [ ] Cualquier fail → regenerar con payload de feedback
- [ ] Tope p. ej. `max_iterations=3`; luego `needs_human_review`

### 4. Tests (`tests/test_grant_evaluate.py`)

| #   | Escenario                          | Esperado                                     |
| --- | ---------------------------------- | -------------------------------------------- |
| 1   | Borrador limpio                    | Todos pass; handoff con contenido + scores   |
| 2   | Falta importe                      | Guidelines fail → regenerar → pass o límite  |
| 3   | Promesa de domingos                | `G2` fail con feedback específico            |
| 4   | Límite de iteraciones              | Ticket no descartado; sección marcada humana |
| 5   | Generador + un evaluador unitarios | Solo mocks                                   |

---

## Verificar juntos

- [ ] Departamentos redactan en paralelo sin bloquearse
- [ ] Feedback nombra la regla / ask faltante (no “mejora la calidad”)
- [ ] Estado del ticket pasa por drafting / under_evaluation
- [ ] JSON de handoff tiene contenido **y** resultado de evaluación por departamento

---

## Preguntas de discusión

1. ¿Por qué la salida estructurada del evaluador gana a un solo “score: 7/10”?
2. ¿Cómo escriben resultados los evaluadores en paralelo sin pisar el estado compartido?
3. Límite agotado: ¿descartar sección, escalar, o enviar con warning?
