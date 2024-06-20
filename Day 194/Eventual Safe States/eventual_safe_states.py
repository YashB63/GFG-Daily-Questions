from typing import List
from collections import deque

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        
        indegree = [0]*V
        adjRev = [[]for i in range(V)]
        for n in range(len(adj)):
            for i in adj[n]:
                indegree[n]+=1
                adjRev[i].append(n)
                
                
        q = deque()
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
                
        
        safeNodes = []
        while(len(q)>0):
            node = q.popleft()
            safeNodes.append(node)
            for i in adjRev[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
                    
        safeNodes.sort()
        return safeNodes