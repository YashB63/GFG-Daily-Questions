class Solution:
    def maxAdj(self, arr):
        return [max(arr[i - 1], arr[i]) for i in range(1, len(arr))]