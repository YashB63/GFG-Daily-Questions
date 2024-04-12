class Solution:
	def maxDotProduct(self, n, m, a, b):
		
        dp=[[-1]*m for _ in range(n)]
        def helper(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            ans1=a[i]*b[j]+helper(i-1,j-1)
            ans2=0
            if i>j:
                ans2=helper(i-1,j)
            dp[i][j]= max(ans1,ans2)
            return dp[i][j]
        return helper(n-1,m-1)