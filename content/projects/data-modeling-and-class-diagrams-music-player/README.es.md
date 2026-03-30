# Reproductor de Listas de Música — Modelado de objetos

<!-- hide -->

Por [@ehiber](https://github.com/ehiber) y [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en inglés](./README.md)._

**Antes de comenzar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/como-iniciar-un-proyecto-de-programacion) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Una startup está construyendo una plataforma de streaming de música y necesita diseñar la capa de datos antes de escribir una sola línea de código de aplicación. Te han contratado como el ingeniero responsable de definir el modelo de objetos: el plano que los desarrolladores usarán para implementar el sistema.

La responsable de producto te ha dado una descripción breve de lo que la plataforma debe soportar:

> Los usuarios pueden crear múltiples listas de reproducción. Cada lista tiene un nombre y puede contener muchas canciones. Cada canción pertenece al menos a un álbum, y cada álbum tiene un artista. Las canciones pueden aparecer en más de una lista de reproducción, pero siempre pertenecen a un único álbum.

Tu trabajo no es escribir código todavía — es representar este sistema como un **diagrama de clases** que muestre claramente las entidades, sus propiedades tipadas y cómo se relacionan entre sí. Piensa en ello como el plano arquitectónico antes de comenzar la construcción.

Un modelo limpio y bien razonado ahora evita días de refactorización más adelante.

---

## 🌱 Cómo iniciar el proyecto

No se necesita ningún repositorio de código para este proyecto. Todo tu trabajo se realizará dentro de la herramienta de diagramas.

1. Abre [diagram.4geeks.com](https://diagram.4geeks.com/)
2. Crea un nuevo diagrama para este ejercicio
3. Modela tus entidades, añade propiedades tipadas a cada una y dibuja las relaciones entre ellas
4. Cuando termines, exporta el resultado como archivo PNG con el nombre `music-playlist-class-diagram.png`

---

## 💻 Qué debes hacer

- [ ] Identificar y crear al menos **5 modelos** (entidades) para el sistema
- [ ] Añadir cada propiedad con su **tipo de dato explícito** (ej. `name: string`, `duration: number`, `releaseDate: date`)
- [ ] Definir y dibujar las **relaciones** entre todos los modelos de forma clara — especifica qué entidades están conectadas y la naturaleza de cada relación (uno a uno, uno a muchos, muchos a muchos)
- [ ] Asegurarse de que el diagrama sea **legible y organizado** — los modelos no deben superponerse y las relaciones deben ser trazables
- [ ] Exportar el diagrama final como **`music-playlist-class-diagram.png`**

> Nota: Puedes incluir más de 5 modelos si el sistema que diseñas lo requiere. Punto de partida sugerido: `User`, `Playlist`, `Song`, `Album`, `Artist` — pero puedes nombrarlos y estructurarlos como consideres adecuado.

---

## ✅ Qué vamos a evaluar

- [ ] El diagrama contiene al menos 5 modelos distintos
- [ ] Cada propiedad en todos los modelos incluye un tipo de dato explícito
- [ ] Las relaciones entre modelos están presentes y correctamente tipadas (uno a muchos, muchos a muchos, etc.)
- [ ] El modelo refleja con precisión el sistema descrito en el brief — las relaciones tienen sentido lógico
- [ ] El diagrama es visualmente claro y está bien organizado
- [ ] El archivo está exportado y nombrado `music-playlist-class-diagram.png`

> Nota: La herramienta específica utilizada para producir el diagrama no se evalúa — solo la calidad y corrección del modelo en sí.

---

## 📦 Cómo entregar

Entrega tu archivo **`music-playlist-class-diagram.png`** siguiendo las instrucciones de entrega de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
