# CONTEXT — Brasaland

## Hito 8 · Memoria y Auto-mejora de Agentes

---

## Por qué importa esta memoria para Brasaland

Tu agente ya conoce las 14 locations de Brasaland (Colombia y Florida), consulta el Incidents Manager y el inventario a través del MCP Server, y no se sale de su guardrail. El problema que reporta Felipe Guerrero (Operations Director): los mismos gerentes de local repiten las mismas correcciones semana tras semana — "el proveedor de carne de Medellín entrega los martes, no los lunes", "la ubicación de Miami cierra a las 10pm los viernes, no a las 9pm" — y el agente los sigue tratando como preguntas nuevas cada vez.

## Qué SÍ vale la pena recordar

- **Correcciones operativas recurrentes por location**: horarios reales de apertura/cierre, días de entrega de proveedores específicos, excepciones locales a un procedimiento estándar.
- **Contexto de una escalación resuelta**: si una alerta de "sin ventas en 2 horas" en una location resultó ser un problema conocido (ej. corte de luz programado en esa zona), vale la pena recordarlo para no re-escalar lo mismo.
- **Preferencias de comunicación de un gerente de local**: si Carlos Jiménez (supervisor senior) siempre pide reportes en un formato específico, eso es memorizable.

## Qué NUNCA debe entrar en la memoria

- Datos personales de clientes de Brasa Points más allá de lo estrictamente operativo (no se necesita memoria de agente para eso — vive en el CRM).
- Cifras de nómina o compensación individual del personal de las 14 locations.
- Cualquier dato que solo aplique a una conversación puntual sin patrón repetible (por ejemplo, una queja de un cliente específico un solo día no es memorable).

## Ejemplos para tu checklist de "Auto-evaluación"

**Deberían generar una propuesta de memoria:**
1. "En realidad el proveedor de vegetales en Zaragoza... espera, es Medellín, entrega los miércoles, no los martes como dijiste antes."
2. "La location de Miami Beach ahora cierra a las 11pm los fines de semana, cambió el mes pasado."
3. "Esa alerta de ventas en cero en la location 7 fue porque hubo un apagón, no fue un error del POS — ya pasó dos veces este mes."

**NO deberían generar una propuesta:**
1. "¿Cuál fue el ticket promedio de ayer en Bogotá?" (consulta puntual, dato ya vive en el pipeline de telemetría, no en la memoria del agente).
2. "Gracias, eso resuelve mi duda." (cierre de conversación, nada nuevo que recordar).
3. "¿Puedes traducir esto al inglés para el reporte de Ashley?" (tarea de un solo uso, sin valor de persistir).

## Consolidación sugerida

Con 14 locations activas, la memoria episódica puede crecer rápido si no se agrupa por location. Considera que la consolidación resuma por location + categoría (horarios, proveedores, incidentes conocidos) en vez de guardar cada corrección como una entrada suelta — esto es una decisión de diseño que debes justificar tú, no un requisito fijo.

## Restricciones de la empresa

Brasaland opera en dos monedas (COP/USD) y dos idiomas. Si tu agente soporta bilingüe, la propuesta de memoria y la confirmación del usuario deben funcionar en el idioma base elegido — no asumas que el usuario siempre corrige en español.
