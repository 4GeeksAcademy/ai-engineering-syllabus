# Puesta en marcha del monorepo – Reglas de trabajo para agentes de código

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

![build by developers](https://img.shields.io/badge/build_by-Developers-blue)
![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: lee el **[BRIEFING de tu empresa](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts)** antes de escribir una sola regla — no para decidir qué construir, sino para detectar qué datos maneja la empresa, en qué países opera y qué sistemas no se pueden tocar a la ligera. De ahí salen tus líneas rojas.

<!-- endhide -->

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya sabes elegir el modo del agente adecuado para cada tarea. El problema ahora no es cómo usas tú tu agente, sino que en el equipo hay tantas formas de trabajar como agentes. Tu CTO ha abierto un ticket con una petición concreta: definir el **mínimo común** que cualquier agente — y cualquier persona — debe respetar al trabajar en el monorepo de la empresa. Las reglas tienen que valer igual para quien acaba de entrar sin experiencia, para un perfil junior y para un senior: nadie trabaja con un agente que tenga más permisos que el resto.

El punto de entrada es un fichero `AGENTS.md` en la raíz del repositorio, la convención abierta que leen la mayoría de agentes de código. Ese fichero es **la única fuente de verdad**: si tu herramienta usa su propio fichero de instrucciones, ese fichero solo apunta a `AGENTS.md`, nunca duplica reglas. Y como el agente lo carga en cada sesión, cada línea cuesta tokens en cada conversación: `AGENTS.md` es un índice con lo que no se negocia, y el detalle vive en reglas separadas por preocupación.

Este trabajo trata de **cómo se trabaja**, no de **qué es la empresa**. `AGENTS.md` no describe el negocio, los clientes ni la operación: eso vive en el `CONTEXT.md` del monorepo. El briefing de la empresa solo te sirve para encontrar los riesgos que deben convertirse en límites.

Hay dos trampas habituales. La primera es escribir una regla sobre secretos sin comprobar si el repositorio los protege de verdad: **antes de dar por buena cualquier regla de entorno, verifica que el repositorio cumple lo que la regla promete y corrige lo que falte**. La segunda es dar las reglas por buenas porque existen. Una regla que no cambia lo que hace el agente sobra o está mal escrita, así que **necesitas una línea base: cómo se comporta el agente antes de que existan las reglas**, para poder demostrar después que sí cambian algo.

> **De:** tu CTO
> **Asunto:** Ticket — reglas mínimas para trabajar con agentes en el monorepo
>
> Cada uno trabaja con su agente como le parece, y se nota en los Pull Requests. No quiero un manual de cincuenta páginas. Quiero el mínimo que no se negocia, el mismo para quien acaba de entrar y para quien lleva años programando. La seniority cambia cómo revisas lo que produce el agente, no lo que el agente tiene permitido hacer.
>
> Como mínimo, el brief cubre tres áreas. En cada una te dejo cosas que ya he visto pasar en este equipo; todas tienen que quedar cubiertas por alguna regla, pero no son la lista completa.
>
> 1. **Convenciones de código y estilo.** Nombrado, formato, linting y los modismos propios de este repositorio. Si una convención la puede comprobar una herramienta, la regla nombra la herramienta y el comando. Lo que depende solo de la buena voluntad del agente no es una convención, es un deseo.
>    - Los gestores de paquetes son **pnpm** para JavaScript/TypeScript y **uv** para Python, sin excepciones. Ya he visto un `npm install` y un `pip install` en este repositorio: la dependencia funciona en una máquina y no queda registrada en ninguna parte.
>    - Lockfiles que no se suben o que alguien edita a mano para resolver un conflicto. El lockfile se versiona y lo regenera la herramienta, nunca una persona.
>    - Un cambio de tres líneas dentro de un diff de cuatrocientas, porque el agente reformateó el fichero entero. El formato va en su propio commit, o no va.
> 2. **Antipatrones y tabúes explícitos.** Una lista en negativo: librerías, patrones y atajos que el agente tiene prohibido usar. Cada prohibición con su motivo en una línea. Un "no" sin motivo es lo primero que alguien se salta.
>    - Errores silenciados para que algo "funcione": un `except: pass`, un `any`, un `eslint-disable`, un commit con `--no-verify`.
>    - Un test que fallaba y se borró o se marcó para saltarlo. Un test en rojo se arregla o se discute, no se esconde.
>    - URLs, puertos e identificadores escritos a mano en el código, que funcionan en local y rompen en cualquier otro entorno.
> 3. **Entorno y acceso.** Dónde viven los secretos y dónde no pueden aparecer nunca, cómo se integran APIs externas y, sobre todo, en qué momentos el agente se detiene y pide aprobación humana antes de ejecutar algo destructivo o de alto riesgo.
>    - Un `.env` subido por error y "borrado" en el commit siguiente. Sigue en el historial: una clave filtrada se revoca y se rota, no basta con quitar el fichero.
>    - Una clave de API en código de frontend. Todo lo que llega al navegador es público, también lo que lleva un prefijo como `NEXT_PUBLIC_`.
>    - Un `git add .` que se llevó ficheros que nadie revisó, un `git clean -fdx` que borró el `.env` local de alguien y un `git push --force` sobre una rama compartida.
>
> Si crees que falta algo en ese mínimo, propónlo y justifícalo. Pero no lo infles: cada línea de `AGENTS.md` la paga cada sesión de cada agente.
>
> Lee el briefing de la empresa buscando qué podría salir mal, no qué construir. Ahí están las líneas rojas que una regla genérica nunca va a cubrir.
>
> Los criterios de aceptación son los del checklist. El sign-off lo doy sobre el Pull Request, y lo que más me importa no es que las reglas existan, sino ver que cambian lo que hace el agente.

### Conocimiento complementario: qué va en `AGENTS.md` y qué va en una regla

**`AGENTS.md`** se carga siempre. Contiene lo imprescindible: para qué sirve el fichero, el stack y los comandos clave (instalar, formatear, lint, tests), las líneas rojas y un índice de reglas que dice cuándo aplica cada una.

**Una regla** (`.agents/rules/<tema>.md`) cubre una sola preocupación y declara en su cabecera su **ámbito** (a qué ficheros aplica), su **forma de activación** (siempre, por patrón de fichero o bajo demanda) y su **motivo**.

Para que una regla sea verificable, usa verbos normativos — **DEBE**, **NO DEBE**, **DEBERÍA** — y evita "intenta", "en lo posible" o "si tiene sentido". Los disparadores de aprobación humana se leen mejor en formato EARS orientado a eventos: _"Cuando el agente vaya a eliminar un fichero o carpeta, el agente debe detenerse y solicitar aprobación antes de ejecutarlo."_

> 🔀 **PR aprobado → haz merge a `main`.** Si no, las reglas no llegan a la rama principal y el siguiente desarrollo arranca con agentes trabajando sin ellas.

---

## 🌱 Cómo empezar el proyecto

1. Trabaja sobre tu copia del monorepo de la empresa. Crea la rama `feature/agent-rules`.
2. Lee el briefing de tu empresa con mirada de riesgo y anota qué datos sensibles maneja, en qué países y monedas opera y qué sistemas existen.
3. Antes de escribir ninguna regla, prepara y ejecuta tus pruebas de línea base. Ese resultado es tu punto de partida.
4. Haz un commit separado por cada fase: línea base, `AGENTS.md`, reglas, higiene del repositorio y verificación. El historial es parte de la entrega.

---

## 💻 Qué debes hacer

### Línea base

- [ ] Diseña al menos cuatro tareas de prueba (_probes_) pensadas para tentar al agente a saltarse una regla, con al menos una por cada área del ticket: convenciones, tabúes, y entorno y acceso. Por ejemplo: pedirle que añada una librería para resolver algo trivial, que deje una clave de API "solo para probar" en el código o que borre una carpeta que "sobra".
- [ ] Usa siempre valores ficticios en las probes. Nunca pegues un secreto real en un prompt.
- [ ] Ejecuta las probes que implican acciones destructivas o de riesgo en modo Plan o Ask, para que el agente describa lo que haría sin ejecutarlo.
- [ ] Ejecuta todas las probes sin reglas y registra en `docs/agent-rules/probes.md` qué hizo o propuso el agente en cada una.

### `AGENTS.md`

- [ ] Crea `AGENTS.md` en la raíz del monorepo como punto de entrada único para cualquier agente.
- [ ] Incluye el propósito del fichero, el stack y los comandos clave del repositorio, las líneas rojas no negociables y un índice de reglas con cuándo aplica cada una.
- [ ] Mantén `AGENTS.md` por debajo de 120 líneas. El detalle vive en las reglas, no aquí.
- [ ] No describas la empresa, su negocio ni su operación. Enlaza a `CONTEXT.md` para eso.
- [ ] Si tu herramienta usa su propio fichero de instrucciones (`CLAUDE.md`, `.cursor/rules/`, `.github/copilot-instructions.md`…), haz que solo apunte a `AGENTS.md`, sin duplicar contenido.

### Reglas del proyecto

- [ ] Crea el directorio `.agents/rules/` con una regla por preocupación, cada una con cabecera de ámbito, forma de activación y motivo.
- [ ] Crea la regla de **convenciones de código y estilo**: nombrado por lenguaje del stack, formato, linting y los modismos propios del monorepo (ubicación de cada tipo de pieza según la estructura de carpetas).
- [ ] Fija en esa regla pnpm y uv como únicos gestores de paquetes, con los comandos permitidos para añadir, eliminar e instalar dependencias en cada uno.
- [ ] Para cada convención que pueda comprobar una herramienta, nombra la herramienta y el comando, y añade la configuración mínima que la haga posible (por ejemplo, `.editorconfig` o la configuración del formateador del lenguaje).
- [ ] Crea la regla de **antipatrones y tabúes**: al menos seis prohibiciones explícitas, cada una con su motivo en una línea y la alternativa permitida cuando exista.
- [ ] Crea la regla de **entorno y acceso**: dónde viven los secretos, dónde no pueden aparecer nunca (código, logs, commits, prompts, datos de prueba) y cómo se integra una API externa.
- [ ] Incluye en esa regla al menos cinco disparadores de aprobación humana en formato EARS orientado a eventos, que cubran como mínimo: borrado de ficheros o carpetas, reescritura del historial de Git, alta o baja de dependencias, cambios en ficheros de entorno o infraestructura, y cambios en `AGENTS.md` o en las propias reglas.
- [ ] Añade al menos una regla más que consideres parte del mínimo y justifícala en el Pull Request. Algunas candidatas: flujo de Git y commits, definición de terminado (qué comprueba el agente antes de dar algo por acabado), disciplina de alcance (no tocar nada fuera del ticket), protocolo ante ambigüedad (preguntar y declarar suposiciones en lugar de rellenar huecos). También puedes proponer otra.
- [ ] Asegúrate de que cada caso que menciona tu CTO en el ticket queda cubierto por al menos una regla, redactada como norma verificable y no como copia de la anécdota.
- [ ] Redacta todas las reglas con verbos normativos (DEBE, NO DEBE, DEBERÍA) y sin formulaciones ambiguas.

### Líneas rojas de la empresa

- [ ] Identifica en el briefing al menos dos riesgos propios de tu empresa — por ejemplo, el tipo de datos personales o sensibles que maneja, la operación en varios países, monedas o idiomas, o sistemas heredados que no se pueden tocar sin coordinación — y conviértelos en reglas o tabúes concretos.
- [ ] Indica junto a cada línea roja de qué parte del briefing sale.

⚠️ **IMPORTANTE:** las líneas rojas deben derivarse del briefing de tu empresa asignada. Un conjunto de reglas genérico, que serviría igual para cualquier empresa, no será aceptado.

### Higiene del repositorio

- [ ] Comprueba que el repositorio cumple lo que promete tu regla de secretos y corrige lo que falte.
- [ ] Crea `.env.example` con los nombres de las variables necesarias y valores ficticios.

### Verificación

- [ ] Ejecuta de nuevo las mismas probes, en el mismo modo, con las reglas activas, y registra el resultado junto al de la línea base.
- [ ] Para cada probe en la que el comportamiento no cambió, ajusta la regla o justifica por qué no aplica.
- [ ] Abre una sesión nueva del agente, pídele que explique las reglas del proyecto sin ayuda y comprueba que identifica las líneas rojas y los disparadores de aprobación.
- [ ] Revisa todo lo que el agente haya escrito antes de commitearlo. Tú eres responsable de cada línea que entra en el repositorio.

---

## ✅ Qué evaluaremos

- [ ] `AGENTS.md` existe en la raíz, tiene menos de 120 líneas e incluye stack, comandos clave, líneas rojas e índice de reglas.
- [ ] `AGENTS.md` no contiene descripción del negocio y enlaza a `CONTEXT.md`.
- [ ] Los ficheros de instrucciones propios de una herramienta, si existen, solo hacen referencia a `AGENTS.md` y no duplican reglas.
- [ ] `.agents/rules/` contiene al menos cuatro reglas: las tres áreas del ticket más una adicional justificada.
- [ ] Cada regla declara ámbito, forma de activación y motivo.
- [ ] La regla de convenciones establece pnpm y uv como únicos gestores de paquetes e indica sus comandos.
- [ ] Cada convención comprobable por herramienta nombra la herramienta y el comando, y la configuración correspondiente existe en el repositorio.
- [ ] La regla de tabúes tiene al menos seis prohibiciones, cada una con su motivo.
- [ ] Existen al menos cinco disparadores de aprobación humana en formato EARS que cubren los cinco casos mínimos.
- [ ] Cada uno de los nueve casos del ticket del CTO está cubierto por al menos una regla identificable.
- [ ] Ninguna regla usa formulaciones ambiguas como "intenta", "en lo posible" o "si tiene sentido".
- [ ] Hay al menos dos líneas rojas propias de la empresa asignada, cada una trazable a una parte del briefing.
- [ ] El repositorio excluye los ficheros de entorno del control de versiones, existe `.env.example` con valores ficticios y no hay secretos en el historial.
- [ ] `docs/agent-rules/probes.md` recoge al menos cuatro probes, cubre las tres áreas del ticket y compara línea base y resultado con reglas.
- [ ] Al menos tres probes muestran un cambio de comportamiento atribuible a una regla concreta.
- [ ] El historial de commits separa las fases del trabajo; no existe un commit único que agrupe todo.

---

## 📦 Cómo entregar

Sube tu rama `feature/agent-rules` a tu copia del monorepo y abre un Pull Request contra la rama principal.

En la descripción del Pull Request incluye:

- Las líneas rojas de tu empresa y de qué parte del briefing sale cada una.
- La regla adicional que has añadido al mínimo y por qué.
- Una tabla resumen de las probes: qué hizo el agente sin reglas, qué hizo con reglas y qué regla provocó el cambio.
- Una regla que hayas descartado para no inflar el mínimo, y el motivo.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
