class Solution:
    def countFriendsPairings(self, n):
        
        dp=[]
        for i in range(n+1):
            dp.append(None)
            
        def solve(idx):
            if idx==n-1:
                return 1
            if idx==n-2:
                return 2
            if dp[idx]!=None:
                return dp[idx]
            a=solve(idx+1)%(10**9+7)
            b=(((n-idx-1)%(10**9+7))*(solve(idx+2)%(10**9+7)))%(10**9+7)
            dp[idx]=a+b
            return dp[idx]
        
        return solve(0)%(10**9+7)