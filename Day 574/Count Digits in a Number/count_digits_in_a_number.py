class Solution:
    def countDigits(self, n):
        if n < 0: n = -n
        if n < 10:
            return 1
        return 1 + (self.countDigits(n // 10))