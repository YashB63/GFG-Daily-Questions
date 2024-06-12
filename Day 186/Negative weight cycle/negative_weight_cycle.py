from collections import deque

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		
        adj = [[] for i in range(n)]
        for i,j,w in edges:
            adj[i].append((j,w))
        
        
        for v in range(n):
            q = deque([])
            visited = [0 for _ in range(n)]
            q.append((v,0))
            while q:
                u,d = q.popleft()
                visited[u] = 1
                for j,w in adj[u]:
                    if not visited[j]:
                        q.append((j,d+w))
                    else:
                        if v == j and d+w < 0:
                            return 1
                        
        
        else:
            return 0