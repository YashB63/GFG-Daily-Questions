class Solution:
    def countMin(self, s):
        # code here
        sec_s = s[::-1]
        n = len(s)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1) ]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==sec_s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        res = len(s) - dp[n][n]
        return res