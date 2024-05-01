import heapq

class Solution:
    def minOperations(self, arr, n, k):
       
        heapq.heapify(arr)
        count = 0

        while arr[0] < k and len(arr) > 1:
        
            
            m1 = heapq.heappop(arr)
            m2 = heapq.heappop(arr)
            
            heapq.heappush(arr, m1 + m2)
            
            count +=1
        
        if arr[0] < k:
            
            return -1
        
        return count