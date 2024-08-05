import heapq
from typing import List

class Solution:
    
    def shortestPath(self, l: List[List[int]], s: List[int], d: List[int]) -> int:
        m, n = len(l), len(l[0])
        dis = [[1000000001 for i in range(n)] for j in range(m)]
        dis[s[0]][s[1]] = 0
        tp = [[0, s]]
        at = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def check(a, b, di):
            if(a<0 or b<0 or a>=m or b>=n):
                return
            if(l[a][b]==1 and di+1<dis[a][b]):
                dis[a][b] = di+1
                tp.append([di+1, [a, b]])
                
        while(tp):
            ps = tp.pop(0)
            for k in at:
                i, j = ps[1][0]+k[0], ps[1][1]+k[1]
                check(i, j, ps[0])
        if(dis[d[0]][d[1]]==1000000001):
            return -1
        return dis[d[0]][d[1]]