class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        
        return dp[n]


#Second Approach BFS
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, int(n**0.5) + 1)]
        queue = deque([(n, 0)])
        visited = set([n])
        
        while queue:
            curr, steps = queue.popleft()
            for sq in squares:
                nxt = curr - sq
                if nxt == 0:
                    return steps + 1
                if nxt < 0:
                    break
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
