class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [10**8] * V
        dist[src] = 0
        
        for _ in range(V - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != 10**8 and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    updated = True
            if not updated:
                break  
        
        for u, v, w in edges:
            if dist[u] != 10**8 and dist[v] > dist[u] + w:
                return [-1]
        
        return dist