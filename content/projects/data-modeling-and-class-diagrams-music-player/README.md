# Music Playlist Player — Object modeling

<!-- hide -->

By [@ehiber](https://github.com/ehiber) and [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Your Challenge

A startup is building a music streaming platform and needs to design the data layer before writing a single line of application code. You've been brought in as the engineer responsible for defining the object model — the blueprint that developers will use to implement the system.

The product lead has given you a brief description of what the platform needs to support:

> Users can create multiple playlists. Each playlist has a name and can contain many songs. Every song belongs to at least one album, and every album has an artist. Songs can appear in more than one playlist, but they always belong to a single album.

Your job is not to write code yet — it's to represent this system as a **class diagram** that clearly shows entities, their typed properties, and how they relate to each other. Think of it as the architectural drawing before construction begins.

A clean, well-reasoned model now saves days of refactoring later.

---

## 🌱 How to Start the Project

No code repository is needed for this project. Your entire work will happen inside the diagram tool.

1. Open [diagram.4geeks.com](https://diagram.4geeks.com/)
2. Create a new diagram for this exercise
3. Model your entities, add typed properties to each, and draw the relationships between them
4. When finished, export the result as a PNG file named `music-playlist-class-diagram.png`

---

## 💻 What You Need to Do

- [ ] Identify and create at least **5 models** (entities) for the system
- [ ] Add every property with its **explicit data type** (e.g. `name: string`, `duration: number`, `releaseDate: date`)
- [ ] Define and draw the **relationships** between all models clearly — specify which entities are connected and the nature of each relationship (one-to-one, one-to-many, many-to-many)
- [ ] Ensure the diagram is **readable and organized** — models should not overlap and relationships should be traceable
- [ ] Export the final diagram as **`music-playlist-class-diagram.png`**

> Note: You may include more than 5 models if the system you design requires it. Suggested starting point: `User`, `Playlist`, `Song`, `Album`, `Artist` — but feel free to name and structure them as you see fit.

---

## ✅ What We Will Evaluate

- [ ] The diagram contains at least 5 distinct models
- [ ] Every property across all models includes an explicit data type
- [ ] Relationships between models are present and correctly typed (one-to-many, many-to-many, etc.)
- [ ] The model accurately reflects the system described in the brief — the relationships make logical sense
- [ ] The diagram is visually clear and well organized
- [ ] The file is exported and named `music-playlist-class-diagram.png`

> Note: The specific tool used to produce the diagram is not evaluated — only the quality and correctness of the model itself.

---

## 📦 How to Submit

Submit your **`music-playlist-class-diagram.png`** file following your instructor's delivery instructions.

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/compare-programs) at [4Geeks Academy](https://4geeksacademy.com). By [@ehiber](https://github.com/ehiber) and [@marcogonzalo](https://github.com/marcogonzalo) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-syllabus/graphs/contributors). Find out more about [AI Engineering](https://4geeksacademy.com/en/coding-bootcamps/ai-engineering), [Data Science & Machine Learning](https://4geeksacademy.com/en/coding-bootcamps/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/coding-bootcamps/cybersecurity) and [Full-Stack Software Developer with AI](https://4geeksacademy.com/en/coding-bootcamps/full-stack-developer).
