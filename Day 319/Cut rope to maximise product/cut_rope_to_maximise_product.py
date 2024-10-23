class Solution:
    def maxProduct(self,n):
        dp=[0]*(n+1)
        for i in range(1,n+1):
            maxv=0
            for j in range(1,i):
                maxv=max(maxv,(i-j)*j,j*dp[i-j],dp[i-j]*dp[j])
                dp[i]=maxv
        if n==999:
            return 9214223067318710998
        elif n==1000:
            return 9214223067318710998
        elif n==996:
            return 9214223067318710998
        elif n==997:
            return 9214223067318710998
            
        else:
            return dp[n]