# 2026-01-02 — 961. N-Repeated Element in Size 2N Array

Notes and approach for problem 961.
961. N-Repeated Element in Size 2N Array

Difficulty: Easy
Topic: Arrays, Hashing
Source: LeetCode

Problem Statement

You are given an integer array nums of size 2N containing N + 1 unique elements, where exactly one element is repeated N times.

Return the element that is repeated N times.

Key Observation

Since:

The array length is 2N

Only one element appears N times

All other elements appear exactly once

The repeated element must appear very frequently and early in the array.

Approach 1: Hash Set (Straightforward)
Idea

Traverse the array

Store seen elements in a set

The first element already present in the set is the answer

Why it works

The repeated element appears many times, so it will be detected quickly.

Algorithm

Initialize an empty set seen

For each element in nums:

If it exists in seen, return it

Otherwise, add it to seen

Time and Space Complexity
Metric	Complexity
Time	O(n)
Space	O(n)
Python Implementation
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

Alternative Insight (Interview Note)

Because the repeated element occurs N times in an array of size 2N, it is guaranteed that:

It will appear at least twice within a distance of at most 3 indices.

This allows for a constant-space solution by checking:

nums[i] == nums[i+1] or nums[i] == nums[i+2] or nums[i] == nums[i+3]


However, the hash-set approach is clearer and safer.

Key Takeaway

When one element dominates the frequency distribution, early detection using hashing is often the simplest and most reliable solution.