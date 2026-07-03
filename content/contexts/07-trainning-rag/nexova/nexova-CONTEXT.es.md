# CONTEXT — Nexova

## Hito 7 — RAG y Base de Conocimiento

---

## 1. Introducción

Marcos Ibáñez (Director de Ventas) tiene 18 personas entre account managers y SDRs que repiten las mismas explicaciones a cada prospecto: qué incluye cada línea de servicio, cómo funciona el modelo de tarifas, cuánto tarda un proceso típico de headhunting. Cuando un SDR es nuevo, tarda semanas en dar respuestas seguras sin escalar a un account manager senior.

El **brief** que Marcos envió a través de un **RFP** interno pide un asistente que cualquier SDR pueda usar antes o durante una llamada con un prospecto, respondiendo **desde la perspectiva de un vendedor de Nexova**: seguro, orientado a cerrar, y sin inventar condiciones comerciales que no existen.

Tu base de conocimiento debe construirse a partir de los documentos fuente de la sección 2.

---

## 2. Documentos Fuente para la Base de Conocimiento

Usa los siguientes documentos fuente como base de tu base de conocimiento. Cada uno se entrega como un archivo independiente para que lo cargues directamente en tu pipeline de chunking.

| Archivo | Contenido |
|---|---|
| [`nexova-service-lines.es.md`](nexova-service-lines.es.md) | Líneas de Servicio |
| [`nexova-pricing-model.es.md`](nexova-pricing-model.es.md) | Modelo de Tarifas |
| [`nexova-hiring-process-sla.es.md`](nexova-hiring-process-sla.es.md) | SLA del Proceso de Contratación |
| [`nexova-objection-handling.es.md`](nexova-objection-handling.es.md) | Manejo de Objeciones Comunes de Prospectos |

---

## 3. Estructura de Datos de Dominio

```json
{
  "id": "uuid-del-chunk",
  "vector": [/* embedding */],
  "payload": {
    "company": "nexova",
    "source_document": "service-lines | pricing-model | hiring-process-sla | objection-handling",
    "section": "título o subtítulo de la sección de origen",
    "language": "es",
    "chunk_index": 0
  }
}
```

---

## 4. KPIs y Umbrales de la Respuesta

- **Recall@3**: al menos el 80% de las preguntas de prueba deben tener el
  chunk correcto entre los 3 primeros resultados recuperados.
- **Faithfulness**: ningún porcentaje, monto o plazo mencionado en la
  respuesta puede diferir de lo indicado en los chunks recuperados.
- Ante preguntas sobre descuentos o condiciones no cubiertas en los
  documentos (por ejemplo, un descuento del 22% al 15%), la respuesta debe
  indicar que esa condición requiere aprobación y no debe inventarla.

---

## 5. Instrucciones de Datos Semilla

- Indexa los cuatro documentos fuente completos de la sección 2.
- Cada documento debe producir al menos 3 chunks.
- Crea `data/eval/test-queries.json` con al menos 8 preguntas, incluyendo al
  menos dos objeciones de venta reales tomadas de `nexova-objection-handling.es.md`.

---

## 6. Restricciones de Negocio

- Nunca se debe ofrecer un descuento sobre la tarifa del 22% en una
  respuesta generada — el sistema debe remitir esa decisión a un humano.
- Los tiempos de entrega deben presentarse siempre como promedios, no como
  garantías, salvo la garantía de reemplazo de 6 meses que sí es contractual.
- Las respuestas sobre clientes de la competencia deben mantener la
  transparencia indicada en `nexova-objection-handling.es.md`.

---

## 7. Entregables Esperados

- Base de conocimiento indexada en Qdrant con los cuatro documentos fuente.
- Endpoint FastAPI que responde preguntas como "¿cuánto cuesta un programa
  de formación de 8 semanas?" o "¿qué pasa si la terna no me convence?" con
  una respuesta generada y trazable a la fuente.
- Interfaz mínima de consulta funcionando contra ese endpoint.
