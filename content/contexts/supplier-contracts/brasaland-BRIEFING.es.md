# BRIEFING.md — Brasaland

## Agentic Engineering – Gestión de Proveedores y Contratos

*These instructions are [available in English](./brasaland-BRIEFING.en.md).*

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**Brasaland** es una cadena de restaurantes de comida a la brasa fundada en 2008 en Medellín, Colombia. Opera 14 restaurantes propios en Colombia y Estados Unidos (Florida), emplea a unas 115 personas y factura alrededor de 6 millones de dólares al año. Trabaja con unos 20 proveedores entre los dos países, con proveedores distintos en cada mercado, y opera con dos monedas: pesos colombianos (COP) y dólares (USD).

---

## Tu departamento y el problema que debes resolver

Trabajas en **Brasaland Digital**, el equipo interno que lidera la transformación digital de la empresa, y reportas al CTO Nicolás Park.

La carne es la principal partida de coste de Brasaland y su precio fluctúa de forma distinta en Colombia y en Florida. Hoy el equipo de Compras de Lucía Fernández se entera de las subidas cuando llega la factura. Los contratos con proveedores están en PDF repartidos entre correos y carpetas, y nadie sabe de memoria cuándo vence cada uno, cuánto preaviso exige o qué subidas permite. Felipe Guerrero, director de Operaciones, sufre las consecuencias en los márgenes de cada local y quiere un sistema que cruce precios y contratos.

---

## Tu stakeholder

**Felipe Guerrero**, Director de Operaciones (Medellín)

> Equipo:
>
> - Las subidas de carne me están comiendo el margen y me entero tarde.
> - Necesito una alerta cuando un proveedor sube un precio por encima de lo normal.
> - Con la alerta, quiero saber si el contrato lo permite. Sí o no, y por qué.
> - Si no lo permite, quiero un brief para renegociar: histórico, comparación con otros proveedores de lo mismo, cuánto nos cuesta y qué dice el contrato sobre salir.
> - Avisadme antes de que venza un contrato o se pase la fecha de preaviso. Ya nos renovó uno solo por no avisar a tiempo.
> - Nada sale hacia un proveedor sin mi visto bueno. Si el contrato es grande, también el de Mariana.
>
> Felipe

---

## Alcance de idioma

- El soporte multilingüe es **opcional pero muy recomendable**, porque Brasaland tiene contratos en español (Colombia) y en inglés (Florida).
- Elige un **idioma base** para las respuestas, los briefs y las alertas.
- Los contratos se analizan en su idioma original. Las citas de cláusulas se reproducen en el idioma del contrato, aunque la respuesta esté en el otro idioma.

---

## Proveedores

| ID | Proveedor | País | Categoría | Moneda |
|---|---|---|---|---|
| BR-S01 | Carnes del Valle S.A.S. | Colombia | Carne de res | COP |
| BR-S02 | Avícola Antioquia | Colombia | Pollo | COP |
| BR-S03 | Hortalizas La Sabana | Colombia | Verduras | COP |
| BR-S04 | Frigorífico Andino | Colombia | Carne de res | COP |
| BR-S05 | Sunshine Prime Meats | Estados Unidos | Carne de res | USD |
| BR-S06 | Gulf Coast Beef Co. | Estados Unidos | Carne de res | USD |
| BR-S07 | Gulf Poultry Co. | Estados Unidos | Pollo | USD |
| BR-S08 | Brava Beverages FL | Estados Unidos | Bebidas | USD |

Las comparativas de precio se hacen **entre proveedores de la misma categoría y el mismo país**.

---

## Contratos

Genera un contrato ficticio en PDF por cada fila, con cada término redactado como cláusula numerada. Las fechas son relativas a la fecha de carga de los datos, para que las alertas sean comprobables en cualquier momento.

| Contrato | Proveedor | Vencimiento | Preaviso | Revisión de precio | Salida y penalización | Valor anual estimado |
|---|---|---|---|---|---|---|
| CT-BR-01 | Carnes del Valle | Hoy + 120 días | No renovación: 60 días antes del vencimiento | Semestral, como máximo el IPC anual de Colombia más 1 punto, con preaviso escrito de 30 días | Cualquiera de las partes, con 60 días de preaviso, sin penalización | COP 1.276.800.000 |
| CT-BR-02 | Sunshine Prime Meats | Hoy + 75 días | Renovación automática por 12 meses salvo aviso 45 días antes del vencimiento | Precio fijo durante la vigencia, salvo que el índice de referencia de carne de res suba más de un 10% en el trimestre, con preaviso escrito de 30 días | Rescisión anticipada con penalización de 2 meses de compra media | USD 207.360 |
| CT-BR-03 | Avícola Antioquia | Hoy + 200 días | **El contrato no incluye cláusula de preaviso** | Anual, como máximo un 5% | Con 90 días de preaviso, sin penalización | COP 586.500.000 |
| CT-BR-04 | Brava Beverages FL | Hoy + 20 días | No renovación: 15 días antes del vencimiento | Libre según lista de precios trimestral del proveedor | Sin penalización | USD 86.400 |

