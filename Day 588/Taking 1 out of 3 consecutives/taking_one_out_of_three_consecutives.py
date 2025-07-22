class Solution:
    def minSum(self, arr):
        n = len(arr)
        
        dp = [0 for i in range(n + 5)]
        minans = arr[0]

        if (n < 3):
            return 0

        else:
            dp[0] = arr[0]
            dp[1] = arr[1]
            dp[2] = arr[2]

            for i in range(3, n):
                minans = min(dp[i - 1], dp[i - 2], dp[i - 3])
                dp[i] = arr[i] + minans

            return min(dp[n - 1], dp[n - 2], dp[n - 3])