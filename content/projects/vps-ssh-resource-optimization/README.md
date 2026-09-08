# SSH into a VPS, audit resources, and optimize RAM

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/vps-ssh-resource-optimization/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your challenge

The **CTO of your company** wants you to prepare the **VPS** where the applications the team will build for the company will be deployed. Before anyone ships app code there, the machine must be reachable over SSH, inventoried, and optimized so unused OS services stop wasting RAM.

Treat this like an internal ops handoff for the company platform — connect, measure, optimize, then close the loop with leadership.

The CTO sent this brief:

> **From:** CTO  
> **To:** You  
> **Subject:** Prepare the company VPS for upcoming deployments
>
> Access the server **only via SSH** (terminal or Remote SSH in your editor). Do not use a provider web console as your deliverable.
>
> Capture a **before** picture of OS and resources for your own notes. Apply the safe Ubuntu cleanup from the course lesson so unused desktop/cloud services stop eating RAM. Do **not** break SSH — if you are unsure about a service, leave it alone and document why.
>
> When you finish, **tell me everything is ready** and **report how many resources the VPS has after optimization** (RAM, disk, and OS info). That after report is what I need to green-light deployments.

This is not an app-coding project. The outcome is a **prepared company VPS** plus clear **after** evidence you can hand the CTO.

Read the lesson **[Optimize Ubuntu on a VPS to use RAM more efficiently](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/lessons/optimize-ubuntu-vps-ram-efficiency/optimize-ubuntu-vps-ram-efficiency.md)** before you disable services. Use it as your playbook — do not invent random `systemctl` targets.

Prepare the VPS, then show the CTO it is ready and what resources remain.

---

## 🌱 How to Start the Project

This project does not use a starter application repository — it is a server configuration task. Delivery is a GitHub repo with the evidence you would send the CTO.

1. Get VPS credentials from the course platform (or your instructor).
2. Connect with SSH from your terminal or editor:

   ```bash
   ssh your_user@your_vps_ip
   ```

3. Create an empty GitHub repository for delivery (name suggestion: `vps-optimize-<your_github_username>`). You will push evidence files later — not the whole server disk.

> If you work on a local VM instead of the course VPS, confirm with your instructor first. Commands stay the same; credentials differ.

---

## 💻 What You Need to Do

### SSH access

- [ ] Get the VPS credentials from the course platform (or your instructor).
- [ ] Connect to the VPS over SSH from a terminal or Remote SSH (not only a provider web console).
- [ ] Confirm you have a shell prompt on the remote machine (`hostname`, `whoami`).

### Inventory (before)

- [ ] Record OS / version (for example `cat /etc/os-release` or `lsb_release -a`).
- [ ] Record RAM with `free -h`.
- [ ] Record disk with `df -h`.
- [ ] Optionally list running services with `systemctl list-units --type=service --state=running`.
- [ ] Save your before snapshot locally (notes or a `resources-before.txt` file) — useful for comparison, not the graded delivery format.

### Optimize

- [ ] Follow the course lesson to disable the safe unused-service set with `systemctl disable --now` (and optional Snap / multipath decisions as described there).
- [ ] Re-check that SSH still works after the changes.
- [ ] Optionally reboot once and reconnect to confirm services stay disabled.

### Report to the CTO (after) — this is your delivery

- [ ] Create a **TXT file** (recommended name: `resources-after.txt`) with at least `free -h` and `df -h` output after optimization (OS info welcome), plus a short line that the VPS is ready for company deployments.
- [ ] Push that TXT file to your GitHub delivery repository.

⚠️ **IMPORTANT:** Delivery must be a **TXT** showing the machine **after** optimization and communicating readiness + remaining resources. A before-only file does not count. Do not commit secrets, private keys, or full dumps of `/etc` with credentials.

---

## ✅ What We Will Evaluate

- [ ] SSH was used to reach the VPS (evidence consistent with a remote shell session).
- [ ] Student can identify OS and main resources (RAM and disk appear in their notes or evidence).
- [ ] Unused services were disabled following the course lesson (not random destructive commands).
- [ ] Deliverable is a **`resources-after.txt`** (or equivalent TXT) with after-optimization resources.
- [ ] The TXT communicates that the VPS is **ready** and reports available resources after optimization.
- [ ] The file is in a GitHub repository the instructor can open.
- [ ] No secrets or private keys in the repository.

> Note: Resource totals depend on the assigned VPS image. We care that you measured, applied the safe cleanup, and submitted clear **after** proof for the CTO.

---

## 📦 How to Submit this Project

Create a GitHub repository (for example `vps-optimize-<your_username>`) and push your **after** evidence as a TXT file:

- `resources-after.txt`

Share the repository URL with your instructor.

**Submission format:** `https://github.com/your_username/vps-optimize-your_username`

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/vps-ssh-resource-optimization/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
