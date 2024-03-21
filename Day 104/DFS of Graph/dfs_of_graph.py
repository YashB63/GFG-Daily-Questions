class Solution:
    
    def dfsOfGraph(self, V, adj):
        
        res= []
        visited = [False]*V
        
        def dfs(node, adj, visited, res):
            res.append(node)
            visited[node] = True
            
            for i in adj[node]:
                if not visited[i]:
                    dfs(i, adj, visited, res)
                    
        dfs(0, adj, visited, res)
        return res