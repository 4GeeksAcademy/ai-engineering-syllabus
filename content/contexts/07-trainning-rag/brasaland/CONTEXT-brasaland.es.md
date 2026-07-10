# CONTEXT — Brasaland

## Hito 7 — RAG y Base de Conocimiento

---

## 1. Introducción

En Brasaland, el equipo de **Operaciones** y el de **Marketing** reciben constantemente las mismas preguntas de gerentes de local, clientes y hasta de nuevos empleados: cómo funciona el programa de puntos, cuáles son los protocolos de desperdicio, qué alérgenos tiene cada plato, cómo se hace un pedido a proveedores. Hoy, cada gerente responde "a su manera" según lo que recuerda — y eso genera respuestas inconsistentes entre Colombia y Florida.

Felipe Guerrero (Director de Operaciones) pidió, a través de un **ticket**, un asistente que cualquier gerente de local pueda usar para responder **como lo haría un vendedor entrenado**: con seguridad, con los datos correctos, y sin inventar información que no está en los manuales oficiales.

Tu base de conocimiento debe construirse a partir de los documentos fuente de la sección 2. Debes fragmentarlos (chunking) y convertirlos en embeddings — no debes inventar contenido adicional más allá de lo que estos documentos contienen.

---

## 2. Documentos Fuente para la Base de Conocimiento

Usa los siguientes documentos fuente como base de tu base de conocimiento. Cada uno se entrega como un archivo independiente para que lo cargues directamente en tu pipeline de chunking.

| Archivo | Contenido |
|---|---|
| [`brasaland-loyalty-program.es.md`](brasaland-loyalty-program.es.md) | Programa de Lealtad "Brasa Points" |
| [`brasaland-waste-protocol.es.md`](brasaland-waste-protocol.es.md) | Protocolo de Control de Desperdicio |
| [`brasaland-menu-allergens.es.md`](brasaland-menu-allergens.es.md) | Guía de Alérgenos del Menú |
| [`brasaland-supplier-ordering.es.md`](brasaland-supplier-ordering.es.md) | Procedimiento de Pedido a Proveedores |

---

## 3. Estructura de Datos de Dominio

Cada punto (point) que insertes en Qdrant debe incluir, como mínimo, el
siguiente payload:

```json
{
  "id": "uuid-del-chunk",
  "vector": [/* embedding */],
  "payload": {
    "company": "brasaland",
    "source_document": "loyalty-program | waste-protocol | menu-allergens | supplier-ordering",
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
- **Faithfulness**: la respuesta generada no debe contener ningún dato
  numérico (porcentajes, montos, kg) que no aparezca en los chunks
  recuperados.
- **Umbral mínimo de similitud**: define un umbral y documenta por qué lo
  elegiste; si ningún chunk lo supera, la respuesta debe indicar
  explícitamente que no tiene información suficiente — nunca debe inventar.

---

## 5. Instrucciones de Datos Semilla

- Como mínimo, indexa los cuatro documentos fuente completos de la sección 2.
- Cada documento debe producir al menos 3 chunks (ni un chunk por documento,
  ni un chunk por línea).
- Guarda un archivo `data/eval/test-queries.json` con al menos 8 preguntas de
  prueba y la respuesta esperada (o el chunk fuente esperado), cubriendo los
  cuatro documentos.

---

## 6. Restricciones de Negocio

- Las respuestas deben mantener el idioma base elegido para el proyecto; si
  implementas soporte bilingüe, la respuesta debe coincidir con el idioma de
  la pregunta.
- Nunca debe responderse "sin riesgo" ante preguntas de alérgenos — debe
  seguirse literalmente la redacción de `brasaland-menu-allergens.es.md`.
- Los montos en dólares y pesos colombianos deben mantenerse tal como
  aparecen en el documento fuente; no hagas conversión de moneda automática
  a menos que el CONTEXT lo pida explícitamente en un hito posterior.

---

## 7. Entregables Esperados

- Base de conocimiento indexada en Qdrant con los cuatro documentos fuente.
- Endpoint FastAPI que responde preguntas como "¿cuántos puntos necesito para
  el nivel Oro?" o "¿la Costilla BBQ tiene alérgenos?" con una respuesta
  generada, precisa y trazable a la fuente.
- Interfaz mínima de consulta funcionando contra ese endpoint.
