class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        
        n,m,MOD=len(s1),len(s2),1000000007
        
        pre=[0]*(m+1)
        pre[m]=1
        for i in range(n-1,-1,-1):
            curr=[0]*(m+1)
            curr[m]=1
            for j in range(m-1,-1,-1):
                ans=pre[j]%MOD
                if s1[i]==s2[j]:
                    ans+=pre[j+1]%MOD
                curr[j]=ans%MOD
            pre=[k for k in curr]
        return curr[0]%MOD