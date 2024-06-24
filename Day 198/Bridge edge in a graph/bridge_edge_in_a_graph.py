class Solution:
   
    def remove_edge(self, adj, u, v):
        if v in adj[u]:
            adj[u].remove(v)
        if u in adj[v]:
            adj[v].remove(u)

    def dfs(self, adj, u, visited):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                self.dfs(adj, v, visited)
    
    #Function to find if the given edge is a bridge in graph.
    def isBridge(self, V, adj, c, d):
        
        visited = [False] * V
        self.remove_edge(adj, c, d)
        self.dfs(adj, c, visited)
        is_bridge = not visited[d]  # Check if d is unreachable from c after removing the edge
        self.remove_edge(adj, d, c)  # Restore the edge
        if is_bridge:
            return 1
        return 0