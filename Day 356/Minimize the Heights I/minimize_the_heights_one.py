class Solution:
    def getMinDiff(self,k, arr):
        n=len(arr)
        arr.sort()
        min_diff = arr[n-1] - arr[0]
        for i in range(n - 1):
            high = max(arr[i] + k, arr[n-1] - k)
            low = min(arr[0] + k, arr[i+1] - k)
            min_diff = min(min_diff, high - low)
        return min_diff