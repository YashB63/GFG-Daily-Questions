from typing import List

class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        
        arr.sort()
        s,e=0,1
        
        while e<n:
            diff=arr[e]-arr[s]
            if diff==x and e!=s:
                return 1
            elif diff>x:
                s+=1
            else:
                e+=1
        
        
        return -1 