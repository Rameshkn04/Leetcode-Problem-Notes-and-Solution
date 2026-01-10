class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]

        for i in range(1,n+1):
            for k in range(i):
                for left in dp[k]:
                    for right in dp[i-1-k]:
                        dp[i].append("(" + left + ")" + right)
        return dp[n]
