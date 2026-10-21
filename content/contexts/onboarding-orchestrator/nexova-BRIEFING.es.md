# BRIEFING.md — Nexova

## Agentic Engineering – Agente de incorporaciones

_These instructions are [available in English](./nexova-BRIEFING.en.md)._

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**Nexova** es una consultora de recursos humanos y captación de talento fundada en 2011, con sede en Valencia (España) y una oficina de expansión en Miami (Florida). Tiene 120 empleados y opera tres líneas de negocio: headhunting de perfiles directivos y de mandos intermedios, externalización de equipos de soporte al cliente para empresas tecnológicas, y formación corporativa en habilidades interpersonales y liderazgo. Factura alrededor de 8 millones de dólares al año. Sus clientes son principalmente empresas medianas de tecnología, retail y servicios financieros.

---

## Tu departamento y el problema que debes resolver

Formas parte del equipo de AI Engineering que la CEO Laura Mendoza ha creado para convertir la IA en una ventaja competitiva de Nexova, y reportas al CTO Sergio Molina.

Nexova incorpora personas con frecuencia: consultores de selección, SDRs, agentes de soporte, formadores y perfiles internos. Hoy, Patricia Solís envía a cada persona un PDF con instrucciones y hace el seguimiento por Slack, mensaje a mensaje. Las nuevas incorporaciones tardan semanas en entender cómo se relacionan las tres líneas de negocio, cómo es un proceso de selección de principio a fin o por qué los datos de un candidato no se comparten fuera de Selección. Y el acuerdo de confidencialidad, que es imprescindible en un negocio que maneja perfiles de candidatos y datos de clientes, a veces se firma después de que la persona ya tiene acceso al ATS.

Patricia necesita un orquestador que convierta ese PDF y esos mensajes en un recorrido completo, verificable y en el orden correcto.

---

## Tu stakeholder

**Patricia Solís**, HR Manager (Valencia)

> Hola:
>
> Te resumo lo que necesito para el onboarding, porque llevo años haciéndolo a mano y sé exactamente dónde falla.
>
> 1. Toda persona que entra en Nexova tiene que entender las tres líneas de negocio, no solo la suya. Un consultor de selección que no sabe qué hace Formación pierde oportunidades de venta cruzada todos los días.
> 2. Cinco bloques de contenido: la empresa, cómo operamos, su función, cómo trabajamos y nuestros lineamientos. Cada uno con una comprobación al final. Si no la pasa, repasa.
> 3. Lo más importante: **nadie recibe acceso al ATS, a HubSpot ni al helpdesk hasta haber firmado el acuerdo de confidencialidad y haber superado el bloque de lineamientos.** Esto no es negociable. Ya hemos tenido sustos.
> 4. El responsable directo aprueba el bloque de función. Yo apruebo el cierre.
> 5. Si preguntan algo que no está en nuestra documentación, no quiero que el sistema se lo invente. Que me llegue a mí.
>
> Plazo objetivo: 8 días hábiles.
>
> Patricia

---

## Alcance de idioma

- El soporte multilingüe es **opcional pero muy recomendable**, porque Nexova incorpora personas en Valencia y en Miami.
- Elige un **idioma base** para todo el flujo (contenido, comprobaciones, mensajes del agente).
- Si implementas un segundo idioma, el material oficial y las comprobaciones deben existir también en ese idioma. El agente nunca traduce sobre la marcha un contenido oficial que no existe.

---

## A quién se incorpora

Cualquier nueva incorporación a la plantilla de Nexova, en Valencia o en Miami, en cualquiera de sus departamentos: Selección de Talento, Ventas, Soporte al Cliente, Formación Corporativa, Marketing, RR. HH. interno o Tecnología.

Cada incorporación tiene: nombre, puesto, departamento, oficina (Valencia o Miami), responsable directo y fecha de inicio.

---

## Etapas del onboarding

