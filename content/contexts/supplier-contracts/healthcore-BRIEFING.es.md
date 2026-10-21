# BRIEFING.md — HealthCore

## Agentic Engineering – Gestión de Proveedores y Contratos

*These instructions are [available in English](./healthcore-BRIEFING.en.md).*

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**HealthCore** es una empresa de servicios de salud ambulatoria fundada en 2011 en Austin, Texas. Opera 12 clínicas, 9 en Estados Unidos y 3 en Reino Unido, emplea a unas 200 personas y factura alrededor de 28 millones de dólares al año. Opera con dos monedas, dólares (USD) y libras esterlinas (GBP), y bajo dos marcos de protección de datos de salud: HIPAA en Estados Unidos y UK GDPR en Reino Unido.

---

## Tu departamento y el problema que debes resolver

Formas parte de **HealthCore Digital**, la unidad interna que construye la infraestructura de la empresa, y reportas al CTO James Osei.

Las clínicas dependen de proveedores de material clínico, laboratorios de análisis y servicios de interpretación médica para pacientes que no hablan inglés. Los precios suben sin que nadie lo note hasta la factura, y los contratos están repartidos entre Operaciones Clínicas y Cumplimiento. Hay además un riesgo que no existe en otros sectores: varios de estos proveedores procesan datos de pacientes, y la ley exige que tengan firmado un acuerdo de protección de datos. Hoy nadie comprueba de forma sistemática que esos acuerdos existen.

---

## Tu stakeholder

**Dr. Marcus Reid**, Director of Clinical Operations (Austin)

> Equipo:
>
> Os resumo lo que hablamos por teléfono, para que quede por escrito.
>
> - Quiero saber cuándo un proveedor clínico nos sube el precio por encima de lo razonable, y si el contrato se lo permite.
> - Quiero aviso con tiempo antes de que venza un contrato. Quedarnos sin laboratorio o sin interpretación un lunes por la mañana no es una opción para los pacientes.
> - Si hay que renegociar, un resumen con el histórico, lo que cobran otros proveedores y lo que nos permite el contrato.
> - Los laboratorios y el servicio de interpretación manejan datos de pacientes. Claire insiste, con razón, en que el sistema compruebe siempre que tienen firmado su acuerdo de protección de datos. Si falta, es lo primero que tiene que saber ella, antes de hablar de precios.
> - Ninguna comunicación sale a un proveedor sin mi aprobación. Si el proveedor maneja datos de pacientes, también la de Claire.
>
> Marcus

---

## Alcance de idioma

- El idioma base es el **inglés**: todos los contratos y las comunicaciones con proveedores están en inglés.
- El español es **opcional** para las respuestas internas del sistema.

---

## Proveedores

| ID | Proveedor | País | Categoría | Moneda | ¿Procesa datos de pacientes? |
|---|---|---|---|---|---|
| HC-S01 | MedSupply Partners | Estados Unidos | Material clínico | USD | No |
| HC-S02 | CareSource Medical | Estados Unidos | Material clínico | USD | No |
| HC-S03 | ClearPath Labs | Estados Unidos | Laboratorio | USD | Sí |
| HC-S04 | Lone Star Diagnostics | Estados Unidos | Laboratorio | USD | Sí |
| HC-S05 | BritMed Supplies | Reino Unido | Material clínico | GBP | No |
| HC-S06 | Thames Pathology | Reino Unido | Laboratorio | GBP | Sí |
| HC-S07 | LinguaCare Interpreting | Estados Unidos | Interpretación médica | USD | Sí |

Las comparativas de precio se hacen **entre proveedores de la misma categoría y el mismo país**.

---

## Contratos

Genera un contrato ficticio en PDF por cada fila, en inglés, con cada término redactado como cláusula numerada. Las fechas son relativas a la fecha de carga de los datos.

| Contrato | Proveedor | Vencimiento | Preaviso | Revisión de precio | Salida y penalización | Acuerdo de protección de datos | Valor anual estimado |
|---|---|---|---|---|---|---|---|
| CT-HC-01 | MedSupply Partners | Hoy + 180 días | No renovación: 60 días antes | Anual, como máximo un 5% | Con 90 días de preaviso, sin penalización | No aplica | USD 537.600 |
| CT-HC-02 | ClearPath Labs | Hoy + 60 días | No renovación: 45 días antes | Anual, como máximo el IPC de Estados Unidos | Rescisión anticipada con penalización de 2 meses de facturación media | BAA firmado, anexo al contrato | USD 540.000 |
| CT-HC-03 | Thames Pathology | Hoy + 210 días | No renovación: 90 días antes | Anual, como máximo un 3% | Con 90 días de preaviso, sin penalización | **El contrato no incluye DPA** | GBP 121.800 |
| CT-HC-04 | LinguaCare Interpreting | Hoy + 28 días | No renovación: 15 días antes | Precio fijo durante toda la vigencia | Sin penalización | BAA firmado, anexo al contrato | USD 210.600 |

