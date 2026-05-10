> **Ejemplo para usar en clase (solo instructores).** Usa este escenario para introducir HTML semántico, Flexbox, accesibilidad y Schema.org en una sesión de ~1-2 horas. Este archivo es un recurso pedagógico con un *dominio diferente* al del proyecto asignado. No lo compartas con los estudiantes como su brief de proyecto.

# Web Personal de un Chef — HTML, CSS, SEO y Accesibilidad (Ejemplo en Clase)

## Escenario

Un chef autónomo llamado Marco Rossi organiza cenas privadas y eventos pop-up. Te ha pedido que construyas una landing page sencilla para que los clientes puedan encontrarle y contactar con él.

Tras una breve conversación, acordáis la siguiente estructura:

> La página tendrá una **barra de navegación** con enlaces a tres secciones: Sobre mí, Trayectoria y Próximos Eventos. La primera sección será un **hero** que dé la bienvenida a los visitantes e introduzca al chef. Cada sección debe sentirse como una "página" completa — aproximadamente la altura del viewport. El pie de página incluirá un correo de contacto.

El sitio debe funcionar para todos, incluidas las personas que usan lectores de pantalla. También debe ser indexable por los buscadores usando datos estructurados Schema.org.

---

## Estructura acordada de la página

| Sección | Contenido |
|---------|-----------|
| `<header>` / `<nav>` | Nombre/logo + enlaces a `#about`, `#experience`, `#events` |
| Hero (`<section id="hero">`) | Nombre del chef, tagline, breve presentación |
| Sobre mí (`<section id="about">`) | Párrafo biográfico, placeholder de foto con atributo `alt` |
| Trayectoria (`<section id="experience">`) | Lista de restaurantes o platos destacados |
| Próximos Eventos (`<section id="events">`) | 2-3 tarjetas de eventos (fecha, lugar, descripción) |
| `<footer>` | Correo de contacto |

---

## Lista de verificación

### Estructura y HTML semántico

- [ ] Crear `index.html` con un esquema de documento válido (`<!DOCTYPE html>`, `<html lang="es">`, `<head>`, `<body>`)
- [ ] Usar `<header>`, `<nav>`, `<main>`, `<section>`, `<article>` y `<footer>` — evitar usar solo `<div>`
- [ ] Cada sección tiene un `id` que coincide con los enlaces de la nav (ancla de scroll suave)
- [ ] La jerarquía de encabezados es correcta: un `<h1>` → `<h2>` por sección → `<h3>` dentro de las secciones si es necesario

### Layout y estilos

- [ ] Crear un archivo `styles.css` separado, enlazado desde `index.html`
- [ ] Cada sección ocupa aproximadamente `100vh`
- [ ] Usar **Flexbox** para el layout (navbar, hero, cuadrícula de tarjetas de eventos) — sin `float` ni `inline-block` para la estructura
- [ ] Los enlaces de la nav están alineados horizontalmente en escritorio

### Accesibilidad

- [ ] El elemento `<nav>` tiene `aria-label="Navegación principal"`
- [ ] Todas las imágenes tienen atributos `alt` descriptivos
- [ ] Los elementos interactivos (enlaces, botones) son accesibles por teclado y visibles al recibir el foco
- [ ] El contraste de color cumple los requisitos mínimos de legibilidad

### SEO / Schema.org

- [ ] Añadir un `<title>` y `<meta name="description">` en `<head>`
- [ ] Añadir datos estructurados Schema.org como un bloque `<script type="application/ld+json">` que describa al chef como `Person` con `jobTitle`, `name` y `email`

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Marco Rossi",
  "jobTitle": "Chef autónomo",
  "email": "mailto:marco@example.com",
  "url": "https://marcorossi.example.com"
}
```

### Organización de archivos

- [ ] `index.html` y `styles.css` están en la raíz del proyecto y correctamente enlazados

---

## Preguntas de debate

1. ¿Cuál es la diferencia entre usar `<div id="about">` y `<section id="about" aria-labelledby="about-title">`? ¿Por qué importa para los usuarios de lectores de pantalla?
2. El chef quiere añadir un formulario de contacto más adelante. ¿Qué elemento HTML usarías y qué atributos `aria` mejorarían su accesibilidad?
3. ¿Por qué le importa a Google el marcado Schema.org? ¿Qué le dice un esquema `Person` a un buscador que un simple `<h1>Marco Rossi</h1>` no transmite?
