class Solution:
    def findMinInsertions(self, s):
        n = len(s)
        dp = [[0]*n for i in range(n)]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]