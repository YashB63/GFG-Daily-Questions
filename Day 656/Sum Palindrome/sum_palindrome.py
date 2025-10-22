class Solution:
    def isSumPalindrome(self, n):
        def reverse(n):
            rev_num = 0
            while n > 0:
                rev_num = rev_num * 10 + n % 10
                n = n // 10
            return rev_num

        def isPalindrome(n):
            return reverse(n) == n

        count = 0
    
        while ((isPalindrome(n) == False) and count < 5):
            k = reverse(n)
            n += k
            count += 1

        if isPalindrome(n):
            return n
        return -1