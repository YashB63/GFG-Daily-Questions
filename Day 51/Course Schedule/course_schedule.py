from collections import defaultdict

class Solution:
    def findOrder(self, N, m, P):
        
        graph = defaultdict(list)
        for a,b in P: graph[a].append(b)
        res, visited = [], [0] * N
        
        def DFS(i):
            if visited[i]: return visited[i] == 1
            visited[i] = -1
            
            if any(not DFS(node) for node in graph[i]): return False
            visited[i] = 1
            res.append(i)
            return True
        
        return all(DFS(node) for node in range(N)) and res or []