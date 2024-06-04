class Solution:
    def findWinner(self, n : int, x : int, y : int) -> int:
       
        dp=[0]*(n+1)
        for i in range(n):
            if dp[i]==0:
                dp[i+1]=1
                if i+x<=n:
                    dp[i+x]=1
                if i+y<=n:
                    dp[i+y]=1
        return dp[n]