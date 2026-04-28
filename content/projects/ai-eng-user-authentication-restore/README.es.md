# La Pieza Que Faltaba: Flujo de Restablecimiento de Contraseña

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/como-iniciar-un-proyecto-de-programacion) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu Reto

El sistema de autenticación está funcionando. Los usuarios pueden registrarse, iniciar sesión, gestionar su perfil y cambiar su contraseña — siempre que la recuerden.

¿Pero qué ocurre cuando no la recuerdan?

Ahora mismo, un usuario que olvida su contraseña no tiene forma de recuperar su cuenta. Y más allá de eso: en cualquier sistema en producción, cambiar la contraseña periódicamente es una práctica básica de seguridad. Tu plataforma no tiene ningún mecanismo para ninguna de las dos cosas.

Tu tech lead ha abierto el ticket:

> #### AUTH-03 — Flujo de restablecimiento de contraseña
>
> La plataforma necesita un mecanismo completo de restablecimiento de contraseña. Esto cubre tanto la API como el frontend:
>
> **Backend:**
> - `POST /auth/forgot-password` — recibe un email, valida que el usuario existe, genera un token de restablecimiento firmado de corta duración y envía un enlace de restablecimiento a la dirección del usuario.
> - `POST /auth/reset-password` — recibe el token de restablecimiento y una nueva contraseña, valida el token (firma + expiración), hashea la nueva contraseña y actualiza el registro del usuario. El token debe quedar invalidado tras su uso.
>
> **Frontend:**
> - `/forgot-password` — formulario donde el usuario introduce su email. Siempre muestra un mensaje de confirmación tras el envío, independientemente de si la dirección existe, para evitar la enumeración de usuarios.
> - `/reset-password` — formulario donde el usuario establece una nueva contraseña. Lee el token de restablecimiento del query string de la URL y lo envía a la API junto con la nueva contraseña. Si tiene éxito, redirige a `/login`.
>
> Para el envío de correos, elige uno de los siguientes servicios e intégralo:
> - [Mailgun](https://www.mailgun.com/)
> - [MailerSend](https://www.mailersend.com/)
> - [SendGrid (Twilio)](https://www.twilio.com/en-us/sendgrid)
>
> Los tres ofrecen un tier gratuito suficiente para desarrollo. Las API keys deben almacenarse en variables de entorno — nunca en el código fuente.

### Conocimiento complementario: cómo funciona un flujo de restablecimiento de contraseña

El flujo tiene tres pasos y dos momentos separados en el tiempo:

1. **Solicitud** — el usuario envía su email. El servidor genera un token de restablecimiento (un JWT firmado o una cadena aleatoria almacenada en la base de datos), construye una URL de restablecimiento que contiene ese token (`/reset-password?token=<token>`) y la envía al email del usuario mediante un servicio de correo transaccional.

2. **Restablecimiento** — el usuario hace clic en el enlace, llega a la página `/reset-password`, introduce una nueva contraseña y envía el formulario. El frontend envía el token (leído de la URL) y la nueva contraseña a la API. El servidor valida el token — si la firma es válida y no ha expirado — actualiza la contraseña e invalida el token para que no pueda reutilizarse.

3. **Confirmación** — el usuario es redirigido a `/login` y puede iniciar sesión con la nueva contraseña.

**¿Por qué mostrar siempre un mensaje de confirmación?** Si el formulario muestra "email no encontrado" para direcciones que no existen, un atacante puede usar eso para enumerar qué emails están registrados. Responder siempre con "si esa dirección está en nuestro sistema, recibirás un enlace" lo evita.

**La expiración del token importa.** Un token de restablecimiento debe tener una vida corta — entre 15 y 60 minutos es lo estándar. Una vez usado o expirado, no debe poder reutilizarse. Si usas un JWT, codifica la expiración en el payload. Si usas una cadena aleatoria almacenada en la base de datos, guarda el timestamp de expiración junto a ella.

---

## 🌱 Cómo Iniciar el Proyecto

Este proyecto continúa dentro de tu monorepo existente. Abre una nueva rama: `git checkout -b feature/password-reset`.

Antes de empezar, regístrate en uno de los servicios de email listados arriba y obtén una API key. Guárdala en tu archivo `.env`. Asegúrate de que `.env` está en tu `.gitignore` — nunca hagas commit de API keys.

---

## 💻 Qué Debes Hacer

### Backend

- [ ] `POST /auth/forgot-password` — acepta `{ email }`. Si el usuario existe, genera un token de restablecimiento con expiración corta (15–60 minutos) y envía un email con el enlace de restablecimiento. Devuelve siempre `200` independientemente de si el email fue encontrado.
- [ ] `POST /auth/reset-password` — acepta `{ token, new_password }`. Valida el token (firma y expiración). Si es válido, hashea la nueva contraseña, actualiza el registro del usuario e invalida el token. Devuelve `400` para tokens inválidos o expirados.
- [ ] Integra un servicio de correo transaccional (Mailgun, MailerSend o SendGrid) para enviar el email de restablecimiento. El email debe incluir el enlace de restablecimiento y ser legible en móvil.
- [ ] Almacena la API key del servicio de email en una variable de entorno. Documenta el nombre de la variable en tu `README` o en un `.env.example`.

### Frontend

- [ ] `/forgot-password` — formulario con campo de email. Al enviarlo, llama a `POST /auth/forgot-password` y muestra un mensaje de confirmación ("Si esa dirección está registrada, recibirás un enlace en breve"). El formulario debe desactivarse tras el envío para evitar peticiones duplicadas.
- [ ] `/reset-password` — formulario de nueva contraseña con campo de confirmación. Lee el `token` del query string de la URL. Al enviarlo, llama a `POST /auth/reset-password`. Si tiene éxito, redirige a `/login` con un mensaje de éxito. Si falla (token expirado o inválido), muestra un error claro y un enlace de vuelta a `/forgot-password`.
- [ ] Añade un enlace "¿Olvidaste tu contraseña?" en la página `/login` que apunte a `/forgot-password`.

### Seguridad

- [ ] Los tokens de restablecimiento deben expirar e invalidarse tras su uso — un token no puede usarse dos veces.
- [ ] El endpoint `/forgot-password` debe devolver siempre `200`, nunca revelar si un email está registrado.
- [ ] Las API keys no deben aparecer nunca en el código fuente — usa exclusivamente variables de entorno.

---

## 🚀 Para ir más lejos (opcional)

No se evalúan, pero son extensiones válidas si el tiempo lo permite:

- **Plantilla de email en HTML** — envía un email con estilos en lugar de un enlace en texto plano.
- **Rate limiting** — limita el número de solicitudes de restablecimiento por dirección de email por hora para prevenir abusos.
- **Registro de auditoría** — registra cada evento de restablecimiento de contraseña (timestamp, dirección IP) en la base de datos.

---

## ✅ Qué Vamos a Evaluar

- [ ] `POST /auth/forgot-password` envía un email real con el enlace de restablecimiento cuando se llama con una dirección registrada.
- [ ] `POST /auth/forgot-password` devuelve `200` incluso cuando la dirección no está registrada — no se filtra información.
- [ ] El token de restablecimiento expira tras la ventana configurada y no puede usarse después de expirar.
- [ ] `POST /auth/reset-password` actualiza la contraseña e invalida el token en caso de éxito.
- [ ] `POST /auth/reset-password` devuelve `400` para tokens expirados o ya utilizados.
- [ ] `/forgot-password` muestra un mensaje de confirmación tras el envío independientemente del resultado.
- [ ] `/reset-password` lee el token de la URL, envía el formulario y redirige a `/login` en caso de éxito.
- [ ] `/reset-password` muestra un error claro con un enlace de vuelta a `/forgot-password` cuando el token es inválido o ha expirado.
- [ ] La página `/login` tiene un enlace visible a "¿Olvidaste tu contraseña?".
- [ ] Ninguna API key está en el código fuente — todos los secretos se cargan desde variables de entorno.

---

## 📦 Cómo Entregar

Sube tu rama y abre un pull request contra `main` en tu monorepo. La descripción del PR debe incluir: qué servicio de email elegiste, el nombre de la variable de entorno necesaria para ejecutar la feature y confirmación de que probaste el flujo completo de extremo a extremo.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
