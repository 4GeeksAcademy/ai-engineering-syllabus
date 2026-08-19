# Plataforma – Autenticación Federada

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee tu **[COMPANY-BRIEF.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts)** y tu **[CONTEXT-federated-auth.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/federated-authentication)** antes de escribir una sola línea de código — ahí está el proveedor de identidad elegido y las reglas de seguridad específicas de tu empresa.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa — no en un repositorio nuevo.

El equipo de soporte ha filado varios **tickets** de usuarios pidiendo iniciar sesión con su cuenta de Google o Microsoft en lugar de recordar otra contraseña más. Tu CTO acepta la idea, pero pone una condición de seguridad que no es negociable.

> _"Quiero autenticación federada, pero con una regla estricta: el login federado **solo puede usarse para entrar a una cuenta que ya existe y que el propio usuario vinculó explícitamente desde su perfil**. No quiero que alguien pueda crear una cuenta nueva simplemente apareciendo con un login de Google — eso abre la puerta a que cualquiera con acceso a un correo externo se cree una identidad dentro de nuestro sistema sin pasar por ningún control nuestro. La vinculación es un acto consciente del usuario, hecho desde dentro de la aplicación, no un efecto secundario del login."_
>
> — CTO

Léelo con atención porque cambia el flujo que probablemente tenías en mente:

1. **El login federado no crea cuentas.** Si alguien intenta iniciar sesión con un proveedor externo y ese proveedor no está vinculado a ninguna cuenta existente, el sistema debe rechazarlo — nunca crear una cuenta nueva automáticamente a partir de ese intento.
2. **La vinculación ocurre en un solo lugar: el perfil del usuario ya autenticado.** Un usuario con sesión iniciada por el método tradicional decide, desde su configuración de cuenta, asociar un proveedor externo. A partir de ese momento, ese proveedor puede usarse para futuros inicios de sesión.
3. **La desvinculación debe ser igual de accesible que la vinculación**, y no debe dejar al usuario sin ninguna forma de acceder a su cuenta.

### Conocimiento complementario: por qué esto es una decisión de seguridad, no de conveniencia

Permitir que el login federado cree cuentas automáticamente parece más simple, pero traslada la decisión de "quién puede entrar a mi sistema" a un proveedor externo que no controlas. Si el flujo permite crear cuenta con solo aparecer con un correo válido, alguien podría registrarse con un correo que técnicamente no le pertenece de forma verificable para tu negocio, o suplantar el patrón de correo corporativo si no hay una validación explícita detrás. Exigir que la vinculación se haga desde una sesión ya autenticada garantiza que siempre hay un humano con una identidad ya verificada por tu sistema tomando esa decisión — el proveedor externo nunca es, por sí solo, la puerta de entrada.

---

## 🌱 Cómo Empezar el Proyecto

1. Haz `pull` de los últimos cambios de tu fork del monorepo.
2. Lee `COMPANY-BRIEF.md` y `CONTEXT-federated-auth.md` completos antes de tocar código.
3. Crea una rama nueva: `feature/federated-auth`.
4. Revisa el flujo de autenticación actual y el modelo de usuario existente antes de decidir cómo se almacenará la vinculación.
5. Diseña primero el diagrama de los dos flujos por separado — vinculación y login federado — porque comparten proveedor pero no comparten lógica.

---

## 💻 Qué Debes Hacer

**Modelo de datos**

- [ ] Modela la relación entre un usuario y sus proveedores externos vinculados, permitiendo cero, uno o varios proveedores por usuario
- [ ] Almacena únicamente los identificadores necesarios del proveedor externo — nunca credenciales ni tokens de larga duración sin cifrar

**Flujo de vinculación (desde el perfil)**

- [ ] Implementa la vinculación de un proveedor externo accesible únicamente desde el perfil de un usuario ya autenticado
- [ ] Verifica que el proveedor externo que se intenta vincular no esté ya vinculado a otra cuenta distinta
- [ ] Confirma al usuario, dentro de la interfaz, que la vinculación se completó y qué proveedor quedó asociado
- [ ] Implementa la desvinculación desde el mismo lugar, con una advertencia si es el único método de acceso disponible

**Flujo de login federado**

- [ ] Implementa el inicio de sesión con el proveedor externo únicamente para cuentas que ya tienen ese proveedor vinculado
- [ ] Rechaza explícitamente el intento de login cuando el proveedor externo no está vinculado a ninguna cuenta — sin crear una cuenta nueva como efecto colateral
- [ ] Registra en el sistema de auditoría todo evento de vinculación, desvinculación e intento de login federado rechazado

**Seguridad**

- [ ] Implementa el flujo OAuth con validación de `state` y `redirect_uri` para prevenir ataques de fijación de sesión
- [ ] Asegura que la sesión creada tras un login federado exitoso tiene el mismo nivel de expiración y revocación que una sesión tradicional

⚠️ **IMPORTANTE:** el proveedor o proveedores de identidad exigidos y cualquier regla adicional de seguridad para tu empresa deben corresponder exactamente a lo especificado en tu `CONTEXT-federated-auth.md`. Una implementación genérica que ignore ese contexto no será aceptada.

---

## ✅ Qué Vamos a Evaluar

- [ ] Un intento de login federado con un proveedor no vinculado es rechazado explícitamente y no crea una cuenta nueva, verificado con una prueba
- [ ] La vinculación de un proveedor externo solo es accesible desde el perfil de una sesión ya autenticada, nunca desde la pantalla de login
- [ ] Un proveedor externo no puede vincularse simultáneamente a dos cuentas distintas
- [ ] La desvinculación funciona y avisa al usuario si queda sin métodos de acceso alternativos
- [ ] Todo evento de vinculación, desvinculación y login federado rechazado queda registrado de forma auditable
- [ ] El flujo OAuth implementa validación de `state` y `redirect_uri`

---

## 📦 Cómo Entregar

Abre un Pull Request desde tu rama `feature/federated-auth` hacia `main` en tu fork. En la descripción del PR incluye un diagrama o descripción de los dos flujos (vinculación y login) y evidencia de que un intento de login con un proveedor no vinculado es rechazado. Solicita el sign-off de tu CTO antes de hacer merge.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
