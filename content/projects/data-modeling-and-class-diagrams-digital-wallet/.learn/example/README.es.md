> **Ejemplo para usar en clase (solo instructores).** Usa este escenario para introducir los diagramas de clases en una sesión de ~1 hora. Este archivo es un recurso pedagógico con un *dominio diferente* al del proyecto asignado. No lo compartas con los estudiantes como su brief de proyecto.

# Sistema de Tarjeta de Puntos — Modelado de Objetos (Ejemplo en Clase)

## Escenario

Una cafetería local quiere construir un sistema digital de tarjeta de fidelización. Antes de escribir ningún código, necesitas modelar la capa de datos como un diagrama de clases.

El gerente del local describe lo que el sistema debe soportar:

> Un cliente puede tener una tarjeta de fidelización. La tarjeta registra el saldo de puntos y pertenece a un nivel de recompensa (Bronce, Plata u Oro). Cada vez que un cliente realiza una compra o canjea una recompensa, se registra una transacción de puntos. Cada transacción tiene un tipo (ganar o canjear), una cantidad de puntos, una marca de tiempo y un estado (pendiente o confirmada).

Tu tarea es modelar este sistema como un **diagrama de clases** con propiedades tipadas y relaciones claramente definidas.

---

## Qué modelar

### Entidades sugeridas

| Modelo | Descripción |
|--------|-------------|
| `Customer` | La persona que tiene la tarjeta de fidelización |
| `LoyaltyCard` | La tarjeta vinculada a un cliente, con saldo de puntos y nivel |
| `PointTransaction` | Registro de cada evento de acumulación o canje de puntos |

### Propiedades tipadas de ejemplo

| Modelo | Propiedad | Tipo |
|--------|-----------|------|
| `Customer` | `id` | `int` |
| `Customer` | `name` | `string` |
| `Customer` | `email` | `string` |
| `LoyaltyCard` | `id` | `int` |
| `LoyaltyCard` | `pointBalance` | `int` |
| `LoyaltyCard` | `tier` | `string` |
| `LoyaltyCard` | `isActive` | `boolean` |
| `PointTransaction` | `id` | `int` |
| `PointTransaction` | `type` | `string` |
| `PointTransaction` | `points` | `int` |
| `PointTransaction` | `createdAt` | `date` |
| `PointTransaction` | `status` | `string` |

### Relaciones a dibujar

- Un `Customer` tiene **una** `LoyaltyCard` (1 a 1)
- Una `LoyaltyCard` tiene **muchas** `PointTransaction` (1 a muchos)
- Cada `PointTransaction` pertenece a **una** `LoyaltyCard`

---

## Lista de verificación

- [ ] Crear al menos **3 modelos** en la herramienta de diagramas
- [ ] Añadir cada propiedad con su **tipo de dato explícito**
- [ ] Dibujar las **relaciones** entre modelos con etiquetas de cardinalidad correctas
- [ ] Asegurarse de que el diagrama sea **legible** — sin cajas superpuestas, con flechas trazables
- [ ] Exportar el resultado como **`loyalty-card-class-diagram.png`**

**Herramienta:** [diagram.4geeks.com](https://diagram.4geeks.com/)

---

## Preguntas de debate

1. La propiedad `tier` es actualmente un `string` simple en `LoyaltyCard`. ¿Qué cambiaría si `RewardTier` pasara a ser su propio modelo con una propiedad `minimumPoints: int`? ¿Cuándo justifica esa complejidad adicional?
2. ¿Qué ocurre con los registros de `PointTransaction` de un cliente si este cierra su cuenta? ¿Cómo representarías esa decisión en el diagrama?
3. Una `PointTransaction` puede representar tanto la acumulación de puntos (una compra) como su canje (una recompensa). ¿Deberían ser dos modelos separados o un único modelo con un campo `type`? ¿Cuáles son las ventajas y desventajas de cada enfoque?
