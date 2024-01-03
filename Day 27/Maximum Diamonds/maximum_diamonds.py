import heapq

class Solution:
    def maxDiamonds(self, A, N, K):
        
        x = []
        heapq.heapify(x)
        
        for i in A:
            heapq.heappush(x, -1*i)
        
        res = 0
        
        for i in range(K):
            num = -1*heapq.heappop(x)
            res += num
            heapq.heappush(x, -1*(num//2))
            
        return res