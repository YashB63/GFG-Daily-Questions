class Solution:
    def upperBound(self, arr, target):
        lo, hi = 0, len(arr) - 1
        res = len(arr)

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] > target:
                res = mid
                hi = mid - 1

            else:
                lo = mid + 1

        return res