Hortalizas La Sabana, Frigorífico Andino, Gulf Coast Beef Co. y Gulf Poultry Co. **no tienen contrato**: se compra por pedido.

**Datos de referencia** para los cálculos:
- IPC anual de Colombia: 5,2%
- Tipo de cambio de referencia: 1 USD = 4.000 COP

---

## Histórico de precios

Genera un CSV con 12 meses de histórico (el último mes es el mes de carga) y estas columnas:

`supplier_id, product, unit, currency, month, unit_price, monthly_volume`

| Proveedor | Producto | Unidad | Precio base | Volumen mensual |
|---|---|---|---|---|
| BR-S01 | Punta de anca | kg | COP 38.000 | 2.800 kg |
| BR-S04 | Punta de anca | kg | COP 36.500 | 0 (solo cotización) |
| BR-S05 | Picanha | lb | USD 7,20 | 2.400 lb |
| BR-S06 | Picanha | lb | USD 7,05 | 0 (solo cotización) |
| BR-S02 | Pollo entero | kg | COP 11.500 | 4.250 kg |
| BR-S07 | Whole chicken | lb | USD 2,10 | 3.000 lb |
| BR-S03 | Surtido de verduras | kg | COP 4.200 | 6.000 kg |
| BR-S08 | Bebidas (caja) | caja | USD 24,00 | 300 cajas |

Durante los 11 primeros meses, los precios pueden variar como máximo un ±1% mensual. En el **último mes** deben aparecer estos escenarios:

| Escenario | Proveedor | Variación del último mes | Resultado esperado |
|---|---|---|---|
| A | BR-S05 Sunshine Prime Meats | +12% | Supera el umbral. **No permitida**: el contrato exige preaviso escrito y prueba del índice, y no hay registro de ninguna de las dos |
| B | BR-S01 Carnes del Valle | +4% | Supera el umbral. **Permitida**: está por debajo del IPC + 1 punto (6,2%) |
| C | BR-S02 Avícola Antioquia | +9% | Supera el umbral. **No permitida**: excede el máximo anual del 5% |
| D | BR-S08 Brava Beverages FL | +6% | No supera el umbral. Sin alerta de precio, pero su contrato dispara alerta de vencimiento |

---

## Umbrales y alertas

| Tipo | Regla |
|---|---|
| Subida de precio, carne de res | Más de un 3% frente al mes anterior |
| Subida de precio, resto de categorías | Más de un 8% frente al mes anterior |
| Vencimiento de contrato | 90 y 30 días antes |
| Fecha límite de preaviso | 15 días antes |

Las alertas se envían a Lucía Fernández (Compras) y a Felipe Guerrero.

---

## Aprobaciones

| Situación | Aprueba |
|---|---|
| Cualquier comunicación a un proveedor | Felipe Guerrero |
| Comunicación sobre un contrato con valor anual superior a USD 200.000 (o su equivalente en COP) | Felipe Guerrero **y** Mariana Restrepo |

---

## Preguntas que el sistema debe poder responder

- "¿La subida de Sunshine Prime Meats está permitida por el contrato?"
- "¿Cuánto nos cuesta al mes la subida de Avícola Antioquia?"
- "¿Qué alternativa tenemos a Carnes del Valle y a qué precio?"
- "¿Cuándo tenemos que avisar a Sunshine Prime Meats si no queremos renovar?"
- "¿Cuál es el preaviso de Avícola Antioquia?" → el sistema debe responder que el contrato no lo especifica.
- "¿Qué dice el contrato de Hortalizas La Sabana?" → el sistema debe responder que no hay contrato.
- "Prepárame un brief para renegociar con Sunshine Prime Meats."

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes de los agentes ni respuestas de la API:

- Datos bancarios de los proveedores incluidos en los contratos
- Datos personales de las personas de contacto de los proveedores (teléfono y correo personales)

Los contratos de prueba deben incluir estos datos en una cláusula de facturación, para poder comprobar que el sistema no los propaga.

---

## Restricción específica

Los briefs de renegociación y las alertas comparan precios solo dentro del mismo país. Si alguien pide comparar un proveedor de Colombia con uno de Florida, el sistema puede hacerlo convirtiendo al tipo de cambio de referencia, pero debe indicar que son mercados distintos y que la comparación es solo orientativa.
