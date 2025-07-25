class Solution:
    def findminoperation(self, n: int) -> int:
        ans, d = 0, 2
        while n > 1:
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans