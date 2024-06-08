class Solution:
    
    mod=10**9+7
    
    def numTrees(self,N):
        
        dp=[None]*(N+1)
        dp[0]=1
        for i in range(1,N+1):
            dp[i]=0
            for j in range(1,i+1):
                dp[i]=(dp[i]+dp[j-1]*dp[i-j])%self.mod
        return dp[N]