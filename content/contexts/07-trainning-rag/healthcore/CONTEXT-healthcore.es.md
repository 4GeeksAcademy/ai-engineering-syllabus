# CONTEXT — HealthCore

## Hito 7 — RAG y Base de Conocimiento

---

## 1. Introducción

Priya Nair (Head of Patient Experience) tiene 8 coordinadores de pacientes que responden constantemente las mismas preguntas en recepción y por teléfono: qué seguros aceptan, cómo funciona la política de cancelación, cuánto tiempo tarda un proceso de referencia interna, qué documentos necesita un paciente nuevo. Cuando un coordinador es nuevo, comete errores por falta de información consistente entre las 12 clínicas.

El **memo** que Priya envió al equipo de HealthCore Digital pide un asistente que cualquier coordinador pueda usar en el mostrador **como lo haría el mejor vendedor de servicios de la clínica**: claro, empático, y sin inventar coberturas de seguro o políticas que no existen.

> ⚠️ **Nota regulatoria:** este hito trabaja únicamente con contenido de políticas, procedimientos y catálogo de servicios — **nunca con datos reales de pacientes**. Ningún documento de esta base de conocimiento debe contener PHI (Protected Health Information) real. Los ejemplos aquí son ficticios y de uso exclusivamente educativo.

Tu base de conocimiento debe construirse a partir de los documentos fuente de la sección 2.

---

## 2. Documentos Fuente para la Base de Conocimiento

Usa los siguientes documentos fuente como base de tu base de conocimiento. Cada uno se entrega como un archivo independiente para que lo cargues directamente en tu pipeline de chunking.

| Archivo | Contenido |
|---|---|
| [`healthcore-insurance-coverage.es.md`](healthcore-insurance-coverage.es.md) | Cobertura de Seguros Aceptados |
| [`healthcore-appointment-policy.es.md`](healthcore-appointment-policy.es.md) | Política de Citas y Cancelaciones |
| [`healthcore-referral-process.es.md`](healthcore-referral-process.es.md) | Proceso de Referencia Interna |
| [`healthcore-new-patient-checklist.es.md`](healthcore-new-patient-checklist.es.md) | Checklist para Pacientes Nuevos |

---

## 3. Estructura de Datos de Dominio

```json
{
  "id": "uuid-del-chunk",
  "vector": [/* embedding */],
  "payload": {
    "company": "healthcore",
    "source_document": "insurance-coverage | appointment-policy | referral-process | new-patient-checklist",
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
- **Faithfulness**: ningún dato de cobertura, tarifa o plazo en la respuesta
  puede diferir de los chunks recuperados.
- Ante preguntas sobre coberturas de seguro no listadas, la respuesta debe
  indicar que debe verificarse con facturación — nunca debe confirmar una
  cobertura no documentada.

---

## 5. Instrucciones de Datos Semilla

- Indexa los cuatro documentos fuente completos de la sección 2.
- Cada documento debe producir al menos 3 chunks.
- Crea `data/eval/test-queries.json` con al menos 8 preguntas, cubriendo los
  cuatro documentos.
- **No agregues ningún dato adicional que simule un registro real de
  paciente** (nombre, diagnóstico, número de historia clínica). Toda la base
  de conocimiento debe limitarse a políticas y procedimientos.

---

## 6. Restricciones de Negocio

- Ningún chunk ni respuesta generada puede contener PHI real ni simulado con
  apariencia de dato real de paciente — esta es una restricción HIPAA / UK
  GDPR que aplica de forma transversal al proyecto.
- Las respuestas sobre cobertura de seguro deben distinguir explícitamente
  entre Estados Unidos y Reino Unido cuando la pregunta no especifique el
  país.
- Los cargos por no-show nunca deben aplicarse a pacientes de Medicare o
  Medicaid en una respuesta generada — debe seguirse literalmente el
  `healthcore-appointment-policy.es.md`.

---

## 7. Entregables Esperados

- Base de conocimiento indexada en Qdrant con los cuatro documentos fuente.
- Endpoint FastAPI que responde preguntas como "¿cobran cargo por
  cancelación con 12 horas de anticipación?" o "¿qué debo traer a mi primera
  cita?" con una respuesta generada y trazable a la fuente.
- Interfaz mínima de consulta funcionando contra ese endpoint.
