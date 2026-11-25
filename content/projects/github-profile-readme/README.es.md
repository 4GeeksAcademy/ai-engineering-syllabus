# Crea el README de tu perfil de GitHub

<!-- hide -->

Por [@ehiber](https://github.com/ehiber) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

🌐 _These instructions are [available in English](./README.md)_.

**Antes de empezar**:

> ¡Te necesitamos! Estos ejercicios se construyen y mantienen en colaboración con personas como tú. Si encuentras algún error 🐞 o falta de ortografía, por favor contribuye y/o repórtalo.

<!-- endhide -->

---

## 🎯 Tu reto

Tu perfil de GitHub es tu carta de presentación como developer. Reclutadores, compañeros y futuros clientes lo van a visitar para saber quién eres, qué estás aprendiendo y cómo contactarte. Hoy está vacío, y ese es tu primer proyecto: **darle una cara a tu perfil**.

GitHub tiene una función especial: si creas un repositorio **público** que se llame **exactamente igual que tu nombre de usuario**, el `README.md` de ese repositorio aparece en la parte superior de tu perfil. Ese archivo se escribe en **Markdown** y lo vas a crear, versionar y publicar con **Git**, igual que cualquier otro proyecto.

El contenido es libre: tú decides cómo presentarte. Lo único obligatorio es que alguien que entre a tu perfil sepa **quién eres** y **cómo contactarte**. A partir de ahí, puedes agregar lo que quieras: qué estás aprendiendo, tecnologías que te interesan, tus hobbies, imágenes, GIFs, badges o estadísticas.

Para inspirarte, mira cómo se presentan algunas personas del equipo de 4Geeks Academy:

- [github.com/alesanchezr](https://github.com/alesanchezr)
- [github.com/marcogonzalo](https://github.com/marcogonzalo)
- [github.com/LoretoConcha](https://github.com/LoretoConcha)
- [github.com/deimianvasquez](https://github.com/deimianvasquez)
- [github.com/ehiber](https://github.com/ehiber)
- [github.com/lbdelilla](https://github.com/lbdelilla)

> Fíjate en qué tienen en común y en qué se diferencian. No hay un único formato correcto: un buen README de perfil es claro, honesto y refleja a la persona que lo escribe.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no usa una plantilla: vas a crear tu propio repositorio desde cero.

1. Inicia sesión en [GitHub](https://github.com/) (si aún no tienes cuenta, créala con un nombre de usuario profesional).
2. Crea un repositorio nuevo desde [github.com/new](https://github.com/new) con estas condiciones:
   - **Nombre del repositorio:** exactamente tu nombre de usuario (respetando mayúsculas y minúsculas). GitHub te mostrará un mensaje indicando que es un repositorio especial ✨.
   - **Visibilidad:** `Public`.
   - Marca la opción **Add a README file**.
3. Clona el repositorio en tu computadora desde la terminal:

```bash
git clone https://github.com/<tu-usuario>/<tu-usuario>.git
cd <tu-usuario>
```

A partir de aquí, sigue el camino principal de la siguiente sección.

---

## 💻 Qué debes hacer

> 💡 **¿Por qué a mano?** Este proyecto existe para que practiques tres cosas que vas a usar todos los días como developer: escribir en **Markdown**, guardar tus cambios con **Git** (`add` y `commit`) y publicarlos en **GitHub** (`push`). Por eso te recomendamos el camino manual: equivocarte y corregir es parte del aprendizaje.

> 🤖 **¿Te bloqueas?** Si no sabes qué escribir, el Markdown te parece raro o te da miedo la terminal, no te detengas. Apóyate en un agente de código (lo explicamos en la alternativa de abajo). Puedes usarlo solo para la parte que te cuesta o para todo el proceso. Lo importante es que termines y entiendas lo que se hizo.

### Camino principal: versión manual (recomendado)

Escribes tú el README, línea por línea.

- [ ] Abre la carpeta del repositorio en tu editor de código (por ejemplo, VS Code).
- [ ] Edita el archivo `README.md` usando Markdown: títulos (`#`, `##`), párrafos, listas, enlaces (`[texto](url)`), imágenes (`![alt](url)`) y, si quieres, emojis.
- [ ] Incluye una **presentación** (quién eres, qué estás aprendiendo o qué te interesa).
- [ ] Incluye al menos una **forma de contactarte** (LinkedIn, email público, portafolio, X, etc.).
- [ ] Revisa cómo se ve con la vista previa de Markdown de tu editor (en VS Code: `Ctrl+Shift+V` / `Cmd+Shift+V`).
- [ ] Guarda los cambios en Git y súbelos a GitHub desde la terminal:

```bash
git status
git add README.md
git commit -m "Add profile README"
git push
```

- [ ] Abre `https://github.com/<tu-usuario>` y comprueba que el README aparece en tu perfil.
- [ ] Si quieres mejorar algo, edita, haz un nuevo `commit` con un mensaje descriptivo y vuelve a hacer `push`.

### Alternativa: con ayuda de un agente de código

Usa un agente de código (Claude Code, Cursor, GitHub Copilot, Codex u otro) como apoyo: para conseguir ideas, completar o mejorar el README que empezaste a mano, o para que te acompañe con los comandos de Git. Tú diriges y revisas.

- [ ] Abre la carpeta del repositorio con tu agente de código.
- [ ] Pídele ayuda con el contenido dándole información real sobre ti. Por ejemplo:

```text
Quiero crear el README de mi perfil de GitHub en el archivo README.md de esta carpeta.
Sobre mí: <tu nombre>, <a qué te dedicas o qué estudias>, estoy aprendiendo <tecnologías>,
me interesa <temas>. Me pueden contactar en <enlaces>.
Usa Markdown, un tono <cercano/profesional>, y agrega <emojis/badges/una imagen> si queda bien.
No inventes información: si te falta algún dato, pregúntame.
Explícame brevemente la sintaxis de Markdown que uses.
```

- [ ] Lee el resultado línea por línea: elimina todo lo que no sea cierto, corrige el tono para que suene a ti y verifica que todos los enlaces e imágenes funcionen.
- [ ] Pide ajustes al agente las veces que necesites hasta que el README te represente.
- [ ] Publica tus cambios. Puedes hacerlo tú con los comandos del camino principal o pedirle al agente que lo haga contigo:

```text
Quiero guardar y subir mis cambios a GitHub.
Antes de ejecutar cada comando de Git, explícame qué hace y por qué.
Usa un mensaje de commit descriptivo.
```

- [ ] Abre `https://github.com/<tu-usuario>` y comprueba que el README aparece en tu perfil.

> ⚠️ **IMPORTANTE:** El agente es tu ayudante, no el autor. Tú eres responsable de cada línea publicada en tu perfil y debes entender cada comando que se ejecutó: los vas a usar en todos tus proyectos. No compartas datos privados (dirección, teléfono personal, documentos de identidad) ni dejes texto de relleno como `<tu nombre>` o información inventada.

---

## ✅ Qué vamos a evaluar

- [ ] Existe un repositorio **público** con el mismo nombre que tu usuario y su `README.md` se muestra en tu perfil de GitHub.
- [ ] El README incluye una **presentación** que deja claro quién eres.
- [ ] El README incluye al menos una **forma de contactarte** con un enlace que funciona.
- [ ] El Markdown se renderiza correctamente: títulos, listas, enlaces e imágenes (si las hay) se ven bien y no hay enlaces rotos.
- [ ] El contenido es real y personal: no hay texto de relleno, plantillas sin completar ni información inventada.
- [ ] El historial del repositorio tiene al menos un `commit` tuyo con un mensaje descriptivo, subido con `git push`.

> Nota: no evaluamos el diseño ni la cantidad de secciones. Un README corto, claro y honesto vale más que uno largo y genérico.

---

## 📦 Cómo entregar este proyecto

Entrega la **URL de tu perfil de GitHub**:

```text
https://github.com/<tu-usuario>
```

Antes de entregar, ábrela en una ventana de incógnito y comprueba que el README se ve sin iniciar sesión.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/es) de 4Geeks Academy. Conoce más sobre los cursos de [Full-Stack Software Developer](https://4geeksacademy.com/es/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/career-programs/data-science-ml), [Ciberseguridad](https://4geeksacademy.com/es/career-programs/cybersecurity) e [Ingeniería de IA](https://4geeksacademy.com/es/career-programs/ai-engineering).
