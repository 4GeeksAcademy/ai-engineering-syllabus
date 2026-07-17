# Hito 9 — Generación de Flujos de Trabajo Agénticos (Parte 3 de 3): Aprobación y Cierre del Documento

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/09-agentic-workflows)** antes de escribir cualquier línea de código — allí está la jerarquía de aprobación por departamento y el formato del documento final de tu empresa.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

En la Parte 2 cada departamento ya genera y autoevalúa su sección de la propuesta económica dentro del mismo ticket abierto en la Parte 1. Falta lo más delicado: que un humano de cada departamento dé el visto bueno antes de que el documento final salga hacia el cliente.

> **Ticket — Aprobación humana y cierre del documento**
>
> > **Contexto:** Ya generamos y autoevaluamos cada sección de la propuesta, pero nadie va a firmar una propuesta económica sin que un humano de cada departamento le dé el visto bueno. Esta es la última pieza del flujo que empezamos en la Parte 1 — y tiene que sentirse como una sola experiencia, no como tres proyectos pegados con cinta.
> >
> > **Qué necesito que construyas:**
> >
> > - Antes de dar por aprobada la sección de un departamento, el flujo debe pasar por un punto de aprobación humana real — un _human-in-the-loop_, no solo un evaluador automático más.
> > - El flujo debe detenerse justo antes de esa acción irreversible, guardar el estado con un checkpointer, y poder reanudarse exactamente donde quedó cuando llegue la aprobación — no reiniciar desde cero.
> > - Esa pausa debe afectar solo la rama del departamento que está esperando aprobación; los demás departamentos que ya tengan su sección lista deben poder seguir avanzando en paralelo, no bloquearse entre sí.
> > - Define un límite de iteraciones y un nodo de arbitraje explícito para los desacuerdos entre departamentos — no dejes que los agentes lo resuelvan solos.
> > - Cuando todos los departamentos den su _sign-off_, el documento final debe generarse solo, consolidando las secciones aprobadas.
> > - Quiero poder ver, para cualquier ejecución, qué agente hizo qué y en qué orden, porque cuando algo salga mal en producción no vamos a tener tiempo de adivinar.
> >
> > Cuando termines, corre el flujo completo de principio a fin — desde que se sube la RFP en la Parte 1 hasta que se genera el documento final aquí — y revisa que se sienta como un solo proceso: sin saltos de estado raros, sin mensajes que no coincidan entre partes, sin pasos que se rompan en la transición de una parte a otra.
> >
> > **Acceptance criteria:** Una RFP puede recorrer las tres partes de punta a punta, pausarse para aprobación humana por departamento sin bloquear a los demás, y terminar en un documento final generado automáticamente, con trazabilidad completa de cada paso.
> >
> > — Tu tech lead

### 📚 Conocimiento complementario: cuándo interrumpir y cuándo poner un guardrail

No todo control debe pausar el flujo para un humano. Los guardrails (validaciones automáticas de esquema, tipo o negocio) deben resolver solos los casos claros; reserva las interrupciones (`interrupt`) para decisiones que de verdad requieren juicio humano, como aprobar una propuesta económica antes de enviarla a un cliente. Y cuando interrumpas, hazlo de forma acotada: la interrupción debe pausar únicamente la rama del grafo que depende de esa aprobación (la sección de ese departamento y lo que dependa de ella), no el flujo completo — un departamento esperando el visto bueno de su gerente no debería frenar a los demás que ya están listos para avanzar.

### 🗺️ Referencia visual: tickets de aprobación y síntesis del documento final

Cuando los tickets de asignación por departamento de la Parte 2 están **totalmente aprobados**, un **ultimate document synthesizer** compila el documento final acordado y lo entrega a Ventas — las ramas por departamento aprueban de forma independiente y luego convergen:

![Aprobación y cierre del documento: tickets de asignación por departamento con estado de aprobación convergen en el ultimate document synthesizer, que produce el documento final acordado para el equipo de Ventas](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-agentic-workflows-produce/.learn/approval-document-completion.jpg)

---

## 🌱 Cómo Empezar el Proyecto

Continúa sobre tu rama del Hito 9 en el fork del monorepo de tu empresa, a partir de donde entregaste la Parte 2. Si todavía no tienes tu fork, créalo desde el [monorepo base](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo).

1. Crea la rama `feature/hito-9-parte-3-aprobacion-documento` a partir de tu rama de la Parte 2.
2. Configura el checkpointer que corresponda a tu entorno (SQLite o Postgres — evita el checkpointer en memoria salvo en desarrollo local).
3. Instala cualquier dependencia nueva con `uv add`.
4. Revisa tu `CONTEXT-company.md` para conocer la jerarquía de aprobación por departamento de tu empresa.

