class Solution:
    def isDigitSumPalindrome(self, n):
        newNum = 0
        
        while (n > 0):
            newNum += n % 10
            n //= 10
        reversedNewNum = 0
        n = newNum
        
        while (n > 0):
            reversedNewNum = reversedNewNum * 10 + n % 10
            n //= 10
        return True if reversedNewNum == newNum else False