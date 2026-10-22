# Puesta en marcha del monorepo – Banco de memoria y contexto del proyecto

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

![build by developers](https://img.shields.io/badge/build_by-Developers-blue)
![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: lee el **[BRIEFING de tu empresa y su carpeta de documentos](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts)** (`<empresa>-BRIEFING.md` y `<empresa>/`) antes de abrir el agente — es la fuente de la visión, los departamentos, los stakeholders y las restricciones de negocio de tu implementación.

<!-- endhide -->

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Tu empresa acaba de abrir su unidad digital y el monorepo está, a propósito, casi vacío: carpetas con una responsabilidad asignada, ningún stack elegido y un `CONTEXT.md` en la raíz que todavía es un marcador de posición. Antes de que nadie escriba la primera funcionalidad, tu CTO ha abierto un ticket con un objetivo claro: que cualquier agente de código que trabaje en este repositorio entienda **qué** se construye, **para quién** y **bajo qué reglas**, sin que nadie tenga que volver a explicárselo en cada sesión.

La materia prima ya existe: el BRIEFING de la empresa y los documentos de sus departamentos. Pero un banco de memoria no es una copia de esos documentos. Volcarlos enteros en el contexto llena al agente de tokens sin decidir nada. Eso no significa que todo deba resumirse: hay documentos que valen por sí mismos — un proceso descrito paso a paso, una política con sus plazos y excepciones — y procesarlos solo les haría perder detalle. Esos documentos se incorporan como documentación de referencia en la carpeta `docs/` del monorepo y el contexto apunta a ellos en lugar de reescribirlos. **Decidir qué se sintetiza y qué se conserva íntegro es tu responsabilidad como desarrollador**; cuando tengas dudas, consúltalo con tu equipo o con tu CTO, como harías en cualquier empresa. Para el resto, el trabajo consiste en **conversar con el agente** sobre ese material — en modo conversacional o de planificación, no en modo agente — para que te pregunte lo que no está claro, para que tú decidas y para que lo que quede escrito sea una síntesis curada: visión, usuarios, criterios de aceptación y una definición de terminado. **Cada fichero del banco de memoria debe citar el documento de origen del que sale o enlazar al documento de `docs/` en el que se apoya**, de modo que cualquiera pueda verificarlo.

Hay una segunda trampa: rellenar huecos. Hoy no existe stack, ni comandos de build, ni convenciones de código. Un agente sin esa información no se detiene: inventa. Por eso lo que todavía no está decidido **se deja escrito como pendiente, con el evento que obligará a definirlo**, en lugar de completarse con suposiciones. Y la prueba final no es que los ficheros existan, sino que **una sesión nueva del agente, sin historial, sepa orientarse leyendo solo el repositorio**.

> **De:** tu CTO
> **Asunto:** ticket — contexto base del monorepo antes de la primera funcionalidad
>
> Antes de abrir el primer PRD de producto, quiero que el repositorio tenga memoria propia. No quiero un volcado del BRIEFING; quiero lo que tú y el agente hayáis destilado de él después de discutirlo. Si algún documento de un departamento describe un proceso que no admite resumen sin perder información, llévalo a `docs/` tal cual y referéncialo desde el contexto. Esa decisión es tuya; si dudas, pregunta antes de inventar.
>
> Sobre el stack, seamos claros: **hoy no hay ninguna tecnología decidida y no la vas a decidir en este ticket.** El documento de stack nace vacío y crece con el proyecto: cada vez que entre una tecnología nueva, se registra ahí. Lo que sí quiero desde hoy es la política de entrada. Solo fuentes oficiales y verificadas por una persona, librerías conocidas y mantenidas, versiones exactas fijadas — nada de `latest` ni rangos abiertos — y APIs en su versión vigente comprobada en la documentación oficial, no en lo que el agente recuerde de su entrenamiento.
>
> Hay otras piezas que todo proyecto serio necesita y que todavía no podemos rellenar: límites de arquitectura y patrones, convenciones de código y guía de estilo, comandos de build, test y ejecución, antipatrones y tabúes explícitos, y reglas de entorno y acceso. Quiero que existan desde ya como sitio reservado. Lo que ya se pueda afirmar — por ejemplo, qué responsabilidad tiene cada carpeta del monorepo o qué restricciones de negocio no se negocian — se escribe. Lo que no, se marca como pendiente. Nadie las inventa para que el documento parezca completo.
>
> Los criterios de aceptación son los del checklist. El sign-off lo doy sobre el Pull Request, después de abrir yo mismo una sesión limpia del agente y hacerle preguntas sobre la empresa. Si tengo que explicarle algo, el ticket vuelve.

### Conocimiento complementario: anatomía de un contexto de proyecto

Un **banco de memoria** es un conjunto de documentos versionados en el repositorio que persisten el conocimiento del proyecto más allá del chat actual. Sus piezas habituales son: **visión y criterios de aceptación** (qué problema resuelve el producto, historias de usuario y definición de terminado, en un formato que pueda convertirse en issues o en un PRD), **stack tecnológico**, **límites de arquitectura**, **convenciones de código**, **comandos**, **tabúes** y **reglas de entorno y acceso**, más un registro del **estado actual**.

El banco de memoria no sustituye a la documentación: la **memoria** resume lo que el agente necesita para orientarse y decidir; la **documentación** en `docs/` conserva el detalle completo de procesos, políticas o procedimientos. La memoria enlaza a la documentación para que el agente la lea solo cuando la tarea lo requiera.

El fichero `CONTEXT.md` en la raíz del monorepo es el punto de entrada al contexto y el índice de todos los documentos que el agente necesita para trabajar: los de `memory-bank/` y los de `docs/`. Es corto, contiene solo lo imprescindible y, para cada documento, indica cuándo leerlo, de modo que el agente cargue únicamente lo que necesita en cada tarea. Varios ficheros pequeños y enfocados cuestan menos tokens y producen menos ambigüedad que un documento único con todo dentro.

> 🔀 **PR aprobado → haz merge a `main`.** Todo el trabajo posterior en el monorepo partirá de este contexto.

---

## 🌱 Cómo empezar el proyecto

1. Trabaja sobre tu copia del monorepo de la empresa. Crea la rama `feature/memory-bank`.
2. Abre el BRIEFING de tu empresa y los documentos de su carpeta. Léelos tú antes de dárselos al agente.
3. Sigue el patrón pensar → conversar → implementar: discute el material con el agente en modo conversacional o de planificación y pásalo a modo agente solo cuando sepas qué se va a escribir.
4. Haz un commit separado por cada documento o decisión relevante. El historial es parte de la entrega.

---

## 💻 Qué debes hacer

### Conversación de descubrimiento

- [ ] Pide al agente que lea el BRIEFING y los documentos de tu empresa y que te haga preguntas sobre lo que sea ambiguo o falte, antes de proponer ningún contenido.
- [ ] Responde, decide y conserva las preguntas del agente que cambiaron lo que acabó escrito en el banco de memoria.
- [ ] Revisa cada propuesta del agente contra los documentos de origen antes de aceptarla.
- [ ] Clasifica cada documento de origen: se sintetiza en el banco de memoria o se incorpora íntegro a `docs/` como documentación de referencia. Consulta a tu equipo o a tu CTO cuando la decisión no esté clara.

### Banco de memoria

- [ ] Crea la carpeta `memory-bank/` con un fichero por preocupación, no un documento único.
- [ ] Escribe la **visión del producto**: qué problema resuelve la plataforma digital de la empresa, para quién y qué no es objetivo.
- [ ] Escribe al menos cinco **historias de usuario** que cubran al menos tres departamentos distintos, cada una con su stakeholder, sus criterios de aceptación verificables y redactada de forma que pueda convertirse directamente en un issue de GitHub.
- [ ] Define una **definición de terminado** común al proyecto.
- [ ] Crea el documento de **stack tecnológico** sin ninguna tecnología registrada, con la política de entrada del CTO (fuentes verificadas, librerías conocidas, versiones exactas, APIs vigentes) y una plantilla de registro para cada tecnología futura: nombre, versión exacta, fuente oficial, fecha de verificación y motivo de la elección.
- [ ] Crea los documentos de **límites de arquitectura y patrones**, **convenciones de código y estilo**, **comandos de build, test y ejecución**, **antipatrones y tabúes explícitos** y **reglas de entorno y acceso**. En cada uno, escribe lo que ya se puede afirmar y marca lo demás como pendiente indicando qué evento obligará a definirlo.
- [ ] Crea un documento de **estado actual** que refleje en qué punto está el proyecto al cerrar el ticket.
- [ ] Indica en cada documento la fuente de la que procede su contenido (documento de la empresa, README del monorepo o decisión tomada en la conversación).
- [ ] Incorpora a `docs/` los documentos que hayas decidido conservar íntegros, organizados por tema, y enlázalos desde el fichero del banco de memoria que los necesite, indicando cuándo debe consultarlos el agente.

⚠️ **IMPORTANTE:** la visión, los stakeholders, los departamentos y las restricciones de negocio deben corresponderse con el BRIEFING de tu empresa asignada. Un banco de memoria genérico, que serviría igual para cualquier empresa, o que vuelque los documentos de origen sin haber decidido qué se sintetiza y qué se referencia desde `docs/`, no será aceptado.

### Punto de entrada al contexto

- [ ] Sustituye el marcador de posición de `CONTEXT.md` en la raíz del monorepo. No pegues en él el BRIEFING: debe ser breve, con la descripción de la empresa en pocas líneas.
- [ ] Convierte `CONTEXT.md` en el índice de todos los documentos necesarios para el agente: cada fichero de `memory-bank/` y cada documento de `docs/`, con una línea que indique cuándo debe leerse.
- [ ] Incluye en `CONTEXT.md` la instrucción de actualizar el índice y el banco de memoria cuando entre una tecnología, se añada documentación, se tome una decisión de arquitectura o cambie el estado del proyecto.

### Verificación

- [ ] Abre una sesión nueva del agente, sin historial, indícale que empiece por `CONTEXT.md` y hazle al menos tres preguntas sobre la empresa, sus usuarios y el stack. Comprueba que responde a partir del repositorio y no inventa.
- [ ] Pídele en esa misma sesión que proponga una librería para cualquier necesidad futura y comprueba que aplica la política de stack (versión exacta y fuente oficial) en lugar de añadirla sin más.
- [ ] Corrige el banco de memoria donde la sesión limpia haya fallado y vuelve a probar.

---

## ✅ Qué evaluaremos

- [ ] `CONTEXT.md` ya no es el marcador de posición, no reproduce el BRIEFING y enlaza a cada fichero de `memory-bank/` y de `docs/` indicando cuándo leerlo.
- [ ] `memory-bank/` contiene ficheros separados para visión y criterios de aceptación, stack, arquitectura, convenciones, comandos, tabúes, entorno y acceso, y estado actual.
- [ ] La visión y las historias de usuario reflejan la empresa asignada y citan su documento de origen.
- [ ] Hay al menos cinco historias de usuario de al menos tres departamentos, cada una con stakeholder y criterios de aceptación verificables.
- [ ] Existe una definición de terminado explícita.
- [ ] El documento de stack no registra ninguna tecnología y contiene la política de entrada y la plantilla de registro con versión exacta y fuente oficial.
- [ ] Los documentos sin información disponible marcan lo pendiente y su disparador; no contienen comandos, librerías ni convenciones inventadas.
- [ ] Los límites de arquitectura recogen la responsabilidad de las carpetas del monorepo.
- [ ] Ningún fichero de `memory-bank/` es una copia literal de los documentos de la empresa; los documentos conservados íntegros están en `docs/` y se enlazan desde el banco de memoria.
- [ ] El Pull Request documenta la prueba con una sesión limpia: preguntas, respuestas y correcciones aplicadas.
- [ ] El historial de commits separa los documentos y decisiones; no existe un commit único con todo el trabajo.

---

## 📦 Cómo entregar

Sube tu rama `feature/memory-bank` a tu copia del monorepo y abre un Pull Request contra la rama principal.

En la descripción del Pull Request incluye:

- Tres preguntas que te hizo el agente durante la conversación y qué cambiaron en el banco de memoria.
- Las preguntas de la prueba con la sesión limpia, un resumen de sus respuestas y lo que corregiste después.
- Qué documentos sintetizaste y cuáles incorporaste a `docs/`, con el motivo de cada decisión y las consultas que hiciste cuando tuviste dudas.
- La lista de elementos que quedaron como pendientes y el evento que los desbloqueará.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
