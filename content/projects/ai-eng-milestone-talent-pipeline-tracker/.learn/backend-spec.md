# Backend Mock API — Technical Specifications

## Candidate Management (Recruitment Module)

---

## Base URL

```text
/api/v1
```

---

## Main Resource: `/records`

---

### `GET /records`

Lists all records. Supports optional filters.

**Optional query params:**

| Param    | Type   | Accepted values                                                                     |
| -------- | ------ | ----------------------------------------------------------------------------------- |
| `status` | string | `received`, `in_progress`, `selected`, `discarded`                                  |
| `stage`  | string | `pending`, `review`, `personal_interview`, `technical_interview`, `offer_presented` |
| `search` | string | Searches in `full_name` or `email`                                                  |
| `page`   | number | Default: `1`                                                                        |
| `limit`  | number | Default: `20`                                                                       |

**Response 200:**

```json
{
  "data": [
    {
      "id": "uuid",
      "full_name": "string",
      "email": "string",
      "phone": "string",
      "position": "string",
      "status": "received | in_progress | selected | discarded",
      "stage": "pending | review | personal_interview | technical_interview | offer_presented",
      "applied_at": "ISO string",
      "updated_at": "ISO string"
    }
  ],
  "meta": {
    "total": 100,
    "page": 1,
    "limit": 20,
    "total_pages": 5
  }
}
```

---

### `GET /records/:id`

Full details of a record.

**Response 200:**

```json
{
  "id": "uuid",
  "full_name": "string",
  "email": "string",
  "phone": "string",
  "position": "string",
  "linkedin_url": "string | null",
  "cv_url": "string | null",
  "status": "received | in_progress | selected | discarded",
  "stage": "pending | review | personal_interview | technical_interview | offer_presented",
  "experience_years": "number",
  "notes_count": "number",
  "applied_at": "ISO string",
  "updated_at": "ISO string"
}
```

**Response 404:**

```json
{
  "error": "Record not found"
}
```

---

### `POST /records`

Registers a new record.

**Request body:**

```json
{
  "full_name": "string", // required
  "email": "string", // required
  "phone": "string", // required
  "position": "string", // required
  "linkedin_url": "string", // optional
  "cv_url": "string", // optional
  "experience_years": "number" // required
}
```

**Response 201:**

```json
{
  "id": "uuid",
  "full_name": "string",
  "email": "string",
  "phone": "string",
  "position": "string",
  "linkedin_url": "string | null",
  "cv_url": "string | null",
  "status": "received",
  "stage": "pending",
  "experience_years": "number",
  "notes_count": 0,
  "applied_at": "ISO string",
  "updated_at": "ISO string"
}
```

**Response 422:**

```json
{
  "error": "Validation error",
  "details": {
    "field": "message"
  }
}
```

---

### `PUT /records/:id`

Replaces the editable data of a record. Does not modify `status` or `stage`.

**Request body:**

```json
{
  "full_name": "string", // required
  "email": "string", // required
  "phone": "string", // required
  "position": "string", // required
  "linkedin_url": "string", // optional
  "cv_url": "string", // optional
  "experience_years": "number" // required
}
```

**Response 200:** Same structure as `GET /records/:id`

**Response 404:**

```json
{
  "error": "Record not found"
}
```

---

### `PATCH /records/:id`

Partially modifies the `status` or `stage`. Accepts one or both fields.

**Request body:**

```json
{
  "status": "received | in_progress | selected | discarded", // optional
  "stage": "pending | review | personal_interview | technical_interview | offer_presented" // optional
}
```

**Response 200:** Same structure as `GET /records/:id`

**Response 400:**

```json
{
  "error": "At least one field (status or stage) is required"
}
```

**Response 422:**

```json
{
  "error": "Invalid value",
  "details": {
    "status": "Must be one of: received, in_progress, selected, discarded"
  }
}
```

---

### `DELETE /records/:id`

Deletes a record and all associated notes.

**Response 204:** no body

**Response 404:**

```json
{
  "error": "Record not found"
}
```

---

## Subresource: `/records/:id/notes`

---

### `GET /records/:id/notes`

Lists all notes for a record.

**Response 200:**

```json
{
  "data": [
    {
      "id": "uuid",
      "record_id": "uuid",
      "content": "string",
      "created_at": "ISO string"
    }
  ],
  "meta": {
    "total": "number"
  }
}
```

---

### `POST /records/:id/notes`

Adds a note to a record.

**Request body:**

```json
{
  "content": "string" // required, minimum 1 character
}
```

**Response 201:**

```json
{
  "id": "uuid",
  "record_id": "uuid",
  "content": "string",
  "created_at": "ISO string"
}
```

**Response 422:**

```json
{
  "error": "Validation error",
  "details": {
    "content": "Content is required"
  }
}
```

---

### `DELETE /records/:id/notes/:note_id`

Deletes a specific note.

**Response 204:** no body

**Response 404:**

```json
{
  "error": "Note not found"
}
```

---

## Endpoint Summary

| Method   | Endpoint                      | Action                     |
| -------- | ----------------------------- | -------------------------- |
| `GET`    | `/records`                    | List records               |
| `GET`    | `/records/:id`                | View record details        |
| `POST`   | `/records`                    | Create a new record        |
| `PUT`    | `/records/:id`                | Edit all data of a record  |
| `PATCH`  | `/records/:id`                | Change `status` or `stage` |
| `DELETE` | `/records/:id`                | Delete record              |
| `GET`    | `/records/:id/notes`          | List notes for a record    |
| `POST`   | `/records/:id/notes`          | Create note for a record   |
| `DELETE` | `/records/:id/notes/:note_id` | Delete specific note       |

---

## Valid Values

### `status`

| Value         | Description                          |
| ------------- | ------------------------------------ |
| `received`    | Application received (initial state) |
| `in_progress` | Under evaluation                     |
| `selected`    | Candidate selected                   |
| `discarded`   | Candidate discarded                  |

### `stage`

| Value                 | Description                   |
| --------------------- | ----------------------------- |
| `pending`             | Not processed (initial state) |
| `review`              | Under review (initial stage)  |
| `personal_interview`  | Personal interview            |
| `technical_interview` | Technical interview           |
| `offer_presented`     | Offer presented               |

---

## Suggested Mock Data

The backend must generate at least **30 records** realistically distributed:

### `status` distribution

| Status        | Suggested % |
| ------------- | ----------- |
| `received`    | 40%         |
| `in_progress` | 35%         |
| `selected`    | 10%         |
| `discarded`   | 15%         |

### `stage` distribution

| Stage                 | Suggested % |
| --------------------- | ----------- |
| `review`              | 40%         |
| `personal_interview`  | 30%         |
| `technical_interview` | 20%         |
| `offer_presented`     | 10%         |

---

## Expected Mock Behavior

- All endpoints must always return data even if the backend does not persist any data between restarts.
- `POST`, `PUT`, `PATCH`, and `DELETE` must simulate success by returning the documented responses.
- Errors `404` and `422` must be triggered properly when the ID does not exist or the request body is invalid.
- Filters on `GET /records` must operate on the mock data in memory.
