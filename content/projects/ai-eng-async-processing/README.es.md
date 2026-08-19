# Plataforma – Procesamiento Asíncrono

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa — no en un repositorio nuevo.

Tu CTO abre un **ticket** después de que un proveedor externo (pasarela de notificación, servicio de terceros, lo que tu sistema ya integre) tuvo una caída de unos minutos. Durante ese tiempo, varias operaciones que dependían de ese proveedor simplemente fallaron y se perdieron — nadie se enteró hasta que un cliente preguntó por qué nunca recibió una confirmación.

> *"No puedo seguir teniendo operaciones que dependen de un servicio externo ejecutándose dentro del mismo ciclo de petición-respuesta del usuario. Si ese servicio tarda o falla, quiero que la operación se reintente sola, sin perderse y sin que el usuario tenga que notar nada. Y si después de varios intentos sigue fallando, quiero saberlo — no quiero que desaparezca en silencio."*
>
> — CTO

Tres exigencias del brief que definen el proyecto:

1. **Fuera del ciclo petición-respuesta.** La operación se encola y un worker la procesa de forma independiente — el usuario no debe esperar a que el proveedor externo responda para recibir su confirmación.
2. **Reintentos con backoff, no reintentos ciegos.** Reintentar inmediatamente y sin límite puede agravar una caída del proveedor externo. El sistema debe esperar progresivamente más entre intentos.
3. **Nada se pierde en silencio.** Una operación que falla definitivamente después de varios intentos debe terminar en un lugar visible (una cola de mensajes fallidos), no simplemente desaparecer del sistema.

### Conocimiento complementario: idempotencia, el problema que nadie ve hasta que ya es tarde

Cuando una operación se reintenta automáticamente, existe un riesgo silencioso: que el intento anterior sí haya tenido éxito del lado del proveedor externo, pero la confirmación nunca llegó a tiempo — y el sistema, al no saberlo, reintenta y ejecuta la misma operación dos veces. Si esa operación es "enviar una notificación", el resultado es molesto. Si es "cobrar a un cliente" o "descontar inventario", el resultado es un incidente. La idempotencia es la propiedad que evita esto: diseñar la operación de forma que ejecutarla dos veces con la misma clave produzca el mismo resultado que ejecutarla una sola vez, normalmente mediante una clave de idempotencia única por operación que el sistema verifica antes de procesar.

---

## 🌱 Cómo Empezar el Proyecto

1. Haz `pull` de los últimos cambios de tu fork del monorepo.
2. Identifica en tu sistema actual qué operaciones dependen de servicios externos y hoy se ejecutan de forma síncrona dentro del ciclo de petición-respuesta.
3. Crea una rama nueva: `feature/async-processing`.
4. Elige una operación candidata concreta de tu sistema para migrar a este patrón (no hace falta migrar todas).
5. Diseña primero el contrato del mensaje de la cola (qué datos necesita el worker para procesar la tarea de forma independiente) antes de escribir el worker.

---

## 💻 Qué Debes Hacer

**Infraestructura de colas**

- [ ] Configura un sistema de colas (por ejemplo Redis con RQ/Celery, o el gestor de colas que ya uses en tu stack)
- [ ] Implementa al menos un worker que consuma la cola de forma independiente del proceso principal de la API

**Reintentos y resiliencia**

- [ ] Implementa reintentos automáticos con backoff exponencial ante fallos del servicio externo
- [ ] Define un número máximo de reintentos, después del cual la tarea se considera fallida definitivamente
- [ ] Implementa una cola de mensajes fallidos (dead-letter queue) donde caen las tareas que agotaron sus reintentos

**Idempotencia**

- [ ] Implementa una clave de idempotencia por operación encolada
- [ ] Verifica, antes de procesar una tarea, que esa clave no fue ya procesada exitosamente
- [ ] Escribe una prueba que demuestre que encolar la misma operación dos veces con la misma clave no produce el efecto duplicado

**Observabilidad mínima**

- [ ] Expón el estado de una tarea encolada (pendiente, en proceso, completada, fallida) de forma consultable
- [ ] Registra cuántos reintentos tuvo cada tarea antes de completarse o fallar definitivamente

---

## ✅ Qué Vamos a Evaluar

- [ ] Al menos una operación real de tu sistema se ejecuta de forma asíncrona a través de la cola, fuera del ciclo de petición-respuesta
- [ ] Un fallo simulado del servicio externo dispara reintentos con backoff, verificable en los logs o en el estado de la tarea
- [ ] Una tarea que agota sus reintentos termina en la dead-letter queue, no desaparece
- [ ] Encolar la misma operación dos veces con la misma clave de idempotencia no produce el efecto duplicado, demostrado con una prueba
- [ ] El estado de cualquier tarea encolada es consultable

---

## 📦 Cómo Entregar

Abre un Pull Request desde tu rama `feature/async-processing` hacia `main` en tu fork. En la descripción del PR incluye qué operación migraste al patrón asíncrono y por qué, y evidencia de la prueba de idempotencia. Solicita el sign-off de tu CTO antes de hacer merge.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
