class Solution:
    def waterOverflow(self, K, R, C):
        dp = [[0]*R for _ in range(R)]
        dp[0][0] = K
        
        for i in range(R-1):
            for j in range(i+1):
                if dp[i][j] > 1:
                    excess = max(0, dp[i][j] - 1)
                    dp[i][j] = 1
                    dp[i+1][j] += excess/2
                    dp[i+1][j+1] += excess/2
                
        return min(1, dp[R-1][C-1])