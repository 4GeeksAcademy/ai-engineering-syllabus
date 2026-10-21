# BRIEFING.md — Nexova

## Agentic Engineering – Cierre Financiero Mensual

*These instructions are [available in English](./nexova-BRIEFING.en.md).*

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**Nexova** es una consultora de recursos humanos y captación de talento fundada en 2011, con sede en Valencia (España) y una oficina de expansión en Miami (Florida). Tiene 120 empleados, opera tres líneas de negocio (headhunting, externalización de soporte al cliente y formación corporativa) y factura alrededor de 8 millones de dólares al año. Opera con euros (EUR) en España y dólares (USD) en Estados Unidos.

---

## Tu departamento y el problema que debes resolver

Formas parte del equipo de AI Engineering de Nexova y reportas al CTO Sergio Molina.

Laura Mendoza, la CEO, recibe cada semana informes en PDF que cada responsable prepara a mano, y no tiene una visión financiera del mes por línea de negocio hasta varios días después del cierre. Cuando una línea se desvía, tiene que llamar a su responsable para entender por qué. Quiere que el cierre de cada mes le llegue listo, por línea de negocio, con las desviaciones explicadas.

---

## Tu stakeholder

**Laura Mendoza**, CEO (Valencia)

> Asunto: Cierre mensual
>
> Hola:
>
> Quiero dejar de esperar al cierre del mes. Esto es lo que necesito:
>
> - El cierre de cada mes, el tercer día hábil a primera hora.
> - Ingresos por línea de negocio (Selección, Soporte y Formación) y gastos por país, frente a presupuesto. El total consolidado en euros.
> - Las desviaciones importantes, con una explicación basada en datos. Si no se sabe por qué, que lo diga.
> - Antes de que me llegue, que lo revise Tom: es quien mejor conoce los números y siempre pide ver el detalle.
> - Una cosa importante: este informe lo va a leer todo el equipo directivo. No quiero nombres de clientes en él.
>
> Gracias,
> Laura

---

## Alcance de idioma

- El soporte multilingüe es **opcional pero muy recomendable**, porque el equipo directivo trabaja en Valencia y en Miami.
- Elige un **idioma base** para el informe.
- Si implementas un segundo idioma, las cifras deben ser idénticas en ambas versiones: solo cambia el texto.

---

## Fuentes de datos

Genera tres archivos CSV para el **mes de cierre** (el último mes completo antes de la fecha de carga):

| Archivo | Columnas | Contenido |
|---|---|---|
| `ledger.csv` | `entry_id, date, country, business_line, category, description, currency, amount, source_ref` | Movimientos de ingresos y gastos del mes. Los ingresos son positivos y los gastos, negativos. Los gastos generales usan `business_line = general` |
| `budget.csv` | `month, country, business_line, category, currency, amount` | Presupuesto del mes |
| `operations.csv` | `month, business_line, metric, value` | Indicadores operativos que sirven de base a las explicaciones |

Cada partida debe tener **varios registros** en `ledger.csv` cuya suma coincida exactamente con la cifra real de la tabla siguiente. Las descripciones de los ingresos **incluyen el nombre de la empresa cliente** (ficticio). En las partidas de proveedores, la descripción incluye el proveedor, el precio unitario y la cantidad.

---

## Presupuesto y cifras reales del mes de cierre

**Ingresos por línea de negocio**

| Línea | País | Moneda | Presupuesto | Real | Desviación |
|---|---|---|---|---|---|
| Selección de talento | España | EUR | 300.000 | 312.000 | +4,0% |
| Soporte externalizado | Estados Unidos | USD | 190.000 | 168.000 | −11,6% |
| Formación corporativa | España | EUR | 120.000 | 96.000 | −20,0% |

**Gastos — España (EUR)**

