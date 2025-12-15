class Solution:
    def searchInsertK(self, arr, k):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == k:
                return mid

            elif arr[mid] > k:
                right = mid - 1

            else:
                left = mid + 1

        return left