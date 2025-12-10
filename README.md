# 🎄 Advent of Code 2025 – Python Solutions

Solutions for **Advent of Code 2025** written in Python.
Each day lives in its own folder, with:

- `p1.py` – solution for Part 1
- `p2.py` – solution for Part 2

---

## 📅 Daily Overview

| Day | Title                | Summary                                                                   |
|-----|----------------------|---------------------------------------------------------------------------|
| 01  | Secret Entrance      | Simulate a circular dial and count how often position `0` is hit/passed. |
| 02  | Gift Shop            | Scan numeric ranges and sum numbers with repeated digit patterns.         |
| 03  | Lobby                | Pick digits from “banks” to form optimal numeric codes.                   |
| 04  | Printing Department  | Iteratively remove sparse `@` cells from a 2D grid until stable.          |
| 05  | Cafeteria            | Work with integer ranges: count covered IDs and merge overlaps.           |
| 06  | Trash Compactor      | Apply per-column `+` / `*` operations to numeric/ASCII digit columns.     |
| 07  | Laboratories         | Simulate falling, splitting signals through a grid of tiles.              |
| 08  | Playground           | Connect 3D junctions, form circuits, and track component merges.          |
| 09  | Movie Theater        | Find the maximum-area axis-aligned rectangle inside a polygon.            |
| 10  | Factory              | Use bitmasks and BFS to solve light toggling puzzles efficiently.         |

---

## 🔍 Day-by-Day Details

### Day 01: Secret Entrance

Simulate turning a **0–99 circular dial** left and right from a starting position.
While processing the instructions, count how often position `0` is **hit or passed**; use this to assemble a password.

---

### Day 02: Gift Shop

Scan **numeric ranges** and sum all numbers whose decimal representations are made from **repeated digit patterns**:

- Simple two-half repeats (like `123123`)
- More general patterns with arbitrary repetition periods

---

### Day 03: Lobby

Given rows of digits representing **“banks”**, choose digits in order to form the **best possible numeric codes**:

- Part 1: focus on **two-digit combinations**
- Part 2: build **fixed-length (12-digit)** maximum values

---

### Day 04: Printing Department

Work on a **2D grid of tiles**, repeatedly:

1. Identify cells with less than 4 neighboring `@` tiles
2. Remove those cells
3. Count how many are removed each round

Continue until the layout reaches a **stable configuration**.

---

### Day 05: Cafeteria

Process **inclusive integer ranges**:

- Count how many given IDs fall in any **“fresh” interval**
- Merge overlapping ranges and compute the **total size of the union**

---

### Day 06: Trash Compactor

Interpret:

- Columns of numbers
- Later, an **ASCII-art style multi-line digit display**

For each column/block, apply a specified operator (`+` or `*`) and compute a combined **checksum**.

---

### Day 07: Laboratories

Simulate a **signal** starting at the top of a grid:

- It falls downward, interacting with tiles
- On `^` tiles it may **split into multiple branches**
- Count both:
  - The number of **splits**
  - The total number of ways the signal can **reach the bottom**

---

### Day 08: Playground

Given coordinates of **junctions in 3D space**:

- Connect nearby pairs to form **circuits**
- Analyze the sizes of the resulting **components**
- Track the **final connection** that merges everything into one network

---

### Day 09: Movie Theater

Given **2D points** and an **axis-aligned polygon boundary**:

- Explore candidate rectangles
- Determine the **maximum-area axis-aligned rectangle** that fits entirely within the allowed region

---

### Day 10: Factory

For each line describing:

- A strip of **lights**
- Groups of **buttons** which toggle subsets of lights

Use **bitmasks** and **BFS** to find the **minimum number of button presses** needed to reach each target light pattern.

Part two may use an **optimized/compiled variant** for better performance.

---
