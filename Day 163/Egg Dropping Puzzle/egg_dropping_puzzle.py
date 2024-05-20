import math
class Solution:
    
    def eggDrop(self,n, k):
        
        dp=[[0 for i in range(n+1)]for j in range(k+1)]
        for i in range(1,n+1):
            dp[1][i]=1
        for i in range(2,k+1):
            dp[i][1]=i
        for i in range(2,k+1):
            for j in range(2,n+1):
                dp[i][j]=math.inf
                for x in range(1,i+1):
                    dp[i][j]=min(dp[i][j],max(dp[x-1][j-1],dp[i-x][j])+1)
        return dp[k][n]