from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		
        def cycle(node):
            for i in adj[node]:
                if not visited[i]:
                    visited[i]=True
                    parent[i]=node
                    if cycle(i):
                        return True
                elif parent[node]!=i:
                    return True
            return False
        visited=[False]*V
        parent=[-1]*V
        for i in range(V):
            if not visited[i]:
                visited[i]=True
                if cycle(i):
                    return True
        return False