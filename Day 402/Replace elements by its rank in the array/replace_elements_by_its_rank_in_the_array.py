import heapq

class Solution:
    def replaceWithRank(self, N, arr):
        heap = [(val,idx) for idx,val in enumerate(arr)]
        heapq.heapify(heap)
        rank = [0]*N
        count=1
        prev= None
        while heap:
            val,idx = heapq.heappop(heap)
            if prev is None or prev!=val:
                prev = val
                rank[idx]=count
                count+=1
            else:
                rank[idx] = count-1
        return rank