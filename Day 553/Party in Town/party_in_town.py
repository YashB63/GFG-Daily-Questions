class Solution:
    def dfs(self,i,vis,d):
        self.md=max(self.md,d)
        vis[i]=True

        for k in self.adj[i]:
            if not vis[k]:
                self.dfs(k,vis,d+1)
           
    def partyHouse(self, N, adj):
        mini=10**10
        self.adj=adj
        
        for i in range(1,N+1):
            self.md=0
            vis=[False]*(N+1)
            self.dfs(i,vis,0)
            mini=min(mini,self.md)
        return(mini)