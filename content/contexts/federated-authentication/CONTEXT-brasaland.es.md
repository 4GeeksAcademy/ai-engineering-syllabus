# CONTEXT — Autenticación Federada · Brasaland

_These instructions are also available in [English](./CONTEXT-brasaland.md)._

> **Proyecto:** Plataforma – Autenticación Federada  
> **Ruta en el repositorio:** `content/contexts/federated-authentication/CONTEXT-brasaland.es.md`

---

## 1. Por qué le importa a Brasaland

Los clientes de Brasaland usan la app de pedidos y el programa de puntos desde el móvil, y odian crear una contraseña más. El personal de sede también inicia sesión a diario en el sistema interno desde tablets compartidas. Reducir fricción de login importa en ambos casos, pero la seguridad de la cuenta importa aún más: nadie externo debe poder entrar a una cuenta con puntos acumulados o datos de un empleado.

## 2. Proveedor de identidad elegido

**Google** — es el proveedor con mayor tasa de uso entre los consumidores de Brasaland en ambos mercados (Colombia y Florida) y ya es el estándar de facto para apps de restaurantes en la región.

Si tu implementación lo justifica, puedes ofrecer un segundo proveedor (por ejemplo Apple, común en el mercado de Florida), pero Google es el requisito mínimo.

| Código `provider` | ¿Obligatorio? | Notas                                                                   |
| ----------------- | ------------- | ----------------------------------------------------------------------- |
| `google`          | **sí**        | OAuth 2.0 / OIDC. Mínimo de este CONTEXT.                               |
| `apple`           | opcional      | Solo si implementas un segundo proveedor. Mismas reglas de vinculación. |

## 3. Dónde aplica

- **App de clientes (Brasa Points):** el cliente final puede vincular su cuenta de Google desde su perfil, después de haberse registrado con el método tradicional.
- **Backoffice interno:** el personal corporativo (no el staff de sede, que suele compartir dispositivo) puede vincular su cuenta de Google corporativa desde su perfil de usuario.

**No** habilites login federado en tablets compartidas de local. Dispositivo compartido + "Iniciar sesión con Google" es riesgo de mezcla de cuentas.

## 4. Regla de vinculación (recordatorio del README)

La vinculación **solo** ocurre desde el perfil de un usuario con sesión ya iniciada. Un cliente que llega por primera vez con "Iniciar sesión con Google" y no tiene cuenta previa debe ser rechazado y dirigido a crear su cuenta primero por el método tradicional.

La desvinculación vive en la misma pantalla de perfil. Si Google es el **único** método de acceso que queda (sin contraseña, sin segundo proveedor), la UI debe advertir y la API debe rechazar la desvinculación hasta que exista otro método.

Una identidad Google (`provider` + `provider_user_id`) no puede vincularse a dos usuarios de Brasaland a la vez.

## 5. Modelo de datos y OAuth

Guarda el vínculo, no la sesión de Google.

| Campo                | Tipo      | Reglas                                      |
| -------------------- | --------- | ------------------------------------------- |
| `user_id`            | FK → User | requerido                                   |
| `provider`           | string    | `google` (o `apple` si lo ofreces)          |
| `provider_user_id`   | string    | `sub` de Google. Único junto con `provider` |
| `email_at_link_time` | string    | snapshot — no es la clave de identidad      |
| `linked_at`          | datetime  | sistema                                     |

**No** persistas access/refresh tokens de Google en texto plano. Si debes guardar un token, cífralo; este proyecto no exige guardar tokens.

OAuth debe validar `state` (CSRF / fijación de sesión) y un `redirect_uri` en lista blanca.

```bash
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
OAUTH_REDIRECT_URI=http://localhost:3000/auth/callback/google
```

Los `redirect_uri` permitidos son coincidencia exacta. Un callback con otro `redirect_uri` se rechaza.

## 6. Dato de seed necesario

Crea al menos un usuario de prueba (cliente) con una cuenta Google vinculada y otro sin vincular, para poder probar ambos caminos del flujo de login.

```python
USERS_SEED = [
    {
        "email": "camila.points@brasaland.example",
        "name": "Camila Ospina",
        "has_password": True,
        "linked_providers": [
            {"provider": "google", "provider_user_id": "google-sub-camila-001"}
        ],
    },
    {
        "email": "guest.unlinked@brasaland.example",
        "name": "Unlinked Guest",
        "has_password": True,
        "linked_providers": [],
    },
]
```

Una tercera identidad Google **que no** esté en `linked_providers` es el fixture de login rechazado (p. ej. `provider_user_id: "google-sub-unknown-999"`).

## 7. Eventos de auditoría (obligatorios)

Registra estos con timestamp, `user_id` (nullable en rechazo), `provider` y `provider_user_id`:

| `event`                    | Cuándo                                                             |
| -------------------------- | ------------------------------------------------------------------ |
| `federated_link`           | Proveedor vinculado desde perfil autenticado                       |
| `federated_unlink`         | Proveedor desvinculado                                             |
| `federated_login_success`  | Sign-in con proveedor ya vinculado                                 |
| `federated_login_rejected` | Sign-in con proveedor no vinculado — **sin crear fila de usuario** |

## 8. Criterio de aceptación específico

Un intento de "Iniciar sesión con Google" desde un correo que nunca se vinculó a ninguna cuenta de Brasaland debe mostrar un mensaje claro invitando a registrarse primero — nunca debe crear silenciosamente una cuenta nueva con puntos en cero.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
