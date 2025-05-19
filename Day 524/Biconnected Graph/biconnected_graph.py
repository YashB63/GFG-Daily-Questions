class Solution:
    def biGraph(self, arr, n, e):
        discover = [-1 for i in range(n)]
        ancestor = [-1 for i in range(n)]
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for i in range(0, len(arr), 2):
            u, v = arr[i], arr[i+1]
            adj[u].append(v)
            adj[v].append(u)
        
        step = 0
        cut_vertex = []
    
        def findCutVertex(node, parent):
            nonlocal adj, step, discover, ancestor, cut_vertex
            
            discover[node] = step
            ancestor[node] = step
            step += 1
            
            child_count = 0
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                
                if discover[neighbor] == -1:
                    child_ancestor = findCutVertex(neighbor, node)
                    ancestor[node] = min(ancestor[node], child_ancestor)
                    child_count += 1
                else:
                    ancestor[node] = min(ancestor[node], discover[neighbor])
            
            if discover[node] == 0:
                if child_count > 1:
                    cut_vertex.append(node)
            else:
                if discover[node] <= ancestor[node] and parent != 0:
                    cut_vertex.append(node)
            
            return ancestor[node]
        
        findCutVertex(0, None)
        
        if step < n or len(cut_vertex) > 0:
            return 0
        else:
            return 1