CareSource Medical, Lone Star Diagnostics y BritMed Supplies **no tienen contrato**: solo hay cotizaciones o pedidos puntuales.

**Datos de referencia** para los cálculos:
- IPC anual de Estados Unidos: 2,9%
- Tipo de cambio de referencia: 1 GBP = 1,27 USD

---

## Histórico de precios

Genera un CSV con 12 meses de histórico (el último mes es el mes de carga) y estas columnas:

`supplier_id, product, unit, currency, month, unit_price, monthly_volume`

Los volúmenes son **agregados mensuales**. El CSV nunca contiene datos por paciente.

| Proveedor | Producto | Unidad | Precio base | Volumen mensual |
|---|---|---|---|---|
| HC-S01 | Kit de consulta desechable | kit | USD 3,20 | 14.000 kits |
| HC-S02 | Kit de consulta desechable | kit | USD 3,05 | 0 (solo cotización) |
| HC-S03 | Panel metabólico básico | prueba | USD 18,00 | 2.500 pruebas |
| HC-S04 | Panel metabólico básico | prueba | USD 17,20 | 0 (solo cotización) |
| HC-S05 | Kit de consulta desechable | kit | GBP 2,70 | 3.500 kits |
| HC-S06 | Panel metabólico básico | prueba | GBP 14,50 | 700 pruebas |
| HC-S07 | Interpretación médica | minuto | USD 1,95 | 9.000 minutos |

Durante los 11 primeros meses, los precios pueden variar como máximo un ±1% mensual. En el **último mes** deben aparecer estos escenarios:

| Escenario | Proveedor | Variación del último mes | Resultado esperado |
|---|---|---|---|
| A | HC-S03 ClearPath Labs | +7% | Supera el umbral. **No permitida**: el contrato la limita al IPC de EE. UU. (2,9%). Además, su contrato dispara alerta de fecha límite de preaviso |
| B | HC-S01 MedSupply Partners | +4,5% | Supera el umbral. **Permitida**: está dentro del máximo anual del 5% |
| C | HC-S06 Thames Pathology | +2% | No supera el umbral y está permitida, pero al evaluar el contrato el sistema debe detectar que **falta el DPA** y alertar a Cumplimiento |
| D | HC-S07 LinguaCare Interpreting | Sin cambio | Sin alerta de precio, pero su contrato dispara alerta de vencimiento |

---

## Umbrales y alertas

| Tipo | Regla |
|---|---|
| Subida de precio, cualquier categoría | Más de un 4% frente al mes anterior |
| Vencimiento de contrato | 90 y 30 días antes |
| Fecha límite de preaviso | 15 días antes |
| Proveedor que procesa datos de pacientes sin BAA (EE. UU.) o DPA (Reino Unido) | Inmediata, en cuanto se detecta |

Las alertas de precio, vencimiento y preaviso se envían al Dr. Marcus Reid. Las alertas de acuerdos de protección de datos se envían a Claire Whitfield.

---

## Aprobaciones

| Situación | Aprueba |
|---|---|
| Cualquier comunicación a un proveedor | Dr. Marcus Reid |
| Comunicación a un proveedor que procesa datos de pacientes | Dr. Marcus Reid **y** Claire Whitfield |
| Comunicación sobre un contrato con valor anual superior a USD 500.000 (o su equivalente en GBP) | Los aprobadores anteriores que correspondan **y** la Dra. Sandra Okonkwo |

---

## Preguntas que el sistema debe poder responder

- "¿ClearPath Labs puede subirnos un 7%?"
- "¿Cuánto nos cuesta al año la subida de ClearPath Labs?"
- "¿Qué alternativa tenemos a ClearPath Labs y a qué precio?"
- "¿Qué proveedores procesan datos de pacientes sin acuerdo de protección de datos firmado?"
- "¿Cuándo tenemos que avisar a ClearPath Labs si no queremos renovar?"
- "¿Qué dice el contrato de BritMed Supplies?" → el sistema debe responder que no hay contrato.
- "Prepárame un brief para renegociar con ClearPath Labs."

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes de los agentes ni respuestas de la API:

- Datos bancarios de los proveedores incluidos en los contratos
- Datos personales de las personas de contacto de los proveedores
- **Cualquier dato de pacientes.** El sistema trabaja solo con precios y volúmenes agregados. Si una petición solicita datos de uso por paciente, el sistema debe rechazarla

Los contratos de prueba deben incluir los dos primeros tipos de dato en una cláusula de facturación, para poder comprobar que el sistema no los propaga.

---

## Restricción específica

Antes de generar un brief de renegociación o redactar cualquier comunicación para un proveedor que procesa datos de pacientes, el sistema debe comprobar que su acuerdo de protección de datos está firmado (BAA en Estados Unidos, DPA en Reino Unido). Si falta, el sistema detiene el brief, alerta a Claire Whitfield y lo indica en la respuesta. El brief solo puede generarse cuando Cumplimiento confirme que puede continuar.
