from typing import List

class Solution:
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        
        Larr = arr[:n//2]
        Rarr = arr[n//2:]
        Larr.sort()
        Rarr.sort()
        count = 0
        i,j = n//2-1,n//2-1
        while(i>=0 and j>=0):
            if(Larr[i]>=5*Rarr[j]):
                count+=(j+1)
                i-=1
            else:
                j-=1
        return count