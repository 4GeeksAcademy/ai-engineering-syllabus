# Asegurando la API: Autenticación y Restricción de Rutas en FastAPI

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/fastapi-auth/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/como-iniciar-un-proyecto-de-programacion) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu Reto

La API de tu empresa está creciendo. Has construido endpoints que sirven datos al frontend, consultan la base de datos y procesan registros — pero en este momento, cualquier persona que conozca una URL puede llamarlos. Antes de que la plataforma pase a su siguiente fase, la CTO ha sido clara: **ninguna ruta que modifique o exponga datos sensibles debe ser accesible sin una sesión válida.**

Tu tech lead acaba de dejarte un ticket en la cola:

> #### AUTH-01 — Implementar autenticación y protección de rutas
>
> La API actualmente no tiene capa de autenticación. Esta tarea incluye:
>
> - Un módulo `users` con CRUD completo (crear, leer, actualizar, eliminar).
> - Un endpoint de login que valide credenciales y devuelva un token JWT firmado.
> - Una dependencia reutilizable `get_current_user` que decodifique el token e identifique al usuario.
> - Aplicación de esa dependencia a todas las rutas que no deben ser de acceso público.
>
> Usa `OAuth2PasswordBearer` de FastAPI y `python-jose` para la firma del token. Las contraseñas deben estar hasheadas — nunca almacenadas ni comparadas en texto plano. El token debe llevar como mínimo el ID del usuario y expirar tras una ventana configurable.
>
> Todas las rutas relacionadas con autenticación deben vivir bajo `/auth`. Las rutas de gestión de usuarios bajo `/users`.

Esto es una cuestión de seguridad, no una feature: el trabajo que hagas aquí protege todo lo que se construyó antes y todo lo que vendrá después. Hazlo bien.

> **Nota:** Una vez que protejas tus rutas, puede que algunas llamadas del frontend dejen de funcionar temporalmente — es algo esperado. El frontend se actualizará para enviar el token en una fase posterior. Por ahora, el foco está en asegurar la API para evitar fuga de datos y accesos indebidos.

### Conocimiento complementario: cómo funciona la autenticación JWT en FastAPI

Si no has implementado auth con JWT antes, este es el modelo mental: cuando un usuario hace login, el servidor firma un pequeño payload JSON (los "claims") usando una clave secreta y devuelve el resultado como una cadena de token. En las solicitudes siguientes, el cliente envía ese token en la cabecera `Authorization`. El servidor lo decodifica — si la firma es válida y el token no ha expirado, la solicitud continúa; si no, recibe un `401`.

En FastAPI, este flujo se implementa como una dependencia. Escribes una función que extrae el token de la solicitud, lo valida y devuelve el objeto usuario. Cualquier ruta que declare esa función como dependencia requerirá autenticación automáticamente.

---

## 🌱 Cómo Iniciar el Proyecto

Este proyecto es una extensión de tu API del proyecto transversal existente. **No crees un repositorio nuevo.** Trabaja dentro del codebase de backend actual de tu empresa.

1. Abre tu proyecto existente en Codespaces o clónalo en local.
2. Crea una nueva rama para esta feature: `git checkout -b feature/auth`.
3. Instala los paquetes necesarios:
   ```bash
   pip install python-jose[cryptography] passlib[bcrypt]
   ```
4. Añádelos a tu `requirements.txt`.



---

## 💻 Qué Debes Hacer

### Modelo de usuario y CRUD

- [ ] Crea un modelo `User` en la base de datos con al menos: `id`, `email`, `hashed_password`, `is_active`, `created_at`.
- [ ] Implementa una capa de servicios con funciones para: crear usuario, obtener usuario por ID, obtener usuario por email, actualizar usuario, eliminar usuario.
- [ ] Expón esos servicios como endpoints REST bajo `/users`:
  - `POST /users` — registrar un nuevo usuario (hashear la contraseña antes de guardar).
  - `GET /users` — listar todos los usuarios (protegida).
  - `GET /users/{id}` — obtener un usuario por ID (protegida).
  - `PUT /users/{id}` — actualizar un usuario (protegida; solo el propio usuario o un admin).
  - `DELETE /users/{id}` — eliminar un usuario (protegida).

### Endpoints de autenticación

- [ ] Implementa `POST /auth/login` — acepta `email` y `password`, valida credenciales y devuelve un token JWT de acceso.
- [ ] Implementa `POST /auth/register` — crea un nuevo usuario y devuelve un token para que el caller quede logueado inmediatamente.
- [ ] Implementa `GET /auth/me` (protegida) — devuelve el perfil del usuario actualmente autenticado.

### Token y dependencia

- [ ] Crea una dependencia `get_current_user` que: extraiga la cabecera `Authorization: Bearer <token>`, decodifique y valide el JWT, recupere el usuario de la base de datos y lance `HTTPException(401)` si algo falla.
- [ ] Configura la expiración del token mediante una variable de entorno (ej. `ACCESS_TOKEN_EXPIRE_MINUTES`). Guarda la clave de firma en `.env` — nunca la hardcodees.

### Protección de rutas

- [ ] Aplica `get_current_user` como dependencia a cada ruta que no deba ser pública. Como mínimo: todos los endpoints de `/users` excepto `POST /users`, y `/auth/me`.
- [ ] Devuelve `401 Unauthorized` para solicitudes no autenticadas y `403 Forbidden` cuando un usuario intenta acceder a un recurso que no le pertenece.

### Verificación

- [ ] Verifica el flujo completo manualmente usando los docs interactivos de FastAPI (`/docs`): registro → login → copiar token → usar el token en una ruta protegida.
- [ ] Confirma que llamar a una ruta protegida sin token devuelve `401`.
- [ ] Confirma que llamar a una ruta protegida con un token expirado o mal formado devuelve `401`.

⚠️ **IMPORTANTE:** No uses autenticación basada en sesiones ni en cookies. Este proyecto implementa únicamente auth JWT stateless.

⚠️ **IMPORTANTE:** Nunca almacenes contraseñas en texto plano. Usa `passlib` con el esquema `bcrypt` para todas las operaciones con contraseñas.

---

## ✅ Qué Vamos a Evaluar

- [ ] El CRUD de usuarios está completamente implementado y accesible a través de la API.
- [ ] Las contraseñas se hashean al crear el usuario y se comparan correctamente en el login — el texto plano nunca toca la base de datos.
- [ ] El endpoint de login devuelve un token JWT válido y firmado.
- [ ] La dependencia `get_current_user` decodifica correctamente el token e identifica al usuario.
- [ ] Las rutas protegidas devuelven `401` al ser llamadas sin un token válido.
- [ ] La expiración del token y la clave de firma se leen desde variables de entorno, no están hardcodeadas.
- [ ] Las rutas de auth están bajo `/auth` y las de usuarios bajo `/users` — estructura limpia y coherente.
- [ ] Las rutas existentes del proyecto continúan funcionando (sin regresiones).

> Nota: El control de acceso basado en roles (admin vs. usuario regular) no es requerido para esta entrega, aunque es una extensión válida si el tiempo lo permite.

---

## 📦 Cómo Entregar

Sube tu rama a GitHub y abre un pull request contra `main` en el repositorio de tu proyecto transversal. Comparte el enlace al PR con tu instructor. La descripción del PR debe incluir una nota breve sobre qué rutas están ahora protegidas y cómo lo verificaste.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
