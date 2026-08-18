# CONTEXT — Autenticación Federada · Nexova

_These instructions are also available in [English](./CONTEXT-nexova.md)._

> **Proyecto:** Plataforma – Autenticación Federada  
> **Ruta en el repositorio:** `content/contexts/federated-authentication/CONTEXT-nexova.es.md`

---

## 1. Por qué le importa a Nexova

Nexova trabaja con candidatos que ya tienen su perfil profesional completo en otra plataforma. Pedirles crear y recordar otra contraseña solo para postularse o seguir su proceso de selección es fricción innecesaria — y tanto Marcos Ibáñez (Ventas) como Javier Almeida (Operaciones) coinciden en que cada paso extra en el formulario reduce postulaciones completadas.

## 2. Proveedor de identidad elegido

**LinkedIn** — es donde el candidato objetivo de Nexova (perfiles de headhunting ejecutivo y mandos medios) ya mantiene su información profesional al día. Usar LinkedIn también permite, en fases futuras, prellenar parte del perfil del candidato — pero eso no forma parte de este proyecto.

| Código `provider` | ¿Obligatorio? | Notas                                                                 |
| ----------------- | ------------- | --------------------------------------------------------------------- |
| `linkedin`        | **sí**        | LinkedIn OAuth 2.0 / OIDC. Único proveedor permitido en este CONTEXT. |

**No** implementes prellenado de perfil, importación de CV ni publicación en LinkedIn. Este proyecto es solo vinculación de identidad y login.

## 3. Dónde aplica

- **Portal de candidatos:** un candidato que ya se registró por el método tradicional puede vincular su cuenta de LinkedIn desde su perfil, para futuros inicios de sesión más rápidos.
- **Uso interno:** el staff de Nexova (consultores, ventas, soporte) no usa LinkedIn como proveedor federado — no apliques este proyecto al staff interno, o usa otro proveedor corporativo si tu contexto lo exige.

## 4. Regla de vinculación (recordatorio del README)

La vinculación solo ocurre desde el perfil de un candidato con sesión ya iniciada. Un visitante que llega con "Continuar con LinkedIn" y no tiene cuenta previa en Nexova debe ser dirigido a registrarse primero.

La desvinculación vive en la misma pantalla de perfil. Si LinkedIn es el **único** método de acceso que queda, la UI debe advertir y la API debe rechazar la desvinculación hasta que exista contraseña.

Una identidad LinkedIn (`provider` + `provider_user_id`) no puede vincularse a dos cuentas de candidato a la vez.

## 5. Modelo de datos y OAuth

Guarda el vínculo, no la sesión de LinkedIn.

| Campo                | Tipo      | Reglas                                                    |
| -------------------- | --------- | --------------------------------------------------------- |
| `user_id`            | FK → User | requerido; solo candidato                                 |
| `provider`           | string    | `linkedin`                                                |
| `provider_user_id`   | string    | member id / `sub` de LinkedIn. Único junto con `provider` |
| `email_at_link_time` | string    | snapshot                                                  |
| `linked_at`          | datetime  | sistema                                                   |

**No** persistas access/refresh tokens de LinkedIn en texto plano. Este proyecto no exige guardar tokens.

OAuth debe validar `state` y un `redirect_uri` en lista blanca.

```bash
LINKEDIN_CLIENT_ID=...
LINKEDIN_CLIENT_SECRET=...
OAUTH_REDIRECT_URI=http://localhost:3000/auth/callback/linkedin
```

Un callback con `redirect_uri` distinto se rechaza.

## 6. Dato de seed necesario

Crea al menos un candidato de prueba con LinkedIn vinculado y otro sin vincular.

```python
USERS_SEED = [
    {
        "email": "candidate.linked@nexova.example",
        "name": "Alex Rivera",
        "audience": "candidate",
        "has_password": True,
        "linked_providers": [
            {"provider": "linkedin", "provider_user_id": "li-sub-alex-001"}
        ],
    },
    {
        "email": "candidate.unlinked@nexova.example",
        "name": "Jordan Lee",
        "audience": "candidate",
        "has_password": True,
        "linked_providers": [],
    },
]
```

Una identidad LinkedIn **que no** esté en `linked_providers` (p. ej. `li-sub-unknown-999`) es el fixture de login rechazado.

## 7. Eventos de auditoría (obligatorios)

Registra estos con timestamp, `user_id` (nullable en rechazo), `provider` y `provider_user_id`:

| `event`                    | Cuándo                                                               |
| -------------------------- | -------------------------------------------------------------------- |
| `federated_link`           | LinkedIn vinculado desde perfil de candidato autenticado             |
| `federated_unlink`         | LinkedIn desvinculado                                                |
| `federated_login_success`  | Continuar con LinkedIn en una cuenta ya vinculada                    |
| `federated_login_rejected` | Continuar con LinkedIn sin vínculo — **sin crear fila de candidato** |

## 8. Criterio de aceptación específico

Un intento de "Continuar con LinkedIn" desde una cuenta no vinculada a ningún candidato existente debe mostrar un mensaje claro invitando a registrarse primero, sin crear un perfil de candidato vacío como efecto secundario.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
