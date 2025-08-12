from math import gcd
from itertools import combinations

class Solution:
    def Count(self, nums, k):
        def lcm(a, b):
            return a * b // gcd(a, b)

        n = len(nums)
        res = 0

        for r in range(1, n + 1):
            for comb in combinations(nums, r):
                l = comb[0]
                for num in comb[1:]:
                    l = lcm(l, num)
                    if l > k:  
                        break
                else:
                    cnt = k // l
                    if r % 2 == 1:
                        res += cnt  
                    else:
                        res -= cnt  

        return res