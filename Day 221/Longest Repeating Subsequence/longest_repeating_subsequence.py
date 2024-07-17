class Solution:
	def LongestRepeatingSubsequence(self, st):
		
        n=len(st)
        dp=[[0 for i in range(n+1)]for j in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if st[i]==st[j] and i!=j:
                    dp[i][j]=dp[i+1][j+1]+1
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]