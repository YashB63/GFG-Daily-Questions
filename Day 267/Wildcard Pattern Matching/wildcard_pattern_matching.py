class Solution:
    def wildCard(self,pattern, string):
        def solve(i,j):
            if i==-1 and j==-1:
                return True
            if i==-1:
                return False
            if j==-1:
                for k in range(i+1):
                    if pattern[k]!='*': 
                        return False
                return True
            if dp[i][j]!=-1: return dp[i][j]
            if pattern[i]==string[j] or pattern[i]=='?':
                dp[i][j] = solve(i-1,j-1)
            elif pattern[i]=='*':
                dp[i][j] = solve(i-1,j) or solve(i,j-1)
            else:
                dp[i][j] = False
            return dp[i][j]
            
        n=len(pattern)
        m=len(string)
        dp=[[-1]*m for _ in range(n)]
        return solve(n-1,m-1)