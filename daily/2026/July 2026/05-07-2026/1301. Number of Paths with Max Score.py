class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        NEG = -10**9

        # Maximum score
        dpScore = [[NEG] * n for _ in range(n)]

        # Number of ways
        dpWays = [[0] * n for _ in range(n)]

        dpScore[n - 1][n - 1] = 0
        dpWays[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X':
                    continue

                if i == n - 1 and j == n - 1:
                    continue

                best = NEG
                ways = 0

                for ni, nj in [(i + 1, j), (i, j + 1), (i + 1, j + 1)]:
                    if ni < n and nj < n:
                        if dpScore[ni][nj] > best:
                            best = dpScore[ni][nj]
                            ways = dpWays[ni][nj]
                        elif dpScore[ni][nj] == best:
                            ways = (ways + dpWays[ni][nj]) % MOD

                if best == NEG:
                    continue

                if board[i][j] not in ('E', 'S'):
                    best += int(board[i][j])

                dpScore[i][j] = best
                dpWays[i][j] = ways % MOD

        if dpWays[0][0] == 0:
            return [0, 0]

        return [dpScore[0][0], dpWays[0][0]]