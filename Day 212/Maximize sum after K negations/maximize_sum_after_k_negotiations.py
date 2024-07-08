import heapq

class Solution:
    def maximizeSum(self, a, n, k):
        
        heapq.heapify(a)
        
        while a[0] < 0 and k > 0:
            mins = heapq.heappop(a)
            mins *= -1
            k -= 1
            heapq.heappush(a, mins)
        
        if k % 2 == 0:
            return sum(a)
        else:
            a[0] *= -1
            return sum(a)