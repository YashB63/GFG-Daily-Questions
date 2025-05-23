import heapq

class Solution:
    def findSmallestRange(self, arr):
        n = len(arr)
        k = len(arr[0])
        heap = []
        maxVal = float('-inf')

        for i in range(n):
            heapq.heappush(heap, (arr[i][0], i, 0))
            maxVal = max(maxVal, arr[i][0])

        minRange = float('inf')
        minEl = maxEl = -1

        while True:
            minVal, row, col = heapq.heappop(heap)

            if maxVal - minVal < minRange:
                minRange = maxVal - minVal
                minEl = minVal
                maxEl = maxVal

            if col + 1 == k:
                break

            nextVal = arr[row][col + 1]
            heapq.heappush(heap, (nextVal, row, col + 1))
            maxVal = max(maxVal, nextVal)

        return [minEl, maxEl]