# Conectando el Candado: Flujos de Autenticación en el Frontend

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/como-iniciar-un-proyecto-de-programacion) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu Reto

En la entrega anterior aseguraste la API. Las rutas protegidas ahora devuelven `401` a cualquiera que no tenga una sesión válida — incluyendo tu propio frontend. Es momento de cerrar ese ciclo.

Tu tech lead ha abierto el siguiente ticket:

> #### AUTH-02 — Flujos de autenticación y vistas protegidas en el frontend
>
> La API ya exige un token JWT en las rutas protegidas. Esta tarea cubre el lado frontend de ese contrato:
>
> - **Vistas de login y registro** — formularios que llaman a la API, reciben el token y lo almacenan correctamente.
> - **Vistas de gestión de cuenta** — página de perfil y formulario para cambiar la contraseña.
> - **Protección de rutas** — cualquier vista que requiera sesión debe redirigir a los usuarios no autenticados al login. Esto aplica a todas las aplicaciones del monorepo **excepto el website público (Hito 1)**, que permanece completamente público.
>
> El token debe almacenarse en `localStorage` y adjuntarse a cada llamada protegida a la API mediante la cabecera `Authorization: Bearer`. Al cerrar sesión, el token se elimina y el usuario es redirigido al login.
>
> No construyas una aplicación de autenticación separada. Integra estos flujos en las aplicaciones Next.js existentes dentro de tu monorepo.

### Conocimiento complementario: el lado frontend del JWT

Una vez que la API devuelve un token en el login, el trabajo del frontend es: almacenarlo, enviarlo y reaccionar a su ausencia. El patrón estándar en Next.js es:

1. **Almacenar** el token en `localStorage` después de una respuesta de login exitosa.
2. **Leer** el token en cada llamada protegida a la API y establecerlo en la cabecera `Authorization`: `Bearer <token>`.
3. **Proteger rutas** — en Next.js App Router esto se gestiona con un middleware o una comprobación a nivel de layout: si no hay token, redirigir a `/login`.
4. **Limpiar** el token al cerrar sesión y redirigir.

> **Nota:** La rotura temporal del frontend de la entrega anterior termina aquí. Al finalizar este proyecto, todas las vistas protegidas deben funcionar de extremo a extremo con autenticación real.

---

## 🌱 Cómo Iniciar el Proyecto

Este proyecto continúa dentro de tu monorepo existente. Trabaja en la misma rama o abre una nueva: `git checkout -b feature/auth-frontend`.

Asegúrate de que tu API de la entrega anterior está corriendo y es accesible desde el frontend antes de empezar.

---

## 💻 Qué Debes Hacer

### Vistas de autenticación

- [ ] `/login` — formulario de email y contraseña. Si tiene éxito: almacena el token en `localStorage`, redirige a la vista autenticada principal. Si falla: muestra un mensaje de error claro.
- [ ] `/register` — formulario de registro. Si tiene éxito: almacena el token, redirige. Si falla: muestra errores de validación a nivel de campo.

### Vistas de gestión de cuenta

- [ ] `/account/profile` — muestra los datos del usuario actual (nombre, email). Permite editar el nombre. Llama a `PUT /users/{id}` con el token en la cabecera.
- [ ] `/account/change-password` — formulario con la contraseña actual, la nueva contraseña y la confirmación. Valida que la nueva contraseña y la confirmación coinciden antes de llamar a la API.

### Protección de rutas

- [ ] Identifica todas las vistas de tus aplicaciones Next.js (excluyendo el website público) que requieren sesión autenticada.
- [ ] Implementa un mecanismo de protección — middleware, layout guard o un hook personalizado — que compruebe el token en `localStorage` y redirija a `/login` si está ausente o no es válido.
- [ ] Asegúrate de que el website público (Hito 1) no se ve afectado — sin comprobación de token, sin redirección.

### Ciclo de vida del token

- [ ] En login y registro: almacena el token en `localStorage`.
- [ ] En cada llamada protegida a la API: lee el token y adjúntalo como `Authorization: Bearer <token>`.
- [ ] Al cerrar sesión: elimina el token de `localStorage` y redirige a `/login`.
- [ ] Si una llamada protegida a la API devuelve `401`: limpia el token y redirige a `/login`.

---

## ✅ Qué Vamos a Evaluar

- [ ] Los formularios de login y registro funcionan de extremo a extremo: el token se almacena tras una llamada exitosa.
- [ ] Las vistas protegidas redirigen a `/login` cuando no hay un token válido en el almacenamiento.
- [ ] El website público (Hito 1) continúa funcionando sin ninguna comprobación de autenticación.
- [ ] La vista de perfil muestra y actualiza los datos del usuario actual usando el token.
- [ ] El logout elimina el token y redirige correctamente.
- [ ] Una respuesta `401` de cualquier llamada protegida a la API limpia la sesión y redirige a `/login`.

---

## 📦 Cómo Entregar

Sube tu rama y abre un pull request contra `main` en tu monorepo. La descripción del PR debe incluir: qué vistas están ahora protegidas y confirmación de que el website público no se vio afectado.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
