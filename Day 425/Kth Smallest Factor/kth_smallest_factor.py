import math

class Solution:
    def kThSmallestFactor(self, N , K):
        factors = []
        
        for i in range(1, int(math.sqrt(N))+1):
            if N % i == 0:
                factors.append(i)
                if  i != N//i:
                    factors.append(N//i)
        
        factors.sort()
        
        if K <= len(factors):
            return factors[K-1]
        
        return -1