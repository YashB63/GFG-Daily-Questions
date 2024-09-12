from typing import List

class Solution:
    def totalTime(self, n : int, arr : List[int], penalty : List[int]) -> int:
        d={}
        t=0
        d[arr[0]]=1
        for i in range(1,n):
            if arr[i] in d:
                t+=penalty[arr[i]-1]
            else:
                t+=1
                d[arr[i]]=1
        return t