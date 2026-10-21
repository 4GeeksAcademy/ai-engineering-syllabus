# BRIEFING.md — Brasaland

## Agentic Engineering – Agente de incorporaciones

_These instructions are [available in English](./brasaland-BRIEFING.en.md)._

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**Brasaland** es una cadena de restaurantes de comida a la brasa fundada en 2008 en Medellín, Colombia. Lo que empezó como un único local familiar es hoy una cadena de 14 restaurantes propios en Colombia y Estados Unidos (Florida). La empresa emplea a unas 115 personas entre el personal de cocina y sala, la gestión de operaciones y el equipo corporativo, con sede en Medellín y una oficina comercial en Miami. Factura alrededor de 6 millones de dólares al año. La marca se sostiene sobre tres pilares: calidad de producto consistente en todos los locales, una experiencia de cliente cálida y fiable, y rapidez de servicio.

---

## Tu departamento y el problema que debes resolver

Trabajas en **Brasaland Digital**, el equipo interno creado por la CEO Mariana Restrepo para liderar la transformación digital de la empresa, y reportas al CTO Nicolás Park.

El equipo corporativo de Brasaland está creciendo: nuevas personas en Brasaland Digital, Marketing, Compras, Operaciones y Personas, tanto en Medellín como en Miami. Cada incorporación recibe un PDF de bienvenida, una llamada con su responsable y acceso a una carpeta de Google Drive que nadie consigue navegar. Los nuevos perfiles corporativos tardan semanas en entender cómo funciona un restaurante de Brasaland por dentro, por qué la empresa opera con dos monedas o qué significa "consistencia" para la marca. Y los trámites (contrato, documentación, accesos) dependen de que Ashley se acuerde de perseguir a cada persona.

Ashley Turner, People Manager, necesita un orquestador que conduzca a cada nueva incorporación corporativa por un recorrido completo y verificable.

---

## Tu stakeholder

**Ashley Turner**, People Manager (Miami)

> Hola equipo:
>
> Retomo nuestra conversación sobre el onboarding corporativo. Esto es lo que necesito, por orden de prioridad:
>
> 1. Toda nueva incorporación corporativa, en Medellín o en Miami, debe pasar por las mismas cinco etapas de contenido: la empresa, cómo operan nuestros restaurantes, su función, cómo trabajamos y nuestros lineamientos. Sin saltos ni atajos.
> 2. Cada etapa de contenido debe terminar con una comprobación breve. Si no la supera, vuelve a revisar el material. No quiero un "ya lo leí": quiero evidencia de que lo entendió.
> 3. Toda nueva incorporación debe pasar un día de acompañamiento en un restaurante antes de terminar el onboarding. Quien nunca ha visto una cocina en hora punta toma malas decisiones sobre ella. El equipo de Felipe debe confirmar que la jornada se realizó.
> 4. El responsable directo aprueba la etapa de la función, y yo apruebo el cierre final. Nadie más.
> 5. Las dudas se responden solo con nuestros documentos oficiales. Si la respuesta no está ahí, que la pregunta me llegue a mí.
> 6. El contrato y los documentos de nómina los gestiona mi equipo. El sistema debe saber si se han recibido, pero no quiero números de identidad ni datos bancarios circulando en registros de chat. Es un riesgo legal en los dos países.
>
> Objetivo: onboarding completo en 10 días hábiles.
>
> Gracias,
> Ashley

---

## Alcance de idioma

- El soporte multilingüe es **opcional pero muy recomendable**, porque Brasaland incorpora personas en Colombia y en Estados Unidos.
- Elige un **idioma base** para todo el flujo (contenido, comprobaciones, mensajes del agente).
- Si implementas un segundo idioma, trátalo como una mejora: el material oficial debe existir en ese idioma y las comprobaciones también. El agente nunca traduce sobre la marcha un contenido oficial que no existe.

---

## A quién se incorpora

