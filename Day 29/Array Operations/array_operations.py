from typing import List

class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        
        i = 0
        j = 0
        k = 0
        
        if sum(arr) == 0:
            return 0
        
        while i <= j and j < n:
            if arr[i] != 0 and arr[j] != 0:
                j += 1
                continue
            elif arr[j] == 0 and arr[i] != 0:
                j += 1
                i = j
                k += 1
                continue
            else:
                j += 1
                i = j
        
        if arr[-1] != 0:
            k += 1
            
        if k == 0 or 0 not in arr:
            return -1
            
        return k