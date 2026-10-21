# BRIEFING.md — HealthCore

## Agentic Engineering – Agente de incorporaciones

_These instructions are [available in English](./healthcore-BRIEFING.en.md)._

> Este documento describe tu empresa y la situación concreta para la que construyes este proyecto. Léelo completo antes de escribir una sola línea de código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**HealthCore** es una empresa de servicios de salud ambulatoria fundada en 2011 en Austin, Texas. Opera una red de 12 clínicas: 9 en Estados Unidos (Texas, Florida y Georgia) y 3 en Reino Unido (Londres y Mánchester), con atención primaria, consultas de especialidad, gestión de enfermedades crónicas y programas de salud preventiva. Emplea a unas 200 personas y factura alrededor de 28 millones de dólares al año. Opera bajo dos marcos regulatorios de protección de datos de salud: HIPAA en Estados Unidos y UK GDPR en Reino Unido.

---

## Tu departamento y el problema que debes resolver

Formas parte de **HealthCore Digital**, la unidad interna creada por la CEO, la Dra. Sandra Okonkwo, para construir la infraestructura que necesitan los equipos clínicos y operativos, y reportas al CTO James Osei.

El equipo corporativo de HealthCore crece en Austin y en Londres: nuevas personas en HealthCore Digital, Ciclo de Ingresos, Cumplimiento, Experiencia del Paciente y Personas. El onboarding es inconsistente, y el problema más grave ya lo ha detectado Diane: **hay personas que reciben acceso a sistemas con datos de pacientes antes de haber completado la formación obligatoria de cumplimiento.** En un entorno regulado, eso no es un descuido administrativo, es un riesgo legal. Además, las nuevas incorporaciones no clínicas tardan semanas en entender cómo es el recorrido de un paciente, por qué la tasa de inasistencia importa tanto o qué significa "mínimo necesario" al acceder a un dato.

Diane Foster, VP of People, necesita un orquestador que garantice el orden correcto y que deje evidencia de cada paso.

---

## Tu stakeholder

**Diane Foster**, VP of People (Austin)

> Equipo:
>
> He dejado la especificación completa en Notion. Resumo lo esencial:
>
> 1. **El orden no es opcional.** Ninguna incorporación recibe acceso a un sistema con información de pacientes hasta haber superado la etapa de cumplimiento y que Claire lo haya aprobado. Si el sistema permite saltarse este paso, no nos sirve.
> 2. Cinco bloques de contenido: la empresa, cómo operamos, su función, cómo trabajamos y nuestros lineamientos de cumplimiento. Cada uno con una comprobación.
> 3. La verificación de antecedentes la gestiona un proveedor externo. El sistema solo necesita saber si está **completada**. El resultado no debe entrar en el sistema en ningún caso.
> 4. El responsable directo aprueba la etapa de función. Claire aprueba la de cumplimiento. Yo apruebo el cierre.
> 5. Las dudas se responden con la documentación oficial y citando la política correspondiente. Las dudas sobre cumplimiento que no estén cubiertas van a Claire, no a mí.
>
> Plazo objetivo: 10 días hábiles. Para cumplimiento no hay atajos: si hace falta más tiempo, se toma.
>
> Gracias,
> Diane

---

## Alcance de idioma

- El idioma base es el **inglés**, porque las dos sedes corporativas (Austin y Londres) trabajan en inglés.
- El español es **opcional pero recomendable** para incorporaciones de Florida. Si lo implementas, el material oficial y las comprobaciones deben existir también en español. El agente nunca traduce sobre la marcha un contenido oficial que no existe, y menos aún una política de cumplimiento.

---

## A quién se incorpora

Solo **personal corporativo no clínico** de HealthCore: HealthCore Digital, Ciclo de Ingresos y Facturación, Cumplimiento y Gobernanza de Datos, Experiencia del Paciente (coordinación central), Personas y Dirección. Sede en Austin o en Londres.

No incluye a médicos, enfermería ni personal de atención directa en clínica: su incorporación tiene requisitos de licencia y acreditación que quedan fuera de este proyecto.

Cada incorporación tiene: nombre, puesto, departamento, sede (Austin o Londres), marco regulatorio aplicable (HIPAA o UK GDPR), responsable directo y fecha de inicio.

---

## Etapas del onboarding

