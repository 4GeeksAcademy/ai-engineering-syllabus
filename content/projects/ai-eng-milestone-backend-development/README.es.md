# Hito 5 — Backend: Gestión de Inventario con ORM y Doble Base de Datos

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros colaboradores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are also available in [English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/05-backend-development)** antes de escribir ningún código — define las entidades específicas, los nombres de campos y las restricciones de negocio para tu implementación.

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Ya has construido la API y la capa de autenticación. Ahora el equipo de operaciones ha enviado una **RFP** a la unidad tecnológica: la empresa necesita un sistema centralizado de gestión de inventario antes de la próxima revisión operativa.

Tu tech lead ha convertido esa RFP en una decisión arquitectónica que condiciona todo lo que construirás aquí: **la autenticación permanece en TinyDB** (búsquedas rápidas, locales y basadas en documentos), y **todos los datos de negocio — productos, órdenes de entrada y órdenes de salida — se mueven a Supabase** (una base de datos PostgreSQL alojada en la nube). Tu aplicación FastAPI mantendrá dos conexiones de base de datos simultáneas y deberá usarlas de forma deliberada: cada petición llega al almacén correcto.

Esto no es solo un ejercicio de persistencia. El equipo de operaciones incluyó una restricción no negociable en el **brief**:

> _"Los niveles de stock no se pueden modificar directamente. La única forma de cambiar el inventario es registrando una orden — ya sea una orden de entrada que añade stock, o una orden de salida que lo reduce. Cada orden debe ser trazable al usuario que la creó."_

Tu trabajo es hacer cumplir esa regla a nivel de API y de modelos, usando un ORM para traducir clases Python en tablas relacionales en Supabase. Todos los endpoints de inventario deben agruparse bajo el prefijo de router `/inventory`.

### ¿Qué es un ORM y por qué importa aquí?

Un ORM (Object-Relational Mapper) es una capa de traducción: una clase Python se convierte en una tabla, una instancia en una fila y un atributo en una columna. No reemplaza conocer SQL — entender lo que el ORM genera por debajo es lo que permite usarlo correctamente y depurar errores cuando algo falla. En este hito usarás **SQLModel**, que combina el motor ORM de SQLAlchemy con el sistema de tipos de Pydantic. No uses SQLAlchemy directamente.

Antes de escribir cualquier consulta, debes conocer el **problema N+1**. Si cargas una lista de órdenes y después accedes a los datos del producto de cada una dentro de un bucle, generas una consulta adicional por elemento — degradando el rendimiento de forma silenciosa. Estructura tus consultas para cargar los datos relacionados desde el inicio, no en el momento del acceso.

### Brief de tu tech lead

> > **De:** Tech Lead
> > **Asunto:** Hito 5 — arquitectura de doble base de datos + ORM de inventario
> >
> > El **PRD** está listo. Esto es lo que debe hacer el sistema:
> >
> > 1. La aplicación FastAPI conecta a **dos bases de datos simultáneamente**: TinyDB (existente, para usuarios y autenticación) y Supabase (nueva, para inventario y órdenes).
> > 2. Los productos y el stock viven en Supabase. El stock **no debe ser una columna editable directamente** — siempre se deriva del historial de órdenes.
> > 3. Las **órdenes de entrada** incrementan el stock; las **órdenes de salida** lo reducen. Ambas se almacenan en Supabase y referencian el UUID del usuario de TinyDB — ninguna tabla de usuarios se replica en Supabase.
> > 4. Los modelos ORM usan **SQLModel**. Los schemas Pydantic para request y response están en un archivo separado de los modelos ORM — nunca devuelvas un objeto ORM directamente desde un endpoint.
> > 5. Todas las rutas de inventario deben registrarse bajo el prefijo `/inventory` usando un `APIRouter` dedicado.
> > 6. Revisa tu CONTEXT.md — los nombres de entidades, las restricciones de campos y las reglas de negocio son específicas de tu empresa.
> >
> > **Criterios de aceptación**: todos los endpoints funcionales bajo `/inventory`, relaciones FK aplicadas a nivel de base de datos, sin mutación directa de stock, ambas conexiones activas y usadas correctamente.

---

## 🌱 Cómo Empezar el Proyecto

Este hito extiende el servicio FastAPI ya presente en tu monorepo. No crearás un nuevo servicio — añadirás la capa de inventario sobre el existente.

1. Abre tu repositorio existente (forkeado desde `https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo`).
2. Navega a `services/` — aquí vive tu aplicación FastAPI.
3. Instala las nuevas dependencias:
   ```bash
   pip install sqlmodel psycopg2-binary
   ```
4. Añade tu cadena de conexión de Supabase a `.env`. Tu configuración de TinyDB ya está ahí — no la modifiques.
5. Lee tu **CONTEXT-company.md** antes de definir cualquier modelo — los nombres de entidades y las restricciones de campos están especificados allí.

### Conexión con Supabase

En el panel de Supabase (**Connect → Direct**), elige **Transaction pooler** como método de conexión y **URI** como tipo — luego copia esa cadena en `DATABASE_URL`.

![Configuración de conexión en Supabase: método Transaction pooler y tipo URI](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-backend-development/.learn/supabase-transaction-pooler-uri.png)

