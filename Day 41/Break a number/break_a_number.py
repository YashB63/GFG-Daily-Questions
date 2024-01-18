class Solution:
    def waysToBreakNumber(self, n):
        
        numerator = (n + 2) * (n + 1)
        denominator = 2
        res = numerator // denominator
        
        return res % (10**9 + 7)
