from collections import defaultdict

class Solution:
    def isBridge(self, V, edges, c, d):
        def dfs(u,visited,graph):
            visited[u]=True
            for v in graph[u]:
                if not visited[v]:
                    dfs(v,visited,graph)
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[False]*V
        dfs(c,visited,graph)
        if not visited[d]:
            return False
        graph[c].remove(d)
        graph[d].remove(c)
        visited=[False]*V
        dfs(c,visited,graph)
        return not visited[d]