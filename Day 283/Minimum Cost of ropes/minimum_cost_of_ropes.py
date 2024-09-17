from typing import List

class Solution:
   def minCost(self, arr: List[int]) -> int:
        tcost=0
        cost=0
        heapq.heapify(arr)
        while len(arr)>1:
            first=heapq.heappop(arr)
            if arr:
                second=heapq.heappop(arr)
            cost = first + second
            heapq.heappush(arr,cost)
            tcost+=cost
        return tcost