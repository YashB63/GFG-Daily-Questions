from typing import List

class Solution:
    def minimumInteger(self, N : int, A : List[int]) -> int:
       
        A.sort()
        A.reverse()
        s = sum(A)
        
        for i in A:
            x = N * i
            if x >= s:
                y = i
        return y