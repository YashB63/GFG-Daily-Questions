class Solution:
    def countWays(self,n):
        mod = 1000000007
        dp = [0]*(n+1)
        dp[0]=1
        for i in range(1,n):
            for j in range(i,(n+1)):
                dp[j]=(dp[j]+dp[j-i])%mod
        return (dp[n]+mod)%mod