class Solution:
	def FindWays(self, n, m, blocked_cells):
        MOD = 10**9 + 7
        blocked_set = {(i-1, j-1) for i, j in blocked_cells}
        dp = [[0] * m for _ in range(n)]
        if (0, 0) not in blocked_set:
            dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if (i, j) in blocked_set:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
                    if j > 0:
                        dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD

        return dp[-1][-1]