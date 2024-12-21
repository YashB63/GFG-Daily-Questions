class Solution:
	def MinCoin(self, nums, amount):
        dp=[0]*(amount+1)
        nums.sort()
        for price in range(1,amount+1):
            ans=float('INF')
            for coin in nums:
               if price>=coin:
                    ans=min(ans,1+dp[price-coin])
               else:
                   break
            dp[price]=ans
            
        if dp[price]>10**9:
            return -1
        else:
            return dp[-1]