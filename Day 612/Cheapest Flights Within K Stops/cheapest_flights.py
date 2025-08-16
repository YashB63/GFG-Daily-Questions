from typing import List
from collections import deque


class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        adj = [[] for _ in range(n)]

        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        q = deque([(0, src, 0)])
        dist = [float('inf')] * n
        dist[src] = 0

        while q:
            stops, node, cost = q.popleft()

            if stops > k:
                continue
            for adj_node, val in adj[node]:
                if cost + val < dist[adj_node] and stops <= k:
                    dist[adj_node] = cost + val
                    q.append((stops + 1, adj_node, cost + val))

        if dist[dst] == float('inf'):
            return -1
        return dist[dst]
        pass