# Voice Command API — Habla con tu Lista de Tareas

<!-- hide -->

Por [@4GeeksAcademy](https://github.com/4GeeksAcademy) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) en [4Geeks Academy](https://4geeks.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en inglés](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/es/lesson/how-to-start-a-coding-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Una startup de productividad ha construido una interfaz de voz que permite a sus usuarios gestionar una lista de tareas únicamente hablando. El frontend ya está listo — funciona en el navegador, captura la voz del usuario a través del micrófono y la transcribe a texto usando la Web Speech API. Tu trabajo es construir el backend que hace que esa interfaz funcione de verdad.

El frontend envía cada transcripción a un único endpoint de entrada: `POST /instruction`. Desde ahí, tu API debe identificar qué pidió el usuario, redirigir la petición al endpoint interno correcto y devolver una respuesta que la interfaz pueda mostrar.

El tech lead del equipo te dejó esta nota antes de irse de vacaciones:

> #### Especificaciones del backend — Voice Command API
>
> **Punto de entrada**
>
> - `POST /instruction` — recibe una transcripción en texto plano y llama a la API de Groq para extraer la intención y los parámetros. Debe devolver un JSON que identifique qué endpoint llamar y con qué argumentos. El frontend usará esta respuesta para hacer la petición de seguimiento.
>
> **Endpoints de tareas (almacenamiento en memoria — sin base de datos)**
>
> - `GET /tasks` — devuelve la lista completa de tareas
> - `POST /tasks` — crea una nueva tarea (requiere `title`, campo opcional `done`, por defecto `false`)
> - `PUT /tasks/<int:task_id>` — reemplaza una tarea completa
> - `PATCH /tasks/<int:task_id>` — marca una tarea como completada o actualiza el título
> - `DELETE /tasks/<int:task_id>` — elimina una tarea por ID
>
> **Almacenamiento**
> Usa una lista a nivel de módulo como almacén de datos. Cada tarea es un diccionario con `id`, `title` y `done`. Sin base de datos, sin sistema de archivos.
>
> **Integración con Groq**
> Usa la API de Groq (modelo: `llama3-8b-8192` o similar) desde tu endpoint `/instruction`. El system prompt debe instruir al LLM para que responda **únicamente** con un objeto JSON en este formato exacto:
>
> ```json
> {
>   "endpoint": "/tasks",
>   "method": "POST",
>   "params": { "title": "Comprar leche" }
> }
> ```
>
> El LLM nunca debe devolver texto libre — solo ese JSON. Tu ingeniería de prompt es lo que hace que esto funcione.

La PM de la startup quiere ver el flujo completo de voz a acción funcionando de extremo a extremo: el usuario dice "añade comprar leche a mi lista" y la tarea aparece. Ese es tu objetivo.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto incluye una plantilla de frontend lista para usar. Haz fork del repositorio y ábrelo en tu entorno preferido:

```
https://github.com/4GeeksAcademy/voice-command-api
```

**Opción A — GitHub Codespaces (recomendado):**

1. Abre el repositorio y haz clic en **Code → Codespaces → Create codespace on main**
2. Espera a que el entorno cargue

**Opción B — Clonar en local:**

```bash
git clone https://github.com/4GeeksAcademy/voice-command-api
cd voice-command-api
```

El repositorio contiene:

- `/frontend` — la interfaz de voz ya construida (no la modifiques)
- `/src` — aquí va tu backend de FastAPI

Crea tu propio repositorio en GitHub, sube tu código y actualiza la URL remota:

```bash
git remote set-url origin https://github.com/TU_USUARIO/TU_REPO
```

Para más información sobre cómo iniciar: [cómo iniciar un proyecto de programación](https://4geeks.com/es/lesson/how-to-start-a-coding-project).

---

## 💻 Qué debes hacer

### Configuración

- [ ] Crea un entorno virtual e instala FastAPI, Uvicorn y el SDK de Python de Groq
- [ ] Guarda tu API key de Groq en un archivo `.env` — nunca la subas al repositorio
- [ ] Configura CORS para que el frontend pueda comunicarse con tu API

### Almacenamiento en memoria

- [ ] Declara una lista a nivel de módulo llamada `tasks` para usarla como almacén de datos
- [ ] Cada tarea debe tener `id` (entero), `title` (cadena de texto) y `done` (booleano, por defecto `false`)

### Endpoints de tareas

- [ ] `GET /tasks` — devuelve todas las tareas como un array JSON
- [ ] `POST /tasks` — crea una tarea a partir del cuerpo de la petición y la añade a la lista; devuelve la tarea creada con su ID asignado
- [ ] `PUT /tasks/<task_id>` — reemplaza el objeto tarea completo para el ID indicado
- [ ] `PATCH /tasks/<task_id>` — actualiza parcialmente una tarea (título y/o estado `done`)
- [ ] `DELETE /tasks/<task_id>` — elimina la tarea con el ID indicado; devuelve un mensaje de confirmación

### Endpoint de instrucción

- [ ] `POST /instruction` — recibe un cuerpo JSON con un campo `transcription` (texto plano)
- [ ] Llama a la API de Groq con un system prompt adecuado que fuerce al LLM a responder únicamente con un objeto JSON estructurado que indique `endpoint`, `method` y `params`
- [ ] Devuelve ese JSON directamente al frontend

### Conexión extremo a extremo

- [ ] Usando la respuesta de `/instruction`, el frontend llama automáticamente al endpoint de tareas correcto — verifica que esto funcione al menos para: crear, listar, actualizar y eliminar tareas hablando en voz alta

⚠️ **IMPORTANTE:** No uses base de datos. Todos los datos deben vivir en una lista de Python en memoria. La lista se reinicia cada vez que el servidor se reinicia — ese es el comportamiento esperado para este proyecto.

⚠️ **IMPORTANTE:** El endpoint `/instruction` no debe contener lógica de detección de intención codificada manualmente (sin `if "añade" in text`). Todas las decisiones de enrutamiento deben provenir de la respuesta del LLM.

---

## ✅ Qué vamos a evaluar

- [ ] Los cinco endpoints de tareas (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) están implementados y devuelven los códigos de estado HTTP apropiados
- [ ] Cada endpoint devuelve una respuesta JSON correctamente serializada
- [ ] El endpoint `POST /instruction` llama a la API de Groq y devuelve el JSON de enrutamiento estructurado
- [ ] El system prompt está bien construido: el LLM devuelve consistentemente JSON válido en el formato requerido para distintas entradas de voz
- [ ] CORS está configurado para que el frontend incluido pueda comunicarse con la API sin errores
- [ ] El archivo `.env` está en el `.gitignore` y la API key nunca está expuesta en el código
- [ ] La lista en memoria se gestiona correctamente: los IDs son únicos y los elementos se añaden, actualizan y eliminan correctamente

> **Nota:** El frontend se proporciona y no será evaluado. No se espera que lo modifiques.

---

## 📦 Cómo entregar

Sube tu repositorio a GitHub y comparte el enlace siguiendo las instrucciones de entrega de tu instructor. Asegúrate de que el repositorio sea público y de que el `README.md` esté en la raíz.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeks.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeks.com/es/comparar-programas) de [Ingeniería de IA](https://4geeks.com/es/programas-de-carrera/ingenieria-ia) y [Agentes y Automatizaciones con IA](https://4geeks.com/es/programas-de-carrera/agentes-y-automatizaciones-con-inteligencia-artificial).
