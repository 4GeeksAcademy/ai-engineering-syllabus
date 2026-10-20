# Bienvenido a TrackFlow

## AI Engineering · 4Geeks Academy — Briefing de la Empresa

---

TrackFlow es una empresa de entrega de última milla y gestión de almacenes fundada en 2009 en Los Ángeles, Estados Unidos. Opera en dos mercados — Estados Unidos y España — con almacenes en Los Ángeles y Zaragoza. La empresa cuenta con aproximadamente 130 empleados y genera alrededor de 9 millones de euros de facturación anual.

TrackFlow existe porque las marcas de e-commerce son buenas fabricando y vendiendo productos, pero no llevándolos hasta la puerta del cliente. TrackFlow lo hace por ellas: almacena su inventario, prepara y empaqueta los pedidos, los envía a través de una red de transportistas y gestiona las devoluciones cuando los productos vuelven. Para las marcas que trabajan con TrackFlow, toda la operación logística — desde que se hace un pedido hasta que se entrega o se devuelve — es un problema que resuelve TrackFlow.

## Cómo está organizada la empresa

TrackFlow está dirigida por **Thomas Harry**, fundador y CEO, con base en Los Ángeles. La empresa tiene una oficina tecnológica en Zaragoza, España, donde están el CTO Andrés Kim y la mayor parte del equipo técnico. Los equipos de operaciones, comercial y atención al cliente están repartidos entre los dos países.

La empresa se organiza en las siguientes áreas:

**Operaciones de Almacén** es donde ocurre el trabajo físico de la logística. Ana Whitfield supervisa los dos almacenes — uno en Los Ángeles y otro en Zaragoza — y a los aproximadamente 70 operarios que los gestionan. Cada día llegan cientos de pedidos que se recogen de las estanterías, se empaquetan y se entregan a los transportistas. Hoy los dos almacenes funcionan con sistemas distintos y no comparten una visión común del inventario.

**Última Milla y Gestión de Transportistas** gestiona la relación con los 8 transportistas con los que TrackFlow trabaja en los dos países — entre ellos UPS, FedEx, MRW y SEUR. Carlos Vega coordina qué transportista se encarga de cada envío, hace seguimiento de las entregas y gestiona las incidencias que inevitablemente ocurren: paquetes perdidos, entregas fallidas, direcciones incorrectas. Hoy la mayor parte de este trabajo se hace manualmente, transportista por transportista.

**Logística Inversa** gestiona lo que ocurre cuando un producto vuelve. Sofía Ramos lidera este equipo de cinco personas. Las devoluciones representan entre el 18% y el 25% del volumen total según el cliente y el país, y cada devolución implica una cadena de decisiones — aprobar o rechazar, recoger o no, reacondicionar o desechar — que hoy pasan todas por revisión humana.

**Experiencia del Cliente** es la primera línea entre TrackFlow y las personas a las que sirve. Valentina Cruz dirige a 15 agentes en Los Ángeles y Zaragoza que atienden consultas tanto de las marcas (que quieren saber cómo va su operación) como de los consumidores finales (que quieren saber dónde está su paquete). La gran mayoría de las consultas son repetitivas, y hoy cada una de ellas la responde una persona.

**Comercial y Relación con Clientes** gestiona la cartera de marcas cliente de TrackFlow. Miguel Torres lidera a los account managers y al equipo de desarrollo de negocio, responsables de retener a los clientes actuales y conseguir otros nuevos. Los contratos son anuales, y las renovaciones se ganan o se pierden según si el cliente siente que su operación logística funciona bien.

**Personas** cuida de quienes hacen funcionar TrackFlow. Rafael Sanz lidera un equipo de tres personas desde Zaragoza y se ocupa de la contratación, la incorporación, las políticas internas y las consultas del personal en los dos países, bajo dos marcos laborales distintos. Cada nueva incorporación al equipo corporativo — Tecnología, Comercial, Experiencia del Cliente o la gestión de operaciones — necesita entender cómo funciona realmente un negocio logístico en dos países antes de poder hacer bien su trabajo, y hoy ese aprendizaje se deja al azar.

**Tecnología** es el equipo que construye y mantiene todo. Andrés Kim lidera desde Zaragoza un equipo de desarrolladores, ingenieros de datos y técnicos de sistemas. La arquitectura actual es un mosaico: dos sistemas de almacén distintos, un ERP de principios de la década de 2010 e integraciones entre ellos construidas deprisa y nunca documentadas. Cuando algo falla, el equipo se entera por un WhatsApp de alguien de operaciones.

**Dirección Ejecutiva** recae en Thomas, que gestiona el negocio desde Los Ángeles con un informe semanal consolidado que cada director prepara manualmente — un proceso que consume horas cada domingo por la noche y que aun así entrega datos que ya tienen uno o dos días de antigüedad.

## Dónde está la empresa hoy

