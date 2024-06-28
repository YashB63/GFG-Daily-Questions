from typing import List

class Solution:
    
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        
        visiting = set()
        visited = set()
        li = []

        def dfs(node, visiting, visited):
            if node in visiting:
                return True
            if node in visited:
                return False
            
            visiting.add(node)
            for neighbor in adj[node]:
                if dfs(neighbor, visiting, visited):
                    return True
            
            visiting.remove(node)
            visited.add(node)
            li.append(node)
            return False

        for i in range(V):
            if i not in visited:
                if dfs(i, visiting, visited):
                    return True
        return False