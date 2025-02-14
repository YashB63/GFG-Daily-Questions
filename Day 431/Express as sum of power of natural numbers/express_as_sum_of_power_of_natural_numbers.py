class Solution:
	def numOfWays(self, n, x):
        MOD = 10**9 + 7
    
        powers = []
        k = 1
        while k**x <= n:
            powers.append(k**x)
            k += 1
    
        dp = [0] * (n + 1)
        dp[0] = 1  
    
        for power in powers:
            for i in range(n, power - 1, -1):
                dp[i] = (dp[i] + dp[i - power]) % MOD
    
        return dp[n]