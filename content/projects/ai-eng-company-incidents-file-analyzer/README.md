# Incident Analyzer — Script and Control Panel

<!-- hide -->

By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

**Before you start:** Read your **[CONTEXT-company.md](https://github.com/4GeeksAcademy/ai-engineering-syllabus/tree/main/content/contexts/incidents-file-analysis)** before writing any code — it defines the exact CSV field names, valid categories, allowed statuses, and the expected output values your implementation must produce.

---

## 🎯 Your challenge

Your company's after-sales support department manages customer incidents: complaints, requests, operational failures. They've just prepared a CSV file with **100 records** extracted from their system — the first sample of a real data volume that could reach one million rows.

The problem is that **this file cannot be sent to an AI tool**. It contains sensitive customer information: personal identifiers, email addresses, contact details. The analysis must happen internally.

Your tech lead has decided to proceed in two phases. First, a Python script to quickly validate that the analysis process works correctly on the 100-record test file. If the output is correct, the script will be run on the full production file. Once the logic is confirmed solid, the functionality will be integrated into the platform your company is already building: a backend API and a web interface from which the team can upload the file, view the summary, and export the results.

> **Note from your tech lead:** _"Start with the script — we need to confirm that the validation logic and metric calculations are correct before building anything on top of them. Once the script works and the numbers match the expected values in the CONTEXT, move it into the API and build the interface. The end goal is that anyone on the team can upload the file from the browser, see the summary on screen, and download it as CSV without touching the terminal."_

### What counts as an incomplete or corrupt record?

Real-world data always has problems. For this project, a record is considered **invalid** if it is missing at least one of the required fields defined in your CONTEXT, or if it contains a value in a field that is not within the allowed set (statuses and categories). The logic must detect them, count them, and exclude them from the main analysis — but never silently ignore them.

---

## 🌱 How to Start the Project

1. Work in [**ai-engineering-company-project-monorepo**](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo). If you have not set it up yet, fork it, then open your fork in **GitHub Codespaces** or clone it locally:

   ```text
   https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo
   ```

2. Read your **CONTEXT-company.md** file before writing a single line of code. It defines the CSV structure, required fields, valid values, and the expected results your implementation must match.
3. Work inside the corresponding folders of the monorepo (see the submission section).

There is no starter code. The project starts from scratch.

---

## 💻 What You Need to Do

### Phase 1 — Analysis script (`/scripts`)

- [ ] Create the main script (`analyze.py`) that accepts the path to the CSV as a command-line argument: `python analyze.py incidents-COMPANY.csv`.
- [ ] The script must load and read the file (with native reading or pandas — your choice).
- [ ] Detect and count invalid records. Detail how many there are and why (missing field, out-of-range value, etc.).
- [ ] Calculate the following metrics on **valid records**:
  - [ ] Total number of elements processed (valid and invalid separately).
  - [ ] Breakdown by incident category.
  - [ ] Breakdown by status (`open`, `closed`, `discarded` — or their equivalents in your CONTEXT).
  - [ ] Average satisfaction index for closed cases that have a recorded score.
- [ ] Print the summary to the console in a readable format: use separators, clear labels, and alignment.
- [ ] At the end of execution, ask the user: `Export results to CSV? [y / n]`. If they choose `y`, save the results to `results.csv` (one row per metric).
- [ ] Verify that the results match exactly the expected values in your CONTEXT.

### Phase 2 — Integration into the platform

Once the script logic is validated, extract that same logic into reusable services and integrate it into the system.

**Backend (`/services/api`)**

- [ ] Create a `POST /api/incidents/analyze` endpoint that accepts a CSV file as `multipart/form-data`.
- [ ] The endpoint must run the same validation and analysis logic as the script and return the summary as JSON.
- [ ] Create a `GET /api/incidents/results/export` endpoint that returns the last analysis as a downloadable CSV.
- [ ] Errors (empty file, incorrect format) must return appropriate HTTP responses with a descriptive message.

**Frontend (`/uis/web`)**

- [ ] Create an incident analysis page accessible from the application menu.
- [ ] Include a file upload component (drag & drop or file selector) that sends the CSV to the API endpoint.
- [ ] Display the results summary on screen: general metrics, category breakdown, status breakdown, and satisfaction index.
- [ ] Include a button to download the results as CSV.
- [ ] Inform the user if the file contains invalid records and how many of each type.

⚠️ **IMPORTANT:** Field names, categories, statuses, and expected values in your implementation must match exactly what is specified in your CONTEXT.md. A generic implementation that ignores your company's context will not be accepted.

---

## ✅ What we will evaluate

### Script

- [ ] Accepts the CSV path as a command-line argument and works without modifying the code.
- [ ] Detects, classifies, and shows invalid records with their type of problem.
- [ ] All five required metrics appear in the console output with a readable format.
- [ ] CSV export works and produces a well-structured file.
- [ ] Results match exactly the expected values in the CONTEXT.

### Backend

- [ ] The analysis endpoint accepts the CSV, processes it, and returns the summary as JSON.
- [ ] The export endpoint returns a correctly formatted downloadable CSV.
- [ ] Input errors return appropriate HTTP status codes.

### Frontend

- [ ] The file can be uploaded from the interface without using the terminal.
- [ ] The summary is displayed on screen in a clear and interpretable way.
- [ ] The export button downloads the results CSV.
- [ ] Invalid records are communicated to the user in an understandable way.

### Cross-cutting

- [ ] The analysis and validation logic is the same in the script and the API — not duplicated but extracted into shared functions or modules.
- [ ] Code is organised according to the monorepo folder structure.

---

## 📦 How to submit this project

The project must be organised in the monorepo as follows:

```text
scripts/
  analyze.py              ← analysis script (Phase 1)
  incidents-COMPANY.csv   ← test file (attached, see CONTEXT)

services/
  api/                    ← backend with analysis and export endpoints

uis/
  web/                    ← web interface with file upload and visualisation
```

1. Push your branch with the structure above and open a Pull Request to the original repository.
2. Make sure the PR includes:
   - A screenshot of the script console output with the 100-row CSV.
   - A screenshot of the web interface with a loaded analysis visible on screen.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4GeeksAcademy](https://github.com/4GeeksAcademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
