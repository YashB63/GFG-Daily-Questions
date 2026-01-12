class Solution:
    def donutsByChef(self, t, r):
        D = 1.0 + (8.0 * t) / r
        return int((-1.0 + math.sqrt(D)) / 2.0)

    def canMake(self, ranks, n, t):
        total = 0
        for r in ranks:
            total += self.donutsByChef(t, r)
            if total >= n:
                return True
        return False

    def minTime(self, ranks, n):
        rmin = min(ranks)
        hi = rmin * n * (n + 1) // 2
        lo, ans = 0, hi

        while lo <= hi:
            mid = (lo + hi) // 2
            if self.canMake(ranks, n, mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans