from collections import deque

class Solution:
    def longestSubarray(self, arr, x):
        minQueue = deque()
        maxQueue = deque()

        n = len(arr)
        start = end = 0

        resStart = resEnd = 0
        while end < n:
            while minQueue and arr[minQueue[-1]] > arr[end]:
                minQueue.pop()

            while maxQueue and arr[maxQueue[-1]] < arr[end]:
                maxQueue.pop()

            minQueue.append(end)
            maxQueue.append(end)

            while arr[maxQueue[0]] - arr[minQueue[0]] > x:
                if start == minQueue[0]:
                    minQueue.popleft()
                if start == maxQueue[0]:
                    maxQueue.popleft()
                start += 1

            if end - start > resEnd - resStart:
                resStart, resEnd = start, end

            end += 1

        return arr[resStart:resEnd + 1]