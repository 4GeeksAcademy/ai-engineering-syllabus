# Ejemplo en clase: Gimnasio del barrio — Tablero de check-in (Docker Compose)

> **Para instructores:** No es la entrega del estudiante. Úsalo como demo en vivo de 60–90 minutos con la misma columna vertebral técnica que `launch-ready-containerized-mvp`: una vista Next.js, un endpoint FastAPI y un contenedor PostgreSQL — todo con Docker Compose. El dominio es un tablero de recepción de gimnasio, no un MVP genérico.

_These instructions are also available in [English](./README.md)._

---

## El reto

Configuras un **tablero de check-in** para un gimnasio pequeño del barrio. Recepción necesita una página en el navegador que confirme si la API de reservas está activa y si la base de datos responde — nada más. Sin membresías, pagos ni panel de administración.

### Nota de alcance

Frente al proyecto oficial del estudiante, este ejemplo mantiene el **mismo patrón de tres contenedores** pero acota la historia:

- **Una** página Next.js (sin rutas extra ni sistema de diseño).
- **Una** ruta en backend: `GET /status`.
- **Una** comprobación de base de datos (solo conexión; sin tablas).
- En clase puedes omitir el Dockerfile multi-stage del frontend y dejarlo como tarea; el estudiante debe cumplir la rúbrica completa del README en la raíz.

---

## Qué construir

### Contenedores (tres servicios)

| Servicio   | Rol                                                                                |
| ---------- | ---------------------------------------------------------------------------------- |
| `frontend` | Next.js — página única "Tablero del gimnasio activo" + fetch al estado del backend |
| `backend`  | FastAPI — `GET /status` devuelve JSON de salud                                     |
| `db`       | PostgreSQL — en ejecución; el backend hace ping con `SELECT 1`                     |

### Checklist frontend

- [ ] Crear `frontend/` con Next.js por defecto (`npx create-next-app@latest`).
- [ ] Una página muestra un título y el JSON parseado de `GET /status`.
- [ ] Leer la URL base de la API desde `NEXT_PUBLIC_API_URL` en `.env`.

### Checklist backend

- [ ] Crear `backend/main.py` con FastAPI y `GET /status`.
- [ ] Forma de respuesta (ejemplo):

```json
{
  "status": "ok",
  "service": "gym-check-in-api",
  "database": "connected"
}
```

- [ ] Conectar a Postgres con hostname **`db`** (no `localhost`).

### Checklist Docker Compose

- [ ] `docker-compose.yml` en la raíz con servicios `frontend`, `backend`, `db`.
- [ ] `depends_on`: `backend` → `db`, `frontend` → `backend`.
- [ ] Volumen nombrado en `db` para persistencia.
- [ ] `.env` y `.env.example` en la raíz; `.env` en `.gitignore`.

### Ejecutar juntos

- [ ] `docker compose up --build` levanta los tres servicios.
- [ ] Abrir `http://localhost:3000` y confirmar que el JSON de estado aparece en pantalla.
- [ ] Probar la URL de estado del backend directamente.

---

## Verificar juntos

- [ ] Los tres contenedores siguen activos tras reiniciar (`docker compose down && docker compose up`).
- [ ] El frontend falla de forma clara si la URL del backend es incorrecta (momento didáctico).
- [ ] Los logs del backend muestran ping exitoso a la BD, no "connection refused" a `localhost`.

---

## Preguntas para debatir

1. ¿Por qué el backend debe usar el nombre de servicio `db` y no `localhost` dentro de Compose?
2. ¿Qué falla si `NEXT_PUBLIC_API_URL` apunta a `http://backend:8000` desde el navegador?
3. ¿Qué añadirías después (healthchecks, migraciones, CI) antes de llamarlo listo para producción?
