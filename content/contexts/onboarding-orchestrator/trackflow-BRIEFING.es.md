# BRIEFING.md — TrackFlow

## Agentic Engineering – Agente de incorporaciones

_These instructions are [available in English](./trackflow-BRIEFING.en.md)._

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**TrackFlow** es una empresa de entrega de última milla y gestión de almacenes fundada en 2009 en Los Ángeles, Estados Unidos. Opera en dos mercados, Estados Unidos y España, con almacenes en Los Ángeles y Zaragoza. Emplea a unas 130 personas y factura alrededor de 9 millones de euros al año. Sus clientes son marcas de e-commerce de moda, electrónica y cosmética que le confían toda su operación logística: almacenamiento, preparación de pedidos, envío a través de una red de 8 transportistas y gestión de devoluciones.

---

## Tu departamento y el problema que debes resolver

Formas parte de **TrackFlow Tech**, la unidad interna creada para liderar la transformación digital de la empresa, y reportas al CTO Andrés Kim.

El equipo corporativo de TrackFlow crece en los dos países: nuevas personas en Tecnología, Comercial, Experiencia del Cliente, Logística Inversa y en la gestión de operaciones. Hoy cada incorporación recibe un PDF de bienvenida distinto según el país y una explicación del negocio que depende de quién se la dé. Un desarrollador nuevo en Zaragoza puede pasar semanas sin saber qué ocurre físicamente con un pedido desde que entra en el almacén hasta que llega al cliente, y un account manager nuevo en Los Ángeles puede no saber que las devoluciones son hasta una cuarta parte del volumen. Además, los accesos a sistemas tardan días porque dependen de que alguien se acuerde de pedirlos.

Rafael Sanz, Head of People, necesita un orquestador que lleve a cada nueva incorporación corporativa por el mismo recorrido, en los dos países.

---

## Tu stakeholder

**Rafael Sanz**, Head of People (Zaragoza)

> Hola equipo:
>
> Os paso los requisitos del nuevo onboarding corporativo. Los he dejado también en Notion con el detalle de cada etapa.
>
> **Objetivo:** que cualquier persona que se incorpore al equipo corporativo, en Los Ángeles o en Zaragoza, entienda cómo funciona TrackFlow de punta a punta antes de empezar a tomar decisiones sobre él.
>
> **Etapas de contenido:** la empresa, cómo operamos, su función, cómo trabajamos y nuestros lineamientos. Cada una termina con una comprobación. Sin superarla, no se avanza.
>
> **Visita al almacén:** toda incorporación pasa media jornada en el almacén de su país. Lo confirma el jefe de almacén. Es la etapa que más valoran después y la que más se olvida programar.
>
> **Aprobaciones:** el responsable directo aprueba la etapa de función. Yo apruebo el cierre.
>
> **Dudas:** se responden con la documentación oficial y citando de dónde sale la respuesta. Si no está documentado, me llega a mí. Prefiero una pregunta sin responder a una respuesta inventada.
>
> **Contrato:** cada país tiene su marco laboral. El sistema debe saber qué documentación corresponde a cada uno y si ya se ha recibido, pero el contenido de esos documentos no debe salir de mi equipo.
>
> **Plazo objetivo:** 10 días hábiles.
>
> Gracias,
> Rafael

---

## Alcance de idioma

- El soporte multilingüe es **opcional pero muy recomendable**, porque TrackFlow incorpora personas en Estados Unidos y en España.
- Elige un **idioma base** para todo el flujo (contenido, comprobaciones, mensajes del agente).
- Si implementas un segundo idioma, el material oficial y las comprobaciones deben existir también en ese idioma. El agente nunca traduce sobre la marcha un contenido oficial que no existe.

---

## A quién se incorpora

Solo **personal corporativo** de TrackFlow: Tecnología, Comercial y Relación con Clientes, Experiencia del Cliente, Logística Inversa, Personas y la gestión de Operaciones (jefes de turno, coordinadores, analistas). No incluye a los operarios de almacén.

Cada incorporación tiene: nombre, puesto, departamento, país (Estados Unidos o España), responsable directo y fecha de inicio.

---

## Etapas del onboarding

