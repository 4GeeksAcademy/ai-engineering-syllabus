# Backoffice de Operaciones – Gestor de Inventario

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/4-devs/inventory-manager-for-devs)** antes de escribir una sola línea de spec — define las unidades de medida, categorías, lotes y puntos de reorden concretos de tu implementación.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya dejaste el repositorio preparado con reglas de proyecto y un banco de memoria. Ahora tu CTO trae el primer requisito de negocio real: un gestor de inventario. A diferencia del ejercicio anterior, aquí no basta con que el agente entienda el proyecto — necesita instrucciones que no dejen espacio para interpretación en los puntos donde una interpretación equivocada cuesta caro.

El inventario tiene una propiedad que lo hace distinto a casi cualquier otro CRUD: el stock disponible de un artículo **no es un dato, es un cálculo**. Se deriva de la suma de sus movimientos — entradas, salidas, ajustes — y nunca se edita directamente. Es la clase de regla que un agente de código, sin instrucciones explícitas, viola en silencio: generará un campo `stock` editable porque es el patrón que ha visto miles de veces, y el resultado parecerá correcto hasta que alguien haga un ajuste manual y el número deje de cuadrar con el historial. Para cuando alguien lo nota, ya hay funcionalidad construida encima del error.

Un prompt suelto — "hazme un CRUD de inventario" — no lleva esa regla dentro. Un spec, sí, si está bien escrito. Esa es la apuesta de este proyecto: cuando es el agente quien escribe el código, el artefacto de mayor valor que produces tú ya no es el código — es la especificación que lo gobierna.

Vas a trabajar con **Spec Driven Development (SDD)**: en lugar de darle órdenes al agente paso a paso, vas a producir tres capas — **spec** (el qué: comportamiento, contratos, invariantes), **plan** (el cómo: decisiones de arquitectura) y **tareas** (el orden: unidades atómicas y verificables) — y vas a dejar que la implementación se ciña a esas capas. El bucle es: `specify → plan → tasks → implement → verify`.

Hay una trampa habitual en este ejercicio: escribir "vibe coding" con más pasos — un spec de una línea, saltar directo a pedirle al agente que implemente, y llamar a eso Spec Driven Development porque hay un fichero de por medio. Un spec no es un prompt largo. Es un contrato que alguien más — un compañero, un agente, tú mismo en tres semanas — puede leer y verificar sin preguntarte nada.

La segunda trampa es la contraria: escribir 20 páginas de spec para un CRUD. La formalidad del spec debe ser proporcional al tamaño del cambio, al riesgo y al número de personas afectadas — no todo requisito necesita el mismo nivel de ceremonia. Las tres capas que vas a construir aquí lo justifican porque el invariante de stock lo justifica; no repitas ese nivel de detalle para cada campo trivial del formulario de un artículo.

> **De:** tu CTO
> **Asunto:** primer requisito de negocio — inventario
>
> > Antes de que el agente escriba una sola línea de código de este módulo, quiero ver el spec. No el código — el spec. Ese es el artefacto que voy a revisar y aprobar, y solo después de aprobarlo se pasa a implementación.
> >
> > El requisito, en una frase: el equipo de operaciones necesita dar de alta artículos de inventario, registrar sus movimientos de entrada, salida y ajuste, y saber en todo momento qué está por debajo del punto de reorden. Los nombres de las entidades, las unidades de medida y los valores de dominio salen de tu CONTEXT, no de tu imaginación.
> >
> > Hay una cosa que no es negociable, y quiero que quede como criterio de aceptación explícito, no como una nota al margen: el stock de un artículo se calcula a partir de sus movimientos. No existe un endpoint, un campo de formulario ni una operación que edite el stock directamente. Si tu spec no lo dice con esa claridad, el agente lo va a hacer mal, y no será culpa suya.
> >
> > Escribe los criterios de aceptación en formato EARS — quiero frases verificables, no descripciones. Divide el trabajo en tareas lo bastante pequeñas como para que cada una se pueda verificar por separado; cuanto más grande la unidad que le entregas al agente, más diverge de lo que pediste.
> >
> > Una vez tengas spec, plan y tareas aprobados, seguimos con esto: te voy a mandar un cambio de requisito sobre la marcha, como pasa siempre. Cuando llegue, el spec se edita primero y las tareas afectadas se regeneran desde ahí — nunca al revés. Si te encuentro parcheando código sin haber tocado antes el spec, esa parte se descarta y se rehace.
> >
> > Cada tarea debe quedar conectada con el criterio de aceptación que verifica y con el commit que la implementa. Quiero poder ir de un requisito a su test y de un test a su commit sin tener que preguntarte nada.
>
> — Handoff al equipo de operaciones en cuanto la suite de verificación esté en verde.

### Conocimiento complementario: EARS y las tres capas

**EARS (Easy Approach to Requirements Syntax)** es una forma estructurada de escribir criterios de aceptación para que dejen de ser ambiguos. Las plantillas más comunes:

- **Ubicuo**: "El sistema debe [comportamiento]." — se cumple siempre, sin condición.
- **Basado en evento**: "Cuando [evento], el sistema debe [comportamiento]."
- **De estado**: "Mientras [estado], el sistema debe [comportamiento]."
- **Comportamiento no deseado**: "Si [condición no deseada], entonces el sistema debe [comportamiento]."
- **Opcional**: "Donde [característica opcional], el sistema debe [comportamiento]."

Las **tres capas** de un spec no van en un único documento: mezclarlas es un antipatrón reconocido. El _spec_ describe comportamiento, contratos e invariantes — el qué. El _plan_ traduce eso en decisiones de arquitectura — el cómo. Las _tareas_ descomponen el plan en unidades atómicas, testeables por separado — el orden. Cuando cambia un requisito, se edita el spec, y desde ahí se regeneran solo las tareas afectadas — nunca se parchea el código primero y se ajusta el spec después para que cuadre.

