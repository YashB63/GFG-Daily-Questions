class Solution:
    def check(self, arr, k, m, days):
        bouquets = 0
        cnt = 0

        for flower in arr:
            if flower <= days:
                cnt += 1
            else:

                bouquets += cnt // k
                cnt = 0

        bouquets += cnt // k

        return bouquets >= m

    def minDaysBloom(self, arr, k, m):
        lo = 0
        hi = max(arr)
        res = -1

        while lo <= hi:
            mid = (lo + hi) // 2

            if self.check(arr, k, m, mid):

                res = mid
                hi = mid - 1
            else:
                
                lo = mid + 1
        return res