TrackFlow tiene buenos clientes, un equipo de operaciones capacitado y una propuesta de valor clara. Lo que le falta es la infraestructura para gestionar a escala un negocio logístico en dos países. Los dos almacenes no pueden ver el inventario del otro. Los datos de rendimiento de los transportistas no existen de forma estructurada. Las devoluciones se aprueban o se rechazan una a una. Las consultas de los clientes se responden consultando un documento de Word en Google Drive. El CEO toma decisiones con un informe montado a mano.

La consecuencia es que TrackFlow es más lenta, comete más errores y es menos rentable de lo que debería — y la distancia crece a medida que la competencia invierte en automatización.

Thomas ha creado una unidad interna llamada **TrackFlow Tech** con un mandato claro: construir los sistemas, las integraciones y las automatizaciones inteligentes que permitan a TrackFlow funcionar como la empresa logística moderna que necesita ser.

**Tú formas parte de esa unidad.**

---

---

## Los Departamentos y sus Problemas

### 🚚 Operaciones de Almacén

**Responsable:** Ana Whitfield (~70 operarios + 2 jefes de almacén)

Los Ángeles y Zaragoza utilizan cada uno un sistema de gestión de almacén distinto — uno es software comercial y el otro una hoja de cálculo avanzada. No existe visibilidad del inventario en tiempo real a nivel global. Los pedidos entrantes llegan por correo en formatos distintos y se transcriben a mano. El picking se hace con listas impresas en papel. Las discrepancias de inventario son frecuentes y se detectan tarde.

**Lo que necesitan:** Una API de inventario unificada que devuelva el stock en tiempo real de cualquier SKU en cualquiera de los dos almacenes, un pipeline de ingesta de pedidos que interprete los correos automáticamente, un dashboard de operaciones de almacén y alertas de stock bajo que avisen a los clientes y al equipo de compras.

---

### 📦 Última Milla y Gestión de Transportistas

**Responsable:** Carlos Vega (6 coordinadores logísticos)

TrackFlow trabaja con 8 transportistas en los dos países (UPS, FedEx y DHL en Estados Unidos; MRW, SEUR y DHL en España, además de dos transportistas locales). La asignación de transportista es manual. El seguimiento de paquetes obliga a consultar uno por uno los portales de cada transportista. No hay datos históricos de rendimiento: ni tasa de entrega a tiempo, ni incidencias por ruta, ni coste por kilo.

**Lo que necesitan:** Un motor de selección de transportista que recomiende el óptimo según destino, peso y urgencia; un endpoint de seguimiento unificado que agregue el estado de cualquier transportista; un portal público de seguimiento para los destinatarios; y un dashboard de rendimiento de transportistas.

---

### 🔄 Logística Inversa

**Responsable:** Sofía Ramos (equipo de 5 personas)

Las devoluciones representan entre el 18% y el 25% del volumen según el cliente y el país. Cada devolución pasa por revisión manual — no hay criterios de aprobación automática. La inspección del producto devuelto es subjetiva e inconsistente. No hay visibilidad sobre qué productos se devuelven más ni por qué.

**Lo que necesitan:** Un motor de aprobación automática de devoluciones con reglas configurables por cliente, un flujo de recogida automatizado (aprobación → etiqueta → programación con el transportista), un sistema de inspección asistida por IA en el que el operario fotografía el producto y la IA clasifica su estado, y un dashboard de devoluciones con análisis de patrones.

---

### 📞 Experiencia del Cliente

**Responsable:** Valentina Cruz (15 agentes en Los Ángeles y Zaragoza)

TrackFlow atiende a dos tipos de cliente: las marcas (B2B) y los consumidores finales (B2C). Los 15 agentes atienden a ambos por correo, WhatsApp y teléfono, sin un sistema de tickets unificado. El 80% de las consultas podría responderse automáticamente. No existe una base de conocimiento. La cobertura fuera del horario de oficina es nula.

**Lo que necesitan:** Un agente de primera línea que resuelva automáticamente las consultas de seguimiento y de estado de devoluciones, una base de conocimiento semántica indexada para RAG, un sistema de tickets unificado, un dashboard de Experiencia del Cliente en tiempo real y análisis de sentimiento para detectar clientes frustrados antes de que escalen. El soporte multilingüe (español + inglés) es opcional pero muy recomendable, empezando por un idioma base.

---

### 🤝 Comercial y Relación con Clientes

**Responsable:** Miguel Torres (4 account managers + 4 de desarrollo de negocio)

Los account managers siguen sus cuentas en hojas de cálculo personales y cadenas de correo — no hay CRM. Los informes a clientes son manuales: cada mes, un account manager reúne datos de distintos sistemas para enviar un PDF a cada cliente. No hay visibilidad sobre qué clientes corren riesgo de no renovar.

