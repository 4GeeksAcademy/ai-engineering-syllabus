# Ejemplo de clase: Auditoría de inventario de librería

> **Nota para el instructor:** Este es un ejemplo de clase para introducir los conceptos del proyecto *Analizador de Incidencias* usando un dominio más sencillo. Cubre el mismo stack y los mismos patrones (script de análisis de CSV con validación y métricas, lógica compartida, API REST para subida de ficheros, interfaz web), pero está pensado para una sesión en vivo de 1 a 2 horas. NO compartir este archivo con los estudiantes antes de que intenten el proyecto principal.

_These instructions are also available in [English](./README.md)._

---

## El escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


Una pequeña librería independiente ha exportado su inventario actual como un fichero CSV con 25 registros. Antes de importar estos datos en el nuevo sistema de gestión, el equipo necesita validarlos y generar un resumen rápido: cuántos libros hay en cada género, cuál es el precio medio según el estado, y cuántos registros tienen problemas.

El análisis debe ejecutarse localmente — el fichero contiene precios de coste que no pueden enviarse a una herramienta externa.

El proceso tiene dos fases: primero un script Python rápido para confirmar que la lógica funciona, y después integrar esa misma lógica en una pequeña herramienta web para que cualquier miembro del equipo pueda ejecutar la auditoría desde el navegador.

---

## Fase 1 — Script de análisis (`analyze.py`)

### CSV de ejemplo

Guarda esto como `books.csv` para usarlo durante la sesión:

```csv
isbn,title,genre,price,stock,status
978-0-06-112008-4,To Kill a Mockingbird,fiction,12.99,5,available
978-0-7432-7356-5,The Great Gatsby,fiction,10.50,3,available
978-0-14-028329-7,Of Mice and Men,fiction,9.99,0,out_of_stock
978-0-39-474673-7,,non-fiction,24.99,2,available
978-0-06-093546-9,Thinking Fast and Slow,non-fiction,18.00,7,available
978-0-14-303943-3,The Odyssey,fiction,11.25,1,available
978-0-19-953556-4,Oxford English Dictionary,reference,45.00,1,available
978-1-40-881274-1,Harry Potter 1,children,14.99,12,available
978-1-40-881275-8,Harry Potter 2,children,14.99,8,available
978-0-14-028726-7,Animal Farm,fiction,8.50,4,available
978-0-14-044913-6,The Alchemist,fiction,-3.00,2,available
978-0-374-52804-1,Sapiens,non-fiction,19.99,0,out_of_stock
978-0-06-192028-5,Quiet,non-fiction,16.50,5,available
978-0-385-33348-1,The Giver,children,11.00,6,available
978-0-06-093548-3,Atomic Habits,non_fiction,17.99,10,available
978-0-7432-7357-2,1984,fiction,10.00,3,damaged
978-0-14-028727-4,Lord of the Flies,,9.25,2,available
978-0-374-52805-8,Educated,non-fiction,20.00,4,available
978-0-316-76948-0,The Catcher in the Rye,fiction,10.75,1,available
978-1-50-117606-0,Dune,fiction,15.00,9,available
978-0-06-112009-1,Brave New World,fiction,11.50,2,available
978-0-14-028728-1,The Road,fiction,12.00,0,out_of_stock
978-0-375-70737-9,The Kite Runner,fiction,13.50,5,available
978-0-06-093547-6,Outliers,non-fiction,,3,available
978-0-385-47423-1,Ender's Game,comics,13.00,2,available
```

### Qué implementar

- [ ] El script acepta la ruta al CSV como argumento: `python analyze.py books.csv`
- [ ] Carga y lee el fichero (módulo `csv` nativo o `pandas` — a tu elección)
- [ ] Detecta y cuenta los **registros inválidos**. Un registro es inválido si:
  - `title` está vacío
  - `genre` no es uno de: `fiction`, `non-fiction`, `children`, `reference`, `comics`
  - `price` está vacío o es negativo
  - `status` no es uno de: `available`, `out_of_stock`, `damaged`
- [ ] Calcula las siguientes métricas solo sobre los **registros válidos**:
  - Total de registros válidos vs. inválidos
  - Recuento de libros por `genre`
  - Recuento de libros por `status`
  - Precio medio (`price`) de los libros con estado `available`
- [ ] Imprime el resumen por consola con etiquetas claras y separadores
- [ ] Al final, pregunta: `¿Exportar resultados a CSV? [s/n]`. Si `s`, guarda en `results.csv`

**Salida esperada (aproximada):**

```
=== Auditoría de Inventario de Librería ===
Total de registros: 25
Válidos: 21 | Inválidos: 4

-- Por género --
fiction       : 12
non-fiction   :  5
children      :  3
reference     :  1
comics        :  0

-- Por estado --
available     : 16
out_of_stock  :  3
damaged       :  2

-- Precios --
Precio medio (available): 14,12 €

-- Registros inválidos --
Fila 4  : título vacío
Fila 11 : precio negativo (-3,00)
Fila 15 : género inválido (non_fiction)
Fila 17 : género vacío
Fila 24 : precio vacío
```

---

## Fase 2 — Integración (FastAPI + Next.js)

Una vez validada la lógica del script, extrae la validación y las métricas en funciones compartidas.

**Backend:**

- [ ] `POST /api/books/analyze` — acepta un CSV como `multipart/form-data`, ejecuta la misma lógica y devuelve el resumen en JSON
- [ ] `GET /api/books/results/export` — devuelve el último análisis como CSV descargable
- [ ] Un fichero vacío o con formato incorrecto devuelve `400` con un mensaje descriptivo

**Frontend:**

- [ ] Componente de carga de fichero (selector o drag & drop) que envía el CSV a la API
- [ ] Muestra los resultados en pantalla: totales, desglose por género, por estado y precio medio
- [ ] Un botón para descargar el CSV de resultados
- [ ] Informa al usuario cuántos registros inválidos se encontraron y por qué motivo

**Lógica compartida:**

- [ ] Las funciones de validación y métricas son las mismas en el script y en la API — extraídas a un módulo compartido, sin duplicación

---

## Preguntas de discusión

1. El script detecta `non_fiction` (con guion bajo) como género inválido, aunque la intención es clara. ¿Debería el script autocorregir erratas obvias como esta, o rechazarlas siempre? ¿Cuáles son las ventajas e inconvenientes de cada enfoque?
2. Si la tienda sube un CSV con 500 registros y el endpoint de la API expira a mitad del procesamiento, ¿qué debería devolver la respuesta? ¿Cómo comunicarías resultados parciales al usuario?
3. ¿Por qué es importante extraer la lógica de análisis y validación a un módulo compartido en lugar de copiarla en la API? ¿Qué se rompe si las dos versiones divergen?
