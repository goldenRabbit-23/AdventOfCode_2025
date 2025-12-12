# 🎄 Advent of Code 2025 – Python Solutions

Solutions for **Advent of Code 2025** written in Python.
Each day lives in its own folder, with:

- `p1.py` – solution for Part 1
- `p2.py` – solution for Part 2

---

## 📅 Daily Overview

| Day | Title                | Summary |
|-----|----------------------|---------|
| 01  | Secret Entrance      | Simulate a 0–99 safe dial and count how often it lands on 0, then how often any click hits 0. |
| 02  | Gift Shop            | Scan product ID ranges and sum IDs whose digits are made from repeated patterns. |
| 03  | Lobby                | From each digit bank, pick batteries to form the largest possible 2-digit and 12-digit values. |
| 04  | Printing Department  | On a 2D `@`/`.` grid, find sparsely surrounded rolls, then iteratively remove them until stable. |
| 05  | Cafeteria            | Work with fresh ID ranges: count which given IDs are fresh, then merge ranges and count all fresh IDs. |
| 06  | Trash Compactor      | Parse column-based math problems and sum per-problem `+`/`*` results, then reinterpret them as right-to-left column numbers. |
| 07  | Laboratories         | Simulate falling tachyon beams through splitters to count splits and total quantum timelines. |
| 08  | Playground           | Connect nearest 3D junctions with union–find to size circuits and track the final joining pair. |
| 09  | Movie Theater        | Use red tiles as opposite rectangle corners; then restrict rectangles to stay inside a red/green loop. |
| 10  | Factory              | Use bitmasks and BFS for light toggling, then solve a minimal-press integer system for jolt counters. |
| 11  | Reactor              | Traverse a directed graph of devices to count paths from start to output, then calculate paths that must visit specific intermediate nodes. |
| 12  | Christmas Tree Farm  | For each rectangular region, determine whether it can fit all presents while satisfying the required counts. |

---

## 🔍 Day-by-Day Details

### Day 01: Secret Entrance

You’re given a sequence of rotations for a circular safe dial labeled `0`–`99`, starting at `50`. Each instruction rotates left (`L`) or right (`R`), wrapping around modulo 100.

**Part 1 – Counting zero endpoints**

- Simulate all rotations on the dial.
- Count how many times the **final position** after a rotation is exactly `0`.

**Part 2 – Counting all zero clicks**

- Now count every **individual click** that lands on `0`, not just the final position.
- Use arithmetic on distances to the next `0` and full revolutions instead of simulating each click.

---

### Day 02: Gift Shop

You’re given inclusive integer ranges of product IDs. Some IDs are “invalid” if their decimal representation consists of repeated digit patterns.

**Part 1 – Two-block repeated IDs**

- An ID is invalid if its digits are exactly **two copies** of the same block (like `123123`).
- Scan each range, detect these two-block repeats, and sum all such IDs.

**Part 2 – Arbitrary-period repeated IDs**

- Generalize the rule: the digits must be **k ≥ 2 repetitions** of some shorter pattern.
- For each ID, try pattern lengths that evenly divide the total length and sum all IDs that match.

---

### Day 03: Lobby

Each line is a “bank” of digits (batteries). You choose some of them (in order) to form the largest possible number under different length constraints, then sum across all banks.

**Part 1 – Best 2-digit output**

- From each bank, choose exactly **two digits** (in order) to maximize the resulting 2-digit number.
- Use a single pass per bank to track the best possible pair.

**Part 2 – Best 12-digit output**

- From each bank, choose exactly **12 digits** (in order) to maximize the 12-digit number.
- Use a DP approach to decide which digits to keep or skip, then sum the best numbers.

---

### Day 04: Printing Department

You get a 2D grid of `@` (paper rolls) and `.` (empty). Rolls are “accessible” if they have fewer than four neighboring rolls in the eight surrounding cells.

**Part 1 – Immediately accessible rolls**

- For each `@`, count neighboring `@` cells.
- Count how many rolls have **< 4 neighbors**, i.e. are directly accessible.

**Part 2 – Cascading roll removal**

- Repeatedly remove all accessible `@` rolls in rounds.
- Keep going until no more rolls qualify; count how many total rolls were removed.

---

