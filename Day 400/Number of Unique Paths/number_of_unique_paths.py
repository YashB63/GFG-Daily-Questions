class Solution:
    def NumberOfPaths(self,a, b):
        dp = [[-1]*(a+1) for _ in range(b+1)]
        
        for i in range(a+1):
            dp[0][i] = 1
        for j in range(b+1):
            dp[j][0] = 1
        
        for i in range(1,b+1):
            for j in range(1,a+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[b-1][a-1]