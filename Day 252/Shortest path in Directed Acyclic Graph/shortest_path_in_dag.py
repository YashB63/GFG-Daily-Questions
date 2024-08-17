from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        def createAdj():
            adj = {}
            for i in range(n):
                adj[i] = []
            
            for fr,to,wt in edges:
                adj[fr].append((to,wt))
                
            return adj
            
        def dfs(node):
            visited[node] = True
            
            for i,wt in adj[node]:
                if not visited[i]:
                    dfs(i)
            stack.append(node)
        
        def topoSort():
            for i in range(n):
                if not visited[i]:
                    dfs(i)
        
        visited = [False]*n
        stack = []
        adj = createAdj()
        
        topoSort()

        distance = [10**9]*n
        distance[0] = 0
        for i in stack[::-1]:
            for j,wt in adj[i]:
                distance[j] = min(distance[j],distance[i] + wt)
        
        for i in range(n):
            if distance[i]==10**9:
                distance[i]=-1
        
        return distance