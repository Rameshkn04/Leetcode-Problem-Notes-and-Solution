from bisect import bisect_left, bisect_right
from typing import List
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        k = len(digits)

        # powers of 10
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix decimal values
        prefixValue = [0] * (k + 1)
        for i in range(1, k + 1):
            prefixValue[i] = (prefixValue[i - 1] * 10 + digits[i - 1]) % MOD

        # prefix digit sums
        prefixSum = [0] * (k + 1)
        for i in range(1, k + 1):
            prefixSum[i] = prefixSum[i - 1] + digits[i - 1]

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r) - 1

            if left > right:
                ans.append(0)
                continue

            a = left + 1      # 1-based
            b = right + 1

            length = b - a + 1

            x = (prefixValue[b] -
                 prefixValue[a - 1] * pow10[length]) % MOD

            digit_sum = prefixSum[b] - prefixSum[a - 1]

            ans.append((x * digit_sum) % MOD)

        return ans