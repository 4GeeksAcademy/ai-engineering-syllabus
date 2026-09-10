# SSH into a VPS, audit resources, and optimize RAM — Reference Solution

## Purpose

Reference for a successful company VPS handoff requested by the CTO: SSH access, resource inventory, safe service cleanup, and an **after-optimization** `resources-after.txt` that states the VPS is ready and reports remaining resources.

## Solution deliverables

- GitHub repository (suggested name: `vps-optimize-<student_username>`).
- Graded after artifact: `resources-after.txt`.
- Optional (not graded format, but good practice): local `resources-before.txt` for comparison.

## Expected workflow

1. Connect with SSH: `ssh user@vps_ip` (or Remote SSH). Confirm with `hostname` / `whoami`.
2. Inventory **before**: OS (`/etc/os-release`), `free -h`, `df -h`, optional running services.
3. Optimize using the course lesson playbook — disable the safe unused-service set with `systemctl disable --now`, and optional Snap / multipath / unattended-upgrades decisions as documented in the lesson.
4. Confirm SSH still works; optionally reboot and reconnect.
5. Write `resources-after.txt` (ready statement + after resources) and push to GitHub.

## Indicative example — `resources-after.txt`

A correct TXT deliverable looks like this (numbers will differ per VPS):

```text
# After optimization — report for CTO
# Status: VPS ready for company application deployments
# date: YYYY-MM-DD
# host: company-vps

=== OS ===
NAME="Ubuntu"
VERSION="22.04.5 LTS (Jammy Jellyfish)"

=== Memory (free -h) ===
               total        used        free      shared  buff/cache   available
Mem:           1.9Gi       220Mi       1.4Gi       1.0Mi       320Mi       1.5Gi
Swap:             0B          0B          0B

=== Disk (df -h) ===
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda1        25G  3.1G   21G  13% /

=== Spot checks ===
systemctl is-active cups avahi-daemon bluetooth apport snapd multipathd
inactive
inactive
inactive
inactive
inactive
inactive
```

## What “good” looks like vs common misses

| Good                                                   | Miss                                          |
| ------------------------------------------------------ | --------------------------------------------- |
| After numbers in `resources-after.txt` + ready for CTO | Only before numbers                           |
| Evidence reachable on GitHub                           | Paste in chat only, no repo                   |
| Safe lesson service list                               | Random `systemctl stop` on ssh/network        |
| No private keys or secrets in repo                     | Committed `~/.ssh/id_*` or provider passwords |

## Validation checklist

- SSH session used for the work.
- OS + RAM + disk identified.
- Lesson-aligned unused services disabled.
- After evidence present as **TXT** (`resources-after.txt`).
- Repo has no secrets.
