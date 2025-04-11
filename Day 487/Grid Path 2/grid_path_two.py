class Solution:
    def totalWays(self, n, m, grid):
        MOD = 10**9 + 7
        if grid[0][0] == 1 or grid[n-1][m-1] == 1:
            return 0
        
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1  
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = (dp[i][j] + dp[i-1][j]) % MOD
                    if j > 0:
                        dp[i][j] = (dp[i][j] + dp[i][j-1]) % MOD
        
        return dp[n-1][m-1]