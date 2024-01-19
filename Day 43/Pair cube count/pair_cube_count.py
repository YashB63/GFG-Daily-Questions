import math

class Solution:
    def pairCubeCount(self, N):
        
        count = 0
        for a in range(1, int(math.pow(N, 1/3)) + 1):
            xa = a*a*a
            xb = N - xa
            b = math.ceil(math.pow(xb, 1/3))
            if b**3 == xb:
                count += 1
        return count