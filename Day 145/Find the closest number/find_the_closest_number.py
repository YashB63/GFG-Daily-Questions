from typing import List

class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        
        min, val = k, 0
        for i in arr:
            if i-k <= min:
                min, val = abs(i-k),i
        return val if val != 0 else arr[0]