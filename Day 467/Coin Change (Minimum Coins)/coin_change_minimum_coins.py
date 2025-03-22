class Solution:
	def minCoins(self, coins, sum):
        dp = [float('inf')]*(sum+1)
        dp[0] = 0
        
        for s in range(1, sum+1):
            for c in coins:
                if s >= c:
                    dp[s] = min(dp[s], dp[s-c]+1)
        return dp[-1] if dp[-1] != float('inf') else -1