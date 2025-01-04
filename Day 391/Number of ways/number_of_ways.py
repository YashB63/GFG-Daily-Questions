class Solution:
    def arrangeTiles(self, N):
        if N == 0:
            return 1 
        if N == 1 or N == 2 or N == 3:
            return 1 
        if N == 4:
            return 2 
        dp = [0] * (N+1)
        
        dp[0] = 1
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2 
        for i in range(5,N+1):
            dp[i] = dp[i-1] + dp[i-4]
        return dp[N]