### Day 05: Cafeteria

The input is split into a section of inclusive fresh ID ranges and a section of available IDs.

**Part 1 – Freshness of given IDs**

- For each available ID, check whether it falls into **any** fresh range.
- Count how many available IDs are fresh.

**Part 2 – Size of the fresh ID universe**

- Ignore the available IDs and just consider the ranges.
- Merge overlapping ranges and count how many distinct IDs are covered by their union.

---

### Day 06: Trash Compactor

You’re given a horizontally laid-out worksheet of column-based math problems (`+` or `*`) and must sum all problem results.

**Part 1 – Standard column problems**

- Interpret each problem as a column of regular integers plus an operator.
- Group numbers by problem and apply `+` or `*`, then sum all results.

**Part 2 – Cephalopod right-to-left math**

- Reinterpret the worksheet so that each **vertical column** within a block is one number, with digits top-to-bottom.
- Split the grid into contiguous non-empty column blocks, extract the column-numbers for each block, apply the operator, and sum the results.

---

### Day 07: Laboratories

You simulate tachyon beams falling through a grid with a start `S`, empty space `.`, and splitters `^`.

**Part 1 – Classical beam splits**

- A classical beam falls straight down.
- When it hits `^`, the current beam stops and splits into two new beams (down-left and down-right); count each such split.

**Part 2 – Quantum timeline counts**

- A single quantum particle branches into all possible paths at each splitter.
- Track how many ways each cell can be reached and sum the counts on the bottom row to get the number of timelines.

---

### Day 08: Playground

You have many junction boxes in 3D (`X,Y,Z`) and want to connect them with strings of lights, always choosing the closest pairs first.

**Part 1 – First 1000 nearest connections**

- Compute all squared pairwise distances.
- Connect the **1000 closest pairs** using union–find, then take the sizes of the three largest resulting components and multiply them.

**Part 2 – Final connection to unify the network**

- Continue connecting closest pairs until everything is in one connected component.
- Record the last pair of junctions that actually merges two components and return the product of their X-coordinates.

---

### Day 09: Movie Theater

You’re given positions of red tiles in a grid and want rectangles whose opposite corners are red.

**Part 1 – Maximum red-corner rectangle**

- For every pair of red tiles, treat them as opposite corners of an axis-aligned rectangle.
- Compute its area and take the maximum over all pairs.

**Part 2 – Largest rectangle inside the red/green loop**

- Red tiles form a closed, axis-aligned loop with green tiles along edges and inside.
- Only consider rectangles that use red corners and lie completely inside (or on) that loop; pick the one with the largest area.

---

### Day 10: Factory

Each machine has indicator lights, buttons, and joltage counters. Buttons either toggle lights (Part 1) or increment counters (Part 2).

**Part 1 – Indicator lights**

- Lights start all off, and buttons toggle specified subsets of lights.
- Model states as bitmasks and use BFS over configurations to find the minimum number of button presses that reaches the target pattern.

**Part 2 – Joltage counters**

- Ignore lights; counters start at zero, and each button adds `+1` to certain counters.
- Form an integer system specifying how many times to press each button to hit all target jolts, and use an optimizer to find the solution with minimal total presses.

---

### Day 11: Reactor

You receive a list of devices and the other devices they feed data into, forming a DAG.

**Part 1 – Paths from `you` to `out`**

- Start at the device labeled `you` and find every possible path to the reactor `out`.
- Use DFS with memoization to efficiently sum the path counts, as the total number of paths can be exponential.

**Part 2 – Paths via `dac` and `fft`**

- Find paths from `svr` to `out` that are required to pass through both `dac` and `fft`.
- Because the graph is acyclic, the nodes must be visited in a linear order (e.g., `svr` → `dac` → `fft` → `out`); calculate path counts for each segment independently and multiply them.

---

### Day 12: Christmas Tree Farm

You’re given a set of 3x3 present shapes and a list of rectangular regions, each with required counts; determine which regions can fit all presents without overlap (allowing rotations/flips and using holes).

**Part 1 - Count regions that can fit the required presents**

- For each region, compute total presents `n` and total area `W * H`.
- Using the fixed per-shape diagram footprint `f`, count the region where `n * f <= W * H`.

---
