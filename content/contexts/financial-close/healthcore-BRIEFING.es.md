# BRIEFING.md — HealthCore

## Agentic Engineering – Cierre Financiero Mensual

*These instructions are [available in English](./healthcore-BRIEFING.en.md).*

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**HealthCore** es una empresa de servicios de salud ambulatoria fundada en 2011 en Austin, Texas. Opera 12 clínicas, 9 en Estados Unidos y 3 en Reino Unido, emplea a unas 200 personas y factura alrededor de 28 millones de dólares al año. Opera con dólares (USD) y libras esterlinas (GBP), y bajo dos marcos de protección de datos de salud: HIPAA en Estados Unidos y UK GDPR en Reino Unido.

---

## Tu departamento y el problema que debes resolver

Formas parte de **HealthCore Digital**, la unidad interna que construye la infraestructura de la empresa, y reportas al CTO James Osei.

La Dra. Sandra Okonkwo, CEO, recibe los datos financieros del mes en informes que cada departamento prepara por separado, con formatos distintos y cifras que a veces se contradicen porque salen de sistemas diferentes. Los ingresos de Estados Unidos dependen de aseguradoras y programas públicos con tasas de denegación de reclamaciones que cambian de un mes a otro, y la CEO necesita ver ese efecto en el cierre sin esperar al informe de Revenue Cycle.

---

## Tu stakeholder

**Dra. Sandra Okonkwo**, CEO (Austin)

> Asunto: Cierre financiero mensual
>
> Equipo:
>
> 1. Necesito el cierre de cada mes el tercer día hábil, a primera hora de Austin.
> 2. Ingresos por país y por pagador (seguros comerciales, Medicare/Medicaid, privado, contrato NHS), y gastos por país. Consolidado en dólares.
> 3. Toda desviación igual o superior al 5% debe explicarse con datos. No acepto explicaciones sin cifras que las sostengan.
> 4. Tom Callahan revisa el informe antes de que llegue al equipo directivo.
> 5. Este informe es financiero. No debe contener ningún dato de pacientes, en ninguna sección y bajo ninguna circunstancia. Si algún registro de origen lo contiene, quiero saberlo, pero sin que el dato aparezca en el informe.
>
> Sandra

---

## Alcance de idioma

- El idioma base es el **inglés**, porque el equipo directivo trabaja en Austin y en Londres.
- El español es **opcional**. Si lo implementas, las cifras deben ser idénticas en ambas versiones: solo cambia el texto.

---

## Fuentes de datos

Genera tres archivos CSV para el **mes de cierre** (el último mes completo antes de la fecha de carga):

| Archivo | Columnas | Contenido |
|---|---|---|
| `ledger.csv` | `entry_id, date, country, payer, category, description, currency, amount, source_ref` | Movimientos de ingresos y gastos del mes. Los ingresos son positivos y los gastos, negativos. Los gastos usan `payer = n/a` |
| `budget.csv` | `month, country, payer, category, currency, amount` | Presupuesto del mes |
| `operations.csv` | `month, country, payer, metric, value` | Indicadores operativos **agregados** que sirven de base a las explicaciones |

Cada partida debe tener **varios registros** en `ledger.csv` cuya suma coincida exactamente con la cifra real de la tabla siguiente. Los ingresos se registran **agregados por clínica y pagador**, nunca por paciente. En las partidas de proveedores, la descripción incluye el proveedor, el precio unitario y la cantidad.

Incluye intencionadamente **un registro de gasto** cuya descripción contenga el nombre ficticio de un paciente (por ejemplo, un reembolso mal registrado), para comprobar la restricción específica.

---

## Presupuesto y cifras reales del mes de cierre

**Ingresos — Estados Unidos (USD)**

| Pagador | Presupuesto | Real | Desviación |
|---|---|---|---|
| Seguros comerciales | 1.150.000 | 1.120.000 | −2,6% |
| Medicare / Medicaid | 520.000 | 468.000 | −10,0% |

**Ingresos — Reino Unido (GBP)**

| Pagador | Presupuesto | Real | Desviación |
|---|---|---|---|
| Privado | 260.000 | 271.000 | +4,2% |
| Contrato NHS | 75.000 | 75.000 | 0,0% |

**Gastos — Estados Unidos (USD)**

