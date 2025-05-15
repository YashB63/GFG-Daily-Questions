class Solution:

    def findMissing(self, arr):
        n = len(arr)

        diff1 = arr[1] - arr[0]
        diff2 = arr[-1] - arr[-2]
        diff3 = (arr[-1] - arr[0]) // n

        if diff1 == diff2:
            diff = diff1
        elif diff1 == diff3:
            diff = diff1
        else:
            diff = diff2

        if diff == 0:
            return arr[0]

        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if (arr[mid] - arr[0]) // diff == mid:
                lo = mid + 1

            else:
                hi = mid - 1

        return arr[hi] + diff