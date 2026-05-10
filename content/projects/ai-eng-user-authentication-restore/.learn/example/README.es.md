# Ejemplo en Clase — Restablecimiento de Contraseña para un Rastreador de Salud de Mascotas

> **Nota para el instructor:** Este es un ejemplo diseñado para el ritmo del aula que introduce los mismos conceptos que el proyecto evaluado (flujo de restablecimiento de contraseña). Se utiliza un dominio diferente para que los estudiantes no lo confundan con su propio trabajo. Un rastreador de salud de mascotas es concreto y personal — los usuarios se preocupan por su cuenta, lo que hace que el escenario de "olvidé mi contraseña" se sienta real. El objetivo es trabajar juntos el flujo completo de restablecimiento: endpoints del backend, correo transaccional y páginas del frontend.

_These instructions are also available in [English](./README.md)._

---

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.


**PawLog** es una app donde los dueños de mascotas registran las vacunas, visitas al veterinario y medicamentos de sus animales. El sistema de auth (registro, login, perfil) ya está funcionando. Lo que falta: los usuarios que olvidan su contraseña no tienen forma de recuperar su cuenta.

Hoy construimos el flujo completo de restablecimiento de contraseña — endpoints de la API + páginas del frontend + un correo transaccional.

---

## Cómo Funciona el Flujo

```
1. /forgot-password  →  POST /auth/forgot-password { email }
                    ←  200 OK (siempre, aunque el email no exista)
                    →  Email enviado con enlace: /reset-password?token=<token>

2. Usuario hace clic → /reset-password?token=<token>
                    →  POST /auth/reset-password { token, new_password }
                    ←  200 OK → redirigir a /login
                    ←  400 Bad Request (expirado o ya usado) → mostrar error

3. /login  ← el usuario inicia sesión con la nueva contraseña
```

---

## Backend

### `POST /auth/forgot-password`

- [ ] Aceptar `{ email }` en el cuerpo de la petición.
- [ ] Si el usuario existe: generar un token de restablecimiento de corta duración (JWT con expiración de 30 minutos es suficiente para clase, o una cadena aleatoria almacenada en una tabla `reset_tokens`).
- [ ] Enviar un email con el enlace de restablecimiento: `http://localhost:3000/reset-password?token=<token>`.
- [ ] **Devolver siempre `200`** — nunca revelar si el email está registrado.

```python
# Ejemplo de payload para un JWT de restablecimiento
{
  "sub": user.id,
  "type": "password_reset",
  "exp": datetime.utcnow() + timedelta(minutes=30)
}
```

### `POST /auth/reset-password`

- [ ] Aceptar `{ token, new_password }`.
- [ ] Validar el token: comprobar firma y expiración.
- [ ] Si es válido: hashear la nueva contraseña, actualizar el registro del usuario, invalidar el token (marcar como usado si se almacena en BD, o confiar en la expiración para JWT).
- [ ] Devolver `200` en caso de éxito.
- [ ] Devolver `400` para tokens inválidos, expirados o ya utilizados.

### Integración de correo

Elige uno de estos servicios con tier gratuito:

| Servicio | Tier gratuito |
|---|---|
| [MailerSend](https://www.mailersend.com/) | 3.000 correos/mes |
| [Mailgun](https://www.mailgun.com/) | 100 correos/día |
| [SendGrid](https://sendgrid.com/) | 100 correos/día |

- [ ] Guardar la API key en `.env` (ej. `MAILERSEND_API_KEY`). Nunca hardcodearla.
- [ ] El correo debe contener el enlace de restablecimiento y ser legible en móvil. Un cuerpo en texto plano es suficiente para clase.

---

## Frontend

### `/forgot-password`

- [ ] Formulario con campo de email.
- [ ] Al enviar: llamar a `POST /auth/forgot-password`.
- [ ] **Mostrar siempre este mensaje de confirmación** (independientemente de si el email existe):
  > "Si esa dirección está en nuestro sistema, recibirás un enlace de restablecimiento en breve."
- [ ] Desactivar el formulario tras el envío para evitar peticiones duplicadas.
- [ ] Enlace de vuelta a `/login`.

### `/reset-password`

- [ ] Leer el `token` del query string de la URL: `new URLSearchParams(window.location.search).get('token')`.
- [ ] Mostrar un campo de nueva contraseña y un campo de confirmación.
- [ ] Al enviar: llamar a `POST /auth/reset-password` con `{ token, new_password }`.
- [ ] Si tiene éxito: redirigir a `/login` con un mensaje de éxito (ej. mediante un query param o toast en `localStorage`).
- [ ] Si falla (400 de la API): mostrar *"Este enlace ha expirado o ya ha sido utilizado. [Solicita uno nuevo](/forgot-password)."*

### Actualización de `/login`

- [ ] Añadir un enlace **"¿Olvidaste tu contraseña?"** que apunte a `/forgot-password`.

---

## Lista de Verificación de Seguridad

- [ ] El endpoint `/forgot-password` devuelve `200` incluso para emails no registrados.
- [ ] Los tokens de restablecimiento expiran (15–60 minutos).
- [ ] Un token usado no puede reutilizarse — debe invalidarse tras un restablecimiento exitoso.
- [ ] No hay API keys en el código fuente — solo en `.env`.

---

## Conceptos Clave a Trabajar en Clase

| Concepto | Dónde aparece |
|---|---|
| Token firmado de corta duración para restablecimiento | JWT con claim `"type": "password_reset"` |
| Prevención de enumeración de usuarios | Devolver siempre `200` en forgot-password |
| Invalidación del token tras su uso | Flag en BD o trade-offs de JWT solo con expiración |
| Integración de correo transaccional | API key en `.env`, llamada HTTP al servicio de correo |
| Leer query params en Next.js | `useSearchParams()` o `URLSearchParams` |
| Deshabilitar formulario tras envío | Evitar peticiones de restablecimiento duplicadas |

---

## Preguntas para Debate

1. ¿Por qué devolvemos siempre `200` desde `/forgot-password`, incluso si el email no existe? ¿Qué ataque previene esto?
2. Estamos usando un JWT de corta duración como token de restablecimiento. ¿Cuál es la ventaja frente a almacenar una cadena aleatoria en la base de datos? ¿Cuál es la desventaja?
3. Un usuario solicita un enlace de restablecimiento y luego solicita otro antes de que el primero expire. ¿Debería el primer enlace seguir funcionando? ¿Cómo diseñarías el sistema para manejar esto?
