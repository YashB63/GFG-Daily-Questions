from heapq import heappush, heappop

class Solution:
    def dijkstra(self, V, edges, src):
        res = [0] * V
        q = [(0, src)]
        vis = set()
        adj = [[] for i in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        while len(vis) < V:
            w, v = heappop(q)
            if v in vis:
                continue
            res[v] = w
            vis.add(v)
            for u, uw in adj[v]:
                if u not in vis:
                      nw = w + uw
                      heappush(q, (nw, u))
        return res