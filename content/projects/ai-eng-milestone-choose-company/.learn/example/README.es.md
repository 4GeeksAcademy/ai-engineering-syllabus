# Ejemplo de clase: Elige un negocio local para digitalizar

> **Nota para el instructor:** Este es un ejemplo de clase para introducir los conceptos del proyecto *Milestone 0 — Elige tu empresa* usando un dominio más cercano y sencillo. Cubre las mismas habilidades (leer un documento de contexto, tomar una decisión estructurada, proponer una idea de agente de IA, configurar el entorno de desarrollo) pero con tres pequeños negocios locales en lugar de un escenario corporativo complejo. Úsalo como actividad de calentamiento de 30 a 45 minutos antes de que los estudiantes aborden el milestone principal. NO compartir este archivo con los estudiantes antes de que intenten el proyecto principal.

---

## La actividad

Estás a punto de empezar un sprint de proyecto breve. Durante las próximas sesiones construirás una herramienta digital para un negocio local — y esta decisión condiciona todo lo que construirás a partir de aquí.

A continuación hay tres perfiles de pequeños negocios. Cada uno tiene problemas operativos reales que el software y la IA podrían resolver. **Lee los tres con atención** y luego elige el que más te motive.

---

## Perfiles de negocio

### Opción A — La panadería del barrio 🧁

**Descripción:** Una panadería familiar con un solo local. Elaboran entre 15 y 20 tipos de productos al día, reciben pedidos por WhatsApp y llevan el control todo en un cuaderno en papel.

**Problemas actuales:**

| Departamento | Problema |
|---|---|
| Pedidos | Los pedidos llegan por WhatsApp y se anotan a mano — es fácil perderlos u olvidarlos |
| Inventario | Los ingredientes se controlan en un cuaderno; a menudo se quedan sin existencias a mitad del día |
| Reparto | Los turnos de entrega se anotan en post-its; la coordinación es caótica |

**Lo que quieren construir:** Una página de gestión de pedidos, un rastreador de stock de ingredientes y un planificador de producción diaria.

**Un posible reto de IA:** Un agente que lea los pedidos del día y sugiera automáticamente cuántas unidades de cada producto hornear, basándose en el historial de pedidos.

---

### Opción B — La librería de segunda mano 📚

**Descripción:** Una librería de libros de segunda mano con más de 2.000 títulos en estanterías que están solo parcialmente catalogadas. Vende en tienda física y ocasionalmente online a través de una página básica de Instagram.

**Problemas actuales:**

| Departamento | Problema |
|---|---|
| Catálogo | La mayoría de los libros no están en ningún sistema digital — el personal se fía de la memoria |
| Peticiones de clientes | Los clientes preguntan por títulos concretos; el personal no tiene forma de comprobar la disponibilidad rápidamente |
| Eventos | Los eventos mensuales del club de lectura se anuncian solo en flyers en papel |

**Lo que quieren construir:** Un catálogo de libros con buscador, un sistema de lista de deseos para clientes y una página de eventos.

**Un posible reto de IA:** Un agente que escanee la foto de la portada de un libro y rellene automáticamente el título, el autor y el género al añadirlo al catálogo.

---

### Opción C — El gimnasio local 🏋️

**Descripción:** Un gimnasio independiente con 150 socios activos. Las membresías se gestionan en una hoja de cálculo. El horario de clases se publica en una pizarra y se actualiza manualmente.

**Problemas actuales:**

| Departamento | Problema |
|---|---|
| Membresías | El personal comprueba manualmente las hojas de cálculo para verificar si el plan de un socio sigue vigente |
| Clases | Los socios no pueden reservar plaza — simplemente se presentan y esperan que haya sitio |
| Asistencia | No hay historial de asistencia — el gimnasio no puede saber qué clases son más populares |

**Lo que quieren construir:** Un rastreador de membresías, un sistema de reserva de clases y un dashboard de asistencia.

**Un posible reto de IA:** Un agente que analice los datos de asistencia de los últimos 3 meses y recomiende el horario óptimo de clases para el mes siguiente.

---

## Qué tienes que hacer

- [ ] **Lee los tres perfiles** con atención. No hagas una lectura rápida — los detalles importan para tus decisiones de diseño.
- [ ] **Elige un negocio** y registra tu decisión en un fichero `business-choice.md`:
  - Indica claramente qué negocio elegiste y por qué (mínimo 3-5 frases).
  - Identifica los **dos departamentos** cuyos problemas encuentres más interesantes de resolver.
  - Identifica **una funcionalidad** de la lista de construcción que más ganas tengas de implementar.
- [ ] **Configura tu entorno:**
  - Clona el repositorio inicial (tu instructor te dará el enlace).
  - Ábrelo en GitHub Codespaces o en local.
  - Confirma que todo carga sin errores.
- [ ] **Propón una solución con un Agente de IA** para el reto de IA del negocio que elegiste:
  - Describe en lenguaje sencillo qué haría el agente, qué datos necesitaría y qué produciría o desencadenaría.
  - No hace falta código — un párrafo corto o una lista de puntos es suficiente.
  - Añade esto al fichero `business-choice.md` bajo una sección titulada `## Mi idea de Agente de IA`.

---

## Qué evaluaremos

- [ ] `business-choice.md` existe y está commiteado.
- [ ] Se ha elegido un negocio concreto con una justificación de al menos 3 frases.
- [ ] Se han identificado dos departamentos con una breve explicación de por qué son interesantes.
- [ ] Se ha nombrado una funcionalidad concreta a construir.
- [ ] La propuesta del agente de IA describe qué hace el agente, qué necesita y qué produce.
- [ ] El entorno de desarrollo se abre correctamente sin errores.

---

## Preguntas de discusión

1. Solo puedes elegir un negocio. ¿Qué criterios usaste para decidir — la familiaridad con el sector, la complejidad de los problemas, u otra cosa? ¿Cómo habría cambiado tu elección las funcionalidades que construirías?
2. Observa el reto del agente de IA del negocio que elegiste. ¿A qué datos necesitaría acceder el agente? ¿Dónde viven esos datos actualmente (papel, hoja de cálculo, memoria de las personas)? ¿Qué tendría que cambiar antes de que el agente pudiera funcionar?
3. Los tres negocios tienen un problema de "el personal se fía de la memoria". ¿Por qué es un patrón tan común en los negocios pequeños? ¿Qué te dice sobre lo más valioso que puede aportar un sistema digital, más allá de la simple automatización?
