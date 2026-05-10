# Ejemplo en Clase: Gestor de Plazas de Aparcamiento

> **Nota para el instructor:** Este es un ejemplo en vivo para clase que enseña los conceptos del proyecto `seats-management-typescript`. Usa este escenario para demostrar arrays bidimensionales, recorrido de matrices y diseño de funciones en TypeScript. **No lo asignes como tarea — es un ejercicio guiado en el aula.**

_These instructions are also available in [English](./README.md)._

---

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


Un pequeño aparcamiento municipal con **4 filas y 6 plazas por fila** necesita una herramienta de gestión sencilla. El vigilante lleva actualmente el control de disponibilidad en una cuadrícula de papel. Tu equipo construirá un programa de línea de comandos en TypeScript que le permita al vigilante ver qué plazas están libres, reservar una plaza para un vehículo y encontrar dos plazas contiguas libres para vehículos de gran tamaño (por ejemplo, una furgoneta o remolque).

**Qué vas a aprender:**
- Cómo representar un espacio físico como un array bidimensional (matriz)
- Cómo recorrer y modificar una matriz con bucles y condicionales
- Cómo diseñar funciones con parámetros y valores de retorno en TypeScript
- Cómo buscar un patrón (celdas libres contiguas) dentro de una matriz

---

## Modelo de Datos

```
Fila 0:  [ 0, 0, 1, 0, 0, 1 ]
Fila 1:  [ 1, 0, 0, 0, 1, 0 ]
Fila 2:  [ 0, 0, 0, 1, 0, 0 ]
Fila 3:  [ 0, 1, 0, 0, 0, 0 ]
```

- `0` = plaza libre
- `1` = plaza ocupada

La visualización en consola usa `_` (libre) y `X` (ocupada), con etiquetas de fila y columna.

---

## Tareas

### Funciones Principales

- [ ] `initLot(): number[][]` — crea una matriz de 4×6 inicializada a `0` (todas las plazas libres)
- [ ] `displayLot(lot: number[][]): void` — imprime el aparcamiento en consola con etiquetas de fila y columna:

  ```
      C0  C1  C2  C3  C4  C5
  F0 [  _   _   X   _   _   X ]
  F1 [  X   _   _   _   X   _ ]
  ...
  ```

- [ ] `reserveSpace(lot: number[][], row: number, col: number): string` — marca una plaza como ocupada (`0 → 1`); devuelve `"Reservada F{row}C{col}"` o `"Plaza ya ocupada"` si estaba tomada
- [ ] `countSpaces(lot: number[][]): { free: number; occupied: number }` — devuelve el conteo de plazas libres y ocupadas

### Función Avanzada

- [ ] `findAdjacentPair(lot: number[][]): [number, number][] | null` — busca en cada fila dos plazas libres consecutivas (`0, 0`) y devuelve sus posiciones `[fila, columna]`; devuelve el primer par encontrado, o `null` si no hay ninguno

### Escenarios de Prueba

Ejecuta tu programa con estos cuatro estados e imprime el aparcamiento después de cada uno:

- [ ] Aparcamiento vacío — todas las plazas libres
- [ ] Parcialmente ocupado (establece manualmente algunas plazas a `1`)
- [ ] Casi lleno (solo una o dos plazas aisladas libres)
- [ ] Completamente lleno — confirma que `findAdjacentPair` devuelve `null`

---

## Salida Esperada por Consola (Ejemplo)

```
=== ESTADO DEL APARCAMIENTO ===
      C0  C1  C2  C3  C4  C5
  F0 [  _   _   X   _   _   X ]
  F1 [  X   _   _   _   X   _ ]
  F2 [  _   _   _   X   _   _ ]
  F3 [  _   X   _   _   _   _ ]

Libres: 16  |  Ocupadas: 8

Reservando F0C0... Reservada F0C0
Reservando F0C0 de nuevo... Plaza ya ocupada

Par contiguo para vehículo grande: F0C3 y F0C4
```

---

## Restricciones

> ⚠️ **No uses** clases ni objetos para almacenar los datos del aparcamiento. La matriz debe ser un `number[][]` simple. Usa parámetros de función y valores de retorno para pasar el estado entre funciones.

---

## Preguntas de Discusión

1. ¿Por qué un array bidimensional es una representación natural para un aparcamiento? ¿Qué problema habría si usaras un array unidimensional plano en su lugar?
2. La función `reserveSpace` actualmente solo reserva plazas, nunca las libera. ¿Cómo añadirías una función `releaseSpace` y qué validación necesitaría?
3. Si el aparcamiento creciera a 100 filas × 200 columnas, ¿qué función se volvería más lenta? ¿Cómo podrías optimizarla?
