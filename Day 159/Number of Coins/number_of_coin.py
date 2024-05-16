class Solution:
	def minCoins(self, coins, M, V):
		
        dp=[float('inf')]*(V+1)
        dp[0]=0
        for i in range(1,V+1):
            for j in range(M):
                if coins[j]<=i:
                    dp[i]=min(dp[i],1+dp[i-coins[j]])
        if dp[V]==float('inf'):
            return -1
        else:
            return dp[V]