from typing import List
class Solution:
    def solve(self, N : int, A : List[int], B : List[int]) -> int:
        if sum(A)!=sum(B):
            return -1
        
        A.sort()  
        B.sort()

        Aodd, Aeven = [], []
        Bodd, Beven = [], []

        for i in range(N):
            if A[i] % 2 == 0:
                Aeven.append(A[i])
            else:
                Aodd.append(A[i])
            if B[i] % 2 == 0:
                Beven.append(B[i])
            else:
                Bodd.append(B[i])

        if len(Aeven) != len(Beven) or len(Aodd) != len(Bodd)  :
            return -1

        res = 0
        for i in range(len(Aeven)):
            res += abs(Aeven[i] - Beven[i])
        for i in range(len(Aodd)):
            res += abs(Aodd[i] - Bodd[i])

        return res // 4