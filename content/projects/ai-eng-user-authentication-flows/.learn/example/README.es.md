# Ejemplo en Clase — Flujos de Auth para una App de Recetas

> **Nota para el instructor:** Este es un ejemplo diseñado para el ritmo del aula que introduce los mismos conceptos que el proyecto evaluado (flujos de autenticación en el frontend). Se utiliza un dominio diferente para que los estudiantes no lo confundan con su propio trabajo. Una colección personal de recetas es suficientemente sencilla para razonar en clase mientras se cubren todos los patrones clave: almacenamiento de token, rutas protegidas, gestión de perfil y cierre de sesión.

_These instructions are also available in [English](./README.md)._

---

## El Escenario

### Nota de alcance

Este ejemplo está acotado para una sesión en vivo en el aula. Mantiene el mismo stack y patrones centrales que el proyecto oficial del estudiante en esta carpeta pero omite requisitos secundarios; ver la nota para instructores arriba. Los estudiantes siguen el enunciado completo en el `README.md` de la raíz del proyecto.

**Recipe Box** es una app Next.js donde los usuarios guardan y organizan sus recetas favoritas. La API ya requiere un token JWT en las rutas protegidas (implementado en la clase anterior). Ahora los estudiantes necesitan conectar el frontend: login, registro, página de perfil y protección de rutas para que solo los usuarios autenticados puedan acceder a su colección de recetas.

---

## Requisitos Previos

- La API FastAPI de auth de la clase anterior está en funcionamiento y es accesible.
- `NEXT_PUBLIC_API_URL` está configurado en `.env.local`.

---

## Qué Construir

### Vistas de autenticación

**`/login`**

- [ ] Formulario de email y contraseña.
- [ ] Si tiene éxito: guardar el token JWT en `localStorage` como `access_token`, luego redirigir a `/recipes`.
- [ ] Si falla: mostrar un mensaje de error claro a nivel de campo (ej. "Email o contraseña inválidos").
- [ ] Enlace a `/register` para nuevos usuarios.

**`/register`**

- [ ] Formulario de nombre, email y contraseña con un campo de confirmación de contraseña.
- [ ] Validar que la contraseña y la confirmación coinciden antes de llamar a la API.
- [ ] Si tiene éxito: llamar a `POST /users`, luego a `POST /auth/login`, guardar el token, redirigir a `/recipes`.
- [ ] Si falla: mostrar errores de validación específicos por campo.

---

### Vistas de cuenta

**`/account/profile`**

- [ ] Obtener `GET /auth/me` (con el token en la cabecera `Authorization`) y mostrar email más campos de perfil (`name`, `phone`, `address`).
- [ ] Permitir editar nombre y contacto. Llamar a `PUT /profiles/me` con el token.
- [ ] Mostrar un mensaje de éxito después de guardar.

---

### Protección de rutas

- [ ] Cada página bajo `/recipes` y `/account` requiere un token válido en `localStorage`.
- [ ] Implementar un guard de layout o middleware: si no se encuentra token, redirigir a `/login`.
- [ ] La página de inicio (`/`) y `/login` y `/register` deben permanecer completamente públicas — sin comprobación de token.

```
Rutas protegidas: /recipes, /account/profile
Rutas públicas:   /, /login, /register
```

---

### Ciclo de vida del token

| Evento                          | Acción                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------- |
| Login / registro exitoso        | Guardar token → `localStorage.setItem('access_token', token)`                     |
| Cada llamada protegida a la API | Leer token → establecer cabecera `Authorization: Bearer <token>`                  |
| Cierre de sesión                | Eliminar token → `localStorage.removeItem('access_token')` → redirigir a `/login` |
| La API responde con `401`       | Limpiar token → redirigir a `/login`                                              |

---

## Helper Sugerido (reutilizar en cada llamada fetch)

```ts
// lib/api.ts
export function authHeader(): HeadersInit {
  const token = localStorage.getItem("access_token");
  return token ? { Authorization: `Bearer ${token}` } : {};
}
```

---

## Conceptos Clave a Trabajar en Clase

| Concepto                                     | Dónde aparece                                    |
| -------------------------------------------- | ------------------------------------------------ |
| `localStorage` para almacenamiento del token | `setItem` / `getItem` / `removeItem`             |
| Adjuntar cabecera `Authorization`            | Cada llamada protegida a `fetch`                 |
| Middleware / guard de layout en Next.js      | `middleware.ts` o comprobación a nivel de layout |
| Redirección por token ausente                | `useRouter().push('/login')`                     |
| Gestión de `401` de la API                   | Limpiar sesión y redirigir                       |
| Validación de confirmación de contraseña     | En el cliente antes de la llamada a la API       |

---

## Preguntas para Debate

1. Estamos guardando el token en `localStorage`. ¿Cuáles son los riesgos de seguridad de este enfoque comparado con las cookies `httpOnly`? ¿Cuándo elegirías uno frente al otro?
2. El guard de layout redirige a `/login` si no hay token. ¿Pero qué pasa si el token existe pero ha expirado? ¿Cómo detectarías eso sin hacer una llamada extra a la API en cada carga de página?
3. Si un usuario tiene la app abierta en dos pestañas del navegador y cierra sesión en una, ¿qué ocurre en la otra pestaña? ¿Cómo lo gestionarías de forma elegante?
