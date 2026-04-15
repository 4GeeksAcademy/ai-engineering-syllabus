# Incident Report Processor Script

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start:** Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts)** before writing any code — it defines the exact CSV field names, valid categories, allowed statuses, and the expected output values your script must produce.

---

## 🎯 The Challenge

A different kind of request arrives: no interface to build, no API to spin up. What you need to deliver is a **data analysis tool** that solves a real, urgent problem.

Your company's after-sales support department manages customer incidents: complaints, requests, operational failures. They've just prepared a CSV file with **100 records** extracted from their system — the first sample of a real data volume that could reach one million rows.

The problem is that **this file cannot be sent to an AI tool**. It contains sensitive customer information: personal identifiers, email addresses, contact details. The team needs to analyse the data internally.

Your job is to write a **Python script** that loads the file, validates it, extracts the key metrics, and delivers a structured summary. If the script works correctly on the 1,000-record sample, it will then be run on the full production file.

> **Note from your tech lead:** _"We need a script that anyone on the team can run with_ `python analyze.py incidents.csv`_. The console output has to be readable and professional. Give them an option to export the results to JSON or CSV too — not everyone works from the terminal. Make sure it catches corrupt or incomplete records; if we don't validate the data before processing, the analysis on the big file is going to be garbage. The expected values for the test CSV are in your CONTEXT."_

### What counts as an incomplete or corrupt record?

Real-world data always has problems. For this project, a record is considered **invalid** if it is missing at least one of the required fields defined in your CONTEXT, or if it contains a value in a field that is not within the allowed set (statuses and categories). Your script must detect them, count them, and exclude them from the main analysis — but never silently ignore them.

---

## 🌱 How to Start the Project

1. Fork the course repository:
   ```text
   https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo
   ```
2. Clone your fork locally.
3. Read your **CONTEXT-company.md** file before writing a single line of code. It defines the CSV structure, required fields, valid values, and the expected results your script must match.
4. Work inside the directory corresponding to this project in the monorepo.

There is no starter code. The script starts from scratch.

---

## 💻 What You Need to Do

### Main analysis script

- [ ] Create the main script (`analyze.py`) that accepts the path to the CSV as a command-line argument: `python analyze.py incidents.csv`.
- [ ] The script must load and read the file row by row (or with pandas — your choice).
- [ ] Detect and count invalid records. Detail how many there are and why (missing field, out-of-range value, etc.).
- [ ] Calculate the following metrics on **valid records**:
  - [ ] Total number of elements processed (valid and invalid separately).
  - [ ] Breakdown by incident category.
  - [ ] Breakdown by status (`open`, `closed`, `discarded` — or their equivalents in your CONTEXT).
  - [ ] Average satisfaction index for closed cases that have a recorded score.
- [ ] Print the summary to the console in a readable format: use separators, clear labels, and alignment. This is not a raw `print` of a dictionary.

### Results export

- [ ] At the end of execution, the script must ask the user (interactive input): `Export results to CSV? [y / n]`
- [ ] If the user chooses `y`, save the results to `results.csv` (one row per metric).
- [ ] If the user chooses `n`, the script exits without exporting.

### Validation against expected values

- [ ] Compare your script's results against the expected values stated in your CONTEXT. The totals must match exactly.

⚠️ **IMPORTANT:** Field names, categories, statuses, and expected values in your implementation must match exactly what is specified in your CONTEXT.md. A generic script that ignores your company's data structure will not be accepted.

---

## ✅ What We Will Evaluate

- [ ] The script accepts the CSV path as a command-line argument and works without modifying the code.
- [ ] Corrupt or invalid records are detected, classified, and shown in the summary with their type of problem.
- [ ] All five required metrics (total processed, by category, by status, corrupt records, satisfaction index) appear in the console output.
- [ ] The console format is readable: not a raw data dump. It includes separators, labels, and alignment.
- [ ] CSV export works correctly and produces a well-structured file.
- [ ] The script's results match the expected values in the CONTEXT.
- [ ] Code is organised into functions with clear responsibilities (loading, validation, analysis, output, export).

---

## 📦 How to Submit

1. Make sure your repository contains:
   - `analyze.py` — the analysis script.
   - `COMPANY-incidents.csv` — has been sent as an attachment (see `COMPANY-incidents.csv` in the project files).
   - A brief `README` in the project directory explaining how to run the script.
2. Push your branch and open a Pull Request to the original repository.
3. Make sure the PR includes a screenshot of the console output with the 100-row CSV.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
