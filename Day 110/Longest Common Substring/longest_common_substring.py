class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        mx =0
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif S1[i - 1] == S2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                mx = max(mx, dp[i][j])
        return mx