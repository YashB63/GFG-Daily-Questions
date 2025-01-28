from typing import List
import heapq

class Solution:
    def maxCoins(self, n : int, ranges : List[List[int]]) -> int:
        ranges = sorted(ranges)
        res = 0
        h1, h2 = [], []
        heapq.heapify(h1)
        heapq.heapify(h2)
        for start, end, value in ranges:
    
            while h2 and h2[0][0] <= start:
                e, v = heapq.heappop(h2)
                heapq.heappush(h1, -v)
            if h1:
                res = max(value - h1[0], res)
            else:
                res = max(value, res)
            heapq.heappush(h2, [end, value])
        return res