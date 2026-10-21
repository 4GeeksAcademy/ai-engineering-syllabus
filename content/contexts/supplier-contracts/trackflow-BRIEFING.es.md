# BRIEFING.md — TrackFlow

## Agentic Engineering – Gestión de Proveedores y Contratos

*These instructions are [available in English](./trackflow-BRIEFING.en.md).*

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**TrackFlow** es una empresa de entrega de última milla y gestión de almacenes fundada en 2009 en Los Ángeles, Estados Unidos. Opera en Estados Unidos y España, con almacenes en Los Ángeles y Zaragoza, emplea a unas 130 personas y factura alrededor de 9 millones de euros al año. Opera con dos monedas: dólares (USD) en Estados Unidos y euros (EUR) en España.

---

## Tu departamento y el problema que debes resolver

Formas parte de **TrackFlow Tech**, la unidad interna que lidera la transformación digital de la empresa, y reportas al CTO Andrés Kim.

Los transportistas son el principal proveedor de TrackFlow y su mayor coste variable. Sus tarifas tienen varios componentes (tarifa base, recargo de combustible) con reglas de revisión distintas, y cada contrato las regula de forma diferente. Hoy, el equipo de Carlos Vega revisa las facturas de cada transportista a mano y detecta las subidas tarde, si las detecta. Lo mismo ocurre con los proveedores de embalaje de los dos almacenes.

---

## Tu stakeholder

**Carlos Vega**, Head of Carrier Operations (Zaragoza)

> Hola equipo:
>
> Os paso el detalle, porque con los transportistas el diablo está en los conceptos de la tarifa.
>
> 1. Cada transportista factura una **tarifa base** por envío y, en algunos casos, un **recargo de combustible** aparte. Los contratos tratan cada concepto de forma distinta: la base suele ser fija durante un periodo y el recargo se ajusta según un índice. Si el sistema los mezcla, todas sus conclusiones serán incorrectas.
> 2. Quiero una alerta cuando suba cualquier concepto por encima del umbral, y la evaluación de si el contrato lo permite **concepto por concepto**.
> 3. Si el contrato exige preaviso para una subida y no lo tenemos registrado, quiero que el sistema lo diga. Que el importe esté permitido no significa que la subida sea válida.
> 4. Para renegociar necesito el impacto real sobre nuestro volumen mensual de envíos y la comparación con los otros transportistas del mismo país.
> 5. Las comunicaciones con transportistas las apruebo yo. Las de embalaje, Ana Whitfield. Si el contrato es grande, también Thomas.
>
> Gracias,
> Carlos

---

## Alcance de idioma

- El soporte multilingüe es **opcional pero muy recomendable**, porque TrackFlow tiene contratos en inglés (Estados Unidos) y en español (España).
- Elige un **idioma base** para las respuestas, los briefs y las alertas.
- Los contratos se analizan en su idioma original. Las citas de cláusulas se reproducen en el idioma del contrato.

---

## Proveedores

| ID | Proveedor | País | Categoría | Moneda |
|---|---|---|---|---|
| TF-S01 | PacificRoute Express | Estados Unidos | Transporte de paquetería | USD |
| TF-S02 | Coastline Parcel | Estados Unidos | Transporte de paquetería | USD |
| TF-S03 | Golden State Couriers | Estados Unidos | Entrega en el día | USD |
| TF-S04 | IberEnvíos | España | Transporte de paquetería | EUR |
| TF-S05 | Ruta Norte Logística | España | Transporte de paquetería | EUR |
| TF-S06 | BoxLine Packaging | Estados Unidos | Embalaje | USD |
| TF-S07 | Embalajes Ebro | España | Embalaje | EUR |

Las comparativas de precio se hacen **entre proveedores de la misma categoría y el mismo país**.

---

## Contratos

Genera un contrato ficticio en PDF por cada fila, con cada término redactado como cláusula numerada. Las fechas son relativas a la fecha de carga de los datos.

| Contrato | Proveedor | Vencimiento | Preaviso | Revisión de precio | Salida y penalización | Valor anual estimado |
|---|---|---|---|---|---|---|
| CT-TF-01 | PacificRoute Express | Hoy + 150 días | No renovación: 90 días antes del vencimiento | **Tarifa base:** fija durante toda la vigencia. **Recargo de combustible:** ajustable mensualmente según el índice publicado de diésel, con un máximo de USD 1,00 por envío | Rescisión anticipada con penalización de 1 mes de facturación media | USD 966.600 |
| CT-TF-02 | IberEnvíos | Hoy + 45 días | No renovación: 30 días antes del vencimiento | Anual, como máximo el IPC de España más 1 punto | Con 30 días de preaviso, sin penalización | EUR 411.600 |
| CT-TF-03 | BoxLine Packaging | Hoy + 300 días | **El contrato no especifica plazo de preaviso de no renovación** | Trimestral, libre según el coste de la materia prima, con preaviso escrito de 30 días | Sin penalización | USD 89.280 |
| CT-TF-04 | Embalajes Ebro | Hoy + 20 días | No renovación: 15 días antes del vencimiento | Precio fijo durante toda la vigencia | Sin penalización | EUR 51.840 |

