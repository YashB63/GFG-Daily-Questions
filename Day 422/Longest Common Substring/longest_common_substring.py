class Solution:
    def longestCommonSubstr(self, s1, s2):
        n = len(s1)+1
        m = len(s2)+1
        dp = [[0]*m for _ in range(n)]
        ml = 0
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] == 0
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ml = max(dp[i][j], ml)
                else:
                    dp[i][j] = 0
                    
        return ml