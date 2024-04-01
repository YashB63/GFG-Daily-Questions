class Solution:
    
    def countWays(self,n):
        
        if n == 1 or n == 2:
            return n
        a = 1
        b = 1
        c = 2
        for i in range(2, n):
            res = a + b + c
            a = b
            b = c
            c = res
        return c % (10**9 + 7)