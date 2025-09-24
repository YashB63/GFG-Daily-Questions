class Solution:
    def convert(self, n):
        if n == 0:
            return 0

        digit = n % 10

        if digit == 0:
            digit = 5

        return self.convert(n // 10) * 10 + digit

    def convertFive(self, n):
        if n == 0:
            return 5
        else:
            return self.convert(n)