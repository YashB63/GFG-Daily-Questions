import math

class Solution:
    def findMinimumIF(self, arr):
        minimum = math.inf
        n = len(arr)  

        for i in range(n):
            arr[i] = int(str(arr[i])[::-1])
        
        arr.sort()

        for i in range(1, n):
            minimum = min(minimum, arr[i] - arr[i - 1])

        return minimum