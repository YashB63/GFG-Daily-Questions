import heapq as hq

class Solution:
    def minimizeSum(self, N, arr):
        sum = 0
        
        hq.heapify(arr)
        while len(arr) > 1:
            min_1 = hq.heappop(arr)
            min_2 = hq.heappop(arr)
            sum += min_1 + min_2
            hq.heappush(arr, min_1+min_2)
            
        return sum