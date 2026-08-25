# Backoffice de Operaciones – Centralizado de Incidencias

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

![build by developers](https://img.shields.io/badge/build_by-Developers-blue)
![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/incident-manager-for-devs)** antes de escribir una sola línea de código — define los canales de entrada, los tipos de incidencia, los niveles de severidad y las áreas responsables de tu implementación.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

El backoffice de tu empresa todavía no existe como producto: existe como estructura. El monorepo ya trae carpetas, convenciones de nombrado, gestión de dependencias, configuración de linters y una separación de responsabilidades que alguien decidió antes de que tú llegaras. Nadie ha documentado ninguna de esas decisiones. Están en el código y en ningún otro sitio.

Tu CTO ha abierto un ticket para el primer desarrollo real sobre esa base: el **gestor centralizado de incidencias** del backoffice. Hoy las incidencias de la operación llegan por canales distintos, se registran donde cada equipo puede y se pierden entre hilos de correo y mensajes sueltos. Nadie sabe cuántas hay abiertas ahora mismo ni quién responde por cada una. La pieza es deliberadamente acotada, y esa es la intención — el entregable de negocio importa, pero el objetivo del ticket es mayor: dejar el repositorio preparado para que cualquier agente de código que entre después trabaje **dentro** de las reglas del proyecto en lugar de inventarse las suyas.

Ese es el problema real. Un agente sin contexto curado no se queda quieto: rellena los huecos. Elige el gestor de dependencias que le parece, nombra los ficheros como le parece, y produce código plausible que no encaja con el resto del repositorio. Cuanto más código genere sobre esa base equivocada, más caro será revertirlo. Por eso el primer trabajo no es escribir la funcionalidad, sino **leer el código base y convertir lo que ya decide en reglas explícitas**.

Hay una trampa habitual en este ejercicio: pedirle al agente un resumen del proyecto y darlo por bueno. El resumen de un agente sobre un repositorio que no ha explorado es una hipótesis, no un hecho. **Tendrás que contrastar ese resumen contra la estructura y el código reales y registrar dónde se equivocó** — esas discrepancias son la mejor pista de qué necesita quedar escrito.

La segunda trampa es escribir un contexto exclusivamente técnico. Un banco de memoria que explica el stack pero no explica qué hace la empresa, quién usa el backoffice ni qué significa una incidencia grave en esta operación concreta, produce código correcto que resuelve el problema equivocado. Una incidencia crítica no quiere decir lo mismo en todas las empresas, y el agente no puede deducirlo del código. **El contexto de producto y de negocio es parte del entregable, no un adorno.**

> **De:** tu CTO
> **Asunto:** primer desarrollo del backoffice — incidencias
>
> > Antes de que empecemos a meter funcionalidad, necesito que el repositorio deje de depender de la memoria de quien lo montó.
> >
> > Tómate el brief en dos partes. La primera: recorre el código base, entiende las convenciones que ya están tomadas y déjalas escritas como reglas del proyecto. No las cambies porque no te gusten — si crees que alguna está mal, la anotas como propuesta y la discutimos; sobrescribir una convención de equipo por preferencia personal es la forma más rápida de romper un monorepo compartido.
> >
> > La segunda: monta el gestor de incidencias. Los stakeholders de operaciones necesitan registrar una incidencia venga del canal que venga, clasificarla, asignarla a un área responsable y saber en qué estado está. Los tipos, las severidades y los canales salen de tu CONTEXT, no de tu imaginación.
> >
> > Una cosa que no es negociable: cuando una incidencia cambia de estado o de responsable, quiero poder reconstruir después quién la movió y cuándo. Si eso no queda registrado, no hay gestor que valga.
> >
> > Los criterios de aceptación son los del checklist. El sign-off lo doy yo sobre el Pull Request, y voy a leer el historial de commits: si veo un único commit con todo dentro, lo devuelvo sin revisar.
>
> — Handoff al equipo de operaciones en cuanto la funcionalidad esté verificada.

### Conocimiento complementario: qué es un banco de memoria

Un **banco de memoria** es un conjunto de documentos versionados en el propio repositorio que persisten el conocimiento del proyecto más allá de la conversación actual con el agente. Resuelve un problema concreto: cada sesión nueva empieza en cero, y volver a explicar el producto en cada prompt es caro en tokens y frágil en resultados.

Un banco de memoria útil cubre, como mínimo, tres capas: **contexto de producto** (qué es la empresa, a quién sirve, qué problema resuelve esta área), **stack tecnológico** (qué hay montado y con qué se trabaja) y **estado actual** (qué está hecho, qué está en curso, qué decisiones quedaron cerradas). Es contenido curado y concreto: si divaga o repite lo que el agente ya puede leer del código, cuesta tokens sin aportar señal.

Las **reglas** son distintas del banco de memoria: la memoria describe el proyecto, las reglas restringen cómo se trabaja sobre él.

---

## 🌱 Cómo empezar el proyecto

1. Trabaja sobre tu copia del monorepo de la empresa. Crea la rama `feature/incident-manager`.
2. Levanta el entorno siguiendo lo que el propio repositorio indica. Si algo no está documentado y tienes que averiguarlo, ese hallazgo es material para tus reglas.
3. Haz un commit separado por cada paso relevante del checklist. El historial es parte de la entrega.
4. Usa el modo de agente adecuado en cada fase: exploración y resumen en modo conversacional, definición de reglas y plan antes de tocar código, implementación una vez el plan está cerrado.

---

## 💻 Qué debes hacer

### Reconocimiento del código base

- [ ] Explora la estructura del monorepo y pide al agente un resumen del proyecto.
- [ ] Contrasta ese resumen contra la estructura y el código reales.
- [ ] Documenta las discrepancias encontradas entre el resumen del agente y la realidad del repositorio.
- [ ] Identifica al menos tres convenciones ya tomadas en el código (nombrado, organización de carpetas, gestión de dependencias, estilo, separación de responsabilidades).
- [ ] Identifica al menos una práctica que consideres mejorable y regístrala como propuesta, sin aplicarla unilateralmente.

### Reglas del proyecto

- [ ] Crea el directorio `.agents/rules` con las reglas derivadas del código base.
- [ ] Separa las reglas por ámbito: una regla por preocupación, no un documento único con todo dentro.
- [ ] Define para cada regla su forma de aplicación (siempre activa, adjunta por patrón de fichero, solicitada por el agente o invocada manualmente) y justifícala.
- [ ] Escribe las reglas en términos verificables: qué se hace, qué no se hace, con qué patrón de fichero aplica. Evita formulaciones ambiguas.
- [ ] Itera las reglas contra el flujo real de trabajo: si una regla no cambia el comportamiento del agente, o sobra o está mal escrita.

### Banco de memoria

- [ ] Crea el directorio `memory-bank/` con, como mínimo: contexto de producto y negocio, stack tecnológico y estado actual del proyecto.
- [ ] El contexto de producto debe explicar la empresa, quién usa el backoffice y qué significa una incidencia en esta operación — no solo la arquitectura.
- [ ] Incluye un plan de implementación para el gestor de incidencias, construido con el agente antes de escribir código.
- [ ] Mantén el banco de memoria actualizado al cerrar el desarrollo: el estado actual del final del proyecto no puede ser el del principio.

⚠️ **IMPORTANTE:** el contexto de producto, los nombres de entidades y los valores de dominio deben corresponderse con lo especificado en tu CONTEXT.md. Un banco de memoria genérico, que serviría igual para cualquier empresa, no será aceptado.

### Gestor de incidencias en el backoffice

- [ ] Implementa el registro, edición, listado y consulta de incidencias, con los campos definidos en tu CONTEXT.
- [ ] Toda incidencia debe registrar su canal de entrada, su tipo y su nivel de severidad, tomados de los catálogos de tu CONTEXT.
- [ ] Implementa la asignación de una incidencia a un área responsable de las definidas en tu CONTEXT.
- [ ] Implementa el ciclo de estados de la incidencia, desde su apertura hasta su cierre.
- [ ] Cada cambio de estado y cada cambio de responsable debe quedar registrado con su marca temporal y su autor, de forma consultable desde la ficha de la incidencia.
- [ ] Añade filtrado del listado por estado, severidad y área responsable.
- [ ] Ofrece una vista que permita ver de un vistazo el volumen de incidencias abiertas por severidad.
- [ ] Respeta el stack y las convenciones que ya trae el monorepo. No introduzcas librerías, gestores de dependencias ni patrones nuevos sin que exista una regla que lo justifique.

⚠️ **IMPORTANTE:** los nombres de campos, identificadores de entidad y valores de dominio de tu implementación deben coincidir con lo especificado en tu CONTEXT.md. Una implementación genérica que ignore el contexto no será aceptada.

### Verificación

- [ ] Verifica el comportamiento del gestor: registro, clasificación, asignación, recorrido completo de estados y trazabilidad de los cambios.
- [ ] Revisa el código generado por el agente antes de commitear. La confianza ciega en su proactividad es un antipatrón, no un atajo.
- [ ] Deja constancia en el Pull Request de qué reglas evitaron una desviación durante el desarrollo.

---

## ✅ Qué evaluaremos

- [ ] El directorio `.agents/rules` existe y contiene al menos tres reglas derivadas del código base preexistente, no de preferencias personales.
- [ ] Cada regla declara explícitamente su forma de aplicación y su ámbito.
- [ ] Las reglas están escritas en términos verificables y sin ambigüedad.
- [ ] El directorio `memory-bank/` contiene contexto de producto y negocio, stack tecnológico y estado actual del proyecto.
- [ ] El contexto de producto refleja la empresa asignada y su operación real, no una descripción genérica.
- [ ] Existe un plan de implementación versionado, y el desarrollo entregado se corresponde con él.
- [ ] Existe un registro de las discrepancias entre el resumen inicial del agente y el código real.
- [ ] El gestor permite registrar una incidencia con canal, tipo y severidad, y asignarla a un área responsable.
- [ ] La incidencia recorre un ciclo de estados completo hasta su cierre.
- [ ] Los cambios de estado y de responsable son consultables con marca temporal y autor desde la ficha de la incidencia.
- [ ] El listado permite filtrar por estado, severidad y área responsable.
- [ ] Existe una vista con el volumen de incidencias abiertas por severidad.
- [ ] Los catálogos de canales, tipos, severidades y áreas coinciden con los del CONTEXT de la empresa asignada.
- [ ] No se han introducido dependencias ni patrones ajenos a las convenciones del monorepo.
- [ ] El historial de commits separa los pasos del desarrollo; no existe un commit único que agrupe todo el trabajo.

---

## 📦 Cómo entregar

Sube tu rama `feature/incident-manager` a tu copia del monorepo y abre un Pull Request contra la rama principal.

En la descripción del Pull Request incluye:

- Las discrepancias detectadas entre el resumen inicial del agente y el repositorio real.
- Las reglas que has definido y de qué evidencia del código sale cada una.
- La propuesta de mejora que has registrado sin aplicar, si la hay.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
