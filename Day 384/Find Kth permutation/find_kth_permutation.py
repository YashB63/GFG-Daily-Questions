from typing import List
import math

class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        res = 0
        nums = [i for i in range(1,n+1)]
        k -= 1
        while len(nums)>0:
            fact = int(math.factorial(len(nums)-1))
            idx = k//fact
            res = res*10 + nums.pop(idx)
            k = k%fact
        return res