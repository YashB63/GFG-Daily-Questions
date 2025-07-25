class Solution:
    def findMaxSum(self, arr):
        n = len(arr)
        dp = [[0]*3 for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for count in range(3):
                take = float('-inf')
                if count < 2:
                    take = arr[i] + dp[i+1][count+1]
                not_take = dp[i+1][0]
                dp[i][count] = max(take, not_take)

        return dp[0][0]