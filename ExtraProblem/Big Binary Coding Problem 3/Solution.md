This is a classic Sliding Window problem. Since all numbers are positive, we can solve it optimally in O(n) time.

🧠 Key Idea (Very Important)

Because all array elements are positive:

Expanding the window → sum increases

Shrinking the window → sum decreases

So we use two pointers (left and right) to maintain a sliding window.

✅ Algorithm (Step-by-step)

Initialize:

left = 0

current_sum = 0

min_len = infinity

Move right from 0 → n-1:

Add a[right] to current_sum

While current_sum >= k:

Update min_len = min(min_len, right - left + 1)

Subtract a[left] from current_sum

Move left forward

If min_len was never updated, return 0

✅ Python Implementation (Complete Function)
def findLengthOfSmallestSubarray(a, k):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for right in range(len(a)):
        current_sum += a[right]

        while current_sum >= k:
            min_len = min(min_len, right - left + 1)
            current_sum -= a[left]
            left += 1

    return 0 if min_len == float('inf') else min_len

✅ Input / Output Handling (If Needed)
n, k = map(int, input().split())
a = list(map(int, input().split()))

print(findLengthOfSmallestSubarray(a, k))

🧪 Example Walkthrough
Example 1
a = [2, 1, 4, 3, 2, 5], k = 7


Subarray [4, 3]

Length = 2 ✅

Example 2
a = [3, 4, 1, 1, 6], k = 8


Subarrays [3,4,1] or [1,1,6]

Length = 3 ✅

⏱️ Complexity Analysis
Metric	Value
Time	O(n)
Space	O(1)

“Since all elements are positive, we use a sliding window to find the minimum-length subarray with sum ≥ k in linear time.”
