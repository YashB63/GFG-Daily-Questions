class Solution:
    def minAmount(self, A, n): 
        dp=[0]*3
        for i in range(n):
            ip=i%3
            i1p=(i-1)%3
            i2p=(i-2)%3
            dp[ip]=min(dp[i1p]+A[i],dp[i2p]+A[i-1] if i-1>=0 else 0)
        return dp[ip]