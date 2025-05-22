class Solution:
    def getSpecialNumber(self, N):
        N -= 1
        result = 0
        multiplier = 1

        while N > 0:
            digit = N % 6
            result += digit * multiplier
            multiplier *= 10
            N //= 6

        return result