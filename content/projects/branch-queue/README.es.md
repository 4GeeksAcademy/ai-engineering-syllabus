# Branch Queue — Gestor de Cola por Servicio

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/branch-queue/graphs/contributors) at [4Geeks Academy](https://4geeks.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Banco Meridional ha modernizado sus sucursales — los clientes toman un ticket numerado en la entrada y esperan sentados. Cada ticket está etiquetado con un tipo de servicio: **depósitos**, **retiros** o **gestión de cuenta**. La sucursal cuenta con agentes dedicados a cada tipo de servicio, y trabajan de forma independiente: el agente de depósitos llama a su siguiente cliente sin importar lo que esté haciendo el agente de retiros.

La responsable de operaciones ha detectado un problema con el sistema en papel actual: cuando el agente de depósitos termina con un cliente y las únicas personas esperando son de retiros, el agente de depósitos se queda sin hacer nada aunque pudiera haber un cliente de depósitos que llegó antes pero está enterrado en la lista general. La sucursal necesita un sistema donde cada agente pueda llamar al siguiente cliente al instante, sin tener que recorrer toda la sala de espera.

El equipo de IT ha recibido el encargo de construir un gestor de colas en terminal para modelar este sistema antes de integrarlo en los quioscos táctiles de la sucursal.

> El documento de requisitos de la responsable de operaciones dice lo siguiente:
>
> #### Emisión de tickets
>
> - Un cliente toma un ticket especificando un **tipo de servicio**: `deposito`, `retiro` o `gestion_cuenta`.
> - El ticket debe registrar el nombre del cliente, el tipo de servicio y el momento de llegada.
> - Los tickets se numeran de forma secuencial a partir del 1 (contador global, entre todos los servicios).
>
> #### Operaciones de los agentes
>
> - Cada agente está asignado a exactamente un tipo de servicio.
> - Cuando un agente queda libre, llama al **siguiente cliente de su cola de servicio** — el que lleva más tiempo esperando para ese tipo de servicio.
> - Un agente no puede llamar a un cliente de una cola de servicio diferente.
>
> #### Operaciones requeridas del sistema
>
> - Emitir ticket: registrar un nuevo cliente en la cola de servicio correspondiente.
> - Llamar al siguiente: dado un tipo de servicio, desencolar y devolver el siguiente cliente que espera por él.
> - Peek siguiente: mostrar quién es el siguiente para un tipo de servicio sin retirarlo.
> - Listar en espera: mostrar todos los clientes en espera, agrupados por tipo de servicio, en el orden en que serán atendidos dentro de cada grupo.
> - Stats globales: reportar el número de clientes en espera por tipo de servicio y en total.

Piensa con cuidado cómo estructurar las colas internamente. Una única lista ordenada de todos los clientes requeriría recorrerla entera cada vez que un agente llama a su siguiente cliente — lo que se vuelve lento a medida que la sucursal se llena. Hay una estructura más simple que hace que la operación `llamar al siguiente` de cada agente sea instantánea, sin importar cuántas personas esperen para otros servicios. ¿Cuál es?

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no requiere repositorio de plantilla — lo construirás desde cero.

1. Crea un nuevo repositorio en GitHub llamado `branch-queue`.
2. Clónalo localmente o ábrelo en un GitHub Codespace.
3. Crea un archivo `branch_queue.py` como punto de entrada.
4. Revisa la guía de [cómo iniciar un proyecto de programación](https://4geeks.com/lesson/how-to-start-a-project) si lo necesitas.

---

## 💻 Qué debes hacer

### Modelo de datos

- [ ] Define una clase `Ticket` (o dataclass) con al menos: `number` (int, global secuencial), `client_name`, `service_type` (string: `"deposito"`, `"retiro"`, `"gestion_cuenta"`) y `issued_at` (timestamp).
- [ ] Define una clase `BranchQueue` que gestione una cola interna por tipo de servicio y un contador global de tickets.

### Operaciones de cola

- [ ] `issue_ticket(client_name, service_type)` — crea y encola un ticket en la cola de servicio correcta; devuelve el ticket emitido.
- [ ] `call_next(service_type)` — desencola y devuelve el siguiente cliente para ese tipo de servicio; debe lanzar un error descriptivo si no hay clientes esperando.
- [ ] `peek_next(service_type)` — devuelve el siguiente cliente para un tipo de servicio sin retirarlo.
- [ ] `list_waiting()` — devuelve un diccionario con cada tipo de servicio como clave y su lista ordenada de tickets en espera como valor.
- [ ] `stats()` — devuelve un diccionario con el número de clientes por tipo de servicio y una clave `"total"`.

### Interacción por CLI

- [ ] Construye un menú de texto simple (en bucle) que permita a un usuario:
  - Emitir un nuevo ticket (solicitar nombre del cliente y tipo de servicio).
  - Llamar al siguiente cliente para un tipo de servicio dado.
  - Ver la lista de espera completa agrupada por servicio.
  - Ver estadísticas de la cola.
  - Salir.

### Correctitud y casos borde

- [ ] Los números de ticket deben ser globalmente secuenciales — dos clientes no pueden compartir número aunque estén en colas de servicio distintas.
- [ ] Los clientes en la misma cola de servicio deben ser llamados en estricto orden de llegada.
- [ ] `call_next()` o `peek_next()` sobre una cola de servicio vacía no debe romper el programa.
- [ ] Un tipo de servicio inválido debe ser rechazado en la emisión del ticket con un mensaje claro.

### Notas de diseño (no se requiere código — incluye como comentarios o en un `DESIGN.md`)

- [ ] Explica por qué una cola separada por tipo de servicio hace que `call_next` sea más eficiente que una única cola compartida.
- [ ] Describe qué ocurriría si dos agentes del mismo tipo de servicio llamasen a `call_next` al mismo tiempo. ¿Qué mutación de estado debe ocurrir primero para garantizar que el mismo cliente no sea llamado dos veces?

⚠️ **IMPORTANTE:** Usa únicamente la biblioteca estándar de Python (`collections.deque`, `datetime`). Sin paquetes externos.

---

## ✅ Qué vamos a evaluar

- [ ] `BranchQueue` mantiene una cola interna por tipo de servicio.
- [ ] Los números de ticket son globalmente secuenciales entre todos los tipos de servicio.
- [ ] Dentro de cada cola de servicio, el orden FIFO se preserva estrictamente.
- [ ] Las cinco operaciones (`issue_ticket`, `call_next`, `peek_next`, `list_waiting`, `stats`) están implementadas y funcionan correctamente.
- [ ] Los casos borde están gestionados: cola vacía no rompe el programa; tipo de servicio inválido se rechaza con mensaje.
- [ ] El código está organizado en clases con responsabilidades claras.
- [ ] La nota de diseño explica por qué la estructura por servicio es más eficiente que una lista compartida única.
- [ ] La nota de diseño aborda el escenario de `call_next` concurrente e identifica el orden de mutación correcto.
- [ ] El bucle de CLI funciona y no rompe ante entradas inválidas.

> Nota: la persistencia, la autenticación o la asignación de agentes no son requeridas y no serán evaluadas.

---

## 📦 Cómo entregar

Sube tu repositorio a GitHub y comparte el enlace según las instrucciones de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeks.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeks.com/es/comparar-programas) de [Ingeniería de IA](https://4geeks.com/es/programas-de-carrera/ingenieria-ia) y [Agentes y Automatizaciones con IA](https://4geeks.com/es/programas-de-carrera/agentes-y-automatizaciones-con-inteligencia-artificial).
