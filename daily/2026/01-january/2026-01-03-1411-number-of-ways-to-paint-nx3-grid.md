# 2026-01-03 — 1411. Number of Ways to Paint N × 3 Grid

Difficulty: Hard  
Topic: Dynamic Programming  
Source: [LeetCode 1411](https://leetcode.com/problems/number-of-ways-to-paint-n-x-3-grid)

Problem
-------
Given an integer n, count the number of ways to paint an n × 3 grid using 3 colors such that no two adjacent cells (horizontally or vertically) have the same color. Return the answer modulo 10^9 + 7.

Overview / Key idea
-------------------
Instead of enumerating all possible colorings of rows and tracking every color, we group valid row colorings into two pattern types. This reduces the state space and makes transitions between rows simple.

Row pattern types (for a single row of length 3 with colors from {A,B,C}):

- Pattern A — "ABA": first and third cells have the same color, middle cell is different.  
  Count per row: 3 (choices for the repeated color) × 2 (choice for the middle) = 6.

- Pattern B — "ABC": all three cells have different colors.  
  Count per row: 3 × 2 × 1 = 6.

Let:
- a = number of valid colorings of the current row that are Pattern A,
- b = number of valid colorings of the current row that are Pattern B.

Initialization
--------------
For the first row:
- a = 6
- b = 6

Transition between rows
-----------------------
We want formulas to compute (new_a, new_b) from (a, b) where new_a/new_b are counts for the next row.

For a fixed previous-row pattern, count how many next-row patterns of each type are allowed by the vertical constraints. The well-known per-pattern counts are:

- If previous row is Pattern A (colors x y x):
  - Possible next rows of type A: 3
  - Possible next rows of type B: 2

- If previous row is Pattern B (colors x y z, all distinct):
  - Possible next rows of type A: 2
  - Possible next rows of type B: 2

Thus, aggregating over all previous rows:
- new_a = 3 * a + 2 * b
- new_b = 2 * a + 2 * b

(Each coefficient counts how many next-row patterns of the given type are valid for a single fixed previous-row pattern.)

Algorithm
---------
Start with a = 6 and b = 6. Repeat the transition n-1 times (since the first row is already counted). Work modulo MOD = 10^9 + 7.

Final answer = (a + b) % MOD

Example
-------
- n = 1 -> a + b = 6 + 6 = 12
- n = 2 -> after one transition:
  - new_a = 3*6 + 2*6 = 30
  - new_b = 2*6 + 2*6 = 24
  - total = 54

Complexity
----------
- Time: O(n) — one constant-time update per row.
- Space: O(1) — only two counters a and b are maintained.

Python implementation
---------------------
```python
class Solution:
    def numOfWays(self, n: int) -> int:
        """
        Return the number of ways to paint an n x 3 grid with 3 colors
        such that no adjacent cells share the same color.
        """
        MOD = 10**9 + 7
        a, b = 6, 6  # counts for patterns A and B on the first row
        for _ in range(1, n):
            new_a = (3 * a + 2 * b) % MOD
            new_b = (2 * a + 2 * b) % MOD
            a, b = new_a, new_b
        return (a + b) % MOD
```

Key takeaway
------------
Grouping row colorings into a small set of reusable patterns (Pattern A and Pattern B) turns an exponential counting problem into a simple constant-space dynamic programming solution with a 2×2 transition structure.

Commit message suggestion
-------------------------
[LeetCode] 1411 Number of Ways to Paint N×3 Grid — DP with pattern classification