![Cadena de conexión en Supabase: detalles del URI con Transaction pooler](https://raw.githubusercontent.com/4GeeksAcademy/ai-engineering-syllabus/main/content/projects/ai-eng-milestone-backend-development/.learn/supabase-transaction-pooler-connection-string.png)

---

## 💻 Qué Debes Hacer

### Configuración de bases de datos

- [ ] Añade la cadena de conexión PostgreSQL de Supabase a `.env`. Nunca escribas credenciales directamente en el código.
- [ ] En `database.py` (o equivalente), inicializa **ambas** conexiones de base de datos: el cliente TinyDB existente y el nuevo motor SQLModel apuntando a Supabase.
- [ ] Crea una dependencia `get_db` que produzca una sesión SQLModel por petición mediante `Depends()`. No uses variables de sesión globales.

### Modelos ORM — `models.py`

- [ ] Define un modelo `Product` con `SQLModel, table=True`, con al menos: `id`, `name`, `sku` y cualquier campo específico de tu empresa indicado en CONTEXT.md.
- [ ] Define un modelo `InboundOrder` con: `id`, `product_id` (FK → Product), `quantity`, `created_at` y `user_uuid` (cadena de texto — referencia al usuario de TinyDB; sin FK, sin replicación de tabla de usuarios).
- [ ] Define un modelo `OutboundOrder` con: `id`, `product_id` (FK → Product), `quantity`, `created_at` y `user_uuid`.
- [ ] Llama a `SQLModel.metadata.create_all(engine)` al inicio de la aplicación para inicializar el esquema en Supabase.

  > ⚠️ `create_all()` es aceptable en contextos de desarrollo y aprendizaje. En un sistema en producción, los cambios de esquema se gestionan siempre mediante archivos de migración (p. ej., Alembic) que mantienen un historial versionado de cada cambio. Nunca uses `create_all()` contra una base de datos compartida o de producción.

### Schemas Pydantic — `schemas.py`

- [ ] Define schemas de request y response para Product, InboundOrder y OutboundOrder como modelos Pydantic independientes — separados de los modelos ORM.
- [ ] El schema de respuesta de Product debe incluir un campo `current_stock` (calculado, no almacenado).
- [ ] Los modelos ORM y los schemas Pydantic deben estar en **archivos separados**. Son clases distintas, aunque algunos campos coincidan.

### Router de inventario — `routers/inventory.py`

- [ ] Crea un `APIRouter` dedicado con `prefix="/inventory"` y regístralo en la aplicación FastAPI principal.
- [ ] Implementa los siguientes endpoints dentro de este router:

| Método | Ruta                         | Descripción                                                  |
| ------ | ---------------------------- | ------------------------------------------------------------ |
| `GET`  | `/inventory/products`        | Lista todos los productos con `current_stock` calculado      |
| `POST` | `/inventory/products`        | Crea un producto (requiere autenticación)                    |
| `GET`  | `/inventory/products/{id}`   | Obtiene un producto con su stock actual                      |
| `POST` | `/inventory/orders/inbound`  | Registra una orden de entrada (requiere autenticación)       |
| `POST` | `/inventory/orders/outbound` | Registra una orden de salida (requiere autenticación)        |
| `GET`  | `/inventory/orders`          | Lista todas las órdenes con datos del producto y `user_uuid` |

### Reglas de negocio

- [ ] `current_stock` se calcula siempre como `SUMA(cantidades de entradas) − SUMA(cantidades de salidas)` para cada producto. Nunca se almacena como una columna que pueda modificarse directamente.
- [ ] Un producto comienza con stock cero al crearse y solo puede acumular stock a través de órdenes de entrada.
- [ ] Cada endpoint de creación de órdenes requiere autenticación. El UUID del usuario autenticado (de TinyDB) debe almacenarse en el campo `user_uuid` de la orden.
- [ ] Una orden de salida que resultaría en stock negativo debe rechazarse **antes de persistir la orden**, devolviendo `HTTP 400` con un mensaje de error descriptivo.

⚠️ **IMPORTANTE:** Los nombres de entidades, nombres de campos y valores específicos del dominio en tu implementación deben coincidir con lo especificado en tu CONTEXT.md. Una implementación genérica que ignore el contexto no será aceptada.

---

## ✅ Qué Vamos a Evaluar

- [ ] Dos conexiones de base de datos están presentes y se usan correctamente: TinyDB para autenticación y consultas de usuario; Supabase (SQLModel) para todas las entidades de inventario.
- [ ] Todos los endpoints de inventario están agrupados bajo `/inventory` mediante un `APIRouter` dedicado.
- [ ] Los modelos ORM SQLModel declaran correctamente las relaciones FK: `InboundOrder.product_id` y `OutboundOrder.product_id` referencian la tabla `Product`.
- [ ] `current_stock` se calcula a partir de órdenes — ningún endpoint permite modificar directamente un campo de stock en el Producto.
- [ ] Una orden de salida que supera el stock disponible se rechaza con `HTTP 400` antes de que ocurra cualquier escritura.
- [ ] Cada orden almacena el `user_uuid` del creador autenticado (obtenido de TinyDB).
- [ ] Los modelos ORM (`models.py`) y los schemas Pydantic (`schemas.py`) están en archivos separados y son estructuralmente distintos — ningún endpoint devuelve un objeto SQLModel directamente.
- [ ] La sesión SQLModel se inyecta por petición mediante `Depends()` — no existe ninguna sesión global en el código.
- [ ] Todos los parámetros de conexión están en `.env`; `.env` aparece en `.gitignore`.
- [ ] Los nombres de entidades y campos coinciden con la especificación del CONTEXT.md del estudiante.

---

## 📦 Cómo Entregar

1. Confirma y sube todos los cambios a tu fork.
2. Verifica que `.env` está en `.gitignore` — nunca subas credenciales.
3. Envía la URL de tu fork a través de la plataforma del estudiante.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
