class Solution:
    def sumOfDigits(self, n):
        sum = 0
        while n != 0:
            last = n % 10
            sum += last
            n //= 10
        return sum