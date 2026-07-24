from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        N = 2048

        f = [0] * N
        for x in nums:
            f[x] = 1

        # Fast Walsh-Hadamard Transform (XOR)
        def fwht(a, inverse=False):
            n = len(a)
            h = 1
            while h < n:
                for i in range(0, n, h * 2):
                    for j in range(i, i + h):
                        x = a[j]
                        y = a[j + h]
                        a[j] = x + y
                        a[j + h] = x - y
                h <<= 1
            if inverse:
                for i in range(n):
                    a[i] //= n

        fwht(f)

        # Cube each frequency (3-fold convolution)
        for i in range(N):
            f[i] = f[i] ** 3

        fwht(f, True)

        ans = 0
        for x in f:
            if x != 0:
                ans += 1
        return ans