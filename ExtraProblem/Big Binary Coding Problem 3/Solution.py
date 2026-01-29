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
