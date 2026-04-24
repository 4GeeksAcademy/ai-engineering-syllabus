# Agent Loop Básico de Inventario con IA

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/exercise-ai-inventory-agent/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

Una pequeña empresa familiar — una tienda de suministros para cafeterías con dos locales físicos — está perdiendo dinero. No por las ventas, sino porque nadie en el equipo puede responder con seguridad a una pregunta simple en un momento dado: _"¿Tenemos suficiente de este producto para cubrir la semana?"_

El stock se lleva en una hoja de cálculo compartida que nadie actualiza de forma consistente. La dueña, Carla, se ha puesto en contacto contigo después de ver una demo de un asistente de IA en una feria del sector. No quiere un panel de control que tenga que mantener a mano — quiere poder hablar con un sistema y obtener respuestas. También quiere que el sistema actúe: registrar entregas, apuntar ventas y avisarle cuando algo esté por agotarse, todo mediante lenguaje natural.

Tu trabajo es construir ese sistema. Tiene dos partes que deben funcionar juntas:

**1. Una API REST** construida con FastAPI que gestiona los datos del inventario. Expone endpoints para listar productos, registrar nuevos, actualizar cantidades y obtener alertas de stock bajo. Los productos se almacenan en un fichero CSV para que los datos persistan entre sesiones.

**2. Un agente de IA** escrito en Python que se conecta a un LLM y utiliza tu API como conjunto de herramientas. El agente funciona en un bucle: recibe un mensaje de Carla, razona sobre qué acción tomar, llama al endpoint de la API correspondiente como una tool, y responde con el resultado. Cada paso de ese bucle queda registrado en un fichero `conversation_log.csv`.

### Conocimiento complementario: el bucle del agente y el uso de tools

A estas alturas del curso ya sabes construir una API con FastAPI y llamar a una API externa desde Python. Un agente de IA añade una capa sobre eso: en lugar de que _tú_ decidas cuándo llamar a qué endpoint, lo decide el **LLM**. Describes tus endpoints como herramientas (tools) — cada una con un nombre, una descripción y sus parámetros esperados — y el modelo selecciona la adecuada según el mensaje del usuario.

El bucle sigue este ciclo:

```
Observar (leer el input del usuario)
    → Pensar (enviar al LLM con las definiciones de tools)
        → Actuar (llamar a la tool que el LLM seleccionó)
            → Actualizar (inyectar el resultado de vuelta en el contexto del LLM)
                → Repetir hasta que el LLM dé una respuesta final
```

Tu agente debe implementar este ciclo en un único fichero Python (`agent.py`). Debe mantener el historial completo de mensajes en memoria durante la sesión para que el LLM pueda razonar sobre intercambios anteriores.

### Registro de conversación

Cada evento del bucle debe añadirse al fichero `conversation_log.csv` con estos cuatro campos:

| Campo       | Descripción                                    |
| ----------- | ---------------------------------------------- |
| `actor`     | `user`, `agent` o `tool`                       |
| `message`   | El contenido del texto o resultado del evento  |
| `tool_call` | Nombre de la tool llamada (vacío si no aplica) |
| `timestamp` | Fecha y hora del evento en formato ISO 8601    |

Este fichero es de solo adición (_append-only_). Cada sesión añade filas — no sobreescribe las anteriores.

> Carla ha enviado los siguientes requisitos por correo electrónico:
>
> _"Necesito poder decirle cosas al sistema como 'acaban de llegar 30 unidades de leche de avena' o 'vendimos 12 bolsas de arábica hoy'. Que me entienda y actualice el stock. También quiero poder preguntarle '¿qué productos están por agotarse?' y recibir una respuesta directa. Que se sienta como una conversación, no como rellenar un formulario."_

Tienes libertad creativa total sobre el catálogo de productos y la estructura de datos, siempre que soporte nombre, cantidad y unidad de medida (unidades, kg, litros, etc.).

Construye algo que Carla pueda usar el lunes por la mañana.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto utiliza una plantilla de inicio en Python. Haz un fork y clónala:

```
https://github.com/4GeeksAcademy/python-hello
```

Puedes trabajar en **GitHub Codespaces** (abre el repositorio y haz clic en _Code → Codespaces → Create_) o clonándolo localmente. Una vez clonado, crea tu propio repositorio en GitHub y actualiza la URL del remote para que tu progreso quede registrado ahí.

