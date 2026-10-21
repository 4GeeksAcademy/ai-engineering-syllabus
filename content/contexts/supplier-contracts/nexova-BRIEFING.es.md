# BRIEFING.md — Nexova

## Agentic Engineering – Gestión de Proveedores y Contratos

*These instructions are [available in English](./nexova-BRIEFING.en.md).*

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**Nexova** es una consultora de recursos humanos y captación de talento fundada en 2011, con sede en Valencia (España) y una oficina de expansión en Miami (Florida). Tiene 120 empleados, opera tres líneas de negocio (headhunting, externalización de soporte al cliente y formación corporativa) y factura alrededor de 8 millones de dólares al año. Opera con dos monedas: euros (EUR) en España y dólares (USD) en Estados Unidos.

---

## Tu departamento y el problema que debes resolver

Formas parte del equipo de AI Engineering de Nexova y reportas al CTO Sergio Molina.

Las tres líneas de negocio de Nexova dependen de proveedores de servicios: plataformas de búsqueda de candidatos, herramientas de evaluación psicométrica, la plataforma de telefonía del servicio de soporte y las salas donde se imparte la formación. Muchas de estas suscripciones se renuevan solas y suben de precio cada año. Javier Almeida, Operations Manager, descubre las subidas en la factura y, a veces, descubre una renovación automática cuando ya no se puede cancelar.

---

## Tu stakeholder

**Javier Almeida**, Operations Manager (Valencia)

> Hola:
>
> Te cuento cómo es esto en la práctica, porque no quiero una herramienta que no use nadie.
>
> El año pasado la plataforma de búsqueda de candidatos nos subió la licencia de los 40 consultores sin que nadie se diera cuenta hasta la factura. Cuando fuimos a negociar, ya había pasado la fecha para cancelar y estábamos atados otro año. No puede volver a pasar.
>
> Lo que necesito es simple: que me avisen cuando un proveedor sube por encima de lo razonable, que me digan si el contrato se lo permite, y que me avisen con tiempo antes de que algo se renueve solo. Si hay que negociar, quiero un resumen con lo que pagamos, lo que cobran los demás y qué nos deja hacer el contrato. Un resumen, no un informe de veinte páginas.
>
> Y una cosa muy importante: a un proveedor no se le manda nada sin que yo lo vea. Y jamás se le pasa información de nuestros candidatos ni de nuestros clientes, ni siquiera "para contextualizar".
>
> Javier

---

## Alcance de idioma

- El soporte multilingüe es **opcional pero muy recomendable**, porque Nexova tiene contratos en español (España) y en inglés (Estados Unidos).
- Elige un **idioma base** para las respuestas, los briefs y las alertas.
- Los contratos se analizan en su idioma original. Las citas de cláusulas se reproducen en el idioma del contrato.

---

## Proveedores

| ID | Proveedor | País | Categoría | Moneda |
|---|---|---|---|---|
| NX-S01 | JobReach Pro | España | Plataforma de búsqueda de candidatos | EUR |
| NX-S02 | TalentPool Network | España | Plataforma de búsqueda de candidatos | EUR |
| NX-S03 | AssessPro | España | Evaluación psicométrica | EUR |
| NX-S04 | MindMetrics | España | Evaluación psicométrica | EUR |
| NX-S05 | VoxCloud Contact | Estados Unidos | Telefonía para soporte | USD |
| NX-S06 | RingStack | Estados Unidos | Telefonía para soporte | USD |
| NX-S07 | Espacios Turia | España | Salas de formación | EUR |
| NX-S08 | Miami Training Rooms | Estados Unidos | Salas de formación | USD |

Las comparativas de precio se hacen **entre proveedores de la misma categoría y el mismo país**.

---

## Contratos

Genera un contrato ficticio en PDF por cada fila, con cada término redactado como cláusula numerada. Las fechas son relativas a la fecha de carga de los datos.

| Contrato | Proveedor | Vencimiento | Preaviso | Revisión de precio | Salida y penalización | Valor anual estimado |
|---|---|---|---|---|---|---|
| CT-NX-01 | JobReach Pro | Hoy + 80 días | Renovación automática por 12 meses salvo aviso 60 días antes del vencimiento | Anual, como máximo un 3%, comunicada con 60 días de antelación | Rescisión anticipada con penalización de 3 meses de cuota | EUR 312.000 |
| CT-NX-02 | AssessPro | Hoy + 240 días | No renovación: 30 días antes del vencimiento | Una vez al año, como máximo un 5% | **El contrato no incluye cláusula de salida anticipada** | EUR 136.800 |
| CT-NX-03 | VoxCloud Contact | Hoy + 400 días | No renovación: 90 días antes del vencimiento | Anual, ligada al IPC de Estados Unidos, con un máximo del 4% | Rescisión anticipada con penalización del 50% de las cuotas restantes | USD 34.200 |
| CT-NX-04 | Espacios Turia | Hoy + 25 días | No renovación: 15 días antes del vencimiento | Precio fijo durante toda la vigencia | Sin penalización | EUR 60.480 |

