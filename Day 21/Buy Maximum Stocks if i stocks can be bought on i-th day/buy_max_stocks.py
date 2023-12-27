from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        res = 0
        for i in sorted([*range(n)], key=lambda x:price[x]):
            p = price[i]
            i = i + 1
            if k >= p*i:
                res += i
                k -= p*i
            elif k//p>0:
                res += k//p
                k=0
            if k==0:
                return res
        return res