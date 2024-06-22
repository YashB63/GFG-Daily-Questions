from collections import defaultdict

class Solution:
    def check(self, N, M, Edges): 
        
        adjList = defaultdict(list)
        
        for i,j in Edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        
        seen = set()
        def dfs(node):
            
            seen.add(node)
            
            if len(seen) == N:
                return True
                
            
            for nei in adjList[node]:
                if nei not in seen:
                    if dfs(nei):
                        return True
            
            seen.remove(node)
            return False
                    
        
        for i in range(1,N+1):
            if dfs(i):
                return 1
        
        return 0