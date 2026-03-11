# Cinema Seat Manager

<!-- hide -->

By [@marcogonzalo](https://github.com/marcogonzalo) and [@ehiber](https://github.com/ehiber) and [other contributors](https://github.com/4GeeksAcademy/typescript-cinema-seat-manager/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_These instructions are [available in Spanish](./README.es.md)._

**Before you start**: 📗 [Read the instructions](https://4geeks.com/lesson/how-to-start-a-project) on how to start a coding project.

<!-- endhide -->

---

## 🎯 Challenge

A local independent cinema is opening a new screening room and has hired your team to build a simple digital seat reservation system. Right now, their staff tracks seat availability manually on paper grids, which causes confusion during busy showtimes and makes it hard to answer customer questions quickly.

The cinema manager explained the situation in your kickoff meeting: "We have a small theater with 8 rows and 10 seats per row. Customers call or visit the box office asking if seats are available, and they often want to sit together — especially couples looking for two adjacent seats. We need something simple where our staff can see which seats are taken, reserve seats for customers, and quickly find available spots."

Your team lead wants you to build a command-line prototype in TypeScript before investing in a full web interface. The cinema doesn't need fancy features yet — just a solid foundation that handles the core logic correctly. If this works well, they'll expand it later with online booking and seat selection maps.

### What makes a good seat reservation system?

The key challenge is **data representation**. You need to model the screening room as a two-dimensional structure where each position represents a seat with two states: occupied or available. Think of it like a grid or matrix where each seat has a row number and a column number.

In real reservation systems, this kind of matrix representation is common because it mirrors the physical layout of the space. Once you have the data structured correctly, the operations (reserving a seat, counting availability, finding adjacent seats) become straightforward.

---

## 🌱 How to Start the Project

1. Make sure you have a GitHub account at [https://github.com](https://github.com).

2. Use the template repository for TypeScript projects:

   ```text
   https://github.com/4GeeksAcademy/typescript-hello
   ```

3. You can start working in Codespaces (recommended) or clone the repository to work locally.

4. Create your own repository and update the remote URL to point to your repo instead of the template:

   ```bash
   git remote set-url origin <your-new-repository-url>
   ```

5. Start coding! Remember to commit frequently as you complete each feature.

📗 Detailed instructions: [How to start a coding project](https://4geeks.com/lesson/how-to-start-a-project)

---

## 💻 What You Need to Do

Build a TypeScript program that manages cinema seat reservations using arrays and functions.

### Core Functionality

- [ ] Create a function that initializes a seating matrix (a two-dimensional array) representing 8 rows and 10 columns
- [ ] Represent occupied seats with `1` and available seats with `0`
- [ ] Create a function that displays the current state of the screening room by printing the matrix to the console, using:
  - `X` for occupied seats
  - `L` for available seats
  - Include row and column numbers to make it easy to identify positions
- [ ] Implement a function to reserve a seat given a row number and a column number (mark it as occupied by changing its value from `0` to `1`)
- [ ] Add validation: the function should check if the seat is already occupied before reserving it, and return a message indicating success or failure
- [ ] Create a function that counts and returns how many seats are occupied and how many are available in the entire room

### Advanced Feature

- [ ] Implement a function that searches for two adjacent available seats (horizontally, in the same row) and returns their positions
- [ ] If multiple pairs of adjacent seats are found, return the first one
- [ ] If no adjacent seats are available, the function should indicate this clearly

### Testing & Output

- [ ] Test your program with different scenarios:
  - Empty room (all seats available)
  - Partially filled room
  - Nearly full room with only scattered single seats
  - Full room (no seats available)
- [ ] Make sure your code displays clear messages for each operation (reservation confirmed, seat already taken, adjacent seats found, etc.)
- [ ] Add comments explaining what each function does

### 🎁 Extra Challenge (Optional)

If you finish the core functionality and want to go further:

- [ ] Ask your AI assistant to generate a simple web interface for your seat manager using HTML and Tailwind and including your file. Provide your TypeScript code as context and ask it to create a visual seat map where users can click to reserve seats instead of using the console.

⚠️ **IMPORTANT:** Do not use objects or classes for this project. Represent the seating data using **a two-dimensional array only**. Use JSON format if you need to structure additional data (like reservation metadata).

---

## ✅ What We Will Evaluate

- [ ] Correct use of a two-dimensional array (matrix) to represent the cinema seating
- [ ] Proper implementation of functions with parameters and return values
- [ ] Correct use of conditional statements (`if`, `else`) to validate seat availability
- [ ] Correct use of loops (`for`, `while`) to process and display the seating matrix
- [ ] The search function correctly identifies adjacent available seats horizontally
- [ ] Code is readable with meaningful variable and function names
- [ ] The program runs without errors and produces the expected output when tested
- [ ] Console output is clear and helpful for the cinema staff using the system

> **Note:** The optional web interface is not part of the evaluation criteria. It's purely for your own learning and experimentation with AI tools.

---

## 📦 How to Submit

1. Push your completed code to your GitHub repository
2. Make sure your repository is public and accessible
3. Submit the repository link according to your instructor's guidelines

---

This and many other projects are built by students as part of the [Career Programs](https://4geeksacademy.com/) at 4Geeks Academy. By [@marcogonzalo](https://github.com/marcogonzalo) and [@ehiber](https://github.com/ehiber) and [other contributors](https://github.com/4GeeksAcademy/typescript-cinema-seat-manager/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack-developer), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
