import heapq

class Solution:

	def kLargest(self,arr, n, k):
		
        if n == k:
            return sorted(arr, reverse=True)
            
        pq = arr[:k]
        heapq.heapify(pq)
        
        ans = [0] * k
        
        for num in arr[k:]:
            if num > pq[0]:
                heapq.heappushpop(pq, num)
        k = k-1        
        while pq:
            ans[k] = heapq.heappop(pq)
            k -= 1
            
        return ans
