from typing import List

class Solution:
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        premax=[0]*N
        c=0
        premax[0]=A[0]
        for i in range(1,N):
            premax[i]=max(premax[i-1],A[i])
        premin=[0]*N
        premin[-1]=A[-1]
        for i in range(N-2,-1,-1):
            premin[i]=min(premin[i+1],A[i])
        
        for i in range(N-1):
            if premax[i]+premin[i+1]>=K:
                c+=1
        return c