> **Ejemplo para usar en clase (solo instructores).** Usa este escenario para introducir diagramas de clases con 5+ modelos en una sesión de ~1 hora. Este archivo es un recurso pedagógico con un *dominio diferente* al del proyecto asignado. No lo compartas con los estudiantes como su brief de proyecto.

_These instructions are also available in [English](./README.md)._

# Plataforma de Podcasts — Modelado de Objetos (Ejemplo en Clase)

## Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


Una startup está construyendo una app de streaming de podcasts. Antes de escribir ningún código, el equipo necesita un modelo de datos claro. La responsable de producto envió esta descripción:

> Los usuarios pueden suscribirse a varios podcasts. Cada podcast está organizado en temporadas, y cada temporada contiene muchos episodios. Un episodio siempre pertenece exactamente a una temporada. Los usuarios también pueden marcar episodios individuales para escucharlos más tarde. Un podcast tiene un título, un nombre de presentador y una categoría (p. ej. Tecnología, True Crime, Comedia). Un episodio tiene un título, una duración en segundos, una fecha de publicación y una URL de audio.

Tu tarea es representar este sistema como un **diagrama de clases** que muestre las entidades, las propiedades tipadas y todas las relaciones, incluyendo su naturaleza (uno a uno, uno a muchos, muchos a muchos).

---

## Qué modelar

### Entidades sugeridas

| Modelo | Descripción |
|--------|-------------|
| `User` | Un oyente registrado en la plataforma |
| `Podcast` | Un programa con título, presentador y categoría |
| `Season` | Una colección numerada de episodios dentro de un podcast |
| `Episode` | Un archivo de audio perteneciente a una temporada |
| `Bookmark` | Una referencia guardada que vincula a un usuario con un episodio |

### Propiedades tipadas de ejemplo

| Modelo | Propiedad | Tipo |
|--------|-----------|------|
| `User` | `id` | `int` |
| `User` | `username` | `string` |
| `User` | `email` | `string` |
| `Podcast` | `id` | `int` |
| `Podcast` | `title` | `string` |
| `Podcast` | `hostName` | `string` |
| `Podcast` | `category` | `string` |
| `Season` | `id` | `int` |
| `Season` | `number` | `int` |
| `Season` | `releaseYear` | `int` |
| `Episode` | `id` | `int` |
| `Episode` | `title` | `string` |
| `Episode` | `durationSeconds` | `int` |
| `Episode` | `publishedAt` | `date` |
| `Episode` | `audioUrl` | `string` |
| `Bookmark` | `id` | `int` |
| `Bookmark` | `createdAt` | `date` |

### Relaciones a dibujar

| Desde | Hacia | Tipo | Nota |
|-------|-------|------|------|
| `User` | `Podcast` | muchos-a-muchos | Un usuario se suscribe a muchos podcasts; un podcast tiene muchos suscriptores |
| `Podcast` | `Season` | uno-a-muchos | Un podcast tiene muchas temporadas |
| `Season` | `Episode` | uno-a-muchos | Una temporada tiene muchos episodios |
| `User` | `Episode` | muchos-a-muchos via `Bookmark` | Los marcadores vinculan usuarios con episodios |

---

## Lista de verificación

- [ ] Crear al menos **5 modelos** en la herramienta de diagramas
- [ ] Añadir cada propiedad con su **tipo de dato explícito**
- [ ] Dibujar las **relaciones** y etiquetar cada una con su cardinalidad (1:1, 1:N, N:M)
- [ ] Incluir al menos **una relación muchos-a-muchos**
- [ ] Asegurarse de que el diagrama sea **legible** — sin cajas superpuestas, con flechas trazables
- [ ] Exportar el resultado como **`podcast-platform-class-diagram.png`**

**Herramienta:** [diagram.4geeks.com](https://diagram.4geeks.com/)

---

## Preguntas de debate

1. La relación `User–Podcast` es de muchos a muchos (suscripciones). ¿Cómo modelarías la tabla intermedia si necesitaras almacenar la fecha de suscripción y si las notificaciones están activadas?
2. `Episode` pertenece a una `Season`, y una `Season` pertenece a un `Podcast`. ¿Necesita `Episode` una relación directa con `Podcast`, o basta con el camino indirecto a través de `Season`? ¿Cuándo importaría ese atajo directo?
3. Compara el modelo `Bookmark` (User ↔ Episode) con un simple array de IDs de episodios almacenado en el modelo `User`. ¿Qué ganas y qué pierdes con cada enfoque?
