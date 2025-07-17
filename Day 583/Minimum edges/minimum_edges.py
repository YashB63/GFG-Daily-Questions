from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minimumEdgeReversal(self, edges: List[List[int]], n: int, m: int, src: int, dst: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((v, 0))  
            graph[v].append((u, 1))  

        pq = [(0, src)]  
        dist = [float('inf')] * (n + 1)
        dist[src] = 0

        while pq:
            cost, u = heapq.heappop(pq)

            for v, w in graph[u]:
                if cost + w < dist[v]:
                    dist[v] = cost + w
                    heapq.heappush(pq, (dist[v], v))

        return -1 if dist[dst] == float('inf') else dist[dst]