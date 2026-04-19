# Hito 1 — Sitio Web Público de tu Empresa

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de comenzar**: Lee tu **[CONTEXT.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/01-web-fundamentals)** antes de escribir cualquier código — define los datos específicos de tu empresa, nombres de campos, valores de dominio y restricciones para tu implementación. También lee las [instrucciones](https://4geeks.com/es/lesson/como-comenzar-un-proyecto-de-codificacion) sobre cómo comenzar un proyecto de programación.

---

## 🎯 El Desafío

Tu empresa lleva años operando exitosamente de forma tradicional, pero el mundo ha cambiado. Los clientes buscan información en línea antes de tomar decisiones. Los competidores ya tienen presencia digital. Y tu empresa, a pesar de su experiencia y calidad, sigue siendo invisible en internet.

La dirección ha decidido iniciar la transformación digital. Tu tarea es construir el primer punto de contacto digital de la empresa: un sitio web público profesional que presente lo que hacen y capture información de personas interesadas a través de un formulario de aplicación o registro.

Este sitio debe funcionar en cualquier dispositivo, cumplir con estándares de accesibilidad web, estar optimizado para motores de búsqueda, y presentar una experiencia de usuario pulida y profesional. No es solo "una página bonita" — es el primer paso hacia la modernización de una empresa que quiere seguir siendo relevante.

### 📋 Instrucciones del Gerente

> **De:** Tu Manager  
> **Para:** Tú  
> **Asunto:** Sitio web público — primera versión
>
> Hola,
>
> Como sabes, hemos decidido dar el salto a lo digital. Necesitamos lanzar nuestro sitio web público lo antes posible. Revisa el `CONTEXT.md` para entender exactamente qué hace nuestra empresa y qué información necesitamos capturar de las personas interesadas.
>
> El sitio debe tener dos partes:
>
> **1. Landing page** — Una página de presentación con:
>
> - Encabezado con navegación clara
> - Sección hero que explique qué hacemos y por qué nos deberían elegir
> - Sección destacando nuestras características principales o beneficios clave (basados en nuestra experiencia en el sector)
> - Información de contacto o llamado a la acción
> - Pie de página profesional
>
> **2. Formulario de aplicación/registro** — Una página separada donde las personas puedan:
>
> - Completar sus datos personales
> - Proporcionar la información específica que necesitamos (ver `CONTEXT.md`)
> - Enviar su aplicación (no necesitas conectarlo a nada todavía, solo validar los datos)
>
> **Requisitos técnicos que debes cumplir:**
>
> - Responsive: debe verse bien en móvil, tablet y escritorio
> - Accesible: usa HTML semántico, etiquetas ARIA cuando sea necesario, y atributos alt en imágenes
> - Optimizado para SEO: implementa Schema.org para marcar la información de la empresa
> - Validación completa del formulario con JavaScript — todos los campos deben validarse antes de "enviar"
> - Mensajes de error claros cuando algo no esté correcto
>
> Usa Tailwind CSS para todo el diseño. No quiero ver CSS personalizado escrito a mano a menos que sea absolutamente necesario.
>
> Hazlo profesional. Este es nuestro debut en el mundo digital y queremos causar una buena impresión.
>
> Saludos,  
> Tu Manager

---

## 🌱 Cómo Comenzar este Proyecto

No clones este repositorio porque vamos a usar una plantilla diferente.

1. Ve a tu repositorio del proyecto de compañía que ya tienes. Si no lo has creado aún, ve al [repositorio plantilla del proyecto transversal](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo) y haz clic en el botón de la derecha "Usar esta plantilla" y selecciona [Crear un nuevo repositorio](https://github.com/new?template_name=ai-engineering-company-project-monorepo&template_owner=4GeeksAcademy).

2. Una vez tengas tu propio repositorio, ábrelo en un Codespace o clónalo localmente.

3. Lee completamente tu archivo [`CONTEXT.md`](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/01-web-fundamentals) — contiene los datos específicos de tu empresa, los campos exactos que tu formulario debe incluir, y cualquier restricción o regla de validación específica del dominio.

4. Crea la estructura básica de tu proyecto:

   ```markdown
   /
   ├── index.html (landing page)
   ├── application.html (formulario de aplicación/registro)
   ├── styles.css (solo si Tailwind CDN no es suficiente)
   └── validation.js (lógica de validación del formulario)
   ```

5. Asegúrate de poder levantar el proyecto en el navegador durante el desarrollo usando un comando compatible con Codespaces desde la raíz del repositorio. Por ejemplo: `npx http-server . -p 3000 -a 0.0.0.0`

6. Comienza por la estructura HTML de la landing page, luego añade estilos con Tailwind, después trabaja en el formulario y finalmente implementa la validación.

---

## 💻 Lo que Necesitas Hacer

### Landing Page

- [ ] Crear `index.html` con estructura HTML5 semántica
- [ ] El proyecto puede ejecutarse localmente con un comando `npx` compatible con Codespaces
- [ ] Implementar un `<header>` con logo/nombre de la empresa y navegación
- [ ] Crear una sección hero que presente la empresa y su propuesta de valor
- [ ] Añadir al menos dos secciones adicionales (características, beneficios, cómo funciona, experiencia, etc.)
- [ ] Implementar un `<footer>` con información de contacto
- [ ] Incluir un enlace/botón que dirija al formulario de aplicación
- [ ] Aplicar estilos con Tailwind CSS usando clases utilitarias
- [ ] Hacer el diseño responsive con breakpoints para móvil, tablet y escritorio
- [ ] Implementar diseño mobile-first
- [ ] Añadir etiquetas `alt` descriptivas a todas las imágenes
- [ ] Usar etiquetas HTML semánticas (`<section>`, `<article>`, `<nav>`, etc.)
- [ ] Implementar atributos ARIA donde sea apropiado (`aria-label`, `role`)
- [ ] Añadir marcado Schema.org para la información de la empresa (tipo Organization o LocalBusiness)

### Formulario de Aplicación/Registro

- [ ] Crear `application.html` con un formulario estructurado
- [ ] Incluir los campos especificados en tu `CONTEXT.md`
- [ ] Usar tipos de input apropiados (`email`, `tel`, `date`, `number`, etc.)
- [ ] Añadir `<label>` asociado correctamente con cada input (usando atributo `for`)
- [ ] Agrupar campos relacionados usando `<fieldset>` y `<legend>` donde sea apropiado
- [ ] Marcar campos obligatorios con el atributo `required`
- [ ] Implementar diseño responsive del formulario
- [ ] Aplicar estilos de Tailwind para el formulario (espaciado, tamaños, estados de foco)
- [ ] Añadir botón de envío y botón secundario para limpiar el formulario
- [ ] Crear `validation.js` para validar todos los campos del formulario
- [ ] Implementar validación en tiempo real (mientras el usuario escribe o al perder foco)
- [ ] Mostrar mensajes de error específicos para cada tipo de validación
- [ ] Estilizar mensajes de error de forma clara y visible
- [ ] Prevenir el envío del formulario si hay errores de validación
- [ ] Mostrar un mensaje de éxito cuando la validación sea correcta (simular envío)

⚠️ **IMPORTANTE:** Los nombres de campos, IDs de entidad y valores específicos del dominio en tu implementación deben coincidir con lo especificado en tu CONTEXT.md. Una implementación genérica que ignore el contexto no será aceptada.

---

## ✅ Lo que Evaluaremos

### Estructura y Semántica HTML

- [ ] El HTML usa etiquetas semánticas apropiadas en lugar de `<div>` genéricos
- [ ] Todas las imágenes tienen atributos `alt` descriptivos
- [ ] Los formularios usan `<label>` correctamente asociados con inputs
- [ ] El marcado Schema.org está presente y correctamente implementado
- [ ] La estructura del documento es lógica y jerárquica

### Diseño Responsive y Tailwind

- [ ] El sitio es completamente responsive (se adapta a móvil, tablet y escritorio)
- [ ] Existe un comando documentado y funcional, compatible con Codespaces, para ejecutar el proyecto localmente con `npx`
- [ ] Se usa diseño mobile-first
- [ ] Todos los estilos usan clases utilitarias de Tailwind
- [ ] Los breakpoints de Tailwind (`sm:`, `md:`, `lg:`) se usan apropiadamente
- [ ] No hay CSS personalizado innecesario (solo Tailwind)
- [ ] El diseño es visualmente coherente y profesional
- [ ] El rendimiento se verifica en la URL pública con [PageSpeed Insights](https://pagespeed.web.dev/) con una puntuación mínima de **80** (ideal: **por encima de 90**)

### Accesibilidad

- [ ] Todos los elementos interactivos son accesibles por teclado
- [ ] Los atributos ARIA se usan donde mejoran la accesibilidad
- [ ] El contraste de colores cumple con estándares mínimos
- [ ] La navegación es lógica y predecible
- [ ] Los mensajes de error son anunciados apropiadamente

### Formulario y Validación

- [ ] Todos los campos especificados en el CONTEXT.md están presentes
- [ ] Los tipos de input son apropiados para cada campo
- [ ] La validación con JavaScript funciona correctamente para todos los campos
- [ ] Los mensajes de error son específicos y útiles (no solo "campo inválido")
- [ ] La validación previene el envío de datos incorrectos
- [ ] Los estados visuales del formulario son claros (foco, error, éxito)
- [ ] El botón de limpiar formulario funciona correctamente

### Adherencia al Contexto

- [ ] La landing page refleja fielmente el tipo de empresa y sector especificado en CONTEXT.md
- [ ] El contenido presenta la experiencia y ventajas competitivas de la empresa
- [ ] Los campos del formulario coinciden exactamente con los requeridos en CONTEXT.md
- [ ] Cualquier regla de validación específica del dominio está implementada
- [ ] El tono y contenido son coherentes con una empresa establecida que se digitaliza

---

## 📦 Cómo Entregar

1. Asegúrate de que tu código esté pusheado a repositorio

2. Verifica que los archivos principales estén presentes:
   - `index.html`
   - `application.html`
   - `validation.js`
   - Tu `CONTEXT.md` (no modificado)

3. Prueba tu sitio abriendo `index.html` en diferentes tamaños de ventana del navegador

4. Prueba todas las validaciones del formulario para asegurarte de que funcionan

5. Envía la URL de tu repositorio para evaluación

**Tip:** Usa las DevTools del navegador (F12) para probar diferentes tamaños de pantalla y verificar que no haya errores en la consola.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de nuestros programas: [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia), [Ciencia de datos y Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Desarrollo Full-Stack con IA](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack).
