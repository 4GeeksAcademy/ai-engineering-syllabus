# BRIEFING.md — TrackFlow

## Agentic Engineering – Cierre Financiero Mensual

*These instructions are [available in English](./trackflow-BRIEFING.en.md).*

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**TrackFlow** es una empresa de entrega de última milla y gestión de almacenes fundada en 2009 en Los Ángeles, Estados Unidos. Opera en Estados Unidos y España, con almacenes en Los Ángeles y Zaragoza, emplea a unas 130 personas y factura alrededor de 9 millones de euros al año con tres servicios: almacenaje, última milla y logística inversa. Opera con dólares (USD) en Estados Unidos y euros (EUR) en España.

---

## Tu departamento y el problema que debes resolver

Formas parte de **TrackFlow Tech**, la unidad interna que lidera la transformación digital de la empresa, y reportas al CTO Andrés Kim.

Thomas Harry, el CEO, recibe cada lunes un informe que sus directores montan a mano el domingo por la noche, y el cierre mensual llega todavía más tarde. No tiene una visión por país y por servicio frente a presupuesto, y cuando un número sorprende, a favor o en contra, tiene que preguntar a tres personas para entender por qué. Quiere el cierre de cada mes automático, comparable entre países y explicado.

---

## Tu stakeholder

**Thomas Harry**, CEO (Los Ángeles)

> Asunto: Cierre mensual — lo que necesito
>
> Equipo:
>
> Versión corta:
>
> 1. Cierre listo el tercer día hábil, a las 6:00 hora de Los Ángeles. Consolidado en euros, con cada país en su moneda.
> 2. Ingresos por país y por servicio: almacenaje, última milla y devoluciones. Costes por país.
> 3. Toda desviación de más del 5%, explicada con datos. **En los dos sentidos.** Si algo fue mejor que el presupuesto, quiero saber por qué tanto como cuando fue peor. Una buena sorpresa que no entendemos es igual de peligrosa.
> 4. Costes de transporte: tarifa base y recargo de combustible en líneas separadas. Carlos lo ha dejado muy claro.
> 5. Brian lo revisa antes de que me llegue a mí y al equipo. No sale nada sin su visto bueno.
>
> ¿Cuánto cuesta ejecutarlo y cuándo estará listo? Decidme.
>
> Thomas

---

## Alcance de idioma

- El soporte multilingüe es **opcional pero muy recomendable**, porque el equipo directivo trabaja en Los Ángeles y en Zaragoza.
- Elige un **idioma base** para el informe.
- Si implementas un segundo idioma, las cifras deben ser idénticas en ambas versiones: solo cambia el texto.

---

## Fuentes de datos

Genera tres archivos CSV para el **mes de cierre** (el último mes completo antes de la fecha de carga):

| Archivo | Columnas | Contenido |
|---|---|---|
| `ledger.csv` | `entry_id, date, country, service, category, description, currency, amount, source_ref` | Movimientos de ingresos y gastos del mes. Los ingresos son positivos y los gastos, negativos. Los gastos generales usan `service = general` |
| `budget.csv` | `month, country, service, category, currency, amount` | Presupuesto del mes |
| `operations.csv` | `month, country, service, metric, value` | Indicadores operativos que sirven de base a las explicaciones |

Cada partida debe tener **varios registros** en `ledger.csv` cuya suma coincida exactamente con la cifra real de la tabla siguiente. En las partidas de proveedores, la descripción incluye el proveedor, el concepto, el precio unitario y la cantidad. En los ingresos de última milla en España, algunos registros deben ser notas de abono con la descripción "Descuento por renovación de contrato".

---

## Presupuesto y cifras reales del mes de cierre

**Ingresos — Estados Unidos (USD)**

| Servicio | Presupuesto | Real | Desviación |
|---|---|---|---|
| Almacenaje | 180.000 | 181.000 | +0,6% |
| Última milla | 260.000 | 248.000 | −4,6% |
| Logística inversa | 40.000 | 46.000 | +15,0% |

**Ingresos — España (EUR)**

| Servicio | Presupuesto | Real | Desviación |
|---|---|---|---|
| Almacenaje | 120.000 | 120.000 | 0,0% |
| Última milla | 150.000 | 139.500 | −7,0% |
| Logística inversa | 25.000 | 25.000 | 0,0% |

**Gastos — Estados Unidos (USD)**

