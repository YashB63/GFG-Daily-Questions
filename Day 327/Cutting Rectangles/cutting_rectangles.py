import math

class Solution:
    def minimumSquares(self, L, B):
        K=math.gcd(L,B)
        N=(L*B)//(K*K)
        return[N, K]