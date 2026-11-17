---
title: "Cómo están estructurados los proyectos"
description: "Aprende a leer cualquier proyecto del curso: qué significa cada sección del README (tu reto, cómo empezar, qué debes hacer, qué evaluaremos, cómo entregar) y cómo usarlas con tu agente de código en las fases Ask → Plan → Agent."
author: "@ehiber"
tags: ["AI Engineering", "Proyectos", "Agentes de código", "Primeros pasos"]
---

# Cómo están estructurados los proyectos

<!-- hide -->

_These instructions are also available in [English](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/lessons/how-projects-are-structured/how-projects-are-structured.md)._

<!-- endhide -->

Abres tu primer proyecto y te encuentras con un README largo: un reto, una lista de pasos, otra lista de tareas con casillas, una lista de cosas que se van a evaluar y unas instrucciones de entrega. Es fácil sentir que todo pesa lo mismo y que tienes que entenderlo todo antes de escribir una sola línea. O lo contrario: copiar el README completo en el agente de código y esperar que salga algo.

Ninguna de las dos funciona. Cada sección del README tiene un **propósito distinto** y merece un **nivel de atención distinto**. Esta lección te enseña a leerlas así, para que pongas tu energía donde está el aprendizaje: **entender el problema y construir una solución**.

## Qué vas a lograr

- Reconocer las cinco secciones que tienen todos los proyectos y saber para qué sirve cada una.
- Distinguir lo que tienes que **pensar** (el reto y la evaluación) de lo que solo tienes que **seguir** (cómo empezar y cómo entregar).
- Usar cada sección en el momento correcto del trabajo con tu agente de código: **Ask → Plan → Agent**.

## La idea central: un proyecto es un viaje

Piensa en cada proyecto como un viaje en coche. Hay un punto de partida, un destino, una ruta sugerida y un lugar donde dejas el coche al final. Pero lo más importante es saber **por qué** viajas y **adónde** quieres llegar.

```mermaid
flowchart LR
  start["🌱 Cómo empezar<br/>(punto de partida)"]
  challenge["🎯 Tu reto<br/>(por qué viajas)"]
  todo["💻 Qué debes hacer<br/>(ruta sugerida)"]
  eval["✅ Qué evaluaremos<br/>(el destino)"]
  submit["📦 Cómo entregar<br/>(dejar el coche)"]
  start --> challenge
  challenge --> todo
  todo --> eval
  eval --> submit
```

En el README, **Tu reto** aparece antes que **Cómo empezar**, porque primero tienes que saber de qué va el proyecto. En la práctica las dos se leen casi a la vez: preparas el entorno mientras entiendes el problema.

## Las cinco secciones, una por una

### 🎯 Tu reto: entiende el problema y empieza desde aquí

Esta es la sección más importante del proyecto. Cuenta **qué problema existe, para quién y por qué importa**. A veces viene como una historia (un amigo artista necesita una web), a veces como un ticket o un brief de tu tech lead, y casi siempre incluye restricciones: cosas que *no* puedes hacer o reglas que tu solución tiene que respetar.

Muchos retos incluyen además bloques **📚 Conocimiento complementario**. Explican el concepto que necesitas para resolver el problema (una máquina de estados, qué es un ORM, el problema N+1…). No son lectura opcional: son la teoría mínima para que entiendas lo que vas a construir.

Cómo leerla:

- Léela **despacio y más de una vez**. Subraya los verbos ("debe", "no puede", "siempre", "nunca"): ahí están las reglas.
- Intenta explicar el problema con tus propias palabras en dos o tres frases. Si no puedes, todavía no lo entendiste.
- Anota lo que no entiendes. Esas dudas son las primeras preguntas para tu agente o tu mentor.

> 💡 Si solo vas a dedicar tiempo de calidad a una sección, que sea esta. Un agente de código puede escribir código por ti, pero no puede entender el problema por ti.

### 🌱 Cómo empezar: sigue los pasos

Aquí te dicen qué repositorio abrir, si tienes que hacer fork o usar una plantilla, si abrirlo en Codespaces, qué dependencias instalar y qué archivo leer primero.

Esta sección **no se interpreta, se sigue**. Está escrita para que arranques sin tener que tomar decisiones. Si un paso no funciona o no lo entiendes, no te quedes bloqueado buscando la manera "perfecta" de empezar: **pregunta** a tu mentor, a tus compañeros o a tu agente y sigue avanzando.

> ⚠️ Quedarse paralizado en "cómo empiezo" es una de las formas más comunes de perder un día entero. El inicio ya está resuelto para ti: úsalo.

### 💻 Qué debes hacer: una ruta, no la única

Es una lista de tareas, a menudo con casillas, nombres de archivos, endpoints o funciones concretas. Parece la parte más "real" del proyecto, pero tómala **con pinzas**.

Piensa en ella como la ruta que te propone Google Maps: es una buena referencia y suele ser el camino más directo, pero **no es el único camino posible**. Además, gran parte de estas tareas las va a ejecutar tu **agente de código**, no tú escribiendo línea por línea.

Cómo usarla:

- Úsala para entender **qué piezas** tendrá la solución y cómo se relacionan.
- Pásasela al agente como **contexto** durante la fase de planificación, no como una orden para ejecutar a ciegas.
- Si el agente propone otro camino que también llega al destino (ver la siguiente sección), está bien, siempre que **sepas explicar por qué** funciona.

### ✅ Qué evaluaremos: el destino

Esta lista es **el destino del viaje**. Es contra lo que se revisa tu entrega, así que es tu checklist personal antes de entregar.

Cómo usarla:

- Léela **al principio**, justo después del reto. Saber adónde vas cambia cómo planificas.
- Durante el trabajo, compara cada avance con esta lista: ¿esto me acerca a algún punto?
- Antes de entregar, revísala punto por punto y comprueba que tu proyecto **cumple** cada uno. No basta con "creo que sí": ábrelo, ejecútalo, compruébalo.

> 💡 Un buen ejercicio es pedirle al agente, en modo Ask, que revise tu proyecto contra esta lista y te diga qué falta. Pero la decisión final de si se cumple es tuya.

### 📦 Cómo entregar: sigue los pasos

Igual que **Cómo empezar**, esta sección son pasos que se siguen sin demasiado cuestionamiento: hacer commit y push, abrir un Pull Request, comprobar que `.env` no se sube, añadir una captura, entregar la URL en la plataforma…

Puedes consultar siempre que lo necesites, pero no conviertas la entrega en un problema nuevo. Es el punto de llegada.

### Dónde poner tu energía

| Sección | Qué es | Cómo tratarla |
| --- | --- | --- |
| 🎯 Tu reto | El problema | **Pensar a fondo** |
| 🌱 Cómo empezar | El punto de partida | Seguir los pasos |
| 💻 Qué debes hacer | Una ruta sugerida | Usar como referencia |
| ✅ Qué evaluaremos | El destino | **Contrastar con tu trabajo** |
| 📦 Cómo entregar | El punto de llegada | Seguir los pasos |

Cómo empezar y cómo entregar son el **inicio y el fin**. Lo que está en medio (entender el problema y construir la solución) es donde realmente aprendes.

## Trabajar el proyecto con tu agente: Ask → Plan → Agent

Durante el curso trabajas con un agente de código en tres fases. Cada sección del README encaja en una de ellas:

```mermaid
flowchart LR
  ask["Ask<br/>Entender"]
  plan["Plan<br/>Diseñar la ruta"]
  agent["Agent<br/>Construir"]
  check["Revisar contra<br/>✅ Qué evaluaremos"]
  ask --> plan
  plan --> agent
  agent --> check
  check -->|falta algo| plan
```

1. **Ask (entender).** Aquí trabajas con **🎯 Tu reto** y **✅ Qué evaluaremos**. Pregúntale al agente lo que no entiendes: conceptos, restricciones, términos nuevos. Todavía no se escribe código. El objetivo es que *tú* entiendas el problema.
2. **Plan (diseñar la ruta).** Ahora entra **💻 Qué debes hacer**. Pide al agente un plan para resolver el reto y cumplir la evaluación, usando la lista de tareas como referencia. Lee el plan, cuestiónalo y ajústalo. Si no entiendes un paso del plan, vuelve a Ask.
3. **Agent (construir).** Con el plan aprobado, deja que el agente implemente. Tu trabajo es revisar lo que hace, ejecutarlo y comprobar que tiene sentido.
4. **Revisar.** Compara el resultado con **✅ Qué evaluaremos**. Si falta algo, vuelve a planificar esa parte.

**🌱 Cómo empezar** ocurre antes de este ciclo y **📦 Cómo entregar**, después. No necesitan un plan: son los pasos de entrada y salida.

## Una forma práctica de leer cualquier proyecto

Cuando abras un proyecto nuevo, prueba este orden:

1. Lee **🎯 Tu reto** completo, incluidos los bloques de conocimiento complementario.
2. Lee **✅ Qué evaluaremos** para saber adónde tienes que llegar.
3. Sigue **🌱 Cómo empezar** hasta tener el entorno listo.
4. Echa un vistazo a **💻 Qué debes hacer** para hacerte una idea de las piezas.
5. Trabaja con tu agente en **Ask → Plan → Agent**.
6. Revisa tu trabajo contra **✅ Qué evaluaremos**.
7. Sigue **📦 Cómo entregar**.

## Checklist antes de empezar cualquier proyecto

- [ ] Leí **🎯 Tu reto** completo y puedo explicar el problema con mis palabras.
- [ ] Leí los bloques de **📚 Conocimiento complementario**.
- [ ] Leí **✅ Qué evaluaremos** y sé cuál es el destino.
- [ ] Seguí **🌱 Cómo empezar** y mi entorno funciona (o ya pregunté lo que no funcionaba).
- [ ] Empecé con el agente en **Ask**, no directamente en **Agent**.

## Conclusión

Los proyectos no son listas de tareas para tachar: son **problemas para resolver**. La estructura del README está pensada para quitarte de encima lo que no es importante (cómo empezar y cómo entregar ya están resueltos) y para que dediques tu atención a lo que sí lo es: **entender el reto, saber cuál es el destino y construir una solución con tu agente** que puedas explicar.

Empieza siguiendo los pasos. Entiende el problema. Planifica la ruta. Construye. Comprueba que llegaste. Entrega.