| #   | Etapa                 | Contenido                                                                                                                                                                         | Condición de salida                                                             | Plazo  | Aprueba             |
| --- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------ | ------------------- |
| 1   | Bienvenida y trámites | Recepción del contrato firmado, documentación de nómina y confirmación de que la verificación de antecedentes está completada                                                     | Personas marca la documentación como recibida y la verificación como completada | Día 2  | Equipo de Personas  |
| 2   | La empresa            | Historia desde 2011, la red de 12 clínicas, líneas de servicio, propuesta de valor (accesibilidad, citas en el día, atención bilingüe)                                            | Comprobación superada                                                           | Día 3  | Automática          |
| 3   | Cómo operamos         | Recorrido del paciente: reserva → visita → documentación clínica → facturación → seguimiento. Inasistencias, derivaciones y denegaciones de facturación como problemas operativos | Comprobación superada                                                           | Día 4  | Automática          |
| 4   | Cumplimiento          | HIPAA y UK GDPR, principio de "mínimo necesario", notificación de incidentes (72 horas en Reino Unido, 60 días en EE. UU.), registro de accesos                                   | Comprobación superada **y** aprobación de Cumplimiento                          | Día 6  | Claire Whitfield    |
| 5   | Tu función            | Responsabilidades del puesto, objetivos de los primeros 90 días, con quién trabaja                                                                                                | Comprobación superada **y** aprobación del responsable directo                  | Día 8  | Responsable directo |
| 6   | Cómo trabajamos       | Herramientas (Jira, Notion, Slack, Microsoft 365), trabajo entre Austin y Londres, cómo se aprueba un nuevo sistema o integración                                                 | Comprobación superada                                                           | Día 9  | Automática          |
| 7   | Accesos y cierre      | Solicitud de accesos a los sistemas del departamento y cierre del onboarding                                                                                                      | Diane aprueba el cierre                                                         | Día 10 | Diane Foster        |

La etapa 4 debe estar **aprobada** antes de que se pueda emitir cualquier solicitud de acceso a un sistema con información de pacientes.

---

## Material oficial que debes preparar

Crea, a partir del briefing general de HealthCore, un documento oficial por cada etapa de contenido (2, 3, 4, 5 y 6). Para la etapa 4, prepara dos variantes: una para incorporaciones bajo HIPAA y otra bajo UK GDPR. Para la etapa 5, prepara al menos dos variantes de puesto (por ejemplo, ingeniero de HealthCore Digital y analista de Ciclo de Ingresos). Estos documentos son la única fuente que el agente puede usar.

---

## Comprobaciones de comprensión

- Entre 4 y 6 preguntas por etapa de contenido, basadas solo en el material oficial.
- Umbral de superación: 80%. En la etapa 4 (cumplimiento) el umbral es del **100%**.
- Si no se supera, el agente presenta de nuevo los puntos fallados y repite la comprobación con preguntas distintas.
- Tras dos intentos fallidos en la etapa 4, el agente notifica a Claire Whitfield. En el resto de etapas, al responsable directo.

---

## Aprobaciones y escalado

- **Recordatorio** a la persona incorporada 24 horas antes del plazo de cada etapa.
- **Escalado** al responsable directo cuando una etapa supera su plazo.
- La etapa 4 **no escala por plazo**: si se retrasa, se notifica a Diane, pero nunca se ofrece una vía para saltarla.
- Las dudas de cumplimiento no cubiertas por el material se derivan a Claire. El resto de dudas no cubiertas, a Diane.
- Si un aprobador **rechaza** una etapa, el flujo vuelve al inicio de esa etapa con un comentario visible para la persona incorporada.

---

## Datos sensibles

Nunca deben aparecer en logs, prompts almacenados, mensajes del agente ni respuestas de la API:

- Número de documento de identidad o fiscal (SSN, National Insurance Number, pasaporte)
- Datos bancarios para nómina
- Salario y condiciones económicas del contrato
- **Cualquier detalle de la verificación de antecedentes.** Solo se registra que está completada, nunca su resultado ni su contenido

Además, el material de la etapa 3 puede describir el recorrido de un paciente, pero **no puede contener datos de pacientes reales ni realistas**. Usa ejemplos genéricos.

---

## Datos semilla

Crea al menos:

- 3 incorporaciones de prueba con datos ficticios: una en Austin, una en Londres y una tercera que intenta solicitar un acceso sin tener la etapa 4 aprobada (para probar el bloqueo)
- 2 responsables directos de departamentos distintos
- 1 usuaria de Cumplimiento con permiso para aprobar la etapa 4
- Los documentos oficiales de contenido, incluidas las dos variantes de cumplimiento

---

## Restricción específica

Cualquier intento de solicitar acceso a un sistema con información de pacientes antes de que la etapa 4 esté aprobada debe rechazarse, quedar registrado como evento de seguridad y notificarse a Claire Whitfield.