Solo **personal corporativo** de Brasaland: Brasaland Digital, Marketing, Compras, Operaciones (supervisores y equipo central, no personal de sala ni cocina), Personas y Formación. Sede en Medellín o en Miami.

Cada incorporación tiene: nombre, puesto, departamento, sede (Medellín o Miami), responsable directo y fecha de inicio.

---

## Etapas del onboarding

| #   | Etapa                     | Contenido                                                                                                                                          | Condición de salida                                            | Plazo  | Aprueba                   |
| --- | ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------ | ------------------------- |
| 1   | Bienvenida y trámites     | Recepción de contrato firmado y documentación de nómina                                                                                            | Personas marca la documentación como recibida                  | Día 2  | Equipo de Personas        |
| 2   | La empresa                | Historia desde 2008, los tres pilares de marca, los 14 locales, los dos mercados                                                                   | Comprobación superada                                          | Día 3  | Automática                |
| 3   | Cómo opera un restaurante | Turnos, cubiertos, ticket medio, pedidos de ingredientes, control de mermas, operación con COP y USD                                               | Comprobación superada                                          | Día 5  | Automática                |
| 4   | Jornada de acompañamiento | Un día completo en un restaurante de su ciudad                                                                                                     | Un supervisor de Operaciones confirma la jornada               | Día 7  | Supervisor de Operaciones |
| 5   | Tu función                | Responsabilidades del puesto, objetivos de los primeros 90 días, con quién trabaja                                                                 | Comprobación superada **y** aprobación del responsable directo | Día 8  | Responsable directo       |
| 6   | Cómo trabajamos           | Herramientas (Slack, Notion, Google Workspace, backoffice), especificaciones en Notion con criterios de aceptación, trabajo entre Medellín y Miami | Comprobación superada                                          | Día 9  | Automática                |
| 7   | Lineamientos              | Guía de marca, política de protección de datos, código de conducta, diferencias laborales entre Colombia y EE. UU.                                 | Comprobación superada                                          | Día 9  | Automática                |
| 8   | Accesos y cierre          | Confirmación de accesos activos y cierre del onboarding                                                                                            | Ashley aprueba el cierre                                       | Día 10 | Ashley Turner             |

La etapa 4 no puede empezar antes de superar la etapa 3.

---

## Material oficial que debes preparar

Crea, a partir del briefing general de Brasaland, un documento oficial por cada etapa de contenido (2, 3, 5, 6 y 7). Para la etapa 5, prepara al menos dos variantes de puesto (por ejemplo, analista de Brasaland Digital y coordinador de Marketing). Estos documentos son la única fuente que el agente puede usar para presentar contenido y responder dudas.

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
- **Escalado** a Ashley cuando una incorporación acumula más de 3 días de retraso total.
- Si el responsable directo **rechaza** la etapa 5, el flujo vuelve al inicio de esa etapa con un comentario visible para la persona incorporada.

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes del agente ni respuestas de la API:

- Número de documento de identidad (cédula, SSN, pasaporte)
- Datos bancarios para nómina
- Salario y condiciones económicas del contrato

El agente trabaja solo con el **estado** de cada trámite ("contrato recibido", "documentación de nómina pendiente"), nunca con su contenido.

---

## Datos semilla

Crea al menos:

- 3 incorporaciones de prueba con datos ficticios: una en Medellín, una en Miami y una tercera bloqueada en la etapa 4 con su plazo vencido (para probar el escalado)
- 2 responsables directos de departamentos distintos
- 1 supervisor de Operaciones con permiso para confirmar la jornada de acompañamiento
- Los 5 documentos oficiales de contenido

---

## Restricción específica

El orquestador es para **personal corporativo**. Si se intenta iniciar un onboarding para un puesto de sala o cocina, el sistema debe rechazarlo con el mensaje: "Este flujo es para incorporaciones al equipo corporativo. Las incorporaciones de restaurante se gestionan con su responsable de local."
