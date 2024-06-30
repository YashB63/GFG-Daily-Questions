from typing import List
from queue import Queue
from collections import deque
class Solution:
    
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q = deque()
        visited=[]
        
        def bfs(node):
            q.append(node)
            visited.append(node)
            
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if nei not in visited:
                        q.append(nei)
                        visited.append(nei)
                        
        bfs(0)
        return visited