# Plataforma – Endurecimiento de Seguridad

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

<!-- endhide -->

---

## 🎯 El Reto

> 📌 Estás construyendo sobre **tu copia** del **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** de la empresa — no en un repositorio nuevo.

Antes de exponer cualquier superficie nueva de cara al público, tu CTO exige una auditoría de seguridad sobre lo que ya existe. Te lo plantea como un **ticket** de prioridad bloqueante: nada nuevo se despliega hasta que esto quede resuelto.

> *"No voy a autorizar que expongamos más superficie pública hasta que sepamos qué vulnerabilidades tiene lo que ya construimos. Quiero que audites la aplicación como lo haría un atacante externo, documentes qué encontraste, lo corrijas, y me entregues evidencia de que estaba roto y ahora no lo está. No me sirve un checklist marcado de memoria — quiero encontrar problemas reales."*
>
> — CTO

Tres exigencias del brief que conviene aclarar antes de empezar:

1. **La auditoría es guiada, no una herramienta automática que se ejecuta sola.** Debes entender por qué cada hallazgo es un problema, no solo pegar la salida de un escáner.
2. **"Corregido" significa demostrado, no asumido.** Cada vulnerabilidad que reportes debe tener una prueba de que existía y una prueba de que ya no existe.
3. **El alcance es tu propia aplicación**, no infraestructura de terceros ni servicios externos que no controlas.

### Conocimiento complementario: el OWASP Top 10 como punto de partida, no como techo

El OWASP Top 10 es una lista de las categorías de vulnerabilidad más comunes y de mayor impacto en aplicaciones web — cosas como control de acceso roto, fallos criptográficos, inyección, configuración de seguridad incorrecta, o componentes con vulnerabilidades conocidas. Es un buen punto de partida porque es la lista que cualquier revisor técnico espera que conozcas, pero no es exhaustiva: una aplicación puede pasar las diez categorías y seguir teniendo problemas específicos de su propia lógica de negocio (por ejemplo, un endpoint que expone más datos de los que debería aunque la autenticación esté bien implementada). El objetivo de este proyecto es pensar como atacante sobre tu aplicación concreta, no solo marcar una lista genérica.

---

## 🌱 Cómo Empezar el Proyecto

1. Haz `pull` de los últimos cambios de tu fork del monorepo.
2. Crea una rama nueva: `feature/security-hardening`.
3. Haz un inventario de los endpoints y flujos de tu aplicación que representan mayor riesgo (autenticación, pagos si existen, datos sensibles, acciones destructivas).
4. Antes de corregir nada, documenta el estado actual — necesitarás el "antes" para demostrar el "después".

---

## 💻 Qué Debes Hacer

**Auditoría guiada**

- [ ] Revisa tu aplicación contra cada categoría del OWASP Top 10 vigente, documentando qué aplica y qué no a tu sistema concreto
- [ ] Identifica al menos tres vulnerabilidades reales en tu propia aplicación, con evidencia reproducible de cada una (petición, payload o pasos concretos)
- [ ] Documenta el impacto de cada vulnerabilidad encontrada: qué podría hacer un atacante si la explotara

**Rate limiting**

- [ ] Implementa límites de tasa en los endpoints más sensibles (login, recuperación de contraseña, endpoints de escritura críticos)
- [ ] Verifica que el límite responde con un código apropiado (429) y no simplemente falla de forma ambigua

**Gestión de secretos**

- [ ] Audita que ningún secreto (claves de API, credenciales, tokens) esté hardcodeado en el código fuente o en el historial de commits
- [ ] Implementa o verifica un mecanismo de rotación de secretos, y documenta el procedimiento para rotar uno sin causar una interrupción de servicio

**Corrección y verificación**

- [ ] Corrige cada vulnerabilidad encontrada en la auditoría
- [ ] Para cada una, documenta evidencia de "antes" (vulnerable) y "después" (corregida) — captura, log o prueba automatizada

---

## ✅ Qué Vamos a Evaluar

- [ ] Existe un informe de auditoría con al menos tres vulnerabilidades reales encontradas en la aplicación propia, no genéricas ni copiadas
- [ ] Cada vulnerabilidad reportada tiene evidencia reproducible de que existía y evidencia de que fue corregida
- [ ] Los endpoints sensibles identificados tienen rate limiting funcional, verificado con una prueba que provoca el límite
- [ ] No existen secretos expuestos en el código fuente ni en el historial de commits
- [ ] Existe documentación clara del procedimiento de rotación de secretos

---

## 📦 Cómo Entregar

Abre un Pull Request desde tu rama `feature/security-hardening` hacia `main` en tu fork. En la descripción del PR incluye el informe de auditoría completo (hallazgos, evidencia de antes/después, y correcciones aplicadas). Solicita el sign-off de tu CTO antes de hacer merge — este proyecto no se aprueba sin evidencia reproducible.

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Full-Stack Software Developer](https://4geeksacademy.com/es/programas-de-carrera/desarrollo-full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/es/programas-de-carrera/ciencia-de-datos-ml), [Ciberseguridad](https://4geeksacademy.com/es/programas-de-carrera/ciberseguridad) e [Ingeniería de IA](https://4geeksacademy.com/es/programas-de-carrera/ingenieria-ia).
