# Riverside Community Theater — Cierre semanal de taquilla (Ejemplo de clase)

> **Para instructores:** Brief de demo en vivo para `ai-eng-financial-close`. Misma columna vertebral (ingesta con `source_ref`, herramientas de cálculo deterministas para totales / real vs presupuesto / desviaciones, un solo agente que interpreta pero no inventa aritmética, declarar datos faltantes, aprobación humana antes de distribuir, identidad de auditoría del agente + redacción). Dominio distinto: cierre semanal de taquilla y costes de sala de un teatro comunitario, no cierre mensual corporativo. Alcance: ~60–90 minutos. El alumnado sigue el brief completo del monorepo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Riverside Community Theater** cierra la taquilla cada lunes de la semana anterior. El personal pega exportaciones CSV y una hoja de presupuesto mínima en un email. Las cifras no cuadran; las explicaciones son a ojo. Vas a demos un **agente de cierre único con herramientas** que monta un informe semanal de una página, marca desviaciones sobre un umbral fijo y **no puede distribuir** hasta que la dirección de sala apruebe.

### Nota de alcance

| Proyecto evaluado (`ai-eng-financial-close`) | Este ejemplo de clase                                            |
| -------------------------------------------- | ---------------------------------------------------------------- |
| Briefing completo (multi-país, FX)           | 1 sala, 1 moneda (USD), umbral fijo de desviación 10%            |
| Varias fuentes + métricas operativas         | 2 CSV: `tickets.csv`, `budget.csv`                               |
| Cierre programado en background              | Un “ejecutar cierre de la semana W” manual basta                 |
| Distribución multi-destinatario              | Un solo revisor: `house_manager`; destinatarios = CC de la junta |
| Suite de privacidad completa                 | Log `agent_id`; solo redactar `patron_email`                     |

---

## Qué construir

### 1. Dataset mínimo (semana `2026-W12`)

`tickets.csv` (reales — una fila por noche de función):

| entry_id | date       | show          | category    | amount | source_ref                |
| -------- | ---------- | ------------- | ----------- | ------ | ------------------------- |
| T-01     | 2026-03-16 | Our Town      | box_office  | 4200   | tickets:T-01              |
| T-02     | 2026-03-17 | Our Town      | box_office  | 3800   | tickets:T-02              |
| T-03     | 2026-03-18 | Our Town      | concessions | 900    | tickets:T-03              |
| T-04     | 2026-03-19 | Our Town      | box_office  | null   | tickets:T-04 (incompleto) |
| T-05     | 2026-03-20 | Rentals: hall | rental      | 1500   | tickets:T-05              |

`budget.csv`:

| week     | category    | amount |
| -------- | ----------- | ------ |
| 2026-W12 | box_office  | 9000   |
| 2026-W12 | concessions | 800    |
| 2026-W12 | rental      | 1200   |

- [ ] Ingesta ambos ficheros; conservar `source_ref` en cada cifra
- [ ] Marcar `T-04` como `uncertain` / incompleto — no inventar 0 ni rellenar a ojo

### 2. Herramientas de cálculo deterministas

- [ ] `sum_by_category(rows)` → totales con `source_refs[]`
- [ ] `actual_vs_budget(actual, budget)` → desviación absoluta + `%`
- [ ] `flag_above_threshold(deviations, 10)` → categorías que superan el umbral
- [ ] Tests unitarios: mismos inputs → mismos outputs; totales conocidos a mano

### 3. Agente de cierre

- [ ] Llamar a las tools; el modelo solo escribe hipótesis a partir de resultados + refs
- [ ] Secciones del informe: totales por categoría, desviaciones ≥ 10%, lista de incompletos
- [ ] Para `box_office`: declarar la noche incompleta; no afirmar un real de semana completa

### 4. Aprobación humana + auditoría

- [ ] Borrador del informe permitido; distribución bloqueada hasta rol `house_manager`
- [ ] Rechazo con comentario → nueva versión que lo aborda
- [ ] Log de acciones con `agent_id=close_agent`; nunca loguear `patron_email`

---

## Verificar juntos

- [ ] Desviación concessions = `(900 - 800) / 800 = +12.5%` → marcada; cifra de la tool, no del modelo
- [ ] Box office: incompleto declarado; sin total falso del jueves
- [ ] Intentar distribuir sin house manager → bloqueado
- [ ] Re-ejecutar la misma semana → cifras no-hipótesis idénticas
- [ ] Mostrar una línea de auditoría; sin `patron_email` en logs

---

## Preguntas de discusión

1. ¿Por qué una suma incorrecta convincente es peor que una cifra faltante evidente en un informe de cierre?
2. ¿Dónde termina el trabajo del agente y dónde empieza el de la herramienta de cálculo?
3. ¿Qué debe ocurrir cuando el revisor rechaza con “explica el pico de alquiler”?
