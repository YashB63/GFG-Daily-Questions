import math

class Solution:
    def isPrime (self, N):
        
        if N <= 1:
            return 0
        if N == 2 or N == 3:
            return 1
        sq = int(math.sqrt(N))
        for i in range(2, sq + 2):
            if N%i == 0:
                return 0
        return 1