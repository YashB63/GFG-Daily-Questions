class Solution:
    def canFillContainer(self, arr, k):
        dp=[False]*(k+1)
        dp[0]=True
        for capacity in arr:
            for litres in range(capacity,k+1):
                if dp[litres-capacity]:
                    dp[litres]=True
        return dp[k]