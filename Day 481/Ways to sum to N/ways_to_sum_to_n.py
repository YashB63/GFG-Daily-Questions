class Solution:
    def countWays(self, arr, m, n):
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            for num in arr:
                if i >= num:
                    dp[i] = (dp[i] + dp[i - num]) % MOD
        
        return dp[n]