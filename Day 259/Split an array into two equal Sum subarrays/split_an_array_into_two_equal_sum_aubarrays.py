from typing import List

class Solution:
    def missingNumber(self, n : int, arr : List[int]) -> int:
        total = (n+1) * n //2
        sum1 =sum(arr)
        sum2 = total -sum1
        return sum2