class Solution:
    def cutRod(self, price, n):
       
        dp = [0] * (n+1)
        for i in range(1, n+1):
            for index in range(1, i+1):
                current_cost = price[index-1] + dp[(i-index)]
                if current_cost > dp[i]:
                    dp[i] = current_cost
        return dp[n]