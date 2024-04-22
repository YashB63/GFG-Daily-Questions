import heapq

class Solution:
    
    def kLargest(self,li,n,k):
        
        heap = []
        for i in li:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for i in range(len(heap)):
           result.append(heapq.heappop(heap)) 
        
        return result[::-1]