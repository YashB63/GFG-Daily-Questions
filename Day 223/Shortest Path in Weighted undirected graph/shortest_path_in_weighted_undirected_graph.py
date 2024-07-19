from collections import defaultdict, deque
from heapq import heappush, heappop

from typing import List
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        
        g = defaultdict(list)
        for frm, to, w in edges:
            g[frm].append((to, w))
            g[to].append((frm, w))
        
        q = [(0, 1)]
        costs = {1: 0}
        parents = {1: None}

        
        def build_path(cost, last):
            nonlocal parents
            q = deque()
            while last:
                q.appendleft(last)
                last = parents[last]
            q.appendleft(cost)
            return q
            
        while q:
            cost0, frm = heappop(q)
            if frm == n:
                return build_path(cost0, frm)
            for to, w in g[frm]:
                cost = cost0+w
                if to not in costs or cost < costs[to]:
                    costs[to] = cost
                    parents[to] = frm
                    heappush(q, (cost, to))
        return [-1]