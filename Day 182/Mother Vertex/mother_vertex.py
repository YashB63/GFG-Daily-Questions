class Solution:
    
    def dfs(self,u,adj,visited):
        visited[u]=True
        for v in adj[u]:
            if visited[v]==False:
                self.dfs(v,adj,visited)
                
	def findMotherVertex(self, V, adj):
		
        visited=[False]*V
        x=None
        for u in range(V):
            if visited[u]==False:
                self.dfs(u,adj,visited)
                x=u
        visited=[False]*V
        self.dfs(x,adj,visited)
        for node in visited:
            if node==False:
                return -1
        return x