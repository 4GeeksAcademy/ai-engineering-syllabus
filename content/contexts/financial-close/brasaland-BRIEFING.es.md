# BRIEFING.md — Brasaland

## Agentic Engineering – Cierre Financiero Mensual

*These instructions are [available in English](./brasaland-BRIEFING.en.md).*

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**Brasaland** es una cadena de restaurantes de comida a la brasa fundada en 2008 en Medellín, Colombia. Opera 14 restaurantes propios en Colombia y Estados Unidos (Florida), emplea a unas 115 personas y factura alrededor de 6 millones de dólares al año. Opera con dos monedas: pesos colombianos (COP) en Colombia y dólares (USD) en Florida.

---

## Tu departamento y el problema que debes resolver

Trabajas en **Brasaland Digital**, el equipo interno que lidera la transformación digital de la empresa, y reportas al CTO Nicolás Park.

Mariana Restrepo, la CEO, gestiona una cadena de dos mercados sin una visión financiera unificada. Los datos de cada mes llegan en informes que se preparan a mano, en dos monedas que nadie consolida igual dos veces, y cuando un mercado se desvía del presupuesto la explicación llega días después, en una llamada. Mariana quiere el cierre de cada mes listo, consolidado y explicado, sin depender de que alguien lo monte.

---

## Tu stakeholder

**Mariana Restrepo**, CEO (Medellín)

> *Transcripción de nota de voz:*
>
> "Hola, chicos. Os cuento rápido lo que necesito, que entro a una reunión. Cada mes quiero el cierre listo el tercer día hábil, a primera hora. Que me diga cuánto vendimos y cuánto gastamos en Colombia y en Florida, cada uno en su moneda, y el total junto en dólares. Que me diga dónde nos desviamos del presupuesto y por qué, pero con datos, no con suposiciones. Si no hay datos para explicar algo, que lo diga y ya. Antes de que me llegue a mí y al equipo, que lo revise Felipe, que es el que mejor conoce los números de los locales. Y si falta algo, que no me lo maquillen: prefiero saberlo. Gracias, ¡chao!"

---

## Alcance de idioma

- El soporte multilingüe es **opcional pero muy recomendable**, porque el equipo directivo trabaja en Medellín y en Miami.
- Elige un **idioma base** para el informe.
- Si implementas un segundo idioma, las cifras deben ser idénticas en ambas versiones: solo cambia el texto.

---

## Fuentes de datos

Genera tres archivos CSV para el **mes de cierre** (el último mes completo antes de la fecha de carga):

| Archivo | Columnas | Contenido |
|---|---|---|
| `ledger.csv` | `entry_id, date, country, category, description, currency, amount, source_ref` | Movimientos de ingresos y gastos del mes. Los ingresos son positivos y los gastos, negativos |
| `budget.csv` | `month, country, category, currency, amount` | Presupuesto del mes por país y partida |
| `operations.csv` | `month, country, metric, value` | Indicadores operativos que sirven de base a las explicaciones |

Cada partida debe tener **varios registros** en `ledger.csv` cuya suma coincida exactamente con la cifra real de la tabla siguiente. En las partidas de compras a proveedores, la descripción incluye el proveedor, el precio unitario y la cantidad.

---

## Presupuesto y cifras reales del mes de cierre

**Colombia (COP)**

| Partida | Presupuesto | Real | Desviación |
|---|---|---|---|
| Ingresos por ventas | 1.120.000.000 | 1.090.000.000 | −2,7% |
| Carne de res (Carnes del Valle) | 106.400.000 | 110.656.000 | +4,0% |
| Pollo (Avícola Antioquia) | 48.875.000 | 53.273.750 | +9,0% |
| Verduras (Hortalizas La Sabana) | 25.200.000 | 25.200.000 | 0,0% |
| Nómina | 320.000.000 | 322.000.000 | +0,6% |
| Alquileres | 95.000.000 | 95.000.000 | 0,0% |
| Marketing | 30.000.000 | 30.500.000 | +1,7% |
| Servicios (energía, agua, gas) | 22.000.000 | 21.800.000 | −0,9% |

