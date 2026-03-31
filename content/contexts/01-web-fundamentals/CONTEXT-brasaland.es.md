# CONTEXT.md — Brasaland

## Hito 1: Sitio Web Público de tu Empresa

_These instructions are [available in English](./CONTEXT-brasaland.md)._

> Este documento describe tu empresa y la situación concreta para la que estás construyendo este hito. Léelo completo antes de escribir ningún código. Todo lo que construyas debe reflejar este contexto.

---

## Tu empresa

**Brasaland** es una cadena de restaurantes de comida a la brasa fundada en 2008 en Medellín, Colombia. Lo que comenzó como un único local familiar ha crecido hasta convertirse en una cadena de 14 restaurantes propios operando en Colombia y Estados Unidos (Florida). La empresa emplea aproximadamente 115 personas entre personal de cocina y sala, gestión de operaciones, y el equipo corporativo con sede en Medellín y oficina comercial en Miami. La facturación anual ronda los 6 millones de dólares. La marca se construye sobre tres pilares: calidad consistente del producto en cada local, experiencia cálida y confiable para el cliente, y rapidez en el servicio.

---

## Tu departamento y el problema que debes resolver

Trabajas en **Brasaland Digital**, el equipo interno creado por la CEO Mariana Restrepo para liderar la transformación digital de la empresa, y reportas directamente al CTO Nicolás Park. El sitio web corporativo actual de Brasaland es de 2019, no permite pedidos en línea, y solo muestra el menú. No refleja que la empresa opera en dos países ni presenta adecuadamente la experiencia de marca. Camila Ospina (Gerente de Marketing) necesita un sitio web renovado que presente la marca profesionalmente, muestre las ubicaciones en ambos países, y capture información de personas interesadas en formar parte del programa de fidelización digital.

---

## Tu stakeholder

**Camila Ospina**, Gerente de Marketing

> Hola,
>
> Necesitamos relanzar nuestro sitio web corporativo. Debe presentar Brasaland como lo que somos: una cadena seria de restaurantes a la brasa con presencia en Colombia y Estados Unidos. Quiero una landing page que explique nuestra propuesta de valor, muestre nuestras ubicaciones en ambos países, y presente nuestro nuevo programa de fidelización digital "Brasa Points". También necesito una página con un formulario para que las personas puedan registrarse en el programa de fidelización. Actualmente usamos tarjetas físicas que se pierden y no generan datos. Quiero capturar: nombre, email, teléfono, país, ciudad, ubicación favorita, preferencias alimentarias, y cómo nos conocieron. El sitio debe ser responsive, accesible, y optimizado para SEO. El soporte multiidioma (español e inglés) es opcional pero altamente recomendado; empieza con un idioma base. Usa Tailwind y asegúrate de que las validaciones funcionen perfectamente.

---

## Alcance de idioma

- El soporte multiidioma es **opcional pero altamente recomendado** por la operación de Brasaland en Colombia y Estados Unidos.
- Debes escoger un **idioma base** para toda la experiencia del sitio y del formulario.
- Si implementas un segundo idioma, trátalo como una mejora (sin reducir la calidad/completitud del idioma base).

## Contenido de la landing page

Tu landing page debe incluir las siguientes secciones, en este orden:

### Header

- Logo o nombre "Brasaland"
- Selector de idioma (ES | EN) si implementas un segundo idioma
- Navegación: Inicio | Ubicaciones | Menú | Brasa Points | Contacto

### Hero

- **Titular:** "El sabor de la brasa, en cada bocado"
- **Subtítulo:** "Desde 2008 sirviendo las mejores carnes a la brasa en Colombia y Estados Unidos. 14 ubicaciones, una misma pasión por la calidad y el sabor."
- **Call to action:** Botón "Únete a Brasa Points" que enlace al formulario

### Nuestra Historia (párrafo + imagen)

Fundada en Medellín en 2008, Brasaland comenzó como un sueño familiar: compartir el auténtico sabor de la carne a la brasa con calidad constante y servicio cálido. Hoy somos 14 restaurantes en dos países, pero mantenemos la misma receta de éxito: productos frescos, técnicas tradicionales, y pasión por cada plato que servimos.

### Lo que nos hace únicos (3 columnas)

1. **Calidad Consistente**
   - Mismas recetas y estándares en todos los locales
   - Ingredientes frescos seleccionados diariamente
2. **Experiencia Cálida**
   - Servicio amable y atento
   - Ambiente familiar en cada visita

3. **Rapidez**
   - Tu comida lista en minutos
   - Sin sacrificar sabor ni calidad

### Nuestras Ubicaciones (2 columnas)

- **Colombia**
  - 10 restaurantes en Medellín, Bogotá y Cali
  - Horario: Lun-Dom 11:00 - 22:00

- **Estados Unidos (Florida)**
  - 4 restaurantes en Miami y Orlando
  - Horario: Mon-Sun 11:00 AM - 10:00 PM

### Brasa Points (sección destacada)

#### Gana puntos con cada visita

- Acumula 1 punto por cada $10.000 COP o $5 USD
- Canjea tus puntos por descuentos y platos gratis
- Ofertas exclusivas para miembros
- Registro 100% digital - ¡ya no más tarjetas de papel!

### Contacto

- Email: <hola@brasaland.com>
- Colombia: +57 4 123 4567
- Florida: +1 305 123 4567

### Footer

- © 2025 Brasaland. Todos los derechos reservados.
- Instagram | Facebook

---

## Campos del formulario de registro Brasa Points

