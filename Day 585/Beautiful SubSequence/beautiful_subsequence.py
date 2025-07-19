class Solution:
    def longest_Subsequence(self, arr):
        n = len(arr)

        arr.sort()

        dp = [1] * n

        for j in range(1, n):
            for i in range(j):
                if arr[j] % arr[i] == 0:
                    dp[j] = max(dp[j], dp[i] + 1)

        maxLength = max(dp)

        return -1 if maxLength == 1 else maxLength