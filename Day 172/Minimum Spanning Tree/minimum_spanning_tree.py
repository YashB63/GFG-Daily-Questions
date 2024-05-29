import heapq

class Solution:
    
    def spanningTree(self, V, adj):
       
        pq = []
        heapq.heappush(pq, (0, 0))
        result = 0
        
        visited = [0]*V
        
        while pq:
            wt, u = heapq.heappop(pq)
            
            if visited[u]:
                continue
            
            result += wt
            visited[u] = 1
            
            for child, wt in adj[u]:
                if not visited[child]:
                    heapq.heappush(pq, (wt, child))
        
        return result