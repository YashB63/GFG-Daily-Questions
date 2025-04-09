import collections

class Solution:
    def bfs(self, adj):
        q = collections.deque([0])
        visited = set([0])
        ans = []
        
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                ans.append(u)
                
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
        return ans