import heapq

class Solution:
    def kthLargest(self, k, arr, n):
        ans = []
        min_heap = []

        for i in range(k):
            heapq.heappush(min_heap, arr[i])
            if i != k-1:
                ans.append(-1)
            elif i == k - 1:
                ans.append(min_heap[0])
            
        n = len(arr)
        i = k
        while i < n:
            if min_heap[0] < arr[i]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, arr[i])
                
            ans.append(min_heap[0])
            i += 1
            
        return ans