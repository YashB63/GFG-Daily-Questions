from collections import defaultdict

class Solution:
    def isCycle(self, V, edges):
        indeg = [0]*V
        adj = defaultdict(list)
        for i, j in edges:
            indeg[j] += 1
            adj[i].append(j)
        topo = []
        q = []
        for i in range(V):
            if indeg[i] == 0:
                q.append(i)
        while(q):
            node = q.pop(0)
            topo.append(node)
            for it in adj[node]:
                indeg[it] -= 1
                if indeg[it] == 0:
                    q.append(it)
        return len(topo) != V