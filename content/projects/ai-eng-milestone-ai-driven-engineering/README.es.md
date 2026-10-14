# Hito — Ingeniería impulsada por IA

<!-- hide -->

Por [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are also available in [English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee el briefing de tu empresa en [`00-general-contexts`](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts) y cópialo en `CONTEXT.md` en la raíz de tu monorepo antes de escribir una sola línea de código — ahí están la identidad, las restricciones y la hoja de ruta de tu empresa.

---

## 🎯 Tu reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Aquí empieza tu proyecto de empresa. Tienes un repositorio de plantilla y un escenario de compañía — pero aún no hay un sistema coherente. Todo lo que construyas de aquí en adelante — interfaces, APIs, agentes, automatizaciones — vivirá en este mismo espacio. Antes de añadir features, hay que construir la infraestructura que hará que ese código sea coherente, mantenible y AI-ready.

Tu tech lead ha dejado una tarea pendiente en el tablero desde hace dos semanas:

> **Asunto: Monorepo AI Setup — necesitamos esto esta semana**
>
> Hola,
>
> He revisado el estado del repo y estamos empezando sin estructura de soporte. Si meto un agente sobre esto ahora mismo va a cometer errores que nos van a costar el triple de tiempo.
>
> Necesito que el repositorio tenga un contexto claro y persistente antes de que sigamos añadiendo features: qué es la empresa, qué estamos construyendo, cuáles son las reglas del proyecto. Eso va al banco de memoria. El agente tiene que leerlo antes de tocar nada — y tiene que incluir tanto el contexto de negocio como el técnico, no solo uno de los dos.
>
> También quiero un `AGENTS.md` que defina cómo opera cualquier agente en este repo — qué flujo tiene que seguir antes de hacer un commit. Nada de agentes que escriban código sin pasar por el proceso de entrega.
>
> Para las reglas más específicas usaremos la carpeta `.agents/`. Piensa en qué convenciones necesita conocer el agente para no romper lo que ya tenemos, y documéntalas ahí con el alcance correcto.
>
> Por último, quiero que formalicemos al menos una skill que capture una tarea recurrente de nuestro flujo de trabajo — algo que el agente pueda ejecutar de forma consistente y que podamos reutilizar a medida que el proyecto crezca. Que tenga criterios de aceptación explícitos: si no se puede verificar, no vale.
>
> En cuanto a la capa de aplicación, **no** inventes un árbol paralelo. Cuando se creen las apps, van en las carpetas que ya mapea la plantilla — sitio público en `./uis/website`, app interna en `./uis/backoffice`, APIs en `/services`. Lee el README de cada carpeta antes de poner nada ahí.
>
> Cuando termines, PR y avísame.
>
> — [Tu tech lead]

### 💡 Banco de memoria, reglas y skills: qué son y por qué importan

Un **banco de memoria** es un conjunto de archivos Markdown que el agente de programación lee antes de cada sesión. No es documentación estática — es el contexto activo del proyecto: negocio, decisiones de arquitectura tomadas, restricciones en vigor y estado actual del desarrollo. Sin él, cada sesión del agente empieza desde cero y repite los mismos errores. Por eso, el banco de memoria debe actualizarse cada vez que el proyecto evoluciona: nuevas decisiones, cambios de arquitectura, features completadas, problemas encontrados. Un banco de memoria que no se mantiene al día deja de ser útil en cuestión de días. **¡Nunca lo olvides!**

La estructura esperada para la configuración de agentes en el monorepo es la siguiente:

```text
./.agents
└─ /rules
   └─ <rule-name>.md
└─ /skills
   └─ /<skill>
      └─ SKILL.md
./memory-bank
└─ <context>.md
```

> ⚠️ **Atención:** No confundas `.agents/` con las carpetas `/agents` y `/skills` que verás en el monorepo. `.agents/` es el directorio de configuración para los agentes de código (Cursor, Windsurf, Claude Code…) — aquí van las reglas y skills que le enseñan al agente cómo trabajar en este repositorio. Las carpetas `/agents` y `/skills` son para los agentes e integraciones que construirás para la empresa en módulos posteriores. Son cosas distintas: una configura cómo trabaja tu herramienta de desarrollo, la otra es código de producto.

Antes de crear ninguna carpeta nueva, revisa el `README.md` de cada carpeta del monorepo — el repositorio de plantilla incluye instrucciones sobre qué debe ir en cada espacio. Siguiéndolas evitarás duplicidades y mantendrás una estructura que el agente pueda navegar sin ambigüedad.

Las **reglas de desarrollo** (`AGENTS.md` y `.agents/rules/`) son el protocolo que el agente sigue automáticamente: qué leer al empezar, qué pasos son obligatorios antes de cada commit, qué convenciones respetar y cuándo detenerse y preguntar. Actúan como el acuerdo de equipo que garantiza que el agente no tome decisiones por su cuenta donde no debería.

Una **skill de agente** es una instrucción estructurada y reutilizable: más concreta que una regla genérica, con inputs definidos, output esperado y criterios de aceptación verificables. Una buena skill tiene un único objetivo y puede testearse de forma independiente.

---

## 🌱 Cómo iniciar el proyecto

Lee el `CONTEXT.md` en la **raíz de tu monorepo** antes de hacer nada más. Ese archivo debe ser el briefing de tu empresa de [`00-general-contexts`](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts) (`CONTEXT-<company>-briefing.es.md` / `.en.md`) — no el placeholder vacío de la plantilla. El banco de memoria que vas a construir debe describir la empresa y el proyecto de tu escenario específico — no una empresa ficticia genérica.

1. Haz fork del repositorio de plantilla: [ai-engineering-company-project-monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)
2. Ábrelo en **GitHub Codespaces** o clónalo localmente y revisa la estructura existente antes de crear carpetas nuevas
3. Configura tu agente de programación con acceso al repositorio completo
4. Documenta las decisiones de configuración inicial en el banco de memoria **antes** de escribir código de aplicación

---

## 💻 Lo que debes hacer

### Infraestructura de agentes

- [ ] Crear la carpeta `memory-bank/` en la raíz del monorepo con al menos los siguientes archivos:
  - [ ] `projectbrief.md` — descripción del negocio, los objetivos del proyecto y el problema que resuelve
  - [ ] `techContext.md` — stack tecnológico, decisiones de arquitectura tomadas y restricciones técnicas
  - [ ] `progress.md` — estado actual del desarrollo y próximos pasos previstos
- [ ] Crear el archivo `AGENTS.md` en la raíz del monorepo que defina:
  - [ ] Qué archivos del banco de memoria debe leer el agente al inicio de cada sesión
  - [ ] El flujo obligatorio antes de cada commit (mínimo 4 pasos ordenados y explícitos)
  - [ ] Las carpetas y archivos que el agente **no debe modificar** sin confirmación explícita del desarrollador
- [ ] Crear la carpeta `.agents/` con al menos una regla de desarrollo documentada con su alcance de aplicación (siempre activa, por patrón de archivo, o solicitada por el agente)
- [ ] Implementar al menos una **skill de agente** para una tarea recurrente del flujo de trabajo, con:
  - [ ] Un objetivo único y claramente definido
  - [ ] Inputs documentados
  - [ ] Criterios de aceptación explícitos y verificables

⚠️ **IMPORTANTE:** El banco de memoria, las reglas y la skill deben estar alineados con los datos, procesos y restricciones del `CONTEXT.md` de tu monorepo (el briefing de tu empresa). Una infraestructura genérica — o construida sobre el placeholder de plantilla sin reemplazar — no será aceptada.

### Carpetas del monorepo (capa de aplicación)

Este hito **no** te pide crear las apps. Aclara en el banco de memoria / reglas de agente dónde debe vivir el código de producto cuando se usen esas carpetas más adelante (o si la plantilla ya las trae). Sigue los README de la plantilla en cada ruta — no crees un segundo árbol de frontend o API en otro sitio.

| Ruta               | Qué va aquí cuando se cree                                                                     |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| `/uis`             | Proyectos frontend de la empresa                                                               |
| `./uis/website`    | Web corporativa de cara al público (ruta `/`, marca y copy alineados con `CONTEXT.md`)         |
| `./uis/backoffice` | App interna de la empresa (layout propio, separado del sitio público; vista de entrada en `/`) |
| `/services`        | APIs y servicios backend                                                                       |

---

## ✅ Lo que evaluaremos

- [ ] El banco de memoria contiene contexto de negocio **y** contexto técnico — no solo uno de los dos
- [ ] `AGENTS.md` especifica un flujo de trabajo con al menos 4 pasos ordenados antes del commit
- [ ] La carpeta `.agents/` contiene al menos una regla con alcance de aplicación explícito
- [ ] La skill implementada tiene objetivo único, inputs documentados y criterios de aceptación verificables
- [ ] El banco de memoria y/o las reglas de agente dejan claro dónde encajan `/uis/website`, `/uis/backoffice` y `/services` — sin carpetas de app paralelas inventadas

---

## 📦 Cómo entregar

1. Asegúrate de que tu rama de trabajo tenga el nombre `feature/agent-memory-bank`
2. Ejecuta el flujo de entrega definido en tu `AGENTS.md` antes del commit final
3. Abre una Pull Request hacia la rama `main` de tu fork
4. En la descripción de la PR incluye un enlace directo a tu `AGENTS.md`
5. Entrega el enlace a tu PR en el campus de 4Geeks

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
