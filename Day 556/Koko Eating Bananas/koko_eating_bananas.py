class Solution:
    def check(self, arr, mid, k):
        hours = 0
        for bananas in arr:
            hours += bananas // mid
            if bananas % mid != 0:
                hours += 1
        return hours <= k

    def kokoEat(self, arr, k):
        lo = 1
        hi = max(arr)
        res = hi

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if self.check(arr, mid, k):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return res