**Florida (USD)**

| Partida | Presupuesto | Real | Desviación |
|---|---|---|---|
| Ingresos por ventas | 230.000 | 205.000 | −10,9% |
| Carne de res (Sunshine Prime Meats) | 17.280 | 19.353,60 | +12,0% |
| Pollo (Gulf Poultry Co.) | 6.300 | 6.300 | 0,0% |
| Bebidas (Brava Beverages FL) | 7.200 | 7.632 | +6,0% |
| Nómina | 78.000 | 77.500 | −0,6% |
| Alquileres | 42.000 | 42.000 | 0,0% |
| Marketing | 9.000 | 15.500 | +72,2% |
| Servicios (energía, agua, gas) | 6.500 | **Sin registros** | — |

**Indicadores operativos (`operations.csv`)**

| País | Indicador | Presupuesto | Real |
|---|---|---|---|
| Colombia | Cubiertos servidos | 28.000 | 27.250 |
| Colombia | Ticket medio (COP) | 40.000 | 40.000 |
| Florida | Cubiertos servidos | 9.200 | 8.200 |
| Florida | Ticket medio (USD) | 25,00 | 25,00 |

**Dato de referencia:** tipo de cambio de consolidación, 1 USD = 4.000 COP.

---

## Umbral de desviación

Una partida es una **desviación relevante** cuando su desviación frente al presupuesto es igual o superior al **5%**, a favor o en contra.

---

## Resultados esperados

| Partida | Resultado esperado |
|---|---|
| Ingresos Florida (−10,9%) | Desviación relevante. Hipótesis sostenida por datos: los cubiertos cayeron un 10,9% y el ticket medio se mantuvo |
| Carne de res Florida (+12,0%) | Desviación relevante. Hipótesis: subida del precio unitario del proveedor, visible en las descripciones de los registros |
| Pollo Colombia (+9,0%) | Desviación relevante. Hipótesis: subida del precio unitario del proveedor, con la misma cantidad comprada |
| Bebidas Florida (+6,0%) | Desviación relevante. Hipótesis: subida del precio unitario del proveedor |
| Marketing Florida (+72,2%) | Desviación relevante. La hipótesis solo puede apoyarse en las descripciones de los registros; si no explican el motivo, el informe debe decirlo |
| Carne de res Colombia (+4,0%) | No es relevante: no supera el umbral |
| Servicios Florida | **Dato faltante.** El informe debe declararlo y no puede tratarlo como 0 ni como una desviación del −100% |

---

## Estructura del informe

1. **Resumen ejecutivo**: cinco líneas como máximo.
2. **Resultado consolidado en USD**: ingresos, gastos y resultado, real frente a presupuesto.
3. **Resultado por país**, en moneda local: todas las partidas, real frente a presupuesto.
4. **Desviaciones relevantes**: una por partida, con la hipótesis y las cifras que la sostienen.
5. **Datos faltantes o dudosos**.
6. **Anexo de trazabilidad**: para cada cifra, los `entry_id` que la producen.

---

## Revisión y distribución

| Paso | Detalle |
|---|---|
| Ejecución | Tercer día hábil de cada mes, 06:00 (hora de Medellín) |
| Revisión | Felipe Guerrero, director de Operaciones |
| Distribución tras la aprobación | Mariana Restrepo, Felipe Guerrero, Nicolás Park, Lucía Fernández, Camila Ospina, Ashley Turner y Jake Morrison |

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes del agente ni respuestas de la API:

- Salarios individuales. La nómina se registra **solo de forma agregada por país**; el libro de movimientos no contiene ninguna línea de nómina por persona
- Datos bancarios de proveedores

---

## Restricción específica

El informe nunca suma importes en monedas distintas sin convertirlos antes. Cada país se presenta en su moneda local y el consolidado en USD al tipo de cambio de referencia, indicando siempre qué tipo de cambio se ha usado.
