from collections import deque, defaultdict

class Solution:
    
    def kosaraju(self, V, adj):
        stack=[]
        vis=set()
        
        def topo(node):
            vis.add(node)
            for nei in adj[node]:
                if nei not in vis:
                    topo(nei)
            stack.append(node)
            return
        
        for i in range(V):
            if i not in vis:
                topo(i)
                
        graph=defaultdict(list)
        for i in range(V):
            for j in adj[i]:
                graph[j].append(i)
        
        vis=set()
        
        def dfs(node):
            vis.add(node)
            for nei in graph[node]:
                if nei not in vis:
                    dfs(nei)
            return
        
        count=0
        while stack:
            cur=stack.pop(-1)
            if cur not in vis:
                dfs(cur)
                count+=1
        return count