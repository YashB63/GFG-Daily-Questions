from collections import deque

class Solution:
    
    def func(self,src,adj,color):
        color[src] = 0
        
        q = deque()
        q.append(src)
        
        
        while q:
            node = q.popleft()
            for it in adj[node]:
                if color[it] == -1:
                    color[it] = not color[node]
                    q.append(it)
                elif color[it] == color[node]:
                    return 0
                    
        return 1
        
	def isBipartite(self, V, adj):
		
        color = [-1] * V
        for i in range(V):
            if color[i] == -1:
                if not self.func(i,adj,color):
                    return 0
        return 1