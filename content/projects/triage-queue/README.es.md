# Triage Queue — Gestor de Cola de Prioridad

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/triage-queue/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

El departamento de informática de un hospital público ha recibido el encargo de modernizar el proceso de triaje en su unidad de urgencias. Actualmente, una enfermera apunta manualmente los nombres de los pacientes en una pizarra y los llama por orden de llegada. Esto genera caos cuando llega un caso crítico y hay que saltarse la cola, o cuando dos personas intentan actualizar la pizarra al mismo tiempo y se borra una entrada.

El responsable técnico del hospital te ha entregado una especificación con lo que debe hacer el nuevo gestor de colas de triaje. El sistema correrá en terminal por ahora — sin interfaz gráfica, solo un programa limpio en Python que modele y opere la cola correctamente, listo para integrarse más adelante en una aplicación mayor.

> La especificación del responsable técnico dice lo siguiente:
>
> #### Entrada de pacientes
>
> - Cuando llega un nuevo paciente, se le asigna un **nivel de triaje** (1 = crítico, 2 = urgente, 3 = estándar).
> - Se deben registrar el nombre del paciente, el momento de llegada y el nivel de triaje.
>
> #### Orden de atención
>
> - Los pacientes con nivel 1 siempre se atienden antes que los de nivel 2, y estos antes que los de nivel 3.
> - Dentro del mismo nivel de triaje, los pacientes se atienden en **orden de llegada** (FIFO).
>
> #### Operaciones requeridas
>
> - Encolar: añadir un nuevo paciente.
> - Desencolar: llamar al siguiente paciente para ser atendido.
> - Peek: mostrar quién es el siguiente sin retirarlo de la cola.
> - Listar cola: mostrar todos los pacientes en espera, en el orden en que serán atendidos.
> - Stats: reportar el número de pacientes en espera por nivel de triaje.

Una `deque` simple no será suficiente aquí — tendrás que pensar con cuidado cómo modelar una cola de prioridad y qué estructura de datos soporta mejor las operaciones requeridas. Piensa en qué ocurre si llega un paciente de nivel 1 mientras la cola se está procesando: ¿cómo garantizas que se coloca correctamente sin reordenar toda la cola en cada inserción?

Este tipo de problema aparece constantemente en sistemas en producción — planificación de jobs, enrutamiento de tickets de soporte, procesamiento de eventos de webhook. Constrúyelo con cuidado y tendrás algo real de lo que hablar en tu próxima entrevista técnica.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no requiere repositorio de plantilla — lo construirás desde cero.

1. Crea un nuevo repositorio en GitHub llamado `triage-queue`.
2. Clónalo localmente o ábrelo en un GitHub Codespace.
3. Crea un archivo `triage_queue.py` como punto de entrada.
4. Revisa la guía de [cómo iniciar un proyecto de programación](https://4geeks.com/lesson/how-to-start-a-project) si lo necesitas.

---

## 💻 Qué debes hacer

### Modelo de datos

- [ ] Define una clase `Patient` (o dataclass) con al menos: `name`, `triage_level` (int, 1–3) y `arrived_at` (timestamp).
- [ ] Define una clase `TriageQueue` que gestione internamente la lógica de cola de prioridad.

### Operaciones de cola

- [ ] `enqueue(patient)` — añade un paciente; la posición en la cola debe respetar el nivel de triaje y el orden de llegada.
- [ ] `dequeue()` — extrae y devuelve el siguiente paciente a ser atendido; debe lanzar un error descriptivo si la cola está vacía.
- [ ] `peek()` — devuelve el siguiente paciente sin extraerlo.
- [ ] `list_queue()` — devuelve todos los pacientes en espera en orden de atención como una lista.
- [ ] `stats()` — devuelve un diccionario con el número de pacientes en espera por nivel de triaje.

### Interacción por CLI

- [ ] Construye un menú de texto simple (en bucle) que permita a un usuario:
  - Añadir un nuevo paciente (solicitar nombre y nivel de triaje).
  - Llamar al siguiente paciente.
  - Ver la cola actual.
  - Ver estadísticas de la cola.
  - Salir.

### Correctitud y casos borde

- [ ] Un paciente crítico (nivel 1) que llega mientras hay pacientes de nivel 2 y 3 esperando debe colocarse delante de ellos.
- [ ] Dos pacientes con el mismo nivel de triaje deben atenderse en estricto orden de llegada.
- [ ] Llamar a `dequeue()` o `peek()` sobre una cola vacía no debe romper el programa — gestiónalo con gracia.

### Notas de diseño (no se requiere código — incluye como comentarios o en un `DESIGN.md`)

- [ ] Explica brevemente por qué elegiste tu estructura de datos interna frente a alternativas (p. ej., una sola `deque`, una lista ordenada, tres colas separadas).
- [ ] Describe cómo gestionarías el caso en que un worker extrae un paciente de la cola en el mismo momento en que otro worker encola un nuevo paciente crítico. ¿En qué orden mutas el estado para evitar el doble procesamiento?

⚠️ **IMPORTANTE:** Usa únicamente la biblioteca estándar de Python (`collections.deque`, `heapq`, `datetime`). Sin paquetes externos.

---

## ✅ Qué vamos a evaluar

- [ ] `TriageQueue` modela correctamente una cola de prioridad: nivel 1 siempre antes que nivel 2, nivel 2 siempre antes que nivel 3.
- [ ] Dentro del mismo nivel de triaje, el orden FIFO se preserva estrictamente.
- [ ] Las cinco operaciones (`enqueue`, `dequeue`, `peek`, `list_queue`, `stats`) están implementadas y funcionan correctamente.
- [ ] Los casos borde están gestionados: desencolar/peek sobre cola vacía no rompe el programa; niveles de triaje duplicados se ordenan por llegada.
- [ ] El código está organizado en clases con responsabilidades claras (sin lógica volcada en `main()`).
- [ ] La nota de diseño explica la elección de la estructura de datos con una razón concreta.
- [ ] La nota de diseño aborda el escenario de mutación concurrente, aunque sea de forma informal.
- [ ] El bucle de CLI funciona y no rompe ante entradas inválidas.

> Nota: la persistencia (guardar en archivo o base de datos) no es requerida y no será evaluada.

---

## 📦 Cómo entregar

Sube tu repositorio a GitHub y comparte el enlace según las instrucciones de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
