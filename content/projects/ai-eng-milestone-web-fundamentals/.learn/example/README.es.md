# Ejemplo en Clase — Sitio Web de Panadería Local

> **Nota para el instructor:** Este es un ejemplo diseñado para el ritmo del aula que introduce los mismos conceptos que el proyecto evaluado (Hito 1). Se utiliza un dominio diferente para que los estudiantes no lo confundan con su propio trabajo. Una panadería es un negocio concreto y familiar que todo el mundo puede entender — ideal para una sesión de codificación en vivo.

_These instructions are also available in [English](./README.md)._

---

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


**Sweet Corner Bakery** lleva 12 años horneando pan artesanal y bollería en el mismo barrio. Sus clientes los conocen de boca en boca, pero no tienen ninguna presencia online. La propietaria quiere dos cosas:

1. Una landing page profesional que muestre lo que hacen y dónde están.
2. Un formulario de pedido personalizado donde los clientes puedan hacer un encargo previo de una tarta o caja de catering para un evento.

Por ahora no se necesita backend — solo validar el formulario con JavaScript y mostrar un mensaje de éxito.

---

## Qué Construir

### Estructura de archivos

```
/
├── index.html        ← landing page
├── order.html        ← formulario de pedido personalizado
└── validation.js     ← toda la lógica de validación del formulario
```

Servir con: `npx http-server . -p 3000 -a 0.0.0.0`

---

### Landing Page (`index.html`)

- [ ] `<header>` con el nombre de la panadería y enlaces de navegación a las secciones y a `order.html`.
- [ ] Sección hero: eslogan ("Pan artesanal horneado fresco cada mañana"), una descripción breve y un botón CTA que enlaza al formulario de pedido.
- [ ] Sección de características: al menos 3 elementos (ej. "Sin conservantes artificiales", "Horneado diario", "Pedidos personalizados disponibles") con un icono o emoji.
- [ ] Sección de ubicación y horario con dirección y horas de apertura.
- [ ] `<footer>` con email de contacto y enlaces a redes sociales.

**Requisitos técnicos:**

- [ ] Usar etiquetas HTML semánticas: `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`.
- [ ] Todas las imágenes tienen atributos `alt` descriptivos.
- [ ] Atributos ARIA donde ayudan (`aria-label` en el nav, `role="banner"` en el header si es necesario).
- [ ] Marcado Schema.org para la panadería como `LocalBusiness`:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Bakery",
  "name": "Sweet Corner Bakery",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Calle Arce 14",
    "addressLocality": "Madrid"
  },
  "openingHours": "Mo-Sa 07:00-19:00",
  "telephone": "+34-555-0183"
}
</script>
```

- [ ] Todos los estilos usan **Tailwind CSS** (el CDN es suficiente para clase). Sin CSS escrito a mano salvo que sea estrictamente necesario.
- [ ] Responsive: se ve correctamente en móvil (`sm:`), tablet (`md:`) y escritorio (`lg:`).

---

### Formulario de Pedido (`order.html`)

La propietaria necesita capturar estos campos de los clientes:

| Campo | Tipo de input | Requerido | Regla de validación |
|---|---|---|---|
| Nombre completo | `text` | Sí | Mínimo 2 caracteres |
| Email | `email` | Sí | Formato de email válido |
| Teléfono | `tel` | Sí | 7–15 dígitos |
| Fecha del evento | `date` | Sí | Debe ser al menos 3 días desde hoy |
| Número de invitados | `number` | Sí | Entre 5 y 500 |
| Tipo de producto | `select` | Sí | Tarta / Caja de catering / Surtido de pan |
| Peticiones especiales | `textarea` | No | Máximo 300 caracteres |

- [ ] Cada campo tiene un `<label>` correctamente vinculado con `for` / `id`.
- [ ] Agrupar los campos de "Detalles del evento" con `<fieldset>` y `<legend>`.
- [ ] Marcar los campos requeridos visualmente y con el atributo `required`.
- [ ] Botón **Enviar** y botón **Limpiar** que reinicia el formulario.
- [ ] Diseño responsive del formulario.

---

### Validación (`validation.js`)

- [ ] Validar cada campo requerido en **blur** (cuando el usuario abandona el campo).
- [ ] Mostrar un mensaje de error específico debajo de cada campo, no una alerta genérica.
- [ ] Evitar el envío del formulario si cualquier campo es inválido.
- [ ] Cuando todas las validaciones sean correctas, mostrar un mensaje de éxito: *"¡Tu pedido ha sido recibido! Nos pondremos en contacto contigo en menos de 24 horas."*
- [ ] Estado de error: borde rojo + texto de error en rojo. Estado de éxito: borde verde.

**Ejemplos de mensajes de error:**

```
Nombre completo: "Por favor, introduce tu nombre completo (al menos 2 caracteres)."
Email: "Por favor, introduce una dirección de email válida."
Fecha del evento: "Por favor, elige una fecha al menos 3 días desde hoy."
Número de invitados: "Por favor, introduce un número entre 5 y 500."
```

---

## Conceptos Clave a Trabajar en Clase

| Concepto | Dónde aparece |
|---|---|
| HTML semántico | `<section>`, `<article>`, `<nav>` en la landing page |
| Datos estructurados Schema.org | `<script type="application/ld+json">` |
| Breakpoints responsive de Tailwind | Clases `sm:`, `md:`, `lg:` |
| `<fieldset>` + `<legend>` | Agrupando los campos de detalles del evento |
| Validación JS de formulario (eventos blur) | `validation.js` |
| Prevenir el envío por defecto del formulario | `event.preventDefault()` en JS |
| ARIA para accesibilidad | `aria-describedby` en campos con errores |

---

## Preguntas para Debate

1. ¿Por qué usamos etiquetas semánticas como `<section>` y `<article>` en lugar de `<div>` en todas partes? ¿Quién se beneficia de esta decisión — los usuarios, los desarrolladores o los motores de búsqueda?
2. La validación de la fecha del evento necesita calcular "3 días desde hoy" de forma dinámica. ¿Cómo escribirías esa comprobación en JavaScript sin usar una librería?
3. Si quisiéramos enviar realmente los datos del formulario a un servidor más adelante, ¿qué tendríamos que añadir o cambiar? ¿Qué se mantiene igual?
