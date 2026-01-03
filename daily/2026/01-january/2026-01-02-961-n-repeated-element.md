# 2026-01-02 — 961. N-Repeated Element in Size 2N Array

Difficulty: Easy  
Topics: Arrays, Hashing  
Source: LeetCode

## Problem

Given an integer array `nums` of length `2N` that contains `N + 1` unique elements, exactly one element is repeated `N` times while every other element appears once. Return the value that is repeated `N` times.

Example:
- Input: `[1,2,3,3]`  
  Output: `3`

## Key observation

- The array length is `2N`. One element appears `N` times and every other element appears once.
- Because the repeated element occupies half of the array, it is very likely to appear early and within a small distance of any of its other occurrences.
- This allows either an O(n) time + O(n) space solution (clear and safe) or an O(n) time + O(1) space solution (using a small fixed-distance check).

---

## Approach 1 — Hash set (clear and reliable)

Idea:
- Traverse the array and keep a set of seen values.
- The first element encountered that is already in the set must be the repeated element.

Algorithm:
1. Initialize an empty set `seen`.
2. For each `num` in `nums`:
   - If `num` is in `seen`, return `num`.
   - Otherwise add `num` to `seen`.

Complexity:
- Time: O(n)
- Space: O(n)

Python implementation:
```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        # Problem guarantees an answer exists, so no explicit fallback needed.
```

---

## Approach 2 — Constant space (O(1) extra space)

Insight:
- Because the repeated element appears N times in an array of length 2N, there must be at least two occurrences within distance 1, 2, or 3 from each other. That is, for some index `i`:
  - `nums[i] == nums[i+1]` OR
  - `nums[i] == nums[i+2]` OR
  - `nums[i] == nums[i+3]`.
- Checking these small fixed offsets while scanning yields O(n) time and O(1) extra space.

Algorithm:
1. For each valid index `i` (0 <= i < len(nums) - 1):
   - If `nums[i] == nums[i+1]`, return `nums[i]`.
   - If `i+2 < len(nums)` and `nums[i] == nums[i+2]`, return `nums[i]`.
   - If `i+3 < len(nums)` and `nums[i] == nums[i+3]`, return `nums[i]`.

Complexity:
- Time: O(n)
- Space: O(1)

Python implementation:
```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
            if i + 2 < n and nums[i] == nums[i + 2]:
                return nums[i]
            if i + 3 < n and nums[i] == nums[i + 3]:
                return nums[i]
        # Problem constraints guarantee an answer.
```

Note: In practice, checking up to distance 3 is enough; many accepted constant-space solutions check only the first few neighbors or use a fixed-window scan.

---

## Example walkthrough

For `nums = [5,1,5,2,5,3,5,4]`:
- Hash-set method: First repeated detection occurs when the second `5` is seen.
- Constant-space method: At index `0`, `nums[0] == nums[2]` (both `5`), so return `5`.

---

## Takeaway

- The hash-set approach is straightforward, easy to reason about, and robust (use it when O(n) space is acceptable).
- The constant-space method leverages the problem's counting constraint to detect the repeated element quickly with only local comparisons.
- For interview settings, present the hash-set solution first for clarity, then explain the constant-space optimization and why checking up to a fixed distance (≤3) is correct.
