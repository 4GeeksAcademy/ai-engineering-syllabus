# Cinema Seat Manager

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [@ehiber](https://github.com/ehiber) y [otros contribuidores](https://github.com/4GeeksAcademy/typescript-cinema-seat-manager/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

🌐 _Estas instrucciones también están [disponibles en inglés](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de programación.

> ¡Te necesitamos! Estos ejercicios se construyen y mantienen en colaboración con personas como tú. Si encuentras algún error 🐞 o falta de ortografía, por favor contribuye y/o repórtalo.

<!-- endhide -->

---

## 🎯 Tu reto

Un cine independiente local está inaugurando una nueva sala y ha contratado a tu equipo para construir un sistema sencillo de reserva de asientos. Actualmente, el personal lleva el control de la disponibilidad de asientos manualmente en cuadrículas de papel, lo que provoca confusiones en las funciones con mucha afluencia y dificulta responder rápido a las preguntas de los clientes.

La persona gerente del cine explicó la situación en la reunión de arranque del proyecto: "Tenemos una sala pequeña con 8 filas y 10 asientos por fila. Las personas llaman o vienen a la taquilla preguntando si hay asientos disponibles y, a menudo, quieren sentarse juntas, especialmente parejas que buscan dos asientos contiguos. Necesitamos algo sencillo con lo que nuestro personal pueda ver qué asientos están ocupados, reservar asientos para los clientes y encontrar rápidamente lugares disponibles".

Tu líder de equipo quiere que construyas un prototipo de línea de comandos en TypeScript antes de invertir en una interfaz web completa. El cine no necesita todavía funcionalidades avanzadas, solo una base sólida que maneje correctamente la lógica central. Si funciona bien, más adelante ampliarán el sistema con reservas en línea y mapas visuales de selección de asientos.

### ¿Qué hace que un buen sistema de reservas de asientos?

El reto clave es la **representación de datos**. Tienes que modelar la sala como una estructura bidimensional en la que cada posición represente un asiento con dos estados posibles: ocupado o disponible. Piensa en ello como una cuadrícula o matriz donde cada asiento tiene un número de fila y un número de columna.

En los sistemas de reserva reales, este tipo de representación en matriz es muy común porque refleja el diseño físico del espacio. Una vez que tengas los datos correctamente estructurados, las operaciones (reservar un asiento, contar la disponibilidad, encontrar asientos contiguos) se vuelven mucho más sencillas.

---

## 🌱 Cómo iniciar el proyecto

1. Asegúrate de tener una cuenta de GitHub en [https://github.com](https://github.com).

2. Usa el repositorio plantilla para proyectos en TypeScript:

   ```text
   https://github.com/4GeeksAcademy/typescript-hello
   ```

3. Puedes empezar a trabajar en Codespaces (recomendado) o clonar el repositorio para trabajar de forma local.

4. Crea tu propio repositorio y actualiza la URL del remoto para que apunte a tu repo en lugar de a la plantilla:

   ```bash
   git remote set-url origin <la-url-de-tu-nuevo-repositorio>
   ```

5. ¡Empieza a programar! Recuerda hacer commits con frecuencia a medida que completes cada funcionalidad.

📗 Instrucciones detalladas: [Cómo iniciar un proyecto de programación](https://4geeks.com/lesson/how-to-start-a-project)

---

## 💻 Qué debes hacer

Construye un programa en TypeScript que gestione las reservas de asientos de un cine usando arreglos y funciones.

### Funcionalidad principal

- [ ] Crea una función que inicialice una matriz de asientos (un arreglo bidimensional) que represente 8 filas y 10 columnas.
- [ ] Representa los asientos ocupados con `1` y los disponibles con `0`.
- [ ] Crea una función que muestre el estado actual de la sala imprimiendo la matriz en la consola, usando:
  - `X` para los asientos ocupados
  - `L` para los asientos libres
  - Incluye números de fila y columna para que sea fácil identificar cada posición
- [ ] Implementa una función para reservar un asiento dado un número de fila y un número de columna (márcalo como ocupado cambiando su valor de `0` a `1`).
- [ ] Añade validación: la función debe comprobar si el asiento ya está ocupado antes de reservarlo y devolver un mensaje indicando si la operación tuvo éxito o falló.
- [ ] Crea una función que cuente y devuelva cuántos asientos están ocupados y cuántos están disponibles en toda la sala.

### Funcionalidad avanzada

- [ ] Implementa una función que busque dos asientos libres contiguos (horizontalmente, en la misma fila) y devuelva sus posiciones.
- [ ] Si se encuentran varios pares de asientos contiguos, devuelve el primero.
- [ ] Si no hay asientos contiguos disponibles, la función debe indicarlo claramente.

### Pruebas y salida por consola

- [ ] Prueba tu programa con distintos escenarios:
  - Sala vacía (todos los asientos disponibles)
  - Sala parcialmente ocupada
  - Sala casi llena con solo asientos sueltos disponibles
  - Sala completamente llena (sin asientos disponibles)
- [ ] Asegúrate de que tu código muestre mensajes claros para cada operación (reserva confirmada, asiento ya ocupado, asientos contiguos encontrados, etc.).
- [ ] Agrega comentarios que expliquen qué hace cada función.

### 🎁 Reto extra (opcional)

Si terminas la funcionalidad principal y quieres ir un paso más allá:

- [ ] Pídele a tu asistente de IA que genere una interfaz web sencilla para tu gestor de asientos usando HTML y Tailwind, incluyendo tu archivo. Proporciónale tu código TypeScript como contexto y pídele que cree un mapa visual de asientos donde las personas usuarias puedan hacer clic para reservar en lugar de usar la consola.

⚠️ **IMPORTANTE:** No uses objetos ni clases en este proyecto. Representa los datos de los asientos usando **solo un arreglo bidimensional**. Usa formato JSON si necesitas estructurar datos adicionales (como metadatos de las reservas).

---

## ✅ Qué vamos a evaluar

- [ ] Uso correcto de un arreglo bidimensional (matriz) para representar los asientos del cine.
- [ ] Implementación adecuada de funciones con parámetros y valores de retorno.
- [ ] Uso correcto de sentencias condicionales (`if`, `else`) para validar la disponibilidad de los asientos.
- [ ] Uso correcto de bucles (`for`, `while`) para procesar y mostrar la matriz de asientos.
- [ ] Que la función de búsqueda identifique correctamente asientos contiguos libres de forma horizontal.
- [ ] Que el código sea legible, con nombres de variables y funciones significativos.
- [ ] Que el programa se ejecute sin errores y produzca la salida esperada al probarlo.
- [ ] Que la salida por consola sea clara y útil para el personal del cine que vaya a usar el sistema.

> **Nota:** La interfaz web opcional no forma parte de los criterios de evaluación. Es únicamente para tu propio aprendizaje y experimentación con herramientas de IA.

---

## 📦 Cómo entregar este proyecto

1. Sube tu código final a tu repositorio en GitHub.
2. Asegúrate de que tu repositorio sea público y accesible.
3. Entrega el enlace al repositorio siguiendo las indicaciones de tu instructor/a.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/data-science-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