Coastline Parcel, Golden State Couriers y Ruta Norte Logística **no tienen contrato**: solo hay cotizaciones o envíos puntuales.

**Datos de referencia** para los cálculos:
- IPC anual de España: 2,8%
- Tipo de cambio de referencia: 1 USD = 0,92 EUR

---

## Histórico de precios

Genera un CSV con 12 meses de histórico (el último mes es el mes de carga) y estas columnas:

`supplier_id, product, unit, currency, month, unit_price, monthly_volume`

La tarifa base y el recargo de combustible son **filas distintas** del CSV.

| Proveedor | Producto | Unidad | Precio base | Volumen mensual |
|---|---|---|---|---|
| TF-S01 | Envío estándar 0–2 kg, tarifa base | envío | USD 8,40 | 9.000 envíos |
| TF-S01 | Recargo de combustible | envío | USD 0,55 | 9.000 envíos |
| TF-S02 | Envío estándar 0–2 kg, tarifa base | envío | USD 8,10 | 0 (solo cotización) |
| TF-S03 | Entrega en el día | envío | USD 14,00 | 600 envíos |
| TF-S04 | Envío estándar 0–2 kg, tarifa base | envío | EUR 4,90 | 7.000 envíos |
| TF-S05 | Envío estándar 0–2 kg, tarifa base | envío | EUR 4,70 | 0 (solo cotización) |
| TF-S06 | Caja mediana | unidad | USD 0,62 | 12.000 unidades |
| TF-S07 | Caja mediana | unidad | EUR 0,48 | 9.000 unidades |

Durante los 11 primeros meses, el recargo de combustible puede variar como máximo un ±2% mensual y el resto de precios no varía. En el **último mes** deben aparecer estos escenarios:

| Escenario | Proveedor y concepto | Variación del último mes | Resultado esperado |
|---|---|---|---|
| A1 | TF-S01, tarifa base | +6% | Supera el umbral. **No permitida**: la tarifa base es fija |
| A2 | TF-S01, recargo de combustible | +10% | Supera el umbral. **Permitida**: queda por debajo del máximo de USD 1,00 por envío |
| B | TF-S04 IberEnvíos | +3,5% | Supera el umbral. **Permitida**: está por debajo del IPC + 1 punto (3,8%) |
| C | TF-S06 BoxLine Packaging | +7% | Supera el umbral. **Permitida en importe, pero no aplicable todavía**: el contrato exige preaviso escrito de 30 días y no consta ninguno |
| D | TF-S07 Embalajes Ebro | Sin cambio | Sin alerta de precio, pero su contrato dispara alerta de vencimiento |

---

## Umbrales y alertas

| Tipo | Regla |
|---|---|
| Subida de precio, transporte (cualquier concepto) | Más de un 3% frente al mes anterior |
| Subida de precio, embalaje | Más de un 5% frente al mes anterior |
| Vencimiento de contrato | 90 y 30 días antes |
| Fecha límite de preaviso | 15 días antes |

Las alertas de transporte se envían a Carlos Vega. Las de embalaje, a Ana Whitfield.

---

## Aprobaciones

| Situación | Aprueba |
|---|---|
| Comunicación a un transportista | Carlos Vega |
| Comunicación a un proveedor de embalaje | Ana Whitfield |
| Comunicación sobre un contrato con valor anual superior a EUR 500.000 (o su equivalente en USD) | El aprobador correspondiente **y** Thomas Harry |

---

## Preguntas que el sistema debe poder responder

- "¿PacificRoute puede subirnos la tarifa base? ¿Y el recargo de combustible?"
- "¿Cuánto nos cuesta al mes la subida de PacificRoute, separando cada concepto?"
- "¿La subida de BoxLine ya se puede aplicar?"
- "¿Qué alternativa tenemos a IberEnvíos en España y a qué precio?"
- "¿Cuándo tenemos que avisar a IberEnvíos si no queremos renovar?"
- "¿Cuál es el preaviso de no renovación de BoxLine?" → el sistema debe responder que el contrato no lo especifica.
- "Prepárame un brief para renegociar con PacificRoute Express."

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes de los agentes ni respuestas de la API:

- Datos bancarios de los proveedores incluidos en los contratos
- Datos personales de las personas de contacto de los proveedores
- Nombres de las marcas cliente de TrackFlow y volúmenes de envío por marca cliente

Los contratos de prueba deben incluir los dos primeros tipos de dato en una cláusula de facturación, para poder comprobar que el sistema no los propaga.

---

## Restricción específica

La tarifa base y el recargo de combustible se evalúan siempre **por separado**, cada uno con su propia regla contractual. El sistema nunca suma ambos conceptos antes de decidir si una subida está permitida. Los informes de impacto pueden mostrar el total, pero siempre junto al desglose por concepto.
