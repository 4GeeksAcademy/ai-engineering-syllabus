# Data modeling and class diagrams – Reference solution

This README describes the reference blueprint for the **"Data modeling and class diagrams"** project and links to the canonical solution document in the repository.

## Repository location of the main solution

The main explanatory solution file lives at:

- [Solution document](https://github.com/4GeeksAcademy/ai-engineering-syllabus/blob/main/content/projects/data-modeling-and-class-diagrams/.learn/solution/solution.md)

Use that file as the canonical reference when comparing or reviewing solutions.

## What the reference solution shows

- A **UML-style data model** for two independent systems, both expressed as **class diagrams**:
  - A **music playlist player** similar to Spotify, where users manage playlists that contain songs, artists, and albums.
  - A **digital wallet** similar to Wise, with multiple accounts, currencies, and a detailed transaction history.
- Clear use of:
  - **Entities (classes)** with meaningful names and responsibilities.
  - **Typed properties** on each class (e.g. `UUID`, `String`, `Int`, `Decimal`, `DateTime`, `Boolean`).
  - **Cardinalities/relationships** between classes, modeled explicitly.
- The diagrams are written in **Mermaid** so they can be rendered or reused in markdown-based tools.

## Diagrams covered in the solution

- **Music playlist player**:
  - Models `User`, `Playlist`, `PlaylistItem`, `Song`, `Artist`, and `Album`.
  - Uses an intermediate `PlaylistItem` class to represent the many‑to‑many relationship between playlists and songs, while also storing the **position** of each song and the **date it was added**.
  - Distinguishes between:
    - The **ownership** of playlists (user → playlists).
    - The **content** of playlists (playlists → playlist items → songs).
    - The **catalog** level information (artists and albums linked to songs).
- **Digital wallet**:
  - Models `User`, `Wallet`, `Account`, `Transaction`, and `Currency`.
  - Separates **wallets** from **accounts**, allowing a user to own multiple wallets, and each wallet to contain multiple currency-specific accounts.
  - Represents a **transaction history** with:
    - Timestamps, amounts, type (deposit, withdrawal, transfer) and status.
    - Explicit associations between transactions, accounts, and currencies.

## How to read and use the solution

- Treat `solution.md` as a **reference for structure and relationships**, not something students must copy literally:
  - Students can choose different names or additional fields as long as the **core relationships and types remain coherent**.
  - The important part is that they show a **clear model** that could be implemented later in code or a database.
- When evaluating a student implementation, check whether:
  - Both diagrams (**music playlist player** and **digital wallet**) exist.
  - Each entity includes **typed properties** (not just names without data types).
  - Relationships and cardinalities between entities are clearly expressed.
  - The overall modeling choices are **consistent and realistic** for the described systems.
