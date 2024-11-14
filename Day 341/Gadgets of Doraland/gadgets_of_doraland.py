import heapq

class Solution:
    def TopK(self, array, k):
        d = {}
        for i in array:
            d[i] = d.get(i, 0)+1
            
        heap = []
        for i in d:
            heapq.heappush(heap, (-d[i], -i))
            
        ans = []
        for _ in range(k):
            _, i = heapq.heappop(heap)
            ans.append(-i)
            
        return ans