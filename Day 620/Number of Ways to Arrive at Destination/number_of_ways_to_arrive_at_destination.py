from typing import List
from collections import defaultdict
import sys
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        
        mod=int(1e9+7)
        
        for u,v,t in roads:
            graph[u].append((t,v))
            graph[v].append((t,u))
        
        heap=[]
        
        shortest=sys.maxsize
        
        heapq.heappush(heap,(0,0))
        
        dist=[[sys.maxsize,0]]*n
        
        dist[0]=[0,1]
        
        while heap:
            time,node=heapq.heappop(heap)
            if node==n-1:
                if shortest==sys.maxsize:
                    shortest=time
                continue
            if shortest!=sys.maxsize and time>shortest:
                break
            for next_time,nei in graph[node]:
                if time+next_time<=dist[nei][0]:
                    if time+next_time==dist[nei][0]:
                        dist[nei][1]+=dist[node][1]
                    else:
                        dist[nei]=[time+next_time,dist[node][1]]
                        heapq.heappush(heap,(time+next_time,nei))  
        return dist[n-1][1]%mod