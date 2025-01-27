class Solution:
    def distinctColoring (self, N, r, g, b):
        dp=[-1 for c in range(3)]
        
        for i in range(N):
            cost=[r[i],g[i],b[i]]
            ndp=[-1 for c in range(3)]
            for c in range(3):
                if i==0:
                    ndp[c]=cost[c]
                else:
                    ndp[c]=cost[c]+min(dp[(c-1)%3],dp[(c-2)%3])
            dp=list(ndp)
        return min(dp)