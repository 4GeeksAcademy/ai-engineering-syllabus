# Ejemplo en Clase: Sitio Web de una Cafetería Local

> **Nota para el instructor:** Este es un ejemplo en clase diseñado para introducir los conceptos técnicos clave del proyecto principal en una sesión de programación en vivo de 60–90 minutos. El dominio es el sitio web de una cafetería de barrio en lugar de una tienda de ropa francesa — mismas habilidades de HTML + Tailwind, flujo de trabajo colaborativo con Git y estructura semántica, pero con 3 vistas en lugar de 5.

## El Escenario

Una cafetería local quiere un prototipo sencillo de sitio web para mostrar su menú y permitir a los clientes hacer un pedido anticipado. Trabajaréis en parejas: una persona se encarga de las vistas Home y Menú, la otra del formulario de pedido. Usaréis ramas de Git y pull requests para unir vuestro trabajo al final.

---

## Conceptos Cubiertos

| Concepto | Dónde aparece |
|---|---|
| HTML semántico | `<header>`, `<nav>`, `<main>`, `<section>`, `<form>` |
| Clases de utilidad de Tailwind | Layout, espaciado, tipografía, breakpoints responsive |
| Diseño responsive | Mobile-first, prefijos `sm:` / `md:` / `lg:` |
| Datos estructurados Schema.org | `CafeOrCoffeeShop`, `MenuItem` en páginas relevantes |
| Ramas de Git | Una rama por vista (`feature/home`, `feature/menu`, `feature/order`) |
| Pull requests | Abre un PR por rama antes de fusionar con `main` |

> ⚠️ **Importante:** Solo usa **HTML y Tailwind CSS**. No añadas React, JavaScript ni ningún otro framework. Indica esta restricción a tu asistente de IA desde el primer mensaje.

---

## Vistas a Construir (3 en total)

### 1) Página de inicio (`index.html`)

- **Navbar** con: logo (texto está bien), enlaces a Menú y Pedido
- **Sección hero** con un titular de bienvenida y un botón de llamada a la acción que enlace al Menú
- **Dos productos destacados** mostrados como tarjetas (nombre, descripción breve, precio)
- **Footer** con: dirección, horario de apertura y enlace a la página de Pedido
- El navbar y el footer deben copiarse de forma coherente en todas las páginas

### 2) Página de menú (`menu.html`)

- Reutiliza navbar y footer
- Una **barra de filtros por categoría** con botones para: Café, Té, Comida (solo visual — no se necesita JavaScript)
- Una **cuadrícula de al menos 8 productos** (4×2), cada tarjeta muestra: imagen del producto (usa un placeholder), nombre y precio

### 3) Formulario de pedido (`order.html`)

- Reutiliza navbar y footer
- Un **formulario** que recoge:
  - Nombre del cliente
  - Hora de recogida (un `<select>` con 3–4 franjas horarias)
  - Selección de productos (al menos 3 checkboxes)
  - Instrucciones especiales (`<textarea>`)
  - Un botón "Realizar pedido" de tipo submit
- Usa elementos `<label>` correctos vinculados a cada input

---

## Lista de Verificación del Flujo de Git

- [ ] Compañero/a A: crea la rama `feature/home` y construye `index.html`
- [ ] Compañero/a B: crea la rama `feature/menu` y construye `menu.html`
- [ ] Cualquiera de los dos: crea la rama `feature/order` y construye `order.html`
- [ ] Abre un **pull request** por cada rama — describe en el cuerpo del PR qué contiene
- [ ] Haz pull del `main` más reciente antes de fusionar para reducir conflictos: `git pull origin main`
- [ ] Resuelve los conflictos de fusión juntos antes de hacer push
- [ ] Usa mensajes de commit claros: por ejemplo, `"Añadir sección hero a la página de inicio"`, `"Añadir cuadrícula del menú con 8 productos"`

---

## Lista de Evaluación

- [ ] Las 3 páginas usan elementos HTML semánticos (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`, `<form>`)
- [ ] Las clases de utilidad de Tailwind se usan de forma coherente — sin archivos CSS adicionales
- [ ] El layout es legible en móvil y escritorio (pruébalo redimensionando el navegador)
- [ ] El navbar y el footer son idénticos en las 3 páginas
- [ ] Al menos un tipo de Schema.org añadido (p. ej., `CafeOrCoffeeShop` en la página de inicio, `MenuItem` en la del menú)
- [ ] El historial de Git muestra al menos una rama y un PR por vista principal
- [ ] No hay trabajo enviado directamente a `main`

---

## Preguntas para Discusión

1. ¿Por qué usamos `<nav>`, `<main>` y `<section>` en lugar de solo `<div>`? ¿Quién se beneficia del HTML semántico?
2. ¿Cuál es el propósito de añadir datos estructurados Schema.org a la página de una cafetería — quién los lee y por qué importa?
3. Si dos compañeros editan `index.html` al mismo tiempo en ramas distintas, ¿qué pasa cuando intentáis fusionarlas? ¿Cómo se resuelve?
