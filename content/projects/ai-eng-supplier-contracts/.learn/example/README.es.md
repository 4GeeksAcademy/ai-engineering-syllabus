# Harbor City Library — Mesa de precios y contratos de proveedores (Ejemplo de clase)

> **Para instructores:** Brief de demo en vivo para `ai-eng-supplier-contracts`. Misma columna vertebral (supervisor + especialistas de precios/contratos, trazabilidad a fuente y cita de cláusula/página, herramientas de cálculo deterministas, presupuesto de consultas, aprobación humana antes de mensajes al proveedor, identidad de auditoría por agente). Dominio distinto: proveedores de impresión/ebook de una biblioteca pública, no carriers ni packaging corporativos. Alcance: ~60–90 minutos. El alumnado sigue el brief completo del monorepo en el `README.md` raíz del proyecto.

_These instructions are also available in [English](./README.md)._

---

## El reto

**Harbor City Library** compra paquetes de impresión y ebook a unos pocos proveedores. Las subidas aparecen en la factura; las cláusulas de renovación viven en PDFs sueltos. Vas a demos un **supervisor + dos especialistas** que detectan un salto de precio, comprueban si el contrato lo permite, calculan el impacto con código (no con el LLM) y redactan un email al proveedor que **no se puede enviar** hasta que la bibliotecaria de adquisiciones apruebe.

### Nota de alcance

| Proyecto evaluado (`ai-eng-supplier-contracts`)     | Este ejemplo de clase                                         |
| --------------------------------------------------- | ------------------------------------------------------------- |
| Briefing completo de empresa (multi-proveedor, FX…) | 3 proveedores, 1 moneda (USD), umbral fijo 8%                 |
| Pipeline PDF completo + flags de confianza          | 1 “contrato” markdown corto por proveedor + etiquetas de pág. |
| Brief de renegociación de producto completo         | Un brief JSON/markdown fusionado basta                        |
| Matriz de aprobación multi-rol                      | Un solo aprobador: `acquisitions_librarian`                   |
| Suite de auditoría/privacidad de producción         | Log `agent_id`; solo redactar `vendor_bank_iban`              |

---

## Qué construir

### 1. Dataset mínimo

| Vendor ID | Categoría | Precio unit. anterior | Precio unit. nuevo | Volumen / mes |
| --------- | --------- | --------------------- | ------------------ | ------------- |
| HCL-V01   | Print     | 12.00                 | 13.50              | 400           |
| HCL-V02   | Print     | 11.80                 | 11.80              | 200           |
| HCL-V03   | Ebook     | 4.00                  | 4.10               | 1000          |

Extracto de contrato de juguete para `HCL-V01` (tratar como página 3, cláusula `B.2`):

```text
Price revisions may not exceed 8% within a calendar year without 30 days written notice.
Either party may exit with 45 days notice; early exit fee = 1 month of average spend.
```

- [ ] Ingesta de precios con `source_ref` (p. ej. `price_history:HCL-V01:2026-04-01`)
- [ ] Guardar texto de cláusula con `clause_id` + `page`

### 2. Especialista de precios

- [ ] Detectar subidas donde `delta_pct >= 8`
- [ ] `impact = volume * (new - old)` como **función pura** con un test unitario
- [ ] Comparar con pares de la misma categoría (print vs ebook)

### 3. Especialista de contratos

- [ ] Responder: ¿encaja el salto de `HCL-V01` en la cláusula `B.2`? Citar página + cláusula
- [ ] Si el aviso escrito no está en los datos de juguete → devolver `missing`, no inventarlo
- [ ] Stub: alerta si la ventana de aviso de renovación/salida está a ≤ 14 días (fecha hard-coded OK)

### 4. Supervisor

- [ ] Ante umbral: llamar a precios **y** contratos, fusionar una sola respuesta
- [ ] Tope de llamadas a especialistas (p. ej. ≤ 4) por petición
- [ ] A demanda: brief corto de renegociación (histórico, par, impacto, apalancamiento)

### 5. Aprobación humana + auditoría

- [ ] Borrador de email permitido; envío bloqueado hasta rol `acquisitions_librarian`
- [ ] Log de acciones con `agent_id` (`supervisor` / `pricing` / `contracts`)
- [ ] Nunca loguear `vendor_bank_iban`

---

## Verificar juntos

- [ ] `HCL-V01` alerta; `HCL-V03` no (bajo 8%)
- [ ] Impacto V01 = `400 * 1.50 = 600` desde la herramienta de cálculo, no del modelo
- [ ] Respuesta de contratos cita `B.2` / página 3; aviso faltante se declara explícito
- [ ] Intento de envío sin rol de bibliotecaria → bloqueado
- [ ] Mostrar una línea de auditoría por agente; sin IBAN en logs

---

## Preguntas de discusión

1. ¿Por qué separar precios y contratos en especialistas en lugar de un solo agente con todas las tools?
2. ¿Qué falla si el LLM “estima” el impacto cuando falta el volumen?
3. ¿Dónde debe vivir el presupuesto de consultas — política del supervisor, límite de aristas del grafo, o ambos?
