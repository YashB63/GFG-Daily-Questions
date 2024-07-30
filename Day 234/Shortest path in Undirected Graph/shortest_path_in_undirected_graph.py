from collections import defaultdict,deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        dist=[float('inf')]*n
        q=deque()
        dist[src]=0
        q.append(src)
        while q:
            node=q.popleft()
            for i in adj[node]:
                if dist[node]+1<dist[i]:
                    dist[i]=dist[node]+1
                    q.append(i)
        ans=[-1]*n
        for i in range(len(dist)):
            if dist[i]!=float('inf'):
                ans[i]=dist[i]
        return ans