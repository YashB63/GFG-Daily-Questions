class Solution:
    def isPalindrome(self, n):
        original = n
        reversed_num = 0

        while n > 0:
            last_digit = n % 10
            reversed_num = reversed_num * 10 + last_digit
            n = n // 10

        return original == reversed_num