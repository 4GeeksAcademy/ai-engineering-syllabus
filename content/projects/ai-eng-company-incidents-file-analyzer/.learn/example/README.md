# In-Class Example: Bookstore Inventory Audit

> **Instructor note:** This is a classroom example to introduce the concepts of the *Incident Analyzer* project using a simpler domain. It covers the same stack and patterns (CSV analysis script with validation and metrics, shared logic, REST API for file upload, web UI) but is scoped to a 1–2 hour live session. Do NOT share this file with students before they attempt the main project.

---

## The scenario

A small independent bookstore has exported its current inventory as a CSV file with 25 records. Before importing this data into the store's new management system, the team needs to validate it and generate a quick summary: how many books are in each genre, what is the average price by status, and how many records have problems.

The analysis must run locally — the file contains cost prices that cannot be sent to an external tool.

The process has two phases: first a quick Python script to confirm the logic works, then integrate that same logic into a small web tool so any staff member can run the audit from the browser.

---

## Phase 1 — Analysis script (`analyze.py`)

### Sample CSV

Save this as `books.csv` to use during the session:

```csv
isbn,title,genre,price,stock,status
978-0-06-112008-4,To Kill a Mockingbird,fiction,12.99,5,available
978-0-7432-7356-5,The Great Gatsby,fiction,10.50,3,available
978-0-14-028329-7,Of Mice and Men,fiction,9.99,0,out_of_stock
978-0-39-474673-7,,non-fiction,24.99,2,available
978-0-06-093546-9,Thinking Fast and Slow,non-fiction,18.00,7,available
978-0-14-303943-3,The Odyssey,fiction,11.25,1,available
978-0-19-953556-4,Oxford English Dictionary,reference,45.00,1,available
978-1-40-881274-1,Harry Potter 1,children,14.99,12,available
978-1-40-881275-8,Harry Potter 2,children,14.99,8,available
978-0-14-028726-7,Animal Farm,fiction,8.50,4,available
978-0-14-044913-6,The Alchemist,fiction,-3.00,2,available
978-0-374-52804-1,Sapiens,non-fiction,19.99,0,out_of_stock
978-0-06-192028-5,Quiet,non-fiction,16.50,5,available
978-0-385-33348-1,The Giver,children,11.00,6,available
978-0-06-093548-3,Atomic Habits,non_fiction,17.99,10,available
978-0-7432-7357-2,1984,fiction,10.00,3,damaged
978-0-14-028727-4,Lord of the Flies,,9.25,2,available
978-0-374-52805-8,Educated,non-fiction,20.00,4,available
978-0-316-76948-0,The Catcher in the Rye,fiction,10.75,1,available
978-1-50-117606-0,Dune,fiction,15.00,9,available
978-0-06-112009-1,Brave New World,fiction,11.50,2,available
978-0-14-028728-1,The Road,fiction,12.00,0,out_of_stock
978-0-375-70737-9,The Kite Runner,fiction,13.50,5,available
978-0-06-093547-6,Outliers,non-fiction,,3,available
978-0-385-47423-1,Ender's Game,comics,13.00,2,available
```

### What to implement

- [ ] The script accepts the CSV path as a command-line argument: `python analyze.py books.csv`
- [ ] Load and read the file (native `csv` module or `pandas` — your choice)
- [ ] Detect and count **invalid records**. A record is invalid if:
  - `title` is missing
  - `genre` is not one of: `fiction`, `non-fiction`, `children`, `reference`, `comics`
  - `price` is missing or negative
  - `status` is not one of: `available`, `out_of_stock`, `damaged`
- [ ] Calculate the following metrics on **valid records only**:
  - Total valid vs. invalid records
  - Count of books by `genre`
  - Count of books by `status`
  - Average `price` for `available` books
- [ ] Print the summary to the console with clear labels and separators
- [ ] At the end, ask: `Export results to CSV? [y/n]`. If `y`, save to `results.csv`

**Expected output (approximate):**

```
=== Bookstore Inventory Audit ===
Total records: 25
Valid: 21 | Invalid: 4

-- By genre --
fiction       : 12
non-fiction   :  5
children      :  3
reference     :  1
comics        :  0

-- By status --
available     : 16
out_of_stock  :  3
damaged       :  2

-- Pricing --
Avg price (available): $14.12

-- Invalid records --
Row 4  : missing title
Row 11 : negative price (-3.00)
Row 15 : invalid genre (non_fiction)
Row 17 : missing genre
Row 24 : missing price
```

---

## Phase 2 — Integration (FastAPI + Next.js)

Once the script logic is validated, extract the validation and metrics into shared functions.

**Backend:**

- [ ] `POST /api/books/analyze` — accepts a CSV as `multipart/form-data`, runs the same logic, returns the summary as JSON
- [ ] `GET /api/books/results/export` — returns the last analysis as a downloadable CSV
- [ ] Empty file or wrong format returns `400` with a descriptive message

**Frontend:**

- [ ] File upload component (file selector or drag & drop) that sends the CSV to the API
- [ ] Display the results on screen: totals, genre breakdown, status breakdown, average price
- [ ] A button to download the results CSV
- [ ] Inform the user how many invalid records were found and why

**Shared logic:**

- [ ] The validation and metrics functions are the same in the script and the API — extracted to a shared module, not duplicated

---

## Discussion questions

1. The script detects `non_fiction` (with underscore) as an invalid genre, even though the intent is clear. Should the script auto-correct obvious typos like this, or always reject them? What are the trade-offs?
2. If the store uploads a CSV with 500 records and the API endpoint times out halfway through, what should the response look like? How would you communicate partial results to the user?
3. Why is it important that the analysis and validation logic is extracted to a shared module instead of being copied into the API? What breaks if you let them diverge?
