import heapq

class Solution:
    def isPossible(self, arr, k):
        pq = []
        i = 0

        while i < len(arr):
            if not pq:
                heapq.heappush(pq, (arr[i], 1))
                i += 1
            else:
                top = pq[0]
                if arr[i] == top[0]:
                    heapq.heappush(pq, (arr[i], 1))
                    i += 1
                elif arr[i] == top[0] + 1:
                    heapq.heappop(pq)
                    heapq.heappush(pq, (arr[i], top[1] + 1))
                    i += 1
                else:
                    if top[1] < k:
                        return False
                    heapq.heappop(pq)

        while pq:
            if pq[0][1] < k:
                return False
            heapq.heappop(pq)

        return True