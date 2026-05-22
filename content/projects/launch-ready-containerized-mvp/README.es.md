# Listo para lanzar: MVP Contenedorizado desde Cero

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/launch-ready-containerized-mvp/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Tienes una idea para un MVP y quieres empezar a construirlo bien desde el principio — no parcheando cosas después, sino estableciendo una base sólida y desplegable desde el primer día.

El objetivo de este proyecto no es construir un producto completo. Es configurar la infraestructura que hace posible construirlo: un entorno contenedorizado donde un frontend, un backend y una base de datos funcionen juntos a través de Docker Compose, de manera consistente, en cualquier máquina.

> **Lo que vas a entregar:**
> Un stack mínimo pero completamente operativo — una página simple en Next.js, un servicio en FastAPI con al menos un endpoint funcional, y una base de datos PostgreSQL conectada — todo orquestado con Docker Compose y ejecutable con un solo comando.

Piénsalo como construir la plataforma de lanzamiento, no el cohete. Una vez que esto esté en su lugar, cualquier funcionalidad que añadas tendrá un entorno fiable y reproducible donde ejecutarse.

### Qué significa "mínimo" aquí

Para mantener el foco en la infraestructura y no en el desarrollo de la aplicación, cada capa del stack debe ser lo más simple posible:

- **Frontend**: Una sola página en Next.js que muestre un título y haga una petición al backend
- **Backend**: Una aplicación FastAPI con al menos un endpoint (`GET /status` o similar) que devuelva una respuesta y confirme que la conexión con la base de datos está activa
- **Base de datos**: Una instancia de PostgreSQL a la que el backend pueda conectarse — sin tablas, sin datos, solo una conexión funcional

El punto es que las tres capas se comuniquen entre sí dentro de la red de Docker. Eso es lo que se entrega.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no tiene plantilla de inicio. Crea un nuevo repositorio en GitHub y configúralo con la siguiente estructura antes de escribir código:

```text
mi-mvp/
├── frontend/          # App Next.js
├── backend/           # App FastAPI
├── docker-compose.yml
├── .env
└── .env.example
```

Inicializa cada servicio dentro de su carpeta (`npx create-next-app` para el frontend, un `main.py` básico para el backend). Mantén ambos lo más cercanos a sus valores predeterminados — construirás sobre ellos más adelante.

> 📗 [Lee cómo iniciar un proyecto de programación](https://4geeks.com/lesson/how-to-start-a-project) si necesitas repasar la configuración del repositorio.

---

## 💻 Qué debes hacer

### Capa de aplicación mínima

- [ ] **Frontend**: Crea una app Next.js con una sola página que muestre un encabezado (por ejemplo, "MVP en marcha") y consulte el endpoint de estado del backend para confirmar que es accesible
- [ ] **Backend**: Crea una app FastAPI con al menos una ruta — `GET /status` — que devuelva una respuesta JSON (por ejemplo, `{"status": "ok"}`) y, opcionalmente, confirme la conexión con la base de datos
- [ ] **Base de datos**: No se requieren tablas ni datos — PostgreSQL solo necesita estar en ejecución y ser accesible desde el backend

### Dockerfile del backend

- [ ] Crea `backend/Dockerfile` usando una imagen base oficial de Python (`python:3.13-slim` recomendada)
- [ ] Define un directorio de trabajo, copia `requirements.txt`, instala dependencias, expone el puerto correcto y define un `CMD` para iniciar `uvicorn`
- [ ] Añade `backend/.dockerignore` excluyendo `__pycache__`, `.env` y carpetas de entornos virtuales

### Dockerfile del frontend

- [ ] Crea `frontend/Dockerfile` usando una construcción multi-stage (etapa de build + etapa de producción, `node:24-alpine` recomendado)
- [ ] La etapa de build instala dependencias y ejecuta `next build`; la etapa de producción copia solo el resultado compilado e inicia el servidor
- [ ] Expone el puerto `3000` y define el `CMD` para iniciar Next.js
- [ ] Añade `frontend/.dockerignore` excluyendo `node_modules`, `.next` y archivos `.env*`

### Docker Compose

- [ ] Crea `docker-compose.yml` en la raíz con tres servicios: `frontend`, `backend` y `db`
- [ ] Servicio `db`: usa la imagen oficial de `postgres`, define las credenciales mediante variables de entorno y monta un volumen nombrado para la persistencia de datos
- [ ] Servicio `backend`: construye desde `./backend`, declara `depends_on: db` y pasa las variables de conexión a la base de datos desde `.env`
- [ ] Servicio `frontend`: construye desde `./frontend`, declara `depends_on: backend` y mapea el puerto `3000`
- [ ] Los servicios deben comunicarse a través de la red interna de Docker — el backend se conecta a `db` por nombre de servicio, no por `localhost`

### Variables de entorno

- [ ] Crea un archivo `.env` en la raíz con todas las variables necesarias: credenciales de base de datos, URL de conexión para el backend y URL del backend para el frontend
- [ ] Crea un `.env.example` con los mismos nombres de variables pero sin valores
- [ ] Añade `.env` al `.gitignore`

⚠️ **IMPORTANTE:** Nunca subas el archivo `.env` a GitHub. Solo `.env.example` debe estar registrado en Git.

### Validación

- [ ] `docker compose up --build` inicia los tres servicios sin errores
- [ ] El frontend es accesible en `http://localhost:3000`
- [ ] El endpoint de estado del backend responde en su puerto mapeado
- [ ] El frontend obtiene y muestra correctamente los datos del backend
- [ ] El contenedor de la base de datos arranca y el backend se conecta sin errores

---

## ✅ Qué vamos a evaluar

- [ ] Existe un `Dockerfile` para el backend y el frontend, siguiendo buenas prácticas (imágenes base ligeras, `.dockerignore` presente, capas mínimas)
- [ ] El `Dockerfile` del frontend usa una construcción multi-stage
- [ ] `docker-compose.yml` define los tres servicios con configuración correcta
- [ ] La comunicación entre servicios usa la red interna de Docker (nombres de servicio, no `localhost`)
- [ ] La base de datos usa un volumen nombrado para la persistencia
- [ ] Todas las credenciales y URLs se gestionan mediante `.env`; `.env.example` está commiteado; `.env` está en `.gitignore`
- [ ] `docker compose up --build` levanta el stack completo sin pasos manuales
- [ ] Las tres capas son accesibles y se comunican correctamente

> Nota: Las funcionalidades y el diseño de la aplicación no se evalúan. El objetivo es un stack mínimo y funcional.

---

## 📦 Cómo entregar

Sube tu proyecto a GitHub y comparte la URL del repositorio siguiendo las instrucciones de entrega de tu instructor. Confirma que el repositorio es público y que el archivo `.env` no está commiteado — solo debe estar presente el `.env.example`.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
