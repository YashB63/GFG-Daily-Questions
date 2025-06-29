class Solution:
    def rec(self, n, adj, lenn):
        if(lenn[n]):
            return lenn[n]
        
        lenn[n] = 0
        
        for u in adj[n]:
            lenn[n] = max(lenn[n], self.rec(u, adj, lenn))
        
        lenn[n] = lenn[n] + 1
        
        return lenn[n]
    
    def minColour(self, N, M, mat):
        adj = [[] for i in range(N+1)]
        
        lenn = [0 for i in range(N+1)]
        
        maxVal = -1
        
        for i in mat:
            adj[i[0]].append(i[1])
        
        for i in range(1, N+1):
            maxVal = max(maxVal, self.rec(i, adj, lenn))
        
        return maxVal