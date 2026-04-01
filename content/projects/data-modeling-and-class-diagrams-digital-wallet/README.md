# Digital Wallet — Object Modeling

<!-- hide -->

By [@ehiber](https://github.com/ehiber) and [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your Challenge

A fintech company is building a digital wallet product — think Wise, Revolut, or a similar service — and needs its data model designed before development begins. You've been assigned to map out the core entities the system will need to operate.

The engineering lead has shared a brief summary of requirements:

> A user can own one or more wallets. Each wallet holds a balance in a specific currency. Users can send and receive money, and every movement of funds is recorded as a transaction. A transaction always has a source, a destination, an amount, a currency, a timestamp, and a status (such as pending, completed, or failed).

Your deliverable is a **class diagram** that accurately represents these entities, their typed properties, and the relationships between them. This model will be used by the development team as the reference for implementation — clarity and precision matter.

Think carefully about what a transaction connects, and how currency fits into the picture.

---

## 🌱 How to Start the Project

No code repository is needed for this project. Your entire work happens inside the diagram tool.

1. Open [diagram.4geeks.com](https://diagram.4geeks.com/)
2. Create a new diagram for this exercise
3. Model your entities, add typed properties to each, and draw the relationships between them
4. When finished, export the result as a PNG file named `digital-wallet-class-diagram.png`

---

## 💻 What You Need to Do

- [ ] Identify and create at least **3 models** (entities) for the system
- [ ] Add every property with its **explicit data type** (e.g. `balance: float`, `status: string`, `createdAt: date`)
- [ ] Define and draw the **relationships** between all models clearly — specify which entities are connected and the nature of each relationship
- [ ] Ensure the diagram is **readable and organized** — models should not overlap and relationships should be traceable
- [ ] Export the final diagram as **`digital-wallet-class-diagram.png`**

> Note: You may include more than 3 models if your design requires it. Suggested starting point: `User`, `Wallet`, `Transaction`, `Currency` — but feel free to name and structure them as you see fit.

---

## ✅ What We Will Evaluate

- [ ] The diagram contains at least 3 distinct models
- [ ] Every property across all models includes an explicit data type
- [ ] Relationships between models are present and clearly defined
- [ ] The model accurately reflects the system described in the brief — particularly the transaction structure and how wallets relate to users and currency
- [ ] The diagram is visually clear and well organized
- [ ] The file is exported and named `digital-wallet-class-diagram.png`

> Note: The specific tool used to produce the diagram is not evaluated — only the quality and correctness of the model itself.

---

## 📦 How to Submit

Submit your **`digital-wallet-class-diagram.png`** file following your instructor's delivery instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@ehiber](https://github.com/ehiber) and [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
