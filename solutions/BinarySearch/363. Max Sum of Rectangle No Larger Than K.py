import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')

        for left in range(n):
            rowSum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    rowSum[i] += matrix[i][right]

                prefix = [0]
                curr = 0
                for s in rowSum:
                    curr += s
                    idx = bisect.bisect_left(prefix, curr - k)
                    if idx < len(prefix):
                        ans = max(ans, curr - prefix[idx])
                    bisect.insort(prefix, curr)

        return ans
