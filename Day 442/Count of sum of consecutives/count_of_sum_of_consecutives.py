import math

class Solution:
    def getCount(self, N):
        ans = 0
        k = 2
        while k < math.sqrt(2 * N):
            if (N - (k * (k - 1) // 2)) % k == 0:
                ans += 1
            k += 1
        return ans