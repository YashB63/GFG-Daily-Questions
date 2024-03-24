class Solution:

    def findMinDiff(self, A,N,M):

        x=float("inf")
        A.sort()
        for i in range(N-M+1):
            p=A[i+M-1]-A[i]
            x=min(x,p)
        return x

