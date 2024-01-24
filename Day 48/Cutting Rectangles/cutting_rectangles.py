import math

class Solution:
    def minimumSquares(self, L, B):
       
        x = math.gcd(L, B)
        y = (L//x) * (B//x)
        return y,x