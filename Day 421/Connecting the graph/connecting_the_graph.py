class Solution:
    def Solve(self, n, edges):
        if len(edges) < n-1:
            return -1
        
        visited = [False]*n
        
        adjList = [[] for _ in range(n)]
        
        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])
            
        def dfs(node):
            visited[node] = True
            
            for neighbour in adjList[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
                    
        component = 0
        for i in range(n):
            if not visited[i]:
                component += 1
                dfs(i)
                
        return component - 1