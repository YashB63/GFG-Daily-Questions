from collections import *
import heapq
from typing import List

class Solution:
    def minimumCost(self, times: List[List[int]], n : int, k : int) -> int:
        adj = defaultdict(list)
        for  u,v,w in times:
            adj[u].append((v,w))
        visit = set()
        minheap = [(0,k)]
        t = 0
        while minheap:
            w1,n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for n2,w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap,(w1+w2,n2))
        return t if len(visit) == n else -1