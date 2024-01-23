from typing import List
class Solution:
    def getMaximum(self, N : int, arr : List[int]) -> int:
        
        x = sum(arr)
        for i in range(N, 0, -1):
            if x%i == 0:
                return i