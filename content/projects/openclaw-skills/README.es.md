# Mi Agente, A Mi Manera: Enseñando Nuevas Skills a Tu Asistente Personal

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are also available in [English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

La fontanería ya está hecha. Tu agente de OpenClaw está instalado, tu conexión de Composio está activa — Google Docs, Google Calendar, Gmail, Google Drive, Google Tasks, GitHub y más son accesibles — y Telegram te permite hablar con él desde el móvil. Lo construiste para ti.

Pero ahora mismo el agente es genérico. Cada vez que quieres que haga algo útil, escribes las mismas instrucciones largas desde cero. No conoce tus patrones, tu estilo, ni lo que significa "útil" específicamente para ti.

Dos cosas van a cambiar eso. Primero, rellenarás los cinco archivos de configuración que definen quién es tu agente y para quién trabaja — ahora mismo están casi en blanco. Segundo, implementarás al menos dos skills personalizadas que eliminen las tareas más repetitivas de tu semana.

---

### Los cinco archivos que hacen que tu agente sea tuyo

Dentro del directorio `.openclaw` encontrarás cinco archivos Markdown. Juntos forman el briefing interno completo del agente. Ahora mismo están casi vacíos — ese es el trabajo.

| Archivo       | Qué controla                                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `IDENTITY.md` | El nombre y símbolo del agente. Cómo se llama a sí mismo.                                                                                  |
| `SOUL.md`     | Personalidad y estilo de trabajo. Si pregunta antes de actuar o se pone en marcha primero. Cómo de directo es. Qué valora.                 |
| `AGENTS.md`   | Reglas de comportamiento y límites inamovibles. Lo que el agente nunca debe hacer independientemente de las instrucciones.                 |
| `USER.md`     | Todo sobre ti: tu nombre, tu trabajo, tus proyectos actuales, tu contexto. Esto es lo que el agente lee para entender para quién trabaja.  |
| `TOOLS.md`    | Qué servicios conectados puede usar el agente, cuándo usar cada uno y convenciones (calendario por defecto, carpetas, etiquetas, canales). |

Estos archivos no son decoración. Cuando le pides a tu agente que redacte un correo o planifique tu semana, los lee primero. Un `USER.md` y un `SOUL.md` bien escritos son la diferencia entre un output que usarías tal cual y uno que reescribirías desde cero.

Rellénalos como si estuvieras haciendo el onboarding de un asistente real en su primer día. Sé específico. Un `SOUL.md` que dice "sé útil" no sirve de nada. Uno que dice "ten opiniones, sé resolutivo antes de preguntar, y dime cuando algo no tiene sentido" sí moldea el comportamiento.

---

### Qué herramientas tiene tu agente a su disposición

A través de Composio, tu agente puede acceder a cualquiera de estos servicios:

- **Google Docs** — crear, actualizar y leer documentos
- **Google Calendar** — crear eventos, consultar tu agenda, encontrar huecos libres
- **Gmail** — leer, redactar y enviar correos
- **Google Drive** — listar, buscar y organizar archivos
- **Google Tasks** — crear y gestionar listas de tareas
- **GitHub** — leer repos, issues, commits y pull requests
- **Telegram** — enviarte mensajes a ti mismo o a un canal

Las skills pueden usar uno o varios de estos servicios a la vez. Cuantas más conexiones combines, más potente es el resultado.

---

### Ideas de skills — elige las tuyas o diseña las propias

Léelas y pregúntate: _¿cuál de estas activaría más de una vez?_ Esa es la que debes construir. También puedes proponer algo completamente diferente — estos son puntos de partida.

**Skills que crean contenido nuevo:**

- **Diario de aprendizaje diario** — le dices al agente qué aprendiste hoy (unos pocos puntos), y formatea y añade una entrada estructurada a un Google Doc que usas como diario personal de conocimiento.
- **Plan de semana** — dado un listado de objetivos y compromisos, el agente escribe un plan semanal priorizado, lo guarda como un nuevo Google Doc y crea los eventos clave en Google Calendar.
- **Notas de reunión** — pegas apuntes en bruto de una reunión; el agente los formatea como decisiones, tareas a hacer y preguntas abiertas, y guarda el resultado en Drive.

**Skills que afinan comportamientos ya instalados:**

- **Eventos de Calendar más inteligentes** — en lugar de pedirle al agente que "cree un evento", esta skill te permite describirlo en lenguaje natural ("sesión de estudio el jueves por la tarde, dos horas, con recordatorio") y gestiona todos los detalles automáticamente.
- **Borradores de Gmail con tu voz** — en lugar de pedirle al agente que "escriba un correo", esta skill ya conoce tu estilo de escritura, tu firma habitual y el tipo de correos que envías — el resultado necesita mínimas correcciones.
- **Resumen diario de GitHub** — el agente lee tus issues abiertos y commits recientes y te envía un briefing breve por Telegram cada vez que activas la skill.

**Skills que conectan herramientas entre sí:**

- **Tarea → Calendar** — añades tareas en Google Tasks; esta skill las lee y crea automáticamente bloques de tiempo en Google Calendar para las que aún no tienen uno.
- **Triaje de bandeja de entrada** — el agente lee tus correos no leídos en Gmail, identifica los que requieren acción y crea una Google Task para cada uno con una descripción breve de qué hay que hacer.

---

### Diseña antes de construir

Antes de escribir ninguna skill, crea un archivo `SKILLS_DESIGN.md` en la raíz de tu repositorio y responde estas tres preguntas para cada skill que vayas a implementar:

1. **¿Qué hace esta skill?** Una frase.
2. **¿Qué input necesita el agente?** ¿Qué le das, en qué formato — y qué ya sabe a partir de los cinco archivos de configuración?
3. **¿Cómo es un buen output?** Formato, destino (un Doc, un evento de Calendar, un mensaje de Telegram…) y cómo sabrás que funcionó.

Haz commit de este archivo antes de empezar la implementación. Forma parte de la entrega y se revisará de forma independiente.

---

## 🌱 Cómo iniciar el proyecto

1. Sigue en el **mismo entorno** donde ya instalaste OpenClaw y completaste los proyectos anteriores del programa (Composio, Telegram, Drive/Calendario, etc.): tu VPS, tu máquina local o tu Codespace. Esta tarea prolonga esa configuración; no reinstalas OpenClaw desde cero.
2. Usa el **mismo repositorio Git** de ese agente si ya lo versionas. Si en tu árbol faltan rutas que pide este proyecto (por ejemplo los cinco Markdown en `.openclaw` y un sitio para las skills personalizadas), créalas o añádelas siguiendo las indicaciones de tu instructor y la documentación oficial de [OpenClaw](https://github.com/openclaw/openclaw), sin depender de un repositorio plantilla externo.
3. Abre ese espacio de trabajo como ya lo haces (**GitHub Codespaces**, clon local o SSH al VPS).
4. Ejecuta `openclaw doctor` para confirmar que tu configuración actual — conexiones de Composio y Telegram — sigue funcionando antes de tocar nada.
5. Lee la guía [cómo iniciar un proyecto de programación](https://4geeks.com/lesson/how-to-start-a-project) si lo necesitas.

---

## 💻 Qué debes hacer

### Configura los cinco archivos

- [ ] Abre `IDENTITY.md` y dale a tu agente un nombre y un símbolo que te encajen.
- [ ] Escribe `SOUL.md` con suficiente especificidad para que la personalidad del agente sea realmente diferente a la genérica — incluye cómo gestiona la incertidumbre, si pregunta o actúa primero, y qué tono usa contigo.
- [ ] Establece los límites inamovibles en `AGENTS.md` — como mínimo, una regla sobre privacidad y una sobre cuándo el agente debe parar y preguntar en lugar de actuar.
- [ ] Rellena `USER.md` con tu contexto real: nombre, proyectos actuales, herramientas que usas, objetivos, cualquier cosa que el agente deba saber siempre sobre ti.
- [ ] Rellena `TOOLS.md` con los servicios a los que tu agente puede acceder vía Composio, cuándo usar cada uno y los valores por defecto (qué calendario, qué carpeta de Drive, cómo firmar en Gmail, etc.).
- [ ] Ejecuta `openclaw doctor` después de editar los cinco. Cero errores antes de continuar.

### Documenta tu diseño

- [ ] Crea `SKILLS_DESIGN.md` en la raíz del repositorio con las tres preguntas de diseño respondidas para cada skill.
- [ ] Haz commit antes de escribir ninguna implementación de skill.

### Implementa tus skills

- [ ] Implementa al menos dos skills personalizadas como skills de OpenClaw correctas — no como prompts en bruto en la terminal.
- [ ] Cada skill debe reflejar visiblemente la configuración de los cinco archivos — el output debe sentirse diferente a lo que el agente produciría sin tu configuración.
- [ ] Al menos una skill debe producir output verificado en un servicio conectado a Composio (Google Docs, Google Calendar, Gmail, Google Tasks, Google Drive) o enviar un mensaje por Telegram.
- [ ] Prueba cada skill con un input real y personal — no con un placeholder.

> ⚠️ **IMPORTANTE:** Todas las skills deben funcionar con las herramientas actualmente conectadas. No configures una nueva API, flujo OAuth ni servicio externo como parte de este proyecto — eso es el tema de mañana. Cualquier skill que requiera una nueva conexión no será aceptada.

---

## ✅ Qué vamos a evaluar

- [ ] Los cinco archivos de configuración (`IDENTITY.md`, `SOUL.md`, `AGENTS.md`, `USER.md`, `TOOLS.md`) contienen contenido específico y no genérico.
- [ ] `openclaw doctor` se ejecuta sin errores.
- [ ] `SKILLS_DESIGN.md` está commiteado antes de la implementación y responde las tres preguntas de diseño para cada skill.
- [ ] Al menos dos skills están implementadas como skills de OpenClaw correctas.
- [ ] Al menos una skill produce output verificado en un servicio conectado (Docs, Calendar, Gmail, Tasks, Drive o Telegram).
- [ ] No se ha configurado ninguna API externa ni flujo OAuth nuevo como parte del proyecto.
- [ ] Los outputs del agente reflejan visiblemente la configuración de los cinco archivos — tono, estilo y contexto son coherentes con lo que se escribió allí.
- [ ] El estudiante puede explicar el razonamiento detrás de cada skill: por qué esa tarea, por qué ese input, por qué ese formato de output.

> Nota: Un `SKILLS_DESIGN.md` bien razonado con una implementación parcial puntúa más alto que una skill que funciona sin ningún razonamiento de diseño documentado.

---

## 📦 Cómo entregar

Sube tu repositorio a GitHub — incluyendo `SKILLS_DESIGN.md` — y comparte el enlace siguiendo las instrucciones de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
