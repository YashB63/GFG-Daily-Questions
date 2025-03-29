from itertools import accumulate

from typing import List
class Solution:
    def solve(self, N : int, K : int, arr : List[int]) -> int:
        S, factors = sum(arr), set()
        
        for i in range(1, int(S ** 0.5) + 1):
            if S % i == 0:
                factors.add(i)
                factors.add(S//i)
        
        factors = sorted(factors, reverse = True)
        prefixsum = list(accumulate(arr))
        
        for i in factors:
            count = 0
            for j in prefixsum:
                count += (not j % i)
                if count >= K: return i

        return -1