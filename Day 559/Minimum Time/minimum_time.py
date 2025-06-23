class Solution:
    def minTimeForWritingChars(self, N, I, D, C):
        dp = [0] * (N + 1)
        dp[1] = I
    
        for idx in range(2, N + 1):
            if idx % 2 == 0:
                dp[idx] = min(dp[idx - 1] + I, dp[idx // 2] + C)
            
            else:
                dp[idx] = min(dp[idx - 1] + I, dp[(idx + 1) // 2] + C + D)
        
        return dp[-1]