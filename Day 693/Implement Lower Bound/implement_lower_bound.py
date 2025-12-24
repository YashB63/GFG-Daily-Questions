class Solution:
    def lowerBound(self, arr, target):
        for i in range(len(arr)):
            if arr[i] >= target:
                return i
        return len(arr)