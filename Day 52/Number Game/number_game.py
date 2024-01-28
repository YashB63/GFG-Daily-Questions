import math

class Solution:
    def numGame(self, n):
         
        mod = 1000000007
        
        if n == 1:
            return n
        
        res = 1
        for i in range(1, n+1):
            res = ((res*i)//math.gcd(res, i))%mod
        return res