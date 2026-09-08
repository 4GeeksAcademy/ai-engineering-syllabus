# Conectar por SSH a un VPS, auditar recursos y optimizar RAM

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/vps-ssh-resource-optimization/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in English](./README.md)._

**Antes de empezar**: 📗 [Lee las instrucciones](https://4geeks.com/lesson/how-to-start-a-project) sobre cómo iniciar un proyecto de programación.

<!-- endhide -->

---

## 🎯 Tu reto

El **CTO de tu compañía** quiere que prepares el **VPS** en el que se desplegarán las aplicaciones que el equipo va a desarrollar para la compañía. Antes de subir código de producto ahí, la máquina debe ser accesible por SSH, estar inventariada y optimizada para que servicios del SO innecesarios dejen de gastar RAM.

Trátalo como un handoff interno de ops de la plataforma de la compañía: conectar, medir, optimizar y cerrar el círculo con leadership.

El CTO te envió este brief:

> **De:** CTO  
> **Para:** Tú  
> **Asunto:** Preparar el VPS de la compañía para los próximos despliegues
>
> Accede al servidor **solo por SSH** (terminal o Remote SSH en tu editor). No uses la consola web del proveedor como entrega.
>
> Captura una foto **antes** del SO y los recursos para tus notas. Aplica la limpieza segura de Ubuntu de la lección del curso para que servicios de escritorio/nube innecesarios dejen de comer RAM. **No** rompas SSH: si dudas de un servicio, déjalo y documenta por qué.
>
> Cuando termines, **indícame que está todo listo** y **hazme saber con cuántos recursos cuenta el VPS después de optimizarlo** (RAM, disco e info de SO). Ese informe after es lo que necesito para dar luz verde a los despliegues.

Esto no es un proyecto de programación de apps. El resultado es un **VPS de la compañía preparado** más evidencia clara **after** que puedas entregar al CTO.

Lee la lección **[Optimizar Ubuntu en un VPS para usar la RAM de forma más eficiente](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/lessons/optimize-ubuntu-vps-ram-efficiency/optimize-ubuntu-vps-ram-efficiency.es.md)** antes de desactivar servicios. Úsala como guion — no inventes targets aleatorios de `systemctl`.

Prepara el VPS y demuestra al CTO que está listo y con qué recursos cuenta.

---

## 🌱 Cómo iniciar el proyecto

Este proyecto no usa un repositorio de aplicación de partida — es una tarea de configuración de servidor. La entrega es un repo de GitHub con la evidencia que enviarías al CTO.

1. Obtén las credenciales del VPS en la plataforma del curso (o tu instructor).
2. Conéctate por SSH desde tu terminal o editor:

   ```bash
   ssh your_user@your_vps_ip
   ```

3. Crea un repositorio vacío en GitHub para la entrega (nombre sugerido: `vps-optimize-<tu_usuario_github>`). Más adelante subirás archivos de evidencia — no el disco entero del servidor.

> Si trabajas en una VM local en lugar del VPS del curso, confírmalo primero con tu instructor. Los comandos son los mismos; cambian las credenciales.

---

## 💻 Qué debes hacer

### Acceso SSH

- [ ] Obtener las credenciales del VPS en la plataforma del curso (o tu instructor).
- [ ] Conectarte al VPS por SSH desde una terminal o Remote SSH (no solo la consola web del proveedor).
- [ ] Confirmar que tienes un prompt remoto (`hostname`, `whoami`).

### Inventario (antes)

- [ ] Anotar SO / versión (por ejemplo `cat /etc/os-release` o `lsb_release -a`).
- [ ] Anotar RAM con `free -h`.
- [ ] Anotar disco con `df -h`.
- [ ] Opcional: listar servicios en ejecución con `systemctl list-units --type=service --state=running`.
- [ ] Guardar el snapshot before en local (notas o un `resources-before.txt`) — útil para comparar; no es el formato de entrega evaluado.

### Optimizar

- [ ] Seguir la lección del curso para desactivar el conjunto seguro de servicios con `systemctl disable --now` (y las decisiones opcionales de Snap / multipath descritas ahí).
- [ ] Comprobar que SSH sigue funcionando tras los cambios.
- [ ] Opcional: reiniciar una vez y reconectar para confirmar que los servicios siguen desactivados.

### Informe al CTO (después) — esta es tu entrega

- [ ] Crear un **archivo TXT** (nombre recomendado: `resources-after.txt`) con al menos la salida de `free -h` y `df -h` después de optimizar (info de SO bienvenida), más una línea breve de que el VPS está listo para los despliegues de la compañía.
- [ ] Subir ese TXT a tu repositorio de entrega en GitHub.

⚠️ **IMPORTANTE:** La entrega debe ser un **TXT** que muestre la máquina **después** de la optimización y comunique que está listo + los recursos disponibles. Un archivo solo before no cuenta. No subas secretos, claves privadas ni dumps completos de `/etc` con credenciales.

---

## ✅ Qué vamos a evaluar

- [ ] Se usó SSH para llegar al VPS (evidencia coherente con una sesión remota).
- [ ] El estudiante identifica SO y recursos principales (RAM y disco aparecen en notas o evidencia).
- [ ] Se desactivaron servicios innecesarios siguiendo la lección del curso (no comandos destructivos al azar).
- [ ] La entrega es un **`resources-after.txt`** (o TXT equivalente) con los recursos after de la optimización.
- [ ] El TXT comunica que el VPS está **listo** y reporta los recursos disponibles tras optimizar.
- [ ] El archivo está en un repositorio de GitHub que el instructor pueda abrir.
- [ ] No hay secretos ni claves privadas en el repositorio.

> Nota: Los totales de recursos dependen de la imagen del VPS asignado. Importa que midieras, aplicaras la limpieza segura y entregaras prueba clara **after** para el CTO.

---

## 📦 Cómo entregar este proyecto

Crea un repositorio en GitHub (por ejemplo `vps-optimize-<tu_usuario>`) y sube tu evidencia **after** como archivo TXT:

- `resources-after.txt`

Comparte la URL del repositorio con tu instructor.

**Formato de entrega:** `https://github.com/tu_usuario/vps-optimize-tu_usuario`

---

Este y muchos otros proyectos son construidos por estudiantes como parte de los [Coding Bootcamps](https://4geeksacademy.com/) de 4Geeks Academy. Encuentra más acerca de los [cursos](https://4geeksacademy.com/es/comparar-programas) de [Ingeniería de IA](https://4geeksacademy.com/es/coding-bootcamps/ingenieria-ia), [Data Science & Machine Learning](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning), [Ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad) y [Full-Stack Software Developer con IA](https://4geeksacademy.com/es/coding-bootcamps/programador-full-stack).
