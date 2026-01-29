def minDistance(houses, k):
    houses.sort()
    n = len(houses)

    # Precompute cost[i][j]
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            median = (i + j) // 2
            cost[i][j] = sum(abs(houses[t] - houses[median]) for t in range(i, j + 1))

    # DP table
    INF = float('inf')
    dp = [[INF] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 0

    for m in range(1, k + 1):
        for i in range(1, n + 1):
            for x in range(i):
                dp[m][i] = min(dp[m][i], dp[m - 1][x] + cost[x][i - 1])

    return dp[k][n]


# Input handling
n = int(input())
houses = list(map(int, input().split()))
k = int(input())

print(minDistance(houses, k))
