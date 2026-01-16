import heapq

class Solution:
    def minProduct(self, arr, k): 
        prod=1
        heap=[] 
        for val in arr:
            heapq.heappush(heap,-val) 
            if len(heap)>k: 
                heapq.heappop(heap)
                
        while heap:   
            prod*=-heapq.heappop(heap)
            
        return prod%(10**9+7)