class Solution:
    def reverseDigits(self, n):
        rev_n = 0

        while n > 0:
            rev_n = rev_n * 10 + n % 10
            n = n // 10

        return rev_n