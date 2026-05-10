# Plataforma de Recetas — Propuesta de Arquitectura de Backend (Ejemplo en Clase)

> **Nota para el instructor:** Este es un ejemplo simplificado en clase para el proyecto "Backend Architecture Proposal". Usa este escenario para practicar la escritura de un documento de arquitectura técnica antes de escribir ningún código — completable en 1–2 horas. El proyecto original aplica los mismos conceptos al monorepo propio de la empresa del alumno, acumulado a lo largo de varios hitos.

---

## Escenario

Acabas de unirte al equipo de backend de **Dishcraft**, una startup que está construyendo una plataforma online para compartir recetas. Los usuarios pueden publicar sus propias recetas, navegar por categorías, dejar valoraciones y guardar favoritas.

Antes de que nadie escriba una línea de código, el CTO te envió este mensaje:

> *"Necesito un documento de arquitectura primero. Dime cómo organizarías el backend, qué patrón usarías y por qué, y cómo se comunicarían el frontend y el backend. No empieces a programar — solo escribe el documento. Un archivo Markdown está bien."*

Tu entregable es `ARCHITECTURE_PROPOSAL.md` dentro de la carpeta `/docs` del proyecto.

---

## ¿Qué Hace un Buen Documento de Arquitectura?

Un documento de arquitectura es **razonamiento técnico documentado** — no una lista de tecnologías. Explica el *qué*, el *por qué* y anticipa consecuencias. Un buen documento permite que cualquier miembro del equipo entienda las decisiones sin tener que preguntar.

---

## Lo que Debes Hacer

Crea `docs/ARCHITECTURE_PROPOSAL.md` cubriendo las siguientes secciones:

### 1. Patrón Arquitectónico

- [ ] Elige un patrón: **arquitectura en capas (MVC)**, **serverless** u otra alternativa justificada.
- [ ] Escribe 2–3 frases explicando *por qué* este patrón encaja con las necesidades de Dishcraft — conecta tu razonamiento con la naturaleza del producto (CRUD de recetas, contenido generado por usuarios, valoraciones).
- [ ] Menciona una compensación: ¿qué hace este patrón más difícil?

### 2. Estructura de Carpetas y Módulos

Propón una estructura de carpetas para el proyecto FastAPI. Debe reflejar el patrón que elegiste y los dominios de negocio del producto.

Ejemplo para una aproximación en capas:

```
dishcraft-api/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── recipes/
│   │   ├── router.py
│   │   ├── service.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── users/
│   │   ├── router.py
│   │   ├── service.py
│   │   ├── models.py
│   │   └── schemas.py
│   └── ratings/
│       ├── router.py
│       └── service.py
├── tests/
└── requirements.txt
```

- [ ] Incluye al menos 3 carpetas de dominio (p. ej., `recipes/`, `users/`, `ratings/`).
- [ ] Para cada carpeta, escribe una frase describiendo su responsabilidad.

### 3. Organización de Routers y Endpoints

Lista las rutas principales de la API agrupadas por dominio. No se necesita código — descríbelas en una tabla:

| Dominio | Método | Ruta | Descripción |
|---------|--------|------|-------------|
| Recetas | GET | `/recipes` | Lista todas las recetas (con filtros) |
| Recetas | POST | `/recipes` | Crea una nueva receta |
| Recetas | GET | `/recipes/{id}` | Obtiene una receta por ID |
| Usuarios | POST | `/users/register` | Registra un nuevo usuario |
| Usuarios | POST | `/users/login` | Autentica y devuelve un token |
| Valoraciones | POST | `/recipes/{id}/ratings` | Envía una valoración para una receta |

- [ ] Añade al menos 2 rutas más que tengan sentido para este dominio.
- [ ] Indica qué rutas requieren autenticación.

### 4. Separación Frontend–Backend

Describe cómo convivirán el frontend Next.js y el backend FastAPI. Aborda:

- [ ] ¿Vivirán en el mismo repositorio (monorepo) o en repositorios separados? Justifica tu elección.
- [ ] ¿Cómo llamará el frontend a la API? (URL base, fetch vs. axios, variables de entorno)
- [ ] ¿Qué configuración de CORS se necesita y por qué?

### 5. Riesgos y Puntos de Atención

- [ ] Lista **al menos 2 riesgos** que el equipo debería conocer antes de empezar a programar. Ejemplos de riesgos útiles: *"Si todas las rutas van en un único `main.py`, el archivo será inmantenible a medida que crezca la API"* o *"Sin una convención de nombres compartida para los esquemas de respuesta, el equipo de frontend encontrará nombres de campos inesperados."*

---

## Criterios de Aceptación

| # | Criterio |
|---|----------|
| 1 | El patrón arquitectónico se justifica con argumentos específicos de Dishcraft — no con preferencias genéricas |
| 2 | La estructura de carpetas es coherente con el patrón elegido y separa los dominios claramente |
| 3 | Todos los routers están agrupados por dominio, no concentrados en un único archivo |
| 4 | El documento aborda la comunicación frontend–backend y el CORS |
| 5 | Se identifican al menos 2 riesgos concretos |

---

## Preguntas para Debatir

1. Un compañero eligió funciones serverless en lugar de una app FastAPI en capas. ¿Qué dominios de este proyecto podrían beneficiarse del enfoque serverless? ¿Cuáles serían más difíciles de implementar así?
2. ¿Por qué importa mantener `router.py`, `service.py` y `models.py` separados dentro de cada carpeta de dominio? ¿Qué ocurre cuando pones todo en un único archivo?
3. ¿Qué añadirías al documento de arquitectura si el producto necesitara soportar notificaciones en tiempo real (p. ej., "tu receta recibió una nueva valoración")?
