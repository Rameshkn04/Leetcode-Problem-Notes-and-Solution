# 2026-01-03 — 1411. Number of Ways to Paint N × 3 Grid

Notes and approach for problem 1411.
1411. Number of Ways to Paint N × 3 Grid

Difficulty: Hard
Topic: Dynamic Programming
Source: LeetCode

Problem Statement

Given an integer n, count the number of ways to paint an n × 3 grid using 3 colors such that:

No two adjacent cells horizontally or vertically have the same color.

Return the answer modulo 10⁹ + 7.

Key Idea

Instead of tracking all color combinations, each row can be classified into two valid patterns:

Pattern A – Two Colors (ABA)

First and third cells have the same color.

Middle cell has a different color.

Valid combinations per row: 6

Pattern B – Three Colors (ABC)

All three cells have different colors.

Valid combinations per row: 6

This classification significantly reduces the state space.

Dynamic Programming Approach

Let:

a = number of ways to paint the current row using Pattern A

b = number of ways to paint the current row using Pattern B

Initialization

For the first row:

a = 6
b = 6

State Transition

For each new row:

new_a = 3a + 2b
new_b = 2a + 2b


These transitions ensure:

Vertical color constraints are maintained

Only valid pattern transitions are counted

All calculations are performed modulo 10⁹ + 7.

Final Answer

The total number of valid ways after n rows is:

a + b

Time and Space Complexity
Metric	Complexity
Time	O(n)
Space	O(1)
Python Implementation

class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        a, b = 6, 6
        
        for _ in range(1, n):
            new_a = (3 * a + 2 * b) % MOD
            new_b = (2 * a + 2 * b) % MOD
            a, b = new_a, new_b
        
        return (a + b) % MOD

Key Takeaway

By grouping row colorings into reusable patterns, we transform a combinatorial explosion into a simple, constant-space dynamic programming problem.

Commit Message Suggestion
[LeetCode] 1411 Number of Ways to Paint N×3 Grid – DP Pattern Optimization

