class Solution:
    def dfs(self,u,N,visited,graph):
        visited[u]=True
        for v in range(N):
            if graph[u][v]==1 and not visited[v]:
                self.dfs(v,N,visited,graph)
                
    
    def transitiveClosure(self, N, graph):
        ans=[[0 for j in range(N)] for i in range(N)]
        
        for i in range(N):
            visited=[False for i in range(N)]
            self.dfs(i,N,visited,graph)
            for j in range(N):
                if visited[j]:
                    ans[i][j]=1
        return ans