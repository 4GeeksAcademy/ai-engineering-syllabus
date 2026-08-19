<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee tu **[COMPANY-BRIEF.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts)** y tu **[CONTEXT-audit-log.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/audit-log)** antes de escribir una sola línea de código — ahí están los eventos críticos de tu empresa y quién debe poder consultarlos.

---

# Plataforma – Registro de Auditoría

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa — no en un repositorio nuevo.

Compliance (o quien haga esa función en tu empresa) abre un **ticket** después de un incidente menor que nadie pudo reconstruir del todo: alguien modificó un dato sensible, pero no había forma confiable de saber quién, cuándo, ni desde dónde. Tu CTO te lo traslada como prioridad.

> _"Necesito poder responder, sin ambigüedad, tres preguntas sobre cualquier acción sensible del sistema: quién la hizo, qué hizo exactamente, y cuándo. No me sirve un log de aplicación normal que cualquiera con acceso a la base de datos pueda editar o borrar después del hecho — necesito algo que, una vez escrito, quede escrito. Si en seis meses alguien pregunta 'quién cambió esto', la respuesta tiene que salir del sistema, no de la memoria de nadie."_
>
> — CTO

Tres exigencias del brief que se prestan a implementarse a medias si no las lees con cuidado:

1. **Append-only de verdad.** Un registro de auditoría que se puede editar o borrar desde la aplicación no es un registro de auditoría — es un log más. La inmutabilidad debe ser una propiedad del diseño, no una convención que el equipo promete respetar.
2. **El "quién" no es solo el usuario humano.** Si tu sistema tiene agentes o procesos automatizados que actúan sobre datos, esas acciones también deben quedar registradas, identificando que el actor fue un proceso y no una persona.
3. **No todo el mundo puede consultar el registro completo.** Quién puede ver qué parte del audit log depende de los roles y departamentos que ya definiste en la plataforma — este proyecto se apoya en esa base, no la reemplaza.

### Conocimiento complementario: qué hace "de auditoría" a un registro

Un log técnico (errores, latencia, trazas) y un registro de auditoría no son lo mismo, aunque ambos "registran cosas". El registro de auditoría existe para responder preguntas de responsabilidad y cumplimiento — quién hizo qué sobre qué recurso — y por eso su diseño prioriza tres propiedades que un log técnico normalmente no necesita: **inmutabilidad** (no se puede alterar después de escrito), **completitud** (cubre toda acción sensible, no solo errores) y **atribución clara** (siempre hay un actor identificado, humano o de sistema). Una técnica común para reforzar la inmutabilidad es el encadenamiento por hash: cada entrada incluye el hash de la entrada anterior, de forma que alterar un registro pasado rompe visiblemente la cadena.

---

## 🌱 Cómo Empezar el Proyecto

1. Haz `pull` de los últimos cambios de tu fork del monorepo.
2. Lee `COMPANY-BRIEF.md` y `CONTEXT-audit-log.md` completos antes de tocar código.
3. Crea una rama nueva: `feature/audit-log`.
4. Haz un inventario de las acciones sensibles que ya existen en tu sistema (creación, modificación, eliminación de recursos críticos, cambios de permisos, accesos a datos restringidos).
5. Diseña primero el esquema de la entrada de auditoría (actor, acción, recurso, timestamp, origen) antes de decidir dónde se dispara cada registro.

---

## 💻 Qué Debes Hacer

**Modelo y almacenamiento**

- [ ] Diseña una tabla o colección append-only dedicada al audit log, separada de las tablas operativas del sistema
- [ ] Cada entrada incluye como mínimo: actor (usuario o proceso), acción realizada, recurso afectado, timestamp, y origen (IP o identificador de proceso)
- [ ] Implementa un mecanismo que haga evidente cualquier alteración posterior de una entrada ya escrita (por ejemplo, encadenamiento por hash)
- [ ] Garantiza a nivel de base de datos o de aplicación que no existe ninguna ruta de `UPDATE` o `DELETE` sobre esta tabla desde la aplicación

**Captura de eventos**

- [ ] Instrumenta la captura de auditoría en las acciones sensibles identificadas en tu inventario inicial
- [ ] Registra las acciones ejecutadas por procesos o agentes automatizados, distinguiéndolas claramente de las acciones humanas
- [ ] Registra los eventos relevantes de autenticación (login exitoso, login fallido, cambios de permisos) si tu sistema ya cuenta con esos flujos

**Visor y consulta**

- [ ] Implementa una vista en el backoffice para consultar el registro, con filtros por actor, tipo de acción, recurso y rango de fechas
- [ ] Restringe el acceso al visor según los roles y departamentos ya definidos en tu plataforma — no todo Admin debe ver necesariamente todo el registro sin restricción, según lo que indique tu contexto de empresa
- [ ] Implementa paginación o límites de consulta razonables para que el visor sea usable con volúmenes de datos reales

⚠️ **IMPORTANTE:** los eventos considerados críticos para tu empresa y las reglas de quién puede consultarlos deben corresponder exactamente a lo especificado en tu `CONTEXT-audit-log.md`. Una implementación genérica que ignore ese contexto no será aceptada.

---

## ✅ Qué Vamos a Evaluar

- [ ] Existe una prueba que demuestra que una entrada del audit log no puede modificarse ni eliminarse desde la aplicación una vez escrita
- [ ] Todas las acciones sensibles identificadas en el inventario quedan registradas correctamente, con actor, acción, recurso y timestamp
- [ ] Las acciones realizadas por procesos o agentes automatizados quedan claramente diferenciadas de las acciones humanas
- [ ] El visor de auditoría permite filtrar por actor, acción, recurso y fecha, y respeta las restricciones de acceso por rol y departamento
- [ ] El mecanismo de evidencia de alteración (por ejemplo, encadenamiento por hash) funciona: alterar manualmente una entrada rompe la cadena de forma detectable

---

## 📦 Cómo Entregar

Abre un Pull Request desde tu rama `feature/audit-log` hacia `main` en tu fork. En la descripción del PR incluye el esquema de la entrada de auditoría que diseñaste, la lista de acciones instrumentadas, y evidencia de que una alteración manual de una entrada resulta detectable. Solicita el sign-off de tu CTO antes de hacer merge.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
