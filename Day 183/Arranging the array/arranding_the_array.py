from typing import List

class Solution:
    def Rearrange(self, n : int, arr : List[int]) -> None:
        
        neg = []
        pos = []
        for i in arr:
            if i >= 0 :
                pos.append(i)
            else:
                neg.append(i)
        arr.clear()
        arr.extend(neg)
        arr.extend(pos)