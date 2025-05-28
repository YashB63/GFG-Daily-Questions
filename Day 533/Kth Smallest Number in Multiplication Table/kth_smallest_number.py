class Solution(object):
    def kthSmallest(self, m, n, k):
        l = 1
        r = m * n

        while (l < r):

            mid = (l + r) // 2
            cnt = 0
            for i in range(1, m + 1):

                cnt += min(mid // i, n)

            if cnt < k:
                l = mid + 1
            else:
                r = mid

        return l