El spec no sustituye a la suite de tests, la origina. El código sigue siendo la verdad ejecutable; los tests son el mecanismo que comprueba que esa verdad cumple lo que el spec prometió.

---

## 🌱 Cómo empezar el proyecto

1. Trabaja sobre tu copia del monorepo de la empresa. Crea la rama `feature/inventory-manager`.
2. Antes de escribir spec alguno, revisa las reglas de `.agents/rules` y el `memory-bank/` que ya existen en tu repositorio — el spec no debe repetir lo que ya está documentado ahí, debe apoyarse en ello.
3. Sigue el bucle `specify → plan → tasks → implement → verify` en ese orden. No empieces a implementar antes de tener spec y plan aprobados.
4. Haz un commit separado por cada tarea implementada, referenciando su identificador. El historial es parte de la entrega.

---

## 💻 Qué debes hacer

### Fase 1 — Specify

- [ ] Crea `specs/inventory-manager/spec.md` con el comportamiento, los contratos y los invariantes del gestor de inventario.
- [ ] Escribe los criterios de aceptación en formato EARS, cada uno con un identificador único (p. ej. `INV-001`).
- [ ] Incluye explícitamente como criterio de aceptación el invariante de stock: el stock se deriva de los movimientos, nunca se edita directamente.
- [ ] Define el comportamiento no deseado: qué debe pasar cuando un movimiento dejaría el stock en negativo, o cuando se intenta registrar una salida de un artículo o lote inexistente.

### Fase 2 — Plan

- [ ] Crea `specs/inventory-manager/plan.md` con las decisiones de arquitectura necesarias para cumplir el spec: modelo de datos, cómo se calcula el stock disponible, dónde vive esa lógica.
- [ ] Justifica cualquier decisión que no sea obvia a partir del spec — el plan explica el cómo, no repite el qué.

### Fase 3 — Tasks

- [ ] Crea `specs/inventory-manager/tasks.md` con tareas atómicas y verificables por separado.
- [ ] Cada tarea referencia el identificador del criterio de aceptación (spec) que implementa.
- [ ] Ninguna tarea agrupa más de un criterio de aceptación no relacionado — si una tarea es difícil de verificar de forma aislada, es demasiado grande.

### Fase 4 — Implement

- [ ] Implementa las tareas en el orden definido, sin saltarte el plan ni improvisar alcance nuevo directamente con el agente.
- [ ] Implementa el alta, edición, listado y baja de artículos de inventario, con los campos definidos en tu CONTEXT.
- [ ] Implementa el registro de movimientos de stock: entrada, salida y ajuste, cada uno con su motivo y su marca temporal.
- [ ] El stock disponible de un artículo se calcula a partir de sus movimientos — no existe operación que lo edite directamente.
- [ ] Implementa un punto de reorden por artículo y una señal visible en el backoffice cuando el stock quede por debajo.
- [ ] Respeta el stack y las convenciones que ya trae el monorepo.

### Fase 5 — Verify

- [ ] Escribe una suite de tests que verifique cada criterio de aceptación del spec, incluyendo el invariante de stock y los comportamientos no deseados.
- [ ] Cada commit de implementación debe quedar conectado con la tarea y el criterio de aceptación que verifica.
- [ ] Revisa el código generado por el agente antes de commitear. La confianza ciega en su proactividad es un antipatrón, no un atajo.

### Cambio de requisito

- [ ] Cuando llegue el cambio de requisito (ver checklist de entrega), edita primero `spec.md`, luego actualiza `plan.md` si aplica, y regenera solo las tareas de `tasks.md` afectadas por el cambio.
- [ ] Documenta en el Pull Request qué secciones del spec cambiaron y qué tareas se regeneraron como consecuencia — no reescribas el spec completo para un cambio puntual.

---

## ✅ Qué evaluaremos

- [ ] Existen `spec.md`, `plan.md` y `tasks.md` en `specs/inventory-manager/`, cada uno con el contenido propio de su capa — sin mezclar comportamiento, arquitectura y tareas en un único documento.
- [ ] Los criterios de aceptación están escritos en formato EARS, son verificables y tienen identificador único.
- [ ] El invariante "el stock se deriva de los movimientos, nunca se edita directamente" está explícito como criterio de aceptación y está verificado por al menos un test.
- [ ] Existen criterios y tests para comportamiento no deseado: movimiento que dejaría stock negativo, movimiento sobre artículo o lote inexistente.
- [ ] Cada tarea en `tasks.md` referencia el criterio de aceptación que implementa, y cada commit de implementación referencia su tarea.
- [ ] La suite de tests verifica los criterios de aceptación del spec, no solo el "happy path".
- [ ] El gestor de inventario permite dar de alta artículos y registrar movimientos de entrada, salida y ajuste, con los nombres de entidad y valores de dominio del CONTEXT de la empresa asignada.
- [ ] El backoffice señala de forma visible los artículos por debajo del punto de reorden.
- [ ] El cambio de requisito se resolvió editando el spec primero y regenerando solo las tareas afectadas — no hay evidencia de parches de código sin spec actualizado.
- [ ] El historial de commits separa las tareas del desarrollo; no existe un commit único que agrupe todo el trabajo.

---

## 📦 Cómo entregar

Sube tu rama `feature/inventory-manager` a tu copia del monorepo y abre un Pull Request contra la rama principal.

En la descripción del Pull Request incluye:

- Enlace a `specs/inventory-manager/spec.md`, `plan.md` y `tasks.md`.
- La tabla o lista de trazabilidad `requisito → test → commit`.
- Qué secciones del spec cambiaron a raíz del cambio de requisito y qué tareas se regeneraron.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
