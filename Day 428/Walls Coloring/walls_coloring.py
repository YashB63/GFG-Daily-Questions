class Solution():
    def minCost(self, colors, N):
        cur=[0]*3
        for y in range(1,N+1):
            prv=cur[:]
            for x in range(3):
                cur[x]=min(prv[(x+1)%3],prv[(x+2)%3])+colors[y-1][x]
        return min(cur)