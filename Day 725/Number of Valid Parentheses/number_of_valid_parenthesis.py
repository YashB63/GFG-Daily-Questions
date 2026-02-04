class Solution:
    def findWays(self, n):
        if n & 1:
            return 0

        k = n // 2  

        res = 1
        for i in range(k):
            res = res * (2 * k - i) // (i + 1)

        return res // (k + 1)