| Partida | Presupuesto | Real | Desviación |
|---|---|---|---|
| Transporte, tarifa base (PacificRoute Express) | 75.600 | 80.136 | +6,0% |
| Transporte, recargo de combustible (PacificRoute Express) | 4.950 | 5.445 | +10,0% |
| Entrega en el día (Golden State Couriers) | 8.400 | 8.400 | 0,0% |
| Embalaje (BoxLine Packaging) | 7.440 | 7.960,80 | +7,0% |
| Nómina | 210.000 | 212.000 | +1,0% |
| Alquiler de almacén | 65.000 | 65.000 | 0,0% |

**Gastos — España (EUR)**

| Partida | Presupuesto | Real | Desviación |
|---|---|---|---|
| Transporte (IberEnvíos) | 34.300 | 35.500,50 | +3,5% |
| Embalaje (Embalajes Ebro) | 4.320 | 4.320 | 0,0% |
| Nómina | 120.000 | 119.000 | −0,8% |
| Alquiler de almacén | 28.000 | 28.000 | 0,0% |
| Energía del almacén | 9.000 | **Sin registros** | — |

**Indicadores operativos (`operations.csv`)**

| País | Servicio | Indicador | Presupuesto | Real |
|---|---|---|---|---|
| Estados Unidos | Logística inversa | Devoluciones procesadas | 2.000 | 2.300 |
| Estados Unidos | Logística inversa | Ingreso medio por devolución (USD) | 20,00 | 20,00 |
| España | Última milla | Envíos entregados | 7.500 | 7.500 |
| España | Última milla | Ingreso medio por envío (EUR) | 20,00 | 18,60 |

**Dato de referencia:** tipo de cambio de consolidación, 1 USD = 0,92 EUR.

---

## Umbral de desviación

Una partida es una **desviación relevante** cuando su desviación frente al presupuesto es igual o superior al **5%**, a favor o en contra.

---

## Resultados esperados

| Partida | Resultado esperado |
|---|---|
| Logística inversa EE. UU. (+15,0%) | Desviación relevante **favorable**. Hipótesis sostenida por datos: se procesaron un 15% más de devoluciones con el mismo ingreso medio |
| Última milla España (−7,0%) | Desviación relevante. Hipótesis: el volumen de envíos se mantuvo y el ingreso medio por envío bajó un 7%, coherente con las notas de abono por renovación |
| Transporte, tarifa base EE. UU. (+6,0%) | Desviación relevante. Hipótesis: subida de la tarifa base por envío, con el mismo número de envíos |
| Transporte, recargo de combustible EE. UU. (+10,0%) | Desviación relevante, presentada en su propia línea. Hipótesis: subida del recargo por envío |
| Embalaje EE. UU. (+7,0%) | Desviación relevante. Hipótesis: subida del precio unitario del proveedor |
| Última milla EE. UU. (−4,6%) e IberEnvíos (+3,5%) | No son relevantes: no superan el umbral |
| Energía del almacén España | **Dato faltante.** El informe debe declararlo y no puede tratarlo como 0 ni como una desviación del −100% |

---

## Estructura del informe

1. **Resumen ejecutivo**: cinco líneas como máximo.
2. **Resultado consolidado en EUR**: ingresos, gastos y resultado, real frente a presupuesto.
3. **Resultado por país**, en moneda local: ingresos por servicio y gastos por partida.
4. **Desviaciones relevantes**, separadas en **favorables** y **desfavorables**, cada una con su hipótesis y las cifras que la sostienen.
5. **Datos faltantes o dudosos**.
6. **Anexo de trazabilidad**: para cada cifra, los `entry_id` que la producen.

---

## Revisión y distribución

| Paso | Detalle |
|---|---|
| Ejecución | Tercer día hábil de cada mes, 06:00 (hora de Los Ángeles) |
| Revisión | Brian Calloway, Senior Data Analyst |
| Distribución tras la aprobación | Thomas Harry, Andrés Kim, Ana Whitfield, Carlos Vega, Sofía Ramos, Valentina Cruz, Miguel Torres y Rafael Sanz |

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes del agente ni respuestas de la API:

- Salarios individuales. La nómina se registra **solo de forma agregada por país**
- Datos bancarios de proveedores

---

## Restricción específica

Las desviaciones favorables se explican con el mismo rigor que las desfavorables y aparecen en su propio bloque. Además, la tarifa base y el recargo de combustible de un transportista son siempre líneas distintas, tanto en el cálculo como en el informe: el informe puede mostrar el total del transportista, pero siempre junto al desglose.
