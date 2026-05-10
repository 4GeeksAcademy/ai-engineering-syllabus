> **In-class example for instructors.** Use this scenario to introduce class diagrams with 5+ models in a ~1-hour session. This file is a teaching aid with a *different domain* than the assigned project. Do not share this with students as their project brief.

# Podcast Platform — Object Modeling (In-Class Example)

## Scenario

A startup is building a podcast streaming app. Before any code is written, the team needs a clear data model. The product lead sent this description:

> Users can subscribe to multiple podcasts. Each podcast is organized into seasons, and each season contains many episodes. An episode always belongs to exactly one season. Users can also bookmark individual episodes to listen to later. A podcast has a title, a host name, and a category (e.g. Technology, True Crime, Comedy). An episode has a title, duration in seconds, a publication date, and an audio URL.

Your task is to represent this system as a **class diagram** that shows entities, typed properties, and all relationships — including the nature of each (one-to-one, one-to-many, many-to-many).

---

## What to Model

### Suggested Entities

| Model | Description |
|-------|-------------|
| `User` | A registered listener on the platform |
| `Podcast` | A show with a title, host, and category |
| `Season` | A numbered collection of episodes within a podcast |
| `Episode` | A single audio file belonging to a season |
| `Bookmark` | A saved reference linking a user to a specific episode |

### Sample Typed Properties

| Model | Property | Type |
|-------|----------|------|
| `User` | `id` | `int` |
| `User` | `username` | `string` |
| `User` | `email` | `string` |
| `Podcast` | `id` | `int` |
| `Podcast` | `title` | `string` |
| `Podcast` | `hostName` | `string` |
| `Podcast` | `category` | `string` |
| `Season` | `id` | `int` |
| `Season` | `number` | `int` |
| `Season` | `releaseYear` | `int` |
| `Episode` | `id` | `int` |
| `Episode` | `title` | `string` |
| `Episode` | `durationSeconds` | `int` |
| `Episode` | `publishedAt` | `date` |
| `Episode` | `audioUrl` | `string` |
| `Bookmark` | `id` | `int` |
| `Bookmark` | `createdAt` | `date` |

### Relationships to Draw

| From | To | Type | Note |
|------|----|------|------|
| `User` | `Podcast` | many-to-many | A user subscribes to many podcasts; a podcast has many subscribers |
| `Podcast` | `Season` | one-to-many | A podcast has many seasons |
| `Season` | `Episode` | one-to-many | A season has many episodes |
| `User` | `Episode` | many-to-many via `Bookmark` | Bookmarks link users to episodes |

---

## Checklist

- [ ] Create at least **5 models** in the diagram tool
- [ ] Add every property with its **explicit data type**
- [ ] Draw **relationships** and label each with its cardinality (1:1, 1:N, N:M)
- [ ] Include at least **one many-to-many relationship**
- [ ] Ensure the diagram is **readable** — no overlapping boxes, traceable arrows
- [ ] Export the result as **`podcast-platform-class-diagram.png`**

**Tool:** [diagram.4geeks.com](https://diagram.4geeks.com/)

---

## Discussion Questions

1. The `User–Podcast` relationship is many-to-many (subscriptions). How would you model the intermediate table if you needed to store the subscription date and whether notifications are enabled?
2. `Episode` belongs to one `Season`, and a `Season` belongs to one `Podcast`. Does an `Episode` need a direct relationship to `Podcast`, or is the indirect path through `Season` enough? When would a direct shortcut matter?
3. Compare the `Bookmark` model (User ↔ Episode) with a simple array of episode IDs stored on the `User` model. What do you gain and lose with each approach?
