class Solution:
    def minCost(self, arr):
        min_heap = []

        for num in arr:
            heapq.heappush(min_heap, num)

        total_cost = 0

        while (len(min_heap) > 1):
            val_1 = heapq.heappop(min_heap)
            val_2 = heapq.heappop(min_heap)

            val = val_1 + val_2
            total_cost += val
            
            heapq.heappush(min_heap, val)

        return total_cost