| #   | Etapa                       | Contenido                                                                                                                                                                                               | Condición de salida                                            | Plazo | Aprueba             |
| --- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----- | ------------------- |
| 1   | Bienvenida y trámites       | Recepción del contrato firmado y la documentación de nómina                                                                                                                                             | RR. HH. marca la documentación como recibida                   | Día 1 | Equipo de RR. HH.   |
| 2   | Acuerdo de confidencialidad | Firma del acuerdo de confidencialidad sobre datos de candidatos y clientes                                                                                                                              | RR. HH. marca el acuerdo como firmado                          | Día 2 | Equipo de RR. HH.   |
| 3   | La empresa                  | Historia, las tres líneas de negocio, tipología de clientes, la apuesta por la IA, Valencia y Miami                                                                                                     | Comprobación superada                                          | Día 3 | Automática          |
| 4   | Cómo operamos               | Un proceso de selección de principio a fin (briefing → búsqueda → shortlist → entrevistas → contratación), cómo funciona el servicio de soporte externalizado y cómo se vende y se imparte la formación | Comprobación superada                                          | Día 4 | Automática          |
| 5   | Tu función                  | Responsabilidades del puesto, objetivos de los primeros 90 días, con quién trabaja                                                                                                                      | Comprobación superada **y** aprobación del responsable directo | Día 6 | Responsable directo |
| 6   | Cómo trabajamos             | Herramientas (HubSpot, ATS, helpdesk, Slack, Google Workspace) según departamento, buenas prácticas de registro en el CRM                                                                               | Comprobación superada                                          | Día 7 | Automática          |
| 7   | Lineamientos                | Confidencialidad de candidatos y clientes, RGPD, exclusividad de candidatos entre procesos, código de conducta                                                                                          | Comprobación superada                                          | Día 7 | Automática          |
| 8   | Accesos y cierre            | Solicitud de accesos a los sistemas del departamento y cierre del onboarding                                                                                                                            | Patricia aprueba el cierre                                     | Día 8 | Patricia Solís      |

Las solicitudes de acceso de la etapa 8 **solo** se pueden emitir cuando las etapas 2 y 7 están completadas.

---

## Material oficial que debes preparar

Crea, a partir del briefing general de Nexova, un documento oficial por cada etapa de contenido (3, 4, 5, 6 y 7). Para la etapa 5, prepara al menos dos variantes de puesto (por ejemplo, consultor de selección y SDR). Para la etapa 6, el contenido debe cambiar según el departamento de la persona. Estos documentos son la única fuente que el agente puede usar.

---

## Comprobaciones de comprensión

- Entre 4 y 6 preguntas por etapa de contenido, basadas solo en el material oficial.
- Umbral de superación: 80%. En la etapa 7 (lineamientos) el umbral es del **100%**: la confidencialidad no admite aproximaciones.
- Si no se supera, el agente presenta de nuevo los puntos fallados y repite la comprobación con preguntas distintas.
- Tras dos intentos fallidos, el agente notifica al responsable directo.

---

## Aprobaciones y escalado

- **Recordatorio** a la persona incorporada 24 horas antes del plazo de cada etapa.
- **Escalado** al responsable directo cuando una etapa supera su plazo.
- **Escalado** a Patricia cuando la etapa 2 (confidencialidad) supera su plazo, por ser bloqueante para los accesos.
- Si el responsable directo **rechaza** la etapa 5, el flujo vuelve al inicio de esa etapa con un comentario visible para la persona incorporada.

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes del agente ni respuestas de la API:

- Número de documento de identidad (DNI, NIE, SSN, pasaporte)
- Datos bancarios para nómina
- Salario y condiciones económicas del contrato

El agente trabaja solo con el **estado** de cada trámite ("acuerdo firmado", "documentación pendiente"), nunca con su contenido.

---

## Datos semilla

Crea al menos:

- 3 incorporaciones de prueba con datos ficticios: una en Valencia, una en Miami y una tercera bloqueada en la etapa 2 con su plazo vencido (para probar el escalado a Patricia)
- 2 responsables directos de departamentos distintos
- Los 5 documentos oficiales de contenido

---

## Restricción específica

Ningún acceso a sistemas con datos de candidatos o clientes (ATS, HubSpot, helpdesk) puede solicitarse antes de que la confidencialidad esté firmada y los lineamientos superados. Si se intenta, el sistema debe rechazarlo y mostrar qué falta.