---

## 💻 Lo Que Debes Hacer

**Aprobación humana por departamento**

- [ ] Implementa un punto de interrupción (`interrupt`) antes de dar por aprobada la sección de cada departamento
- [ ] La interrupción debe pausar únicamente la rama del grafo correspondiente a ese departamento, sin bloquear el avance de los departamentos que ya están listos
- [ ] Persiste el estado del flujo con un checkpointer antes de cada interrupción, para que la ejecución sea reanudable
- [ ] Implementa el `resume` como un punto de entrada explícito del grafo — no como un reinicio del flujo completo
- [ ] Valida la respuesta humana al reanudar (aprobar, rechazar o solicitar cambios) antes de dejarla entrar de nuevo al grafo
- [ ] Extiende la interfaz de ticket construida en la Parte 1 (`uis/backoffice`) para que cada departamento pueda registrar su aprobación o rechazo

**Guardrails y control de flujo**

- [ ] Define un límite máximo de iteraciones en cualquier ciclo restante entre departamentos
- [ ] Implementa un nodo de arbitraje explícito para resolver desacuerdos entre departamentos, en lugar de dejar que los agentes lo resuelvan entre ellos
- [ ] Registra en el estado, para cada ejecución de nodo, el agente, el input, el output y el timestamp (trazabilidad)

**Cierre del documento**

- [ ] Cuando todos los departamentos dan su aprobación, genera el documento final consolidando las secciones aprobadas
- [ ] Actualiza el ticket a su estado final (por ejemplo: `terminado`) y deja accesible el documento generado

**Revisión de extremo a extremo**

- [ ] Corre al menos una RFP de prueba a través de las tres partes completas (recepción → generación → aprobación y cierre) y confirma que los estados del ticket, los mensajes y los datos se mantengan consistentes de principio a fin
- [ ] Corrige cualquier salto, mensaje inconsistente o dato que se pierda en la transición entre partes

⚠️ **IMPORTANTE:** La jerarquía de aprobación por departamento y el formato del documento final deben coincidir con lo especificado en tu `CONTEXT-company.md`. Una implementación genérica que ignore el contexto no será aceptada.

**Pruebas**

- [ ] Incluye pruebas unitarias en `tests/pipelines/` que cubran: interrupción y reanudación exitosa, límite de iteraciones alcanzado, y arbitraje ante desacuerdo

---

## 🧭 Preguntas de Diseño

- ¿Qué pasa si un departamento rechaza su sección después de la interrupción? ¿El flujo vuelve al generador de la Parte 2 o requiere una nueva ejecución?
- ¿Cómo haces _namespacing_ de tu `thread_id` para que ejecuciones concurrentes de distintas RFPs no corrompan el checkpoint de otra?
- ¿Qué información mínima necesita ver un humano en el punto de aprobación para decidir con confianza, sin tener que releer todo el documento?
- Si dos departamentos que dependen entre sí dan resultados contradictorios, ¿quién arbitra y con qué regla?

---

## ✅ Lo Que Evaluaremos

- [ ] El flujo se pausa correctamente antes de la aprobación de cada departamento y persiste su estado
- [ ] La pausa afecta solo la rama del departamento correspondiente — los demás departamentos pueden seguir avanzando sin bloquearse
- [ ] La ejecución se reanuda exactamente desde el punto de interrupción, sin reiniciar el flujo completo
- [ ] Existe un límite de iteraciones aplicado y verificable en el código, no solo mencionado
- [ ] Existe un nodo de arbitraje explícito para desacuerdos entre departamentos
- [ ] Cada ejecución de nodo queda registrada con agente, input, output y timestamp
- [ ] El documento final se genera automáticamente solo cuando todos los departamentos han dado su aprobación
- [ ] El ticket refleja el estado final del proceso y da acceso al documento generado
- [ ] Una RFP de prueba puede recorrerse de principio a fin (Parte 1 a Parte 3) sin saltos de estado ni inconsistencias visibles entre partes
- [ ] Existen pruebas unitarias para la interrupción/reanudación, el límite de iteraciones y el arbitraje

---

## 📦 Cómo Entregar

Esta es la Parte 3 de 3 del Hito 9. Entrégala con su propio Pull Request.

1. Haz commit y push de tu rama `feature/hito-9-parte-3-aprobacion-documento`
2. Abre un Pull Request describiendo qué implementaste y cómo probarlo
3. Incluye en la descripción del PR un ejemplo completo: RFP de entrada, aprobación simulada por cada departamento, y el documento final generado
4. Solicita revisión a tu tech lead

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