**Lo que necesitan:** Una integración con un CRM con perfiles de cliente unificados, informes PDF para clientes generados automáticamente por un agente, un dashboard de salud de clientes con puntuación de riesgo de renovación, alertas de renovación a 90 y 30 días, y un agente comercial que sugiera servicios relevantes a los prospectos.

---

### 🧑‍🤝‍🧑 Personas

**Responsable:** Rafael Sanz (equipo de 3 personas en Zaragoza)

La contratación y la incorporación del equipo corporativo se gestionan por correo, con un PDF de bienvenida distinto en cada país. Cada responsable explica a su manera cómo opera la empresa, y nadie comprueba si la nueva persona entiende de verdad los procesos de almacén, transportistas y devoluciones sobre los que funciona el negocio. Los accesos a los sistemas internos tardan días porque dependen de que alguien se acuerde de pedirlos. Las consultas del personal sobre vacaciones, políticas y beneficios llegan por correo y por chat, y se responden de forma distinta según quién conteste. No hay indicadores de Personas — plantilla, rotación, tiempo de contratación — por país, y el equipo gestiona dos marcos laborales muy distintos (Estados Unidos y España) sin ningún sistema.

**Lo que necesitan:** Un flujo de incorporación estructurado para el equipo corporativo que cubra la empresa, su operación, el puesto, la forma de trabajar y los lineamientos internos — con comprobaciones de comprensión y seguimiento del progreso; solicitudes de acceso a sistemas automatizadas; un portal interno de RR. HH. para vacaciones y consulta de políticas; un dashboard de indicadores de Personas por país; y un agente interno de RR. HH. que responda preguntas sobre políticas a partir de la documentación oficial. El soporte multilingüe (español + inglés) es opcional pero muy recomendable, empezando por un idioma base.

---

### 💻 Tecnología

**CTO:** Andrés Kim (equipo de 7 personas en Zaragoza)

La arquitectura técnica de TrackFlow es el resultado de años de crecimiento sin planificar: dos sistemas de gestión de almacén distintos, un ERP heredado de principios de la década de 2010, scripts de Python punto a punto sin documentar y bases de datos en dos proveedores cloud diferentes. No hay telemetría centralizada. Cuando un endpoint falla en Los Ángeles, el equipo de Zaragoza se entera por WhatsApp. Desplegar una funcionalidad nueva lleva entre una y dos semanas.

**Lo que necesitan:** Telemetría y logging centralizados de los dos países, un pipeline de datos que alimente todos los dashboards de la empresa, monitorización en tiempo real con alertas automáticas, un agente de documentación técnica y tareas de operaciones automatizadas (backups, health checks, notificaciones de incidencias).

---

### 📊 Dirección Ejecutiva

**CEO:** Thomas Espinoza

Thomas recibe cada lunes un informe consolidado que sus directores preparan el domingo por la noche — de 3 a 4 horas de trabajo por director. A las 10 de la mañana del lunes, parte de los datos ya tiene dos días de antigüedad. No hay una visión unificada del negocio por país. Las decisiones estratégicas se toman con datos parciales.

**Lo que necesita:** Un dashboard ejecutivo global con KPIs en tiempo real de las dos operaciones (volumen de envíos, entregas a tiempo, costes, devoluciones, CSAT), un informe semanal generado automáticamente cada lunes a las 7:00, vistas comparativas por país, alertas por umbral y un asistente de IA en lenguaje natural.

--

## ¿Por qué elegir TrackFlow?

Elige TrackFlow si te atraen:

- **La logística y las operaciones físicas** — cada línea de código que escribas está conectada a un paquete que viaja desde la estantería de un almacén hasta la puerta de alguien.
- **La complejidad transfronteriza** — dos países, dos idiomas, dos entornos regulatorios y dos stacks tecnológicos separados que hay que unificar.
- **La ingeniería de datos en su forma más concreta** — las métricas de rendimiento de transportistas, el inventario a nivel de SKU, los flujos de eventos de envíos y la clasificación de devoluciones son datos estructurados, medibles y muy visuales en un dashboard.
- **Los sistemas que funcionan 24/7** — los clientes de TrackFlow no dejan de esperar sus paquetes a partir de las seis de la tarde. El agente de atención, el portal de seguimiento y el dashboard de operaciones tienen que estar siempre disponibles.

Los retos de IA en TrackFlow incluyen la clasificación del estado de productos devueltos a partir de imágenes, la búsqueda semántica sobre políticas logísticas en dos idiomas, la selección inteligente de transportistas con recomendaciones explicables y un agregador de seguimiento de paquetes en tiempo real que consulta las APIs de 8 transportistas distintos. Si quieres construir sistemas que gestionen a escala la complejidad del mundo físico, TrackFlow es tu empresa.

---

_Documento interno — 4Geeks Academy · AI Engineering Track_
_Para uso exclusivo en la generación de proyectos del programa_
