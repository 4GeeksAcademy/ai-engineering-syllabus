# Agente de Mostrador Maple Street Library — Memoria y Auto-mejora (Ejemplo de clase)

> **Para instructores:** Escenario paralelo de aula para `ai-eng-milestone-agentic-engineering`. Misma columna vertebral (interfaz explícita de memoria, `memory_proposal` estructurado, proponer en conversación → confirmar clasificado → auditar → consolidar). Dominio distinto a los agentes CONTEXT de empresa. Continúa la narrativa Maple Street Library del ejemplo de harness. El alumnado sigue el brief completo del `README.md` en la raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

El agente de mostrador de **Maple Street Library** ya responde FAQ (horario, préstamos, multas) y rechaza jailbreaks. Problema: cada turno empieza en frío — el personal vuelve a explicar que “las reservas de letra grande van al estante amarillo” tres veces por semana.

En una sesión: añade un bucle mínimo **proponer–confirmar–recordar** para que los hechos corregidos del mostrador persistan solo cuando una persona dice que sí.

### Nota de alcance

| Proyecto evaluado (`ai-eng-milestone-agentic-engineering`) | Este ejemplo de clase                                 |
| ---------------------------------------------------------- | ----------------------------------------------------- |
| Monorepo de empresa + reglas de memoria del CONTEXT        | Solo mostrador Maple Street                           |
| Redis / VectorDB / híbrido justificado desde CONTEXT       | Dict en memoria + JSON opcional                       |
| Stack completo LangGraph + MCP + guardrails                | Agente stub: retrieve FAQ + hooks de memoria          |
| Lista never-store de empresa                               | Nunca guardar: teléfonos de socios, importes de multa |
| PR completo + dos ciclos de evidencia                      | Demo en vivo + 4 tests automatizados                  |

---

## Columna vertebral (debe cubrirse en vivo)

1. API explícita `read` / `write` de memoria (no “meter todo en el system prompt”)
2. Salida estructurada por turno: `reply` + `memory_proposal` opcional
3. Propuesta dentro de la misma respuesta; **aún no escribir**
4. Una sola propuesta pendiente; silencio/cambio de tema = rechazo
5. Clasificar intención (approve / reject / unclear) — no `"sí" in texto`
6. Log de auditoría para aprobar y rechazar
7. Consolidación mínima (p. ej. máx. 20 entradas o overwrite por `key`)

---

## Hechos semilla del mostrador (indicativo)

```text
[FAQ] Préstamo: 21 días. Renovaciones: una si no hay reservas.
[FAQ] Horario: lun–sáb 09:00–20:00.
[CORRECTABLE] Reservas letra grande: el personal dice "estante amarillo" pero el FAQ aún dice "mostrador de reservas".
```

Never-store: teléfono del socio, saldo exacto de multa de un socio nombrado.

---

## Qué construir

### 1. Interfaz de memoria

- [ ] `memory.read(query)` / `memory.write(key, fact)` / `memory.list()`
- [ ] Dict (o JSON); documentar por qué KV basta para correcciones de mostrador

### 2. Auto-evaluación + propuesta

- [ ] Salida estructurada por turno; la mayoría → `memory_proposal: null`
- [ ] Si el personal corrige “letra grande → estante amarillo” → proponer en la respuesta
- [ ] Documentar 3 turnos no memorables (gracias, “¿a qué hora cierran?”, resumen puntual)

### 3. Confirmación + auditoría

- [ ] Con pendiente: clasificar primero el siguiente mensaje
- [ ] Approve → write; reject/unclear → descartar; ambos auditados
- [ ] Bloquear segunda propuesta hasta cerrar la primera

### 4. Consolidación

- [ ] Misma `key` sobrescribe; o tope duro (p. ej. 20) eliminando la más antigua
- [ ] Rechazar escrituras que parezcan teléfonos / saldos de multa aunque “aprueben”

### 5. Tests (`tests/test_desk_memory.py`)

| #   | Escenario                                                            | Esperado                               |
| --- | -------------------------------------------------------------------- | -------------------------------------- |
| 1   | Corrección → propuesta → approve claro → luego preguntar por estante | Usa el hecho; audit `approve`          |
| 2   | Propuesta → “dime el clima” / unclear                                | Sin write; audit reject/discard        |
| 3   | “Gracias” no memorable                                               | `memory_proposal` null                 |
| 4   | Usuario “aprueba” guardar un teléfono de socio                       | Write rechazado; never-store respetado |

---

## Verificar juntos

- [ ] FAQ in-domain sigue sin proponer en cada turno
- [ ] Ciclo approve: el segundo turno usa el hecho del estante amarillo
- [ ] Ciclo reject: almacén sin cambios
- [ ] Pendiente bloquea una segunda propuesta
- [ ] Auditoría muestra ambos resultados

---

## Preguntas de discusión

1. ¿Por qué escribir al auto-evaluar es peor que proponer–confirmar cuando la memoria es persistente?
2. ¿Cuándo un VectorDB es innecesario para “correcciones de mostrador”, y cuándo lo añadirías?
3. ¿Cómo interactúa el harness previo (nunca tratar RAG como system) con intentos de envenenar la memoria?
