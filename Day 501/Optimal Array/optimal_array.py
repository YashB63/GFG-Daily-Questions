from typing import List

class Solution:
    def optimalArray(self, n : int, a : List[int]) -> List[int]:
        l=[0]
        s=0
        for i in range(1,n):
            m=a[i//2]
            s+=abs(a[i]-m)
            l.append(s)
        return l