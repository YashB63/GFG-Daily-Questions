from typing import List

class Solution:
    def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
        p,s=[0]*N,[0]*N
        ans=[0]*N
        up,us=set(),set()
        for i in range(N):
            p[i]=len(up)
            up.add(A[i])
        for i in range(N-1,-1,-1):
            s[i]=len(us)
            us.add(A[i])
        for i in range(N):
            ans[i]=p[i]-s[i]
        return ans