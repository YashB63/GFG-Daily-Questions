class Solution:
    def lengthOfLongestAP(self,arr):
        n = len(arr)
        if n<=2:
            return n
        result = 0
        dp = [{} for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                diff = arr[i] - arr[j]
                length = dp[j].get(diff, 1)
                dp[i][diff] = length + 1
                result = max(result, dp[i][diff])
        return result