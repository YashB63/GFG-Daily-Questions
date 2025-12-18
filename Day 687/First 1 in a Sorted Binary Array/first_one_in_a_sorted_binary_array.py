class Solution:
    def indexOfFirstOne(self, arr, low, high):
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == 1 and (mid == 0 or arr[mid - 1] == 0):
                return mid
            elif arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def firstIndex(self, arr):
        n = len(arr)
        return self.indexOfFirstOne(arr, 0, n - 1)