Instrucciones completas: [cómo iniciar un proyecto de programación](https://4geeks.com/lesson/how-to-start-a-project)

**Arrancar el sistema:**

Necesitas dos terminales abiertos al mismo tiempo — uno para la API y otro para el agente.

```bash
# Terminal 1 — arrancar la API
uvicorn api.app:app --reload

# Terminal 2 — arrancar el agente
python agent.py
```

**Detener el sistema:**

Pulsa `Ctrl + C` en cada terminal para detener el proceso correspondiente. Detén primero el agente y luego la API. El fichero `conversation_log.csv` se escribe de forma incremental, por lo que no se pierde ningún dato al detener la ejecución a mitad de sesión.

**Relanzar el agente:**

Ejecuta `python agent.py` de nuevo en el Terminal 2. No es necesario reiniciar la API. El agente iniciará una nueva sesión, pero todo el historial de conversaciones anteriores permanecerá intacto en `conversation_log.csv` — las filas nuevas siempre se añaden, nunca se sobreescriben.

Con el entorno listo, instala las dependencias:

```bash
pip install fastapi uvicorn openai python-dotenv
```

Crea un fichero `.env` en la raíz con tu clave de API del LLM:

```
GROQ_API_KEY=tu_clave_aqui
```

⚠️ **IMPORTANTE:** No subas nunca tu fichero `.env` al repositorio. Añádelo al `.gitignore` antes de tu primer commit.

---

## 💻 Qué debes hacer

### API (`api/app.py`)

- [ ] Crear una aplicación FastAPI que almacene los datos de inventario en un fichero `products.csv`
- [ ] `GET /inventory` — Devuelve la lista completa de productos
- [ ] `POST /inventory` — Añade un nuevo producto (`name`, `quantity`, `unit`)
- [ ] `PATCH /inventory/{product_id}` — Actualiza el stock de un producto existente (acepta un valor `delta`: positivo para entradas de stock, negativo para salidas)
- [ ] `GET /inventory/alerts` — Devuelve todos los productos cuya cantidad está por debajo de un umbral configurable (por defecto: 10 unidades)
- [ ] Todos los endpoints deben devolver códigos de estado HTTP apropiados y mensajes descriptivos en caso de error

### Agente (`agent.py`)

- [ ] Definir los endpoints de tu API como **tools** para el LLM — cada tool debe tener un `name`, una `description` y `parameters` tipados claramente
- [ ] Implementar el **bucle del agente** completo: Observar → Pensar → Actuar → Actualizar → Repetir
- [ ] El agente debe mantener el historial de conversación en memoria durante la sesión
- [ ] Cuando el LLM seleccione una tool, el agente debe llamar al endpoint de la API correspondiente e inyectar el resultado de vuelta en el contexto
- [ ] El bucle debe terminar de forma limpia cuando el LLM devuelva una respuesta final sin llamadas a tools pendientes
- [ ] El agente debe exponer una interfaz CLI sencilla: leer el input del usuario desde el terminal e imprimir la respuesta del agente

### Registro de conversación

- [ ] Cada evento (mensaje del usuario, respuesta del agente, llamada a tool, resultado de tool) debe añadirse al fichero `conversation_log.csv`
- [ ] El CSV debe incluir los cuatro campos requeridos: `actor`, `message`, `tool_call`, `timestamp`
- [ ] El fichero debe persistir entre sesiones (solo adición, nunca sobreescribir)

### General

- [ ] La API debe estar en ejecución antes de iniciar el agente. Documenta cómo arrancar ambos procesos en el README
- [ ] ⚠️ **IMPORTANTE:** No uses ningún framework de agentes (LangChain, LlamaIndex, AutoGen, etc.). El bucle del agente debe implementarse manualmente en Python puro

---

## ✅ Qué vamos a evaluar

- [ ] La FastAPI expone los cuatro endpoints requeridos y devuelve respuestas correctas
- [ ] Los productos persisten en `products.csv` y sobreviven un reinicio del servidor
- [ ] El bucle del agente implementa correctamente el ciclo Observar → Pensar → Actuar → Actualizar → Repetir
- [ ] Las tools están definidas con nombres, descripciones y parámetros tipados que el LLM puede utilizar de forma fiable
- [ ] El agente llama al endpoint de la API correcto cuando el LLM selecciona una tool
- [ ] El resultado del LLM se inyecta de vuelta en el historial de conversación antes de la siguiente iteración
- [ ] `conversation_log.csv` se crea y se popula con los cuatro campos en cada evento
- [ ] El registro es de solo adición en múltiples sesiones
- [ ] El agente gestiona al menos una interacción de varios pasos (por ejemplo, añadir un producto y preguntar inmediatamente por las alertas)
- [ ] No se usa ningún framework de agentes — el bucle está codificado a mano en Python

> Nota: El diseño de interfaz y la presentación visual no se evalúan. Una interfaz de terminal es suficiente.

---

## 📦 Cómo entregar

Sube tu repositorio a GitHub y comparte el enlace siguiendo las instrucciones de tu instructor. Asegúrate de incluir tanto `api/app.py` como `agent.py`, junto con una nota breve en tu README sobre cómo arrancar ambos procesos.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