| #   | Etapa                 | Contenido                                                                                                                                                                           | Condición de salida                                            | Plazo  | Aprueba             |
| --- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------ | ------------------- |
| 1   | Bienvenida y trámites | Recepción del contrato firmado y la documentación laboral que corresponda al país                                                                                                   | Personas marca la documentación como recibida                  | Día 2  | Equipo de Personas  |
| 2   | La empresa            | Historia desde 2009, propuesta de valor para las marcas, tipología de clientes, los dos mercados                                                                                    | Comprobación superada                                          | Día 3  | Automática          |
| 3   | Cómo operamos         | Ciclo de vida de un pedido: entrada en almacén → picking → asignación de transportista → entrega → devolución. Los dos almacenes, los 8 transportistas, el peso de las devoluciones | Comprobación superada                                          | Día 5  | Automática          |
| 4   | Visita al almacén     | Media jornada en el almacén de su país                                                                                                                                              | El jefe de almacén confirma la visita                          | Día 6  | Jefe de almacén     |
| 5   | Tu función            | Responsabilidades del puesto, objetivos de los primeros 90 días, con quién trabaja                                                                                                  | Comprobación superada **y** aprobación del responsable directo | Día 8  | Responsable directo |
| 6   | Cómo trabajamos       | Herramientas (Slack, Notion, Linear/Jira, Google Workspace), trabajo entre dos husos horarios con 9 horas de diferencia, especificaciones técnicas y tickets                        | Comprobación superada                                          | Día 9  | Automática          |
| 7   | Lineamientos          | Confidencialidad de los datos de las marcas cliente, protección de datos de consumidores finales, seguridad de la información, código de conducta                                   | Comprobación superada                                          | Día 9  | Automática          |
| 8   | Accesos y cierre      | Confirmación de accesos activos y cierre del onboarding                                                                                                                             | Rafael aprueba el cierre                                       | Día 10 | Rafael Sanz         |

La etapa 4 no puede empezar antes de superar la etapa 3.

---

## Documentación laboral por país

| País           | Documentación requerida                                                               |
| -------------- | ------------------------------------------------------------------------------------- |
| Estados Unidos | Contrato firmado, formulario fiscal de empleado, verificación de elegibilidad laboral |
| España         | Contrato firmado, datos de afiliación a la Seguridad Social, modelo de retenciones    |

El sistema registra solo si cada documento está **pendiente** o **recibido**.

---

## Material oficial que debes preparar

Crea, a partir del briefing general de TrackFlow, un documento oficial por cada etapa de contenido (2, 3, 5, 6 y 7). Para la etapa 5, prepara al menos dos variantes de puesto (por ejemplo, desarrollador de TrackFlow Tech y account manager). Estos documentos son la única fuente que el agente puede usar.

---

## Comprobaciones de comprensión

- Entre 4 y 6 preguntas por etapa de contenido, basadas solo en el material oficial.
- Umbral de superación: 80%.
- Si no se supera, el agente presenta de nuevo los puntos fallados y repite la comprobación con preguntas distintas.
- Tras dos intentos fallidos, el agente notifica al responsable directo.

---

## Aprobaciones y escalado

- **Recordatorio** a la persona incorporada 24 horas antes del plazo de cada etapa.
- **Escalado** al responsable directo cuando una etapa supera su plazo.
- **Escalado** a Rafael cuando una incorporación acumula más de 3 días de retraso total.
- Los recordatorios y escalados se envían en el horario laboral del país del destinatario, no del servidor.
- Si el responsable directo **rechaza** la etapa 5, el flujo vuelve al inicio de esa etapa con un comentario visible para la persona incorporada.

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes del agente ni respuestas de la API:

- Número de documento de identidad o fiscal (SSN, DNI, NIE, pasaporte)
- Número de afiliación a la Seguridad Social
- Datos bancarios para nómina
- Salario y condiciones económicas del contrato
- Resultado de la verificación de elegibilidad laboral (solo se registra si está completada)

---

## Datos semilla

Crea al menos:

- 3 incorporaciones de prueba con datos ficticios: una en Estados Unidos, una en España y una tercera bloqueada en la etapa 4 con su plazo vencido (para probar el escalado)
- 2 responsables directos de departamentos distintos
- 2 jefes de almacén, uno por país, con permiso para confirmar la visita
- Los 5 documentos oficiales de contenido

---

## Restricción específica

La visita al almacén solo puede confirmarla el jefe de almacén **del país de la persona incorporada**. Una confirmación del jefe del otro almacén debe rechazarse.
