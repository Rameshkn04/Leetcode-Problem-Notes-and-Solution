def buildPalindromeDP(s):
    n = len(s)
    isPal = [[False]*n for _ in range(n)]
    
    for i in range(n):
        isPal[i][i] = True
    
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and (length == 2 or isPal[i+1][j-1]):
                isPal[i][j] = True
    return isPal

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        isPal = [[False]*n for _ in range(n)]

        for i in range(n):
            isPal[i][i] = True
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or isPal[i+1][j-1]):
                    isPal[i][j] = True

        dp = [float('inf')] * n

        for i in range(n):
            if isPal[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if isPal[j+1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]

        
