from typing import List

class Solution:
    def uniqueRow(self, row : int, col : int, M : List[List[int]]) -> List[List[int]]:
    
        k = []
        for i in M :
            if i not in k:
                k.append(i)
        return k