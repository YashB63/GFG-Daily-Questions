class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0 
        
        for i in range(1, n):
            for j in range(1, k + 1):
                if i - j >= 0:  
                    dp[i] = min(dp[i], dp[i - j] + abs(arr[i] - arr[i - j]))

        return dp[n - 1]  