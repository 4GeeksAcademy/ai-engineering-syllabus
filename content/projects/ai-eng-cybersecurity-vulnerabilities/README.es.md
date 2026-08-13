# Auditoría y Corrección de Vulnerabilidades Web (OWASP Top 10)

<!-- hide -->

Por [@marcogonzalo](https://github.com/marcogonzalo) y [otros contribuidores](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) en [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

**Antes de empezar**: Lee tu **[CONTEXT-empresa.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/cybersecurity-analysis)** antes de escribir código — te recuerda qué aplicaciones y servicios forman parte de tu monorepo y qué categorías OWASP importan más para tu sistema agéntico.

---

## 🎯 Tu reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa seleccionada al inicio del curso — no en un repositorio nuevo.

Las aplicaciones de la compañía — frontend, backend, y el sistema agéntico — nunca pasaron una auditoría formal de seguridad web. Corren con configuración por defecto en varios puntos: acceso directo como root, puertos abiertos que nadie recuerda por qué están abiertos, y ninguna revisión sistemática de las vulnerabilidades más comunes que expone cualquier aplicación conectada a internet.

Ha llegado un **ticket** de seguridad: antes de que cualquier aplicación de la compañía reciba más tráfico real, necesita pasar una auditoría basada en el **OWASP Top 10**. El **brief** de tu tech lead es claro: no basta con listar los hallazgos, cada vulnerabilidad crítica identificada debe quedar corregida y verificable antes del **sign-off**.

> **De:** Tech Lead
> **Para:** Squad de Ingeniería
>
> **Contexto:** Nuestras aplicaciones nunca pasaron una auditoría formal de seguridad web. Tenemos APIs, frontends, y un sistema agéntico corriendo con configuración por defecto en varios puntos.
>
> **Qué necesito:** Un endurecimiento básico del servidor (acceso SSH, usuario no-root, permisos de carpetas, firewall) y una auditoría completa contra el OWASP Top 10, con las vulnerabilidades críticas corregidas — incluyendo las que son específicas de tu sistema agéntico.
>
> **Acceptance criteria:** El servidor no permite login directo como root; existe un firewall con solo los puertos necesarios abiertos; cada categoría del OWASP Top 10 fue evaluada explícitamente contra tu aplicación, con hallazgo (aplica / no aplica) y evidencia; toda vulnerabilidad marcada como crítica está corregida y demostrada.

---

## 🌱 Cómo Empezar el Proyecto

1. Haz un `git pull` de tu fork del monorepo y crea una rama nueva para este trabajo: `git switch -c feature/owasp-top10-audit`.
2. Revisa cómo accedes actualmente a tu servidor: ¿usas el usuario root para todo? ¿qué puertos están expuestos?
3. Familiarízate con las 10 categorías del OWASP Top 10 antes de auditar — no las adivines mientras revisas código.
4. Antes de corregir nada, documenta el estado actual: es tu línea base para demostrar la mejora.

---

## 💻 Qué Necesitas Hacer

**Endurecimiento del servidor**

- [ ] Crea un usuario de acceso dedicado (no root) para las tareas operativas del día a día.
- [ ] Restringe o deshabilita el acceso SSH directo como root.
- [ ] Define permisos explícitos de carpetas para separar código, logs, y archivos de configuración sensibles.
- [ ] Configura un firewall que solo permita los puertos estrictamente necesarios para que tu aplicación funcione.

**Auditoría OWASP Top 10**

- [ ] Evalúa cada una de las 10 categorías del OWASP Top 10 contra tu backend, tu frontend, y tu sistema agéntico por separado.
- [ ] Para cada categoría, documenta si aplica o no a tu sistema, con la evidencia concreta (endpoint, archivo, línea de código) que sustenta tu conclusión.
- [ ] Presta especial atención a las categorías que interactúan con tu sistema agéntico: control de acceso roto (¿puede un usuario invocar una herramienta que no le corresponde?), fallas criptográficas (¿cómo se almacenan tus API keys?), y configuración de seguridad incorrecta (¿tu agente corre con más permisos de los necesarios?).

**Corrección**

- [ ] Corrige todas las vulnerabilidades marcadas como críticas en tu auditoría.
- [ ] Para cada corrección, deja evidencia reproducible (un test, un screenshot del escaneo, o un comando que demuestre el antes/después).

⚠️ **IMPORTANTE:** Revisa tu `CONTEXT-empresa.md` para confirmar qué aplicaciones y servicios de tu monorepo deben incluirse en el alcance de la auditoría.

---

## ✅ Qué Vamos a Evaluar

- [ ] El servidor no permite acceso SSH directo como root.
- [ ] Existe un usuario dedicado no-root para tareas operativas, con permisos de carpetas explícitos.
- [ ] El firewall solo expone los puertos estrictamente necesarios; el resto están cerrados.
- [ ] Las 10 categorías del OWASP Top 10 fueron evaluadas explícitamente, con hallazgo y evidencia por categoría.
- [ ] El sistema agéntico fue auditado como un componente propio, no asumido como "ya seguro" por estar cubierto en el backend.
- [ ] Toda vulnerabilidad marcada como crítica está corregida, con evidencia reproducible del antes y el después.

---

## 📦 Cómo Entregar

1. Haz commit y push de tu rama.
2. Abre un Pull Request hacia tu propio fork del monorepo, incluyendo el informe de auditoría OWASP Top 10 como archivo markdown dentro de tu carpeta de entrega.
3. En la descripción del PR, enlaza la evidencia de al menos dos correcciones críticas.
4. Solicita revisión a tu tech lead antes del sign-off final.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