Tu formulario debe capturar la siguiente información:

| Campo                                | Tipo     | Validación                                                                          | Obligatorio |
| ------------------------------------ | -------- | ----------------------------------------------------------------------------------- | ----------- |
| **Nombre completo**                  | text     | Mínimo 2 palabras                                                                   | Sí          |
| **Email**                            | email    | Formato válido de email                                                             | Sí          |
| **Teléfono**                         | tel      | Formato: +[código país] [número]                                                    | Sí          |
| **País**                             | select   | Colombia / Estados Unidos                                                           | Sí          |
| **Ciudad**                           | select   | Medellín / Bogotá / Cali / Miami / Orlando (según país)                             | Sí          |
| **Ubicación favorita de Brasaland**  | select   | Lista de 14 restaurantes según país y ciudad                                        | No          |
| **Preferencias alimentarias**        | checkbox | Sin restricciones / Vegetariano / Sin gluten / Otro                                 | No          |
| **¿Cómo nos conociste?**             | select   | Redes sociales / Recomendación / Pasando por el local / Búsqueda en internet / Otro | Sí          |
| **Fecha de nacimiento**              | date     | Mayor de 18 años                                                                    | Sí          |
| **Acepto términos del programa**     | checkbox | Debe estar marcado para enviar                                                      | Sí          |
| **Quiero recibir ofertas por email** | checkbox | Opcional, por defecto no marcado                                                    | No          |

---

## Validaciones específicas

1. **Nombre completo:** Debe contener al menos nombre y apellido
2. **Email:** Debe ser formato válido (contener @ y dominio)
3. **Teléfono:** Debe comenzar con + seguido del código de país (+57 para Colombia, +1 para USA)
4. **Ciudad:** Las opciones de ciudad deben cambiar dinámicamente según el país seleccionado
5. **Ubicación favorita:** Las opciones deben filtrarse según país y ciudad seleccionados
6. **Fecha de nacimiento:** El usuario debe ser mayor de 18 años (validar fecha)
7. **Términos del programa:** El checkbox debe estar marcado para poder enviar

---

## Lógica de campos dependientes

**País → Ciudad:**

- Si selecciona "Colombia": mostrar Medellín, Bogotá, Cali
- Si selecciona "Estados Unidos": mostrar Miami, Orlando

**País + Ciudad → Ubicación favorita:**

- Colombia - Medellín: Brasaland El Poblado, Brasaland Laureles, Brasaland Envigado, Brasaland Sabaneta
- Colombia - Bogotá: Brasaland Usaquén, Brasaland Chapinero, Brasaland Zona Rosa
- Colombia - Cali: Brasaland Granada, Brasaland Ciudad Jardín, Brasaland Unicentro
- USA - Miami: Brasaland Brickell, Brasaland Coral Gables
- USA - Orlando: Brasaland Downtown, Brasaland International Drive

---

## Mensajes de error esperados

Cuando un campo no cumpla la validación, muestra estos mensajes específicos:

- **Nombre completo:** "Ingresa tu nombre completo (nombre y apellido)"
- **Email:** "Ingresa un email válido (ejemplo: <nombre@correo.com>)"
- **Teléfono:** "El teléfono debe incluir código de país (ejemplo: +57 300 123 4567 o +1 305 123 4567)"
- **País:** "Selecciona tu país"
- **Ciudad:** "Selecciona tu ciudad"
- **Cómo nos conociste:** "Cuéntanos cómo conociste Brasaland"
- **Fecha de nacimiento:** "Debes ser mayor de 18 años para registrarte en Brasa Points"
- **Términos del programa:** "Debes aceptar los términos del programa Brasa Points para continuar"

---

## Mensaje de éxito

Cuando el formulario se valide correctamente (simular envío), mostrar:

> **¡Bienvenido a Brasa Points!**
>
> Tu registro ha sido exitoso. Recibirás un email de confirmación en los próximos minutos con los detalles de tu cuenta y cómo empezar a acumular puntos.
>
> ¡Ya puedes disfrutar de tus beneficios en cualquiera de nuestras 14 ubicaciones!

---

## Restricción específica

El programa Brasa Points está diseñado para **clientes mayores de 18 años que quieren acumular puntos con sus visitas**. No es un formulario de reservas ni de pedidos en línea. El sitio debe incluir un mensaje visible que diga: "¿Quieres hacer un pedido? Llama a tu ubicación favorita o visítanos directamente. ¡Pronto tendremos pedidos en línea!"

---

## Schema.org markup requerido

Implementa el siguiente marcado Schema.org en tu landing page:

Si entregas un solo idioma, configura `availableLanguage` únicamente con ese idioma base.

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Brasaland",
  "description": "Cadena de restaurantes de comida a la brasa en Colombia y Estados Unidos",
  "url": "https://brasaland.com",
  "foundingDate": "2008",
  "servesCuisine": "Grilled food, Colombian cuisine",
  "priceRange": "$$",
  "address": [
    {
      "@type": "PostalAddress",
      "addressCountry": "CO",
      "addressLocality": "Medellín",
      "addressRegion": "Antioquia"
    },
    {
      "@type": "PostalAddress",
      "addressCountry": "US",
      "addressLocality": "Miami",
      "addressRegion": "FL"
    }
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+57-4-123-4567",
    "contactType": "customer service",
    "availableLanguage": ["Spanish", "English"]
  },
  "sameAs": [
    "https://instagram.com/brasaland",
    "https://facebook.com/brasaland"
  ]
}
```
