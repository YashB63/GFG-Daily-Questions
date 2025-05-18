from typing import List
import heapq

class Solution:

    def kthLargest(self, arr, k) -> int:
        N = len(arr)
        pre = [0] * (N + 1)
        pre[0] = 0
        pre[1] = arr[0]

        for i in range(2, N + 1):
            pre[i] = pre[i - 1] + arr[i - 1]

        pq = []

        for i in range(1, N + 1):
            for j in range(i, N + 1):
                x = pre[j] - pre[i - 1]

                if len(pq) < k:
                    heapq.heappush(pq, x)
                
                elif pq[0] < x:
                    heapq.heappop(pq)
                    heapq.heappush(pq, x)

        return pq[0]