# CONTEXT — TrackFlow

## Hito 7 — RAG y Base de Conocimiento

---

## 1. Introducción

Miguel Torres (Director Comercial) tiene 8 personas entre account managers y business development que responden constantemente las mismas preguntas de marcas prospecto y clientes actuales: qué SLA de entrega manejan, cómo funciona la política de devoluciones, qué transportistas cubren cada zona, cómo se calculan las tarifas de almacenamiento.

El **ticket** que el equipo comercial trasladó a tecnología pide un asistente que cualquier account manager pueda usar **como lo haría un vendedor de TrackFlow** en una llamada con un cliente: con datos exactos y sin prometer condiciones que no existen en los acuerdos estándar.

Tu base de conocimiento debe construirse a partir de los documentos fuente de la sección 2.

---

## 2. Documentos Fuente para la Base de Conocimiento

Usa los siguientes documentos fuente como base de tu base de conocimiento. Cada uno se entrega como un archivo independiente para que lo cargues directamente en tu pipeline de chunking.

| Archivo | Contenido |
|---|---|
| [`trackflow-sla-delivery.es.md`](trackflow-sla-delivery.es.md) | SLA de Entrega |
| [`trackflow-returns-policy.es.md`](trackflow-returns-policy.es.md) | Política de Devoluciones |
| [`trackflow-carrier-coverage.es.md`](trackflow-carrier-coverage.es.md) | Cobertura de Transportistas |
| [`trackflow-storage-pricing.es.md`](trackflow-storage-pricing.es.md) | Tarifas de Almacenamiento |

---

## 3. Estructura de Datos de Dominio

```json
{
  "id": "uuid-del-chunk",
  "vector": [/* embedding */],
  "payload": {
    "company": "trackflow",
    "source_document": "sla-delivery | returns-policy | carrier-coverage | storage-pricing",
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
- **Faithfulness**: ningún porcentaje, tarifa o plazo en la respuesta puede
  diferir de los chunks recuperados.
- Preguntas sobre descuentos de almacenamiento o excepciones de
  transportista fuera de lo documentado deben responder que requieren
  aprobación, nunca inventar una condición.

---

## 5. Instrucciones de Datos Semilla

- Indexa los cuatro documentos fuente completos de la sección 2.
- Cada documento debe producir al menos 3 chunks.
- Crea `data/eval/test-queries.json` con al menos 8 preguntas cubriendo los
  cuatro documentos, incluyendo al menos una sobre picos de demanda
  (Black Friday / Rebajas).

---

## 6. Restricciones de Negocio

- Nunca se debe prometer un SLA de entrega durante fechas de alta demanda
  declaradas — debe seguirse la advertencia de `trackflow-sla-delivery.es.md`.
- Las devoluciones internacionales nunca deben describirse como
  "automáticas" — deben remitirse siempre a gestión manual.
- Ningún descuento de almacenamiento puede ofrecerse sin mencionar que
  requiere aprobación de Miguel Torres.

---

## 7. Entregables Esperados

- Base de conocimiento indexada en Qdrant con los cuatro documentos fuente.
- Endpoint FastAPI que responde preguntas como "¿cuál es la ventana de
  devolución estándar?" o "¿qué transportista cubre mejor Aragón rural?"
  con una respuesta generada y trazable a la fuente.
- Interfaz mínima de consulta funcionando contra ese endpoint.