| Partida | Presupuesto | Real | Desviación |
|---|---|---|---|
| Material clínico (MedSupply Partners) | 44.800 | 46.816 | +4,5% |
| Laboratorio (ClearPath Labs) | 45.000 | 48.150 | +7,0% |
| Interpretación médica (LinguaCare Interpreting) | 17.550 | 17.550 | 0,0% |
| Nómina | 1.050.000 | 1.060.000 | +1,0% |
| Alquiler de clínicas | 180.000 | 180.000 | 0,0% |

**Gastos — Reino Unido (GBP)**

| Partida | Presupuesto | Real | Desviación |
|---|---|---|---|
| Material clínico (BritMed Supplies) | 9.450 | 9.450 | 0,0% |
| Laboratorio (Thames Pathology) | 10.150 | 10.353 | +2,0% |
| Nómina | 210.000 | 209.000 | −0,5% |
| Alquiler de clínicas | 52.000 | 52.000 | 0,0% |
| Licencias de software clínico | 8.000 | **Sin registros** | — |

**Indicadores operativos (`operations.csv`)**

| País | Pagador | Indicador | Presupuesto | Real |
|---|---|---|---|---|
| Estados Unidos | Medicare / Medicaid | Reclamaciones presentadas | 4.000 | 4.000 |
| Estados Unidos | Medicare / Medicaid | Tasa de denegación | 14,0% | 22,6% |
| Estados Unidos | Seguros comerciales | Reclamaciones presentadas | 6.500 | 6.400 |
| Estados Unidos | Seguros comerciales | Tasa de denegación | 12,0% | 12,0% |

**Dato de referencia:** tipo de cambio de consolidación, 1 GBP = 1,27 USD.

---

## Umbral de desviación

Una partida es una **desviación relevante** cuando su desviación frente al presupuesto es igual o superior al **5%**, a favor o en contra.

---

## Resultados esperados

| Partida | Resultado esperado |
|---|---|
| Medicare / Medicaid (−10,0%) | Desviación relevante. Hipótesis sostenida por datos: se presentaron las mismas reclamaciones, pero la tasa de denegación subió del 14,0% al 22,6% |
| Laboratorio EE. UU. (+7,0%) | Desviación relevante. Hipótesis: subida del precio por prueba, con el mismo número de pruebas |
| Material clínico EE. UU. (+4,5%) y Privado Reino Unido (+4,2%) | No son relevantes: no superan el umbral |
| Licencias de software clínico Reino Unido | **Dato faltante.** El informe debe declararlo y no puede tratarlo como 0 ni como una desviación del −100% |
| Registro con nombre de paciente | Se marca como dudoso y se señala en la sección de datos dudosos **por su `entry_id`**, sin reproducir su descripción |

---

## Estructura del informe

1. **Resumen ejecutivo**: cinco líneas como máximo.
2. **Resultado consolidado en USD**: ingresos, gastos y resultado, real frente a presupuesto.
3. **Ingresos por país y pagador**, en moneda local.
4. **Gastos por país**, en moneda local.
5. **Desviaciones relevantes**: una por partida, con la hipótesis y las cifras que la sostienen.
6. **Datos faltantes o dudosos**.
7. **Anexo de trazabilidad**: para cada cifra, los `entry_id` que la producen.

---

## Revisión y distribución

| Paso | Detalle |
|---|---|
| Ejecución | Tercer día hábil de cada mes, 06:00 (hora de Austin) |
| Revisión | Tom Callahan, Revenue Cycle Director |
| Distribución tras la aprobación | Dra. Sandra Okonkwo, James Osei, Dr. Marcus Reid, Priya Nair, Tom Callahan, Claire Whitfield y Diane Foster |

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes del agente ni respuestas de la API:

- **Cualquier dato de pacientes** (nombres, identificadores, diagnósticos, servicios recibidos por una persona concreta)
- Salarios individuales. La nómina se registra **solo de forma agregada por país**
- Datos bancarios de proveedores

---

## Restricción específica

Antes de que cualquier registro llegue al agente, el sistema debe comprobar si su descripción contiene datos que puedan identificar a un paciente. Si los contiene, el registro se marca como dudoso, su descripción **no se envía al modelo** y en el informe solo se menciona por su `entry_id`. Cumplimiento (Claire Whitfield) recibe una notificación con ese `entry_id` para revisarlo.
