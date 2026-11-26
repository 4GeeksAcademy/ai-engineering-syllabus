# Billetera Digital — Modelado de objetos

<!-- hide -->

Por [@ehiber](https://github.com/ehiber) y [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) en [4Geeks Academy](https://4geeks.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en inglés](./README.md)._

**Antes de comenzar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/como-iniciar-un-proyecto-de-programacion) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Una empresa fintech está construyendo un producto de billetera digital — similar a Wise, Revolut o un servicio parecido — y necesita que su modelo de datos esté diseñado antes de que comience el desarrollo. Te han asignado para mapear las entidades principales que el sistema necesitará para funcionar.

El líder de ingeniería ha compartido un resumen breve de los requisitos:

> Un usuario puede tener una o más billeteras. Cada billetera mantiene un saldo en una moneda específica. Los usuarios pueden enviar y recibir dinero, y cada movimiento de fondos se registra como una transacción. Una transacción siempre tiene un origen, un destino, un monto, una moneda, una marca de tiempo y un estado (como pendiente, completada o fallida).

Tu entregable es un **diagrama de clases** que represente con precisión estas entidades, sus propiedades tipadas y las relaciones entre ellas. Este modelo será utilizado por el equipo de desarrollo como referencia para la implementación — la claridad y la precisión son importantes.

Piensa detenidamente en qué conecta una transacción y cómo encaja la moneda en el diseño.

---

## 🌱 Cómo iniciar el proyecto

No se necesita ningún repositorio de código para este proyecto. Todo tu trabajo se realizará dentro de la herramienta de diagramas.

1. Abre [diagram.4geeks.com](https://diagram.4geeks.com/)
2. Crea un nuevo diagrama para este ejercicio
3. Modela tus entidades, añade propiedades tipadas a cada una y dibuja las relaciones entre ellas
4. Cuando termines, exporta el resultado como archivo PNG con el nombre `digital-wallet-class-diagram.png`

---

## 💻 Qué debes hacer

- [ ] Identificar y crear al menos **3 modelos** (entidades) para el sistema
- [ ] Añadir cada propiedad con su **tipo de dato explícito** (ej. `balance: float`, `status: string`, `createdAt: date`)
- [ ] Definir y dibujar las **relaciones** entre todos los modelos de forma clara — especifica qué entidades están conectadas y la naturaleza de cada relación
- [ ] Asegurarse de que el diagrama sea **legible y organizado** — los modelos no deben superponerse y las relaciones deben ser trazables
- [ ] Exportar el diagrama final como **`digital-wallet-class-diagram.png`**

> Nota: Puedes incluir más de 3 modelos si tu diseño lo requiere. Punto de partida sugerido: `User`, `Wallet`, `Transaction`, `Currency` — pero puedes nombrarlos y estructurarlos como consideres adecuado.

---

## ✅ Qué vamos a evaluar

- [ ] El diagrama contiene al menos 3 modelos distintos
- [ ] Cada propiedad en todos los modelos incluye un tipo de dato explícito
- [ ] Las relaciones entre modelos están presentes y claramente definidas
- [ ] El modelo refleja con precisión el sistema descrito en el brief — en particular la estructura de la transacción y cómo las billeteras se relacionan con los usuarios y la moneda
- [ ] El diagrama es visualmente claro y está bien organizado
- [ ] El archivo está exportado y nombrado `digital-wallet-class-diagram.png`

> Nota: La herramienta específica utilizada para producir el diagrama no se evalúa — solo la calidad y corrección del modelo en sí.

---

## 📦 Cómo entregar

Entrega tu archivo **`digital-wallet-class-diagram.png`** siguiendo las instrucciones de entrega de tu instructor.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeks.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeks.com/es/comparar-programas) de [Ingeniería de IA](https://4geeks.com/es/programas-de-carrera/ingenieria-ia) y [Agentes y Automatizaciones con IA](https://4geeks.com/es/programas-de-carrera/agentes-y-automatizaciones-con-inteligencia-artificial).