| Partida | Presupuesto | Real | Desviación |
|---|---|---|---|
| Plataforma de búsqueda (JobReach Pro) | 26.000 | 28.080 | +8,0% |
| Evaluación psicométrica (AssessPro) | 11.400 | 11.856 | +4,0% |
| Salas de formación (Espacios Turia) | 5.040 | 5.140,80 | +2,0% |
| Nómina | 380.000 | 383.000 | +0,8% |
| Alquiler de oficinas | 18.000 | 18.000 | 0,0% |
| Marketing | 12.000 | 12.400 | +3,3% |
| Viajes y desplazamientos | 6.000 | **Sin registros** | — |

**Gastos — Estados Unidos (USD)**

| Partida | Presupuesto | Real | Desviación |
|---|---|---|---|
| Telefonía de soporte (VoxCloud Contact) | 2.850 | 3.021 | +6,0% |
| Nómina | 95.000 | 94.000 | −1,1% |
| Alquiler de oficinas | 14.000 | 14.000 | 0,0% |

**Indicadores operativos (`operations.csv`)**

| Línea | Indicador | Presupuesto | Real |
|---|---|---|---|
| Selección de talento | Procesos cerrados | 25 | 26 |
| Selección de talento | Honorario medio por proceso (EUR) | 12.000 | 12.000 |
| Soporte externalizado | Horas facturadas | 4.750 | 4.200 |
| Soporte externalizado | Tarifa por hora (USD) | 40 | 40 |
| Formación corporativa | Días de formación impartidos | 15 | 12 |
| Formación corporativa | Ingreso medio por día (EUR) | 8.000 | 8.000 |

**Dato de referencia:** tipo de cambio de consolidación, 1 USD = 0,92 EUR.

---

## Umbral de desviación

Una partida es una **desviación relevante** cuando su desviación frente al presupuesto es igual o superior al **5%**, a favor o en contra.

---

## Resultados esperados

| Partida | Resultado esperado |
|---|---|
| Soporte externalizado (−11,6%) | Desviación relevante. Hipótesis sostenida por datos: las horas facturadas cayeron un 11,6% con la tarifa estable |
| Formación corporativa (−20,0%) | Desviación relevante. Hipótesis: se impartieron 12 días de formación frente a los 15 presupuestados |
| JobReach Pro (+8,0%) | Desviación relevante. Hipótesis: subida del precio por licencia, con el mismo número de licencias |
| VoxCloud Contact (+6,0%) | Desviación relevante. Hipótesis: subida del precio por puesto, con el mismo número de puestos |
| Selección de talento (+4,0%) | No es relevante: no supera el umbral |
| Viajes y desplazamientos | **Dato faltante.** El informe debe declararlo y no puede tratarlo como 0 ni como una desviación del −100% |

---

## Estructura del informe

1. **Resumen ejecutivo**: cinco líneas como máximo.
2. **Resultado consolidado en EUR**: ingresos, gastos y resultado, real frente a presupuesto.
3. **Ingresos por línea de negocio**, en moneda local y en EUR.
4. **Gastos por país**, en moneda local.
5. **Desviaciones relevantes**: una por partida, con la hipótesis y las cifras que la sostienen.
6. **Datos faltantes o dudosos**.
7. **Anexo de trazabilidad**: para cada cifra, los `entry_id` que la producen.

---

## Revisión y distribución

| Paso | Detalle |
|---|---|
| Ejecución | Tercer día hábil de cada mes, 06:00 (hora de Valencia) |
| Revisión | Tom Reeves, Senior Sales Analyst |
| Distribución tras la aprobación | Laura Mendoza, Javier Almeida, Marcos Ibáñez, Elena Vargas, Roberto Díaz, Patricia Solís, Carmen Ruiz y Sergio Molina |

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes del agente ni respuestas de la API:

- Salarios individuales. La nómina se registra **solo de forma agregada por país**
- Datos bancarios de proveedores
- Datos de candidatos

---

## Restricción específica

El informe **no muestra nombres de clientes** en ninguna sección, aunque estén en las descripciones del libro de movimientos. Los ingresos se presentan agregados por línea de negocio, y la trazabilidad del anexo se hace por `entry_id`, sin reproducir las descripciones. Si una hipótesis necesitara mencionar a un cliente concreto, el informe debe indicar que hay un cliente relevante y remitir a la persona revisora, sin nombrarlo.