TalentPool Network, MindMetrics, RingStack y Miami Training Rooms **no tienen contrato**: solo hay cotizaciones o compras puntuales.

**Datos de referencia** para los cálculos:
- IPC anual de Estados Unidos: 2,9%
- Tipo de cambio de referencia: 1 USD = 0,92 EUR

---

## Histórico de precios

Genera un CSV con 12 meses de histórico (el último mes es el mes de carga) y estas columnas:

`supplier_id, product, unit, currency, month, unit_price, monthly_volume`

| Proveedor | Producto | Unidad | Precio base | Volumen mensual |
|---|---|---|---|---|
| NX-S01 | Licencia de reclutador | licencia/mes | EUR 650 | 40 licencias |
| NX-S02 | Licencia de reclutador | licencia/mes | EUR 610 | 0 (solo cotización) |
| NX-S03 | Evaluación psicométrica | evaluación | EUR 38 | 300 evaluaciones |
| NX-S04 | Evaluación psicométrica | evaluación | EUR 35 | 0 (solo cotización) |
| NX-S05 | Puesto de agente | puesto/mes | USD 95 | 30 puestos |
| NX-S06 | Puesto de agente | puesto/mes | USD 89 | 0 (solo cotización) |
| NX-S07 | Sala de formación | día | EUR 420 | 12 días |
| NX-S08 | Training room | día | USD 480 | 4 días |

Durante los 11 primeros meses, los precios no varían salvo en NX-S03 y NX-S07, que pueden variar como máximo un ±1% mensual. En el **último mes** deben aparecer estos escenarios:

| Escenario | Proveedor | Variación del último mes | Resultado esperado |
|---|---|---|---|
| A | NX-S01 JobReach Pro | +8% | Supera el umbral. **No permitida**: excede el máximo anual del 3% |
| B | NX-S03 AssessPro | +4% | Supera el umbral. **Permitida**: está dentro del máximo anual del 5% |
| C | NX-S05 VoxCloud Contact | +6% | Supera el umbral. **No permitida**: el contrato la limita al IPC de EE. UU. (2,9%) |
| D | NX-S07 Espacios Turia | +2% | No supera el umbral. Aun así, **no está permitida** porque el precio es fijo; además, su contrato dispara alerta de vencimiento |

---

## Umbrales y alertas

| Tipo | Regla |
|---|---|
| Subida de precio, cualquier categoría | Más de un 3% frente al mes anterior |
| Vencimiento de contrato | 90 y 30 días antes |
| Fecha límite de preaviso | 15 días antes |

Las alertas se envían a Javier Almeida.

El escenario D es intencionado: una subida pequeña que no dispara la alerta de precio sigue siendo una subida que el contrato no permite. El sistema debe detectarla al evaluar el contrato, aunque no la detecte el umbral.

---

## Aprobaciones

| Situación | Aprueba |
|---|---|
| Cualquier comunicación a un proveedor | Javier Almeida |
| Comunicación sobre un contrato con valor anual superior a EUR 150.000 (o su equivalente en USD) | Javier Almeida **y** Laura Mendoza |

---

## Preguntas que el sistema debe poder responder

- "¿JobReach Pro puede subirnos un 8%?"
- "¿Cuánto nos cuesta al año la subida de VoxCloud?"
- "¿Hasta cuándo podemos cancelar JobReach Pro sin quedar atados otro año?"
- "¿Qué alternativa tenemos a AssessPro y a qué precio?"
- "¿Podemos salir antes de tiempo del contrato de AssessPro?" → el sistema debe responder que el contrato no incluye cláusula de salida anticipada.
- "¿Espacios Turia puede subirnos el precio?"
- "Prepárame un resumen para renegociar con JobReach Pro."

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes de los agentes ni respuestas de la API:

- Datos bancarios de los proveedores incluidos en los contratos
- Datos personales de las personas de contacto de los proveedores

Los contratos de prueba deben incluir estos datos en una cláusula de facturación, para poder comprobar que el sistema no los propaga.

---

## Restricción específica

Ningún brief ni ninguna comunicación a un proveedor puede incluir datos de candidatos ni de clientes de Nexova: ni nombres, ni empresas cliente, ni volúmenes de uso por cliente. Si una petición lo intenta, el sistema debe excluir esos datos e indicar que lo ha hecho.
