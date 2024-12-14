class Solution:
	def MinSquares(self, n):
        def helper(n,dp):
            if n<=3:
                return n
            count=n
            if dp[n]!=-1:
                return dp[n]
            for i in range(1,int(n**0.5)+1):
                count=min(count,1+helper(n-i*i,dp))
            dp[n]=count
            return dp[n]
        
        
        dp=[-1]*(n+1)
        return helper(n,dp)
