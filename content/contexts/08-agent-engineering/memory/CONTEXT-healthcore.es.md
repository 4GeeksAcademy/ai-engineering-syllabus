# CONTEXT — HealthCore

## Hito 8 · Memoria y Auto-mejora de Agentes

---

## Por qué importa esta memoria para HealthCore

Tu agente ya conoce las 12 clínicas de HealthCore (US/UK), consulta el Incidents Manager y el inventario a través del MCP Server, y no se sale de su guardrail. Claire Whitfield (Chief Compliance Officer) revisó el sprint de guardrails y ahora exige que cualquier capacidad nueva pase primero por su filtro — y memoria persistente es exactamente el tipo de capacidad que le preocupa.

> ⚠️ **Restricción no negociable de HealthCore (aplica a todo el proyecto, no solo a este hito):** ningún identificador de paciente ni PHI (Protected Health Information) bajo HIPAA/UK GDPR puede aparecer en ningún evento, tabla, endpoint, log o salida generada — incluyendo, explícitamente, la memoria del agente. Esta restricción es más estricta aquí que en cualquier otra empresa del curso: mientras que en otras compañías la pregunta de diseño sobre "qué nunca debe recordarse" es una decisión a justificar, en HealthCore es un requisito de cumplimiento que no admite excepciones ni justificación en contra.

## Qué SÍ vale la pena recordar

- **Correcciones operativas recurrentes por clínica**: cambios de horario, protocolos locales de recepción, excepciones administrativas por país (US vs. UK).
- **Patrones de incidentes conocidos, sin datos de paciente**: por ejemplo, "el sistema de referidos falla los lunes en la mañana por el batch nocturno" es memorizable; "el paciente Smith tuvo un referido fallido" no lo es.
- **Preferencias de un miembro del staff clínico o administrativo** sobre cómo quiere que se le presente información operativa (no clínica).

## Qué NUNCA debe entrar en la memoria

- Cualquier identificador de paciente: nombre, número de historia clínica, fecha de nacimiento, diagnóstico, número de seguro, o cualquier combinación que permita re-identificar a una persona.
- Notas clínicas, resultados de laboratorio, o cualquier contenido de una consulta médica, aunque el usuario los mencione al pedir que se recuerden.
- Cualquier propuesta de memoria generada por el agente debe pasar, antes de mostrarse al usuario, por una validación explícita que rechace la propuesta si contiene lo que parece ser información de paciente — esto es un requisito adicional específico de HealthCore, sobre el flujo genérico del README.

## Ejemplos para tu checklist de "Auto-evaluación"

**Deberían generar una propuesta de memoria:**
1. "En la clínica de Manchester el proceso de referidos internos ahora pasa primero por el coordinador antes que por el especialista — cambió el trimestre pasado."
2. "Esa alerta de no-show elevado en la clínica de Austin fue porque hubo un cierre de carretera esa semana, no un problema real del programa de recordatorios."
3. "El reporte semanal para Diane Foster debe incluir vacantes por rol, no solo por clínica — eso lo pidió hace dos semanas."

**NO deberían generar una propuesta (y algunas deben rechazarse por contener PHI, no solo por ser puntuales):**
1. "¿Cuál es la tasa de no-show de esta semana?" (consulta puntual, dato vive en el dashboard, no en memoria de agente).
2. "El paciente Johnson canceló su cita de mañana, apúntalo." (⚠️ esto es un intento de guardar PHI — el agente debe rechazar la propuesta explícitamente, no solo ignorarla en silencio, y explicarle al usuario por qué no puede recordar eso).
3. "Gracias, con eso resuelvo mi reporte." (cierre de conversación, nada nuevo que recordar).

## Consolidación sugerida

Dado el volumen y la sensibilidad, cualquier proceso de consolidación o resumen debe re-verificar la ausencia de PHI antes de escribir la versión consolidada — no basta con validar en el momento de la propuesta inicial.

## Restricciones de la empresa

HealthCore opera bajo HIPAA (US) y UK GDPR (UK) simultáneamente. Documenta en tus decisiones de diseño cómo tu validación de "qué nunca debe recordarse" cubre ambos marcos regulatorios, no solo uno.
