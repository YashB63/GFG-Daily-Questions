class Solution:
    def nearlySorted(self, arr, k):
        n = len(arr)
        pq = []

        for i in range(k):
            heapq.heappush(pq, arr[i])

        i = k
        index = 0

        while i < n:
            heapq.heappush(pq, arr[i])
            arr[index] = heapq.heappop(pq)
            i += 1
            index += 1

        while pq:
            arr[index] = heapq.heappop(pq)
            index += 1