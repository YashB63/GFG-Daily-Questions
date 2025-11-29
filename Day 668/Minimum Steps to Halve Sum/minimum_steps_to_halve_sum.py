import heapq

class Solution:
    def minOperations(self, arr):
        totalSum = sum(arr)
        target = totalSum / 2

        pq = [-x for x in arr]
        heapq.heapify(pq)

        ops = 0
        currentSum = totalSum

        while currentSum > target:
            x = -heapq.heappop(pq)
            h = x / 2
            currentSum -= h
            heapq.heappush(pq, -h)
            ops += 1

        return ops