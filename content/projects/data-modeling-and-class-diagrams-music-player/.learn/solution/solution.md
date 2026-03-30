# Data modeling and class diagrams – Solution

This document shows one possible **reference solution** for the project, using **Mermaid class diagrams** for both required exercises:

- A **music playlist player**.
- A **digital wallet** with transaction history.

The focus is on **clear entities, typed properties, and explicit relationships**, so that these diagrams could be implemented later in code or a database.

---

## 1. Music playlist player – Class diagram

### 1.1. Design overview

Key design decisions:

- A `User` can own multiple `Playlist` objects.
- Each `Playlist` contains many `PlaylistItem` elements, which:
  - Link a single `Song` to the playlist.
  - Store the **position** of the song inside the playlist.
  - Store when the song was **added**.
- A `Song` belongs to one `Album` and is performed by one `Artist` (this can be extended to many‑to‑many if needed).

This satisfies the requirement of **at least 5 models** with **typed properties** and clear relationships.

### 1.2. Mermaid diagram

```mermaid
classDiagram
    direction LR

    class User {
      +UUID id
      +String username
      +String email
      +String passwordHash
      +DateTime createdAt
      +Boolean isPremium
    }

    class Playlist {
      +UUID id
      +String name
      +String description
      +Boolean isPublic
      +DateTime createdAt
      +DateTime? updatedAt
    }

    class PlaylistItem {
      +UUID id
      +Int position
      +DateTime addedAt
    }

    class Song {
      +UUID id
      +String title
      +Int durationSeconds
      +DateTime releaseDate
      +String audioUrl
      +Boolean isExplicit
    }

    class Artist {
      +UUID id
      +String name
      +String country
      +DateTime? formedAt
      +String genre
    }

    class Album {
      +UUID id
      +String title
      +DateTime releaseDate
      +String coverImageUrl
      +String label
    }

    %% Ownership of playlists
    User "1" --> "0..*" Playlist : owns >

    %% Playlist content (many-to-many via PlaylistItem)
    Playlist "1" --> "1..*" PlaylistItem : has >
    Song "1" --> "0..*" PlaylistItem : appears_in >

    %% Artist–song relationship
    Artist "1" --> "0..*" Song : performs >

    %% Album–song relationship
    Album "1" --> "0..*" Song : contains >
```

---

## 2. Digital wallet – Class diagram

### 2.1. Design overview

Key design decisions:

- A `User` can own one or more `Wallet` instances (for example, "Personal", "Business").
- Each `Wallet` contains one or more `Account` objects, typically one per `Currency`.
- A `Transaction` represents a single movement of money (deposit, withdrawal, transfer) on an `Account`.
- `Currency` is modeled as a separate entity to centralize code, name, decimals, and symbol.

This satisfies the requirement of **at least 3 entities**, typed properties, and a **transaction history**.

### 2.2. Mermaid diagram

```mermaid
classDiagram
    direction LR

    class User {
      +UUID id
      +String fullName
      +String email
      +String passwordHash
      +DateTime createdAt
      +String country
    }

    class Wallet {
      +UUID id
      +String alias
      +DateTime createdAt
      +Boolean isActive
    }

    class Account {
      +UUID id
      +String accountNumber
      +Decimal balance
      +Boolean isPrimary
      +DateTime createdAt
    }

    class Transaction {
      +UUID id
      +DateTime executedAt
      +Decimal amount
      +String type      // "DEPOSIT" | "WITHDRAWAL" | "TRANSFER"
      +String status    // "PENDING" | "COMPLETED" | "FAILED"
      +String description
    }

    class Currency {
      +String code      // "USD", "EUR", "BTC"
      +String name
      +Int decimals
      +String symbol
    }

    %% User–wallet–account hierarchy
    User "1" --> "1..*" Wallet : owns >
    Wallet "1" --> "1..*" Account : contains >

    %% Account–transaction history
    Account "1" --> "0..*" Transaction : has_history >

    %% Currency associations
    Currency "1" --> "0..*" Account : denominated_in >
    Currency "1" --> "0..*" Transaction : in_currency >
```

---

## 3. How students can vary their solutions

Students do **not** have to match this solution exactly. Some acceptable variations include:

- Adding more properties (e.g. `lastLoginAt` on `User`, `favorite` flag on `Playlist`, fees on `Transaction`).
- Splitting concepts further (e.g. separate `Artist` and `Band`, or modeling `Transfer` as two `Transaction` records).
- Using slightly different data types where justified (e.g. using `BigDecimal` in strongly-typed languages for money).

What matters is that:

- All required entities are present.
- Every property has a **clear data type**.
- Relationships between entities are **explicit and coherent**.
- The diagrams could realistically guide an actual implementation.
