class Solution:
    def searchInSorted(self, arr, K):
        N = len(arr)
        left, right = 0, N - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == K:
                return True
            elif arr[mid] < K:
                left = mid + 1
            else:
                right = mid - 1

        return False