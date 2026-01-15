def buildPalindromeDP(s):
    n = len(s)
    isPal = [[False]*n for _ in range(n)]
    
    for i in range(n):
        isPal[i][i] = True
    
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or isPal[i+1][j-1]:
                    isPal[i][j] = True
    return isPal

class Solution:

    def partition(self, s: str):
        n = len(s)
        isPal = buildPalindromeDP(s)
        res = []

        def backtrack(start, path):
            if start == n:
                res.append(path[:])
                return
            
            for end in range(start, n):
                if isPal[start][end]:
                    backtrack(end + 1, path + [s[start:end+1]])

        backtrack(0, [])
        return res
