import heapq

class Solution:
    def minSum(self, a, N, K):
        arr = [-x for x in a]
        heapq.heapify(arr)
        
        for i in range(N):
            m = -heapq.heappop(arr)
            r = max(m*0.1, K)
            
            if m < K:
                m = 0
            else: m -= r
            heapq.heappush(arr, -m)
        return int(-sum(arr))