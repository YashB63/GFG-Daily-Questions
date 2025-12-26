class Solution:
    def sumOfDigits(self, n):
        if n < 10:
            return n
        return (n % 10) + (self.sumOfDigits(n // 10))