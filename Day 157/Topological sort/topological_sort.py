class Solution:
    
    def topoSort(self, V, adj):
        
        indegree = [0]*V
        queue = []
        ans = []
        
        for i in range(V):
            for node in adj[i]:
                indegree[node]+=1
                
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        while(queue):
            node = queue.pop(0)
            ans.append(node)
            
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return ans