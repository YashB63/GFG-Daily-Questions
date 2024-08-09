class Solution:
    def longestPalinSubseq(self, S):
        n=len(s)
        t=s[::-1]
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if s[i]==t[j]:
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=1+dp[i-1][j-1]
                else:
                    prev_row=prev_col=0
                    if i>0:
                        prev_row=dp[i-1][j]
                    if j>0:
                        prev_col=dp[i][j-1]
                    dp[i][j]=max(prev_col,prev_row)
        return dp[n-1][n-1]