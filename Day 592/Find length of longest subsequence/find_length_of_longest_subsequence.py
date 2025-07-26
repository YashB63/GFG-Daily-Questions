class Solution:
    def maxSubsequenceSubstring(self, X, Y, N, M):
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if X[j - 1] == Y[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        ans = 0
        for i in range(1, M + 1):
            ans = max(ans, dp[i][N])

        return ans
