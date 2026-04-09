class Solution:
    def minHeightRoot(self, V, edges):
        if V == 1:
            return [0]
        count = [0] * V
        graph = [[] for _ in range(V)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            count[a] += 1
            count[b] += 1
            
        q =[]
        for i in range(V):
            if count[i] == 1:
                q.append(i)
                
        remaining = V
        
        while remaining > 2:
            size = len(q)
            remaining -= size
            
            new_q = []
            for i in range(size):
                node = q[i]
                for neighbor in graph[node]:
                    count[neighbor] -= 1
                    if count[neighbor] == 1:
                        new_q.append(neighbor)
                        
            q = new_q
        return q