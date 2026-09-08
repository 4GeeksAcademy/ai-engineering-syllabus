# Ejemplo en clase: Preparar el VPS gemelo del Wi‑Fi de un café (ejemplo de clase)

> **Para instructores:** Demo en vivo paralela a `vps-ssh-resource-optimization`. Misma columna vertebral — SSH, inventario, limpieza segura con `systemctl`, evidencia after — historia distinta. **No lo asignes como tarea.** Objetivo ~60–90 minutos con discusión.

_These instructions are also available in [English](./README.md)._

---

## El escenario

### Nota de alcance

Más corto que el proyecto del estudiante: un VPS guiado, un TXT after, sin reinicio opcional a fondo salvo que haya tiempo. Los estudiantes siguen el `README.md` raíz completo.

Un café de barrio tiene un servidor Ubuntu en la nube solo para una página de estado. El dueño dice que “está lleno” aunque casi no hay tráfico. En clase entrarás por SSH, medirás RAM/disco, apagarás servicios de escritorio inútiles y guardarás un snapshot after que diga que está listo y con qué recursos cuenta.

**Qué estás enseñando:**

- SSH como forma normal de llegar a un servidor
- Leer `free -h` / `df -h` / release del SO
- Servicios seguros vs peligrosos de desactivar en un VPS
- Entregar evidencia after como archivo de texto

---

## Requisitos previos

- Credenciales del VPS del instructor
- Terminal o editor con Remote SSH
- Lección del curso sobre eficiencia de RAM en Ubuntu VPS abierta para copiar/pegar comandos

---

## Tareas paso a paso

### 1. Conectar

- [ ] `ssh cafe_user@vps_ip`
- [ ] Ejecutar `hostname` y `whoami`

### 2. Inventario before (solo demo)

- [ ] `cat /etc/os-release`
- [ ] `free -h`
- [ ] `df -h`
- [ ] Opcional: `systemctl list-units --type=service --state=running | head`

### 3. Optimizar

- [ ] Aplicar la lista segura de la lección con `systemctl disable --now ...`
- [ ] Decidir en vivo con la clase si tocar Snap / multipath
- [ ] Confirmar que SSH sigue

### 4. Capturar evidencia after

- [ ] Crear `resources-after.txt` en el portátil (o en el VPS y bajarlo) con `free -h` y `df -h` tras la limpieza
- [ ] Mostrar el archivo en el editor como la forma de “entrega” que los estudiantes deben subir a GitHub

---

## Preguntas de discusión

1. ¿Por qué medir **antes** si la entrega evaluada es solo **después**?
2. ¿Qué servicios **nunca** desactivarías en un VPS usado solo por SSH, y por qué?
3. ¿Cuándo conviene mantener `unattended-upgrades` en lugar de apagarlo para ganar RAM?
