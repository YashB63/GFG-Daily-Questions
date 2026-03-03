import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, V, a, b, edges):
        adj = defaultdict(list)

        for u, v, w1, w2 in edges:
            adj[u].append((v, w1, w2))
            adj[v].append((u, w1, w2))

        INF = float('inf')
        dist = [[INF, INF] for _ in range(V)]
        dist[a][0] = 0
        heap = [(0, a, 0)]

        while heap:
            cost, node, used_curved = heapq.heappop(heap)

            if cost > dist[node][used_curved]:
                continue

            for nei, w_straight, w_curved in adj[node]:
                if dist[nei][used_curved] > cost + w_straight:
                    dist[nei][used_curved] = cost + w_straight
                    heapq.heappush(heap, (dist[nei][used_curved], nei, used_curved))

                if used_curved == 0 and dist[nei][1] > cost + w_curved:
                    dist[nei][1] = cost + w_curved
                    heapq.heappush(heap, (dist[nei][1], nei, 1))

        ans = min(dist[b][0], dist[b][1])
        
        return ans if ans != INF else -1