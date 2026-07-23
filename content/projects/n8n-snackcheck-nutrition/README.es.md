# ¿Es Saludable Este Snack? — Una Automatización que Verifica Nutrición

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo), [@WaficMikati](https://github.com/WaficMikati) y [otros colaboradores](https://github.com/4GeeksAcademy) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

---

## 🎯 Tu reto

Este es tu **proyecto final**: una sola automatización que reúne todo lo que construiste a lo largo de este microsyllabus. Sin nodos nuevos, sin trucos nuevos — solo tú, demostrando que puedes tomar una idea de producto real y convertirla en una automatización que funciona y está bien documentada, por tu cuenta.

Esta es la situación.

Un fundador está creando una pequeña app de consumo llamada **SnackCheck**. La idea es simple: una persona apunta el teléfono a un alimento empaquetado, la app lee el código de barras y, un momento después, le dice —en lenguaje claro y amigable— si ese producto es una buena elección para el día a día o algo para dejar como un gusto ocasional. El fundador no es técnico. Sabe exactamente cómo quiere que se sienta la experiencia, pero no tiene idea de cómo construirla, y te contrató a ti para hacer el motor que hay detrás.

Te envió un brief informal por correo:

> Hola, gracias otra vez por tomar esto. Te cuento lo que imagino.
>
> La app le envía el **código de barras** de un producto a tu automatización, y tu automatización devuelve un **veredicto** corto que la persona pueda leer. Algo humano, como un amigo que sabe del tema en el supermercado — alentador cuando el producto está bien, y honesto con delicadeza cuando de verdad no lo está.
>
> No quiero que inventemos los datos de nutrición nosotros mismos. Escuché que existe una base de datos abierta y gratuita (**Open Food Facts**) que ya tiene esto para millones de productos, incluyendo esa letra del "Nutri-Score". Por favor usa datos reales de ahí.
>
> Hay algunas cosas que me importan mucho:
>
> - Si alguien llega a la automatización **sin código de barras**, debería **explicarse a sí misma** con amabilidad — qué hace y cómo usarla. No quiero un error en blanco que asuste.
> - Si el código de barras **falta o no es un número**, o si el producto **no está en la base de datos**, la respuesta debe ser un mensaje claro y útil — nunca una caída.
> - El veredicto final que lee la persona debe ser **fácil de leer**: un titular, los números clave con un marcador rojo/verde, y luego el párrafo amigable.
>
> Adjunté mis reglas de "saludable vs no saludable" en la página siguiente. ¡Con muchas ganas de verlo funcionar!

Las reglas que adjuntó el fundador se convierten en tu especificación. Léelas con atención — parte de lo que necesitas está escrito aquí, no en una lista:

> #### Reglas de clasificación de SnackCheck
>
> Observa tres nutrientes, medidos **por 100 g**, y etiqueta cada uno con una regla de semáforo:
>
> - **Azúcar** — `bajo` menos de 5 g · `medio` entre 5 y 22.5 g · `alto` más de 22.5 g
> - **Sal** — `alto` más de 1.5 g
> - **Grasa** — `alto` más de 17.5 g
>
> Luego calcula **dos lecturas independientes** del producto, y que el veredicto sea la **peor** de las dos:
>
> 1. **Conteo de semáforo** — según **cuántos** nutrientes resultaron `alto`:
>    - `0` nutrientes altos → **saludable**
>    - exactamente `1` nutriente alto → **moderado**
>    - `2` o `3` nutrientes altos → **no saludable**
> 2. **Nutri-Score** (`nutriscore_grade`, tal cual viene de la API):
>    - `a` o `b` → **saludable**
>    - `c` → **moderado**
>    - `d` o `e` → **no saludable**
>
> El **nivel de veredicto general es el peor de los dos** — un producto solo cuenta como `saludable` si _ambas_ lecturas coinciden en que está bien. Esto importa: una bebida azucarada puede parecer "segura" solo con el conteo de semáforo (sus números por 100 ml no llegan a `alto`), pero su Nutri-Score ya cuenta la historia real, y ese debe ganar.
>
> Si `nutriscore_grade` es **`unknown` o falta**, usa **solo el conteo de semáforo**. Y si los **campos de nutrientes tampoco existen o vienen vacíos**, **no clasifiques**: responde que el producto **no tiene datos suficientes**. Un producto sin datos nunca debe salir como "saludable" solo porque los campos están en blanco.
>
> Además, produce una **puntuación de preocupación**: simplemente la cantidad de nutrientes `alto` (un número de 0 a 3). Es una señal rápida de un vistazo que quizás mostremos más adelante — no forma parte de cómo se decide el nivel de veredicto en sí.
>
> El **tono** del veredicto escrito **debe coincidir con el nivel**: alentador para `saludable` y `moderado`, cauteloso con delicadeza para `no saludable`.

Ya construiste cada pieza de esto antes — un webhook que responde, una llamada a una API, lógica de ramificación, un pequeño cálculo, un paso de IA, una respuesta con formato. El reto final es hacerlo **de principio a fin, por ti mismo, con orden**, y entregarlo como lo haría un profesional.

### 📚 Un poco de contexto que vas a necesitar

Dos piezas de contexto que viven fuera de la automatización en sí:

**El Nutri-Score y los semáforos.** El Nutri-Score es una sola letra (`a` = mejor a `e` = peor) que resume qué tan saludable es un producto; viene directo de la base de datos. La idea del **semáforo** (verde/ámbar/rojo por nutriente) es una forma muy conocida, de salud pública, de señalar azúcar, sal y grasa de un vistazo. Tu automatización reproduce ese juicio de semáforo usando los umbrales del fundador — no estás inventando ciencia de la nutrición, solo aplicando una hoja de reglas.

**La fuente de datos (Open Food Facts).** Es gratuita, abierta y **no necesita clave ni registro**. Consultas un producto a la vez por su código de barras:

```
GET https://world.openfoodfacts.org/api/v2/product/{barcode}.json?fields=product_name,brands,nutriscore_grade,nutriments
```

- Siempre devuelve **un único objeto de producto plano**. Lee los campos que necesitas por su clave: `product_name`, `brands`, `nutriscore_grade`, y dentro de `nutriments` → `sugars_100g`, `salt_100g`, `fat_100g`, y `energy-kcal_100g`.
- ⚠️ El campo de energía tiene un guion en su nombre, así que léelo con **notación de corchetes**: `{{ $json.nutriments['energy-kcal_100g'] }}`.
- La API te dice si el producto se encontró a través de **dos señales**: el estado HTTP y el cuerpo de la respuesta. Un producto encontrado responde `200` con `status: 1`. Un producto **no encontrado** responde `404`, con un cuerpo como `{"code":"...", "status":0, "status_verbose":"product not found"}`. ⚠️ Como es un `404`, tu nodo **HTTP Request** lo tratará por defecto como una llamada fallida — configúralo para continuar ante el error (o para ramificar según la respuesta), así puedes leer ese cuerpo y dirigirlo a tu respuesta de "no encontrado" en lugar de que el flujo se caiga.
- Códigos de prueba: **Nutella `3017620422003`** (Nutri-Score `e`) y **Coca-Cola `5449000000996`**. Busca tú mismo un producto con **Nutri-Score `a`**, para poder demostrar que la ruta "alentadora" también funciona.

---

## 🌱 Cómo iniciar el proyecto

Aquí no hay repositorio que clonar — esta es una construcción **no-code**. Trabajas por completo dentro de **n8n**, igual que lo hiciste durante todo el curso.

1. Abre tu espacio de trabajo de n8n y **crea un flujo nuevo y vacío**.
2. **Diagrama antes de construir.** Abre Excalidraw y bosqueja todo el flujo primero — el disparador, las decisiones, las salidas de error, el paso de IA y la respuesta final. Construir a partir de un diagrama es el hábito profesional que practicaste en el curso del proyecto final; no te lo saltes.
3. La **única credencial** que necesita este proyecto es tu **clave de Groq** para el paso de IA — y ya la creaste en el curso de integración de IA. Todo lo demás (Open Food Facts) es sin clave.
4. Construye capa por capa, probando cada parte antes de seguir, tal como aprendiste.

---

## 💻 Qué debes hacer

Construye un único flujo de n8n que reciba un código de barras y devuelva un veredicto de salud, siguiendo el brief y las reglas del fundador que están arriba.

**Diseña primero**

- [ ] Produce un **diagrama del flujo** en Excalidraw antes de construir: formas estándar, rombos de decisión, rutas de error claramente dibujadas, una sola dirección de flujo limpia.

**Entrada y validación**

- [ ] Acepta una solicitud **`POST`** en un webhook en la ruta `/nutrition-check`, esperando un cuerpo como `{ "barcode": "3017620422003" }`.
- [ ] Si la solicitud llega **vacía / sin código de barras**, responde con un mensaje JSON **autodocumentado** que explique el servicio, el campo requerido y un ejemplo.
- [ ] **Valida** la entrada: el código de barras debe estar presente **y** ser numérico. Si no, responde con un error claro y estructurado (con un mensaje útil y un ejemplo).

**Datos**

- [ ] Llama al endpoint de **Open Food Facts** con el código de barras inyectado en la URL.
- [ ] Maneja el caso de **no encontrado** (una respuesta `404` con `status: 0` en el cuerpo) con una respuesta estructurada y amigable de "producto no encontrado" que incluya un código de barras de ejemplo válido.
- [ ] **Verifica si faltan datos de nutrientes**: si el producto se encontró pero sus campos de nutrientes también faltan o vienen vacíos, no intentes clasificarlo — responde con un mensaje claro de "datos insuficientes".
- [ ] **Extrae** los campos que necesitas en variables planas — recuerda la notación de corchetes para el campo de energía.

**Lógica**

- [ ] **Clasifica** el azúcar, la sal y la grasa por 100 g usando los umbrales de semáforo del fundador, y establece una marca para cada uno. (Esto solo se alcanza una vez que confirmaste que el producto tiene datos de nutrientes utilizables.)
- [ ] Calcula la **lectura de semáforo** (`saludable` / `moderado` / `no saludable`) a partir de la cantidad de nutrientes `alto`, y la **lectura de Nutri-Score** a partir de `nutriscore_grade`.
- [ ] Establece el **nivel de veredicto general** como la **peor de las dos lecturas** — usando solo la lectura de semáforo cuando `nutriscore_grade` sea `unknown` o falte.
- [ ] Calcula la **puntuación de preocupación** (0–3) con un cálculo de un solo ítem, solo a partir de las marcas de semáforo.

**Inteligencia (IA)**

- [ ] Haz que la **IA escriba un párrafo de veredicto corto** usando el nombre del producto, los números y las marcas.
- [ ] Haz que el **tono se adapte al nivel del veredicto** — alentador para `saludable`/`moderado`, cauteloso con delicadeza para `no saludable`. (Este es el patrón de "IA dentro de tu lógica de decisión"; asegúrate de que se ejercite de verdad, no un único prompt fijo.)

**Salida**

- [ ] Construye un mensaje de veredicto **con formato y de varias secciones**: un titular con emoji, los números clave alineados con marcadores rojo/verde, y luego el párrafo de la IA.
- [ ] Devuelve el **veredicto como texto plano**; devuelve la **autodocumentación, la respuesta de datos insuficientes y las respuestas de error como JSON** — con el `Content-Type` correspondiente y los códigos de estado: `200` para el veredicto y para docs/datos insuficientes, `400` para errores de validación, `404` para no encontrado.

⚠️ **IMPORTANTE — algunas reglas base:**

- Asegúrate de usar, como mínimo, los nodos que aprendiste a lo largo de este curso: Webhook, Respond to Webhook, HTTP Request (GET), IF, Merge (Append), Set / Edit Fields, Code (un ítem), y el nodo LLM de Groq.
- El nodo **Code** hace **un pequeño cálculo sobre un solo ítem** (la puntuación de preocupación). Sin bucles sobre arreglos.
- Cada API debe ser **sin clave y sin registro**. Tu clave de Groq es la única cuenta de todo el proyecto — y ya existe.

**Entrégalo como un profesional**

- [ ] Renombra **cada nodo** con la convención `[Acción] - [Propósito]` (por ejemplo `API Call - Open Food Facts Product`, `Validate - Barcode Present`, `AI - Health Verdict (Cautionary)`).
- [ ] Agrega **documentación en línea** a tus nodos, y escribe un **README del flujo** con las secciones que practicaste: Propósito, Cómo Funciona, Configuración, Uso, Manejo de Errores, Limitaciones.
- [ ] Mantén un **registro de pruebas en formato `TC-XXX`** que cubra los cuatro tipos de prueba: funcional (código válido → veredicto), integración (la API en vivo), error (código desconocido, entrada mal formada, cuerpo vacío, producto sin datos de nutrición) y una nota corta de rendimiento.
- [ ] Mantén un **CHANGELOG** siguiendo SemVer.

---

## ✅ Qué vamos a evaluar

- [ ] Existe un **diagrama** y claramente se hizo primero: formas correctas, rombos de decisión, rutas de error visibles, una sola dirección limpia.
- [ ] El webhook acepta un código de barras por `POST` y devuelve una respuesta a través del nodo Respond.
- [ ] Una **solicitud vacía** devuelve un mensaje JSON de uso autodocumentado.
- [ ] La **validación** rechaza un código de barras ausente o no numérico con un `400` estructurado y un ejemplo útil.
- [ ] La llamada a **Open Food Facts** funciona con el código inyectado, y la **ruta de no encontrado** (un `404` con `status: 0`) se maneja sin que el flujo se caiga y devuelve un `404` estructurado propio al usuario.
- [ ] Un producto encontrado pero sin datos de nutrición devuelve una respuesta de "datos insuficientes", no un veredicto.
- [ ] Los campos se **extraen correctamente**, incluido el campo de energía por notación de corchetes.
- [ ] El azúcar, la sal y la grasa se **clasifican correctamente** frente a los umbrales; el **nivel general** toma correctamente la **peor** de la lectura de semáforo y la lectura de Nutri-Score (con el respaldo aplicado cuando `nutriscore_grade` es `unknown` o falta); la **puntuación de preocupación** es correcta.
- [ ] Un producto con mucha azúcar y mal Nutri-Score (por ejemplo, una gaseosa) **no** queda mal clasificado como `saludable` solo porque ninguno de sus números por 100 g cruza los umbrales de `alto`.
- [ ] Se produce un **veredicto de IA**, y su **tono cambia** con el nivel del veredicto mediante enrutamiento condicional (no un único prompt fijo).
- [ ] El veredicto final es un mensaje de texto plano **limpio y de varias secciones** con marcadores rojo/verde; la documentación, la respuesta de datos insuficientes y los errores son todos JSON, con el `Content-Type` y los códigos de estado correctos (`200` / `400` / `404` según corresponda).
- [ ] Los **nombres de los nodos** siguen `[Acción] - [Propósito]`; los nodos están documentados en línea; el **README del flujo** tiene todas las secciones requeridas.
- [ ] El **registro de pruebas** usa `TC-XXX` y cubre funcional, integración, error y rendimiento.
- [ ] Está presente un **CHANGELOG** con SemVer.
- [ ] La construcción usa los nodos aprendidos en este curso, y toda API además de Groq es **sin clave**.

> Nota: esta es una automatización de una sola solicitud y un solo producto, así que no necesitarás manejo de arreglos ni bucles para resolverla — mantén el cálculo del nodo Code en un solo ítem.

---

## 📦 Cómo entregar

1. **Exporta tu flujo terminado** desde n8n como un archivo JSON (menú del flujo → _Download_).
2. Reúne el conjunto completo de entregables: el **JSON del flujo**, tu **diagrama de Excalidraw**, el **README del flujo**, el **registro de pruebas** y el **CHANGELOG**.
3. Entrégalos juntos de la forma que indique tu instructor.

Asegúrate de que tu automatización esté probada de principio a fin: un producto no saludable devuelve un veredicto cauteloso, un producto con Nutri-Score `a` devuelve uno alentador, un producto con mucha azúcar y mal Nutri-Score (como una gaseosa) se detecta correctamente como no saludable, un producto sin datos de nutrición recibe la respuesta de datos insuficientes en lugar de un veredicto, y cada ruta de error responde con gracia.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
