class Solution:
    def count(self, N):
        pairs = N // 2

        dp = [0] * (pairs + 1)
        dp[0] = 1  
        
        for n in range(1, pairs + 1):
            for i in range(n):
                dp[n] += dp[i] * dp[n - i - 1]

        return dp[pairs]