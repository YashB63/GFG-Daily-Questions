class Solution:
    def maximumAmount(self, arr):
        n = len(arr)
        sum = 0
        dp = [0] * n
        for i in range(n - 1, -1, -1):

            sum += arr[i]
            for j in range(i, n):
                if i == j:
                    dp[j] = arr[j]
                else:
                    dp[j] = max(arr[i] - dp[j], arr[j] - dp[j - 1])

        return (sum + dp[n - 1]) // 2