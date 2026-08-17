<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: lee tu **[COMPANY-BRIEF.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/00-general-contexts)** y tu **[CONTEXT-roles-permissions.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/roles-permissions)** antes de escribir una sola línea de código — ahí están los roles, departamentos y reglas de acceso concretas de tu empresa.

---

# Plataforma – Roles y Permisos

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa — no en un repositorio nuevo.

Tu CTO abre un **ticket** con prioridad alta: el sistema hoy trata a cualquier usuario autenticado como si tuviera el mismo nivel de acceso. Eso funcionó mientras el equipo era pequeño y todo el mundo confiaba en todo el mundo — pero ya no es sostenible, y Legal lo ha señalado como un riesgo antes de seguir creciendo.

El **brief** es claro en un punto que se presta a confusión, así que léelo con cuidado: te piden **dos mecanismos distintos que trabajan juntos, no uno solo**.

> _"Necesito dos cosas separadas y no quiero que las mezcles en una sola tabla de permisos. Primero, el **rol** de una persona: qué puede hacer, qué puede ver, y qué responsabilidad tiene dentro del sistema — Empleado, Supervisor y Admin, como mínimo. Segundo, el **departamento** al que pertenece: eso no le da ni le quita permisos de acción, pero sí determina qué información concreta le compete. Un Supervisor de Operaciones y un Supervisor de Finanzas tienen exactamente las mismas capacidades como Supervisores — pero no deberían ver los mismos datos."_
>
> — CTO

Tres requisitos quedan implícitos en ese brief y **debes identificarlos leyendo con atención**:

1. Rol y departamento son **ejes independientes**. Cambiar el departamento de una persona no debe alterar lo que su rol le permite hacer; cambiar su rol no debe alterar automáticamente qué información departamental ve.
2. El sistema necesita **al menos tres roles** con una jerarquía de capacidades clara y verificable — no basta con un booleano `is_admin`.
3. Las reglas de acceso deben aplicarse **en el backend**, no solo esconder botones en el frontend. Un usuario sin permiso que llama directamente al endpoint debe recibir un rechazo, no una respuesta silenciosa con datos vacíos.

### Conocimiento complementario: rol vs. departamento

Es fácil confundir estos dos conceptos porque ambos "restringen" algo, pero restringen cosas distintas. El **rol** responde a la pregunta _"¿qué puede hacer esta persona en el sistema?"_ — es sobre capacidades y responsabilidad (crear, aprobar, eliminar, administrar usuarios). El **departamento** responde a _"¿qué información le compete a esta persona?"_ — es sobre alcance de datos (ver reportes de su área, no de todas). Un diseño correcto evalúa ambos ejes en cada decisión de acceso: primero si el rol permite la acción, después si el departamento permite ver ese dato concreto.

---

## 🌱 Cómo Empezar el Proyecto

1. Haz `pull` de los últimos cambios de tu fork del monorepo.
2. Lee `COMPANY-BRIEF.md` y `CONTEXT-roles-permissions.md` completos antes de tocar código.
3. Crea una rama nueva: `feature/roles-permissions`.
4. Mapea todos los endpoints existentes en tu sistema y clasifícalos por el rol mínimo requerido para usarlos.
5. Diseña el modelo de datos de roles, departamentos y su relación con el usuario antes de escribir la primera migración.

---

## 💻 Qué Debes Hacer

**Modelo de datos**

- [ ] Define al menos tres roles con una jerarquía de capacidades explícita y documentada (por ejemplo: Empleado, Supervisor, Admin)
- [ ] Define el concepto de departamento como entidad independiente del rol
- [ ] Modela la relación usuario–rol–departamento de forma que un usuario pueda cambiar de departamento sin perder su rol, y viceversa

**Backend**

- [ ] Implementa un mecanismo centralizado de verificación de permisos (middleware o dependencia), no validaciones repetidas endpoint por endpoint
- [ ] Aplica la restricción de rol a cada endpoint según la capacidad que expone
- [ ] Aplica la restricción de departamento a cada endpoint que devuelva datos con alcance departamental
- [ ] Devuelve un código de rechazo explícito (403) cuando el rol no alcanza — nunca una respuesta con datos vacíos o silenciados
- [ ] Escribe pruebas automatizadas que demuestren que un usuario de rol y departamento incorrectos no puede acceder a un recurso restringido

**Frontend / backoffice**

- [ ] Oculta o deshabilita en la interfaz las acciones que el rol del usuario no permite
- [ ] Muestra únicamente los datos departamentales que corresponden al usuario autenticado
- [ ] Implementa una vista de administración de roles y departamentos accesible solo para el rol Admin

⚠️ **IMPORTANTE:** los nombres exactos de los roles, los departamentos existentes y las reglas de qué información compete a cada departamento deben corresponder exactamente a lo especificado en tu `CONTEXT-roles-permissions.md`. Una implementación genérica que ignore ese contexto no será aceptada.

---

## ✅ Qué Vamos a Evaluar

- [ ] Existen al menos tres roles con capacidades diferenciadas y verificables mediante pruebas
- [ ] Rol y departamento se comportan como ejes independientes: modificar uno no altera el otro
- [ ] Todo endpoint sensible rechaza explícitamente (403) a un usuario sin el rol requerido, verificado con una llamada directa a la API, no solo desde la interfaz
- [ ] Un usuario del mismo rol pero distinto departamento no puede acceder a datos fuera de su alcance departamental
- [ ] La verificación de permisos está centralizada, no duplicada por endpoint
- [ ] Existe una vista de administración de roles y departamentos restringida al rol Admin

---

## 📦 Cómo Entregar

Abre un Pull Request desde tu rama `feature/roles-permissions` hacia `main` en tu fork. En la descripción del PR incluye la tabla de roles y capacidades que definiste, y evidencia (captura o log de prueba) de que un endpoint sensible rechaza a un usuario sin permisos. Solicita el sign-off de tu CTO antes de hacer merge.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
