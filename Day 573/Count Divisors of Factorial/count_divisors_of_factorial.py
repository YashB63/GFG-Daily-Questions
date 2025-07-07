from math import sqrt
from collections import defaultdict

class Solution:
    def totalDivisors(self, N: int) -> int:
        if N <= 2:
            return N
        
        ans = 1
        mp = defaultdict(int)
        
        for i in range(2, N + 1):
            x = i
            for j in range(2, int(sqrt(x)) + 1):
                while x % j == 0:
                    x //= j
                    mp[j] += 1
            if x >= 2:
                mp[x] += 1

        for exponent in mp.values():
            ans *= (exponent + 1)

        return ans