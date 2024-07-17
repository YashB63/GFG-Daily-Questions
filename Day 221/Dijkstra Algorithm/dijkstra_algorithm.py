import heapq
class Solution:

    def dijkstra(self, V, adj, S):
        
        dist = [float("inf")] * V
        dist[S] = 0  
        
        pq = [(0, S)]
        
        while pq:
            curr_dist, curr_vex = heapq.heappop(pq)
            
            
            if curr_dist > dist[curr_vex]:
                continue
            
            for nei, wei in adj[curr_vex]:
                distance = curr_dist + wei
                
                
                if distance < dist[nei]:
                    dist[nei] = distance
                    heapq.heappush(pq, (distance, nei))
        
        return dist