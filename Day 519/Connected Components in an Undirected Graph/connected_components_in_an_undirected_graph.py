class Solution:
    def buildGraph(self, V, edges):
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v = edge[0], edge[1]
            adj[u].append(v)
            adj[v].append(u)
        return adj
    
    def dfs(self, node, adj, vis, component):
        vis[node] = True
        component.append(node)
        for neighbor in adj[node]:
            if not vis[neighbor]:
                self.dfs(neighbor, adj, vis, component)
    
    def getComponents(self, V, edges):  
        adj = self.buildGraph(V, edges)  
        vis = [False] * V
        res = []
        for i in range(V):
            if not vis[i]:
                component = []
                self.dfs(i, adj, vis, component)  
                res.append(component)
        return res