# CONTEXT — TrackFlow

## Hito 8 · Memoria y Auto-mejora de Agentes

---

## Por qué importa esta memoria para TrackFlow

Tu agente ya conoce las operaciones de TrackFlow en Los Ángeles y Zaragoza, consulta el Incidents Manager y el inventario a través del MCP Server, y no se sale de su guardrail. Valentina Cruz (CX Manager) reporta que sus 15 agentes de soporte, distribuidos entre ambos países, tienen que corregirle al asistente las mismas reglas de carrier una y otra vez — el asistente no aprende de una sesión a la siguiente.

## Qué SÍ vale la pena recordar

- **Reglas de asignación de carrier corregidas**: si un carrier cambió su cobertura para cierta zona, o si dejó de operar cierta ruta, vale la pena recordarlo.
- **Contexto de incidentes conocidos y recurrentes**: "los retrasos en la ruta de Zaragoza a Cataluña esta semana son por una huelga de transportistas, no un problema de TrackFlow" — útil para no re-escalar la misma alerta.
- **Preferencias de clientes B2B recurrentes** sobre su reporte mensual (formato, métricas destacadas).

## Qué NUNCA debe entrar en la memoria

- Direcciones exactas de clientes finales (B2C) o rutas internas del almacén — es información sensible de seguridad física, tal como señala el propio README de guardrails de la empresa.
- Datos de una incidencia puntual de un solo paquete sin patrón repetible (una queja aislada de un cliente no es memorizable).
- Información de contratos comerciales activos en negociación (eso lo maneja el CRM del equipo comercial, no la memoria del agente de soporte).

## Ejemplos para tu checklist de "Auto-evaluación"

**Deberían generar una propuesta de memoria:**
1. "En realidad SEUR ya no cubre esa zona rural de Zaragoza, hay que usar el carrier local desde el mes pasado."
2. "Esos retrasos reportados en incidencias de Los Ángeles esta semana son por la huelga portuaria, no por un problema nuestro — ya van tres tickets sobre lo mismo."
3. "El cliente de cosméticos siempre quiere su reporte mensual con el desglose de devoluciones primero, antes que el volumen de envíos."

**NO deberían generar una propuesta:**
1. "¿Dónde está el paquete con tracking XJ4471?" (consulta puntual de tracking, no un patrón).
2. "Perfecto, ya quedó resuelto." (cierre de conversación).
3. "Tradúceme esto al inglés para el cliente." (tarea de un solo uso).

## Consolidación sugerida

TrackFlow opera con 8 carriers entre dos países. Considera consolidar la memoria por carrier + país en vez de por ticket individual, para que las reglas de asignación no queden fragmentadas en decenas de entradas sueltas.

## Restricciones de la empresa

TrackFlow distingue entre clientes B2B (marcas) y B2C (destinatarios finales). Tu validación de "qué nunca debe recordarse" debe cubrir explícitamente los datos sensibles de ubicación de ambos tipos de cliente, no solo uno.
