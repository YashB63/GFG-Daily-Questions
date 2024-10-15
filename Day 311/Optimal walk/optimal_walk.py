class Solution:
    def optimalWalk(self, N, A, B):
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = A
        
        for i in range(2, N + 1):
            dp[i] = min(A + dp[i - 1], B + dp[(i + 1) // 2] + (i % 2) * A)
            
        
        return dp[N]