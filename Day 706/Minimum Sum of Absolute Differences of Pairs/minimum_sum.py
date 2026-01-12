class Solution:
    def findMinSum(self, A,B,N):
        sum=0
        
        A.sort()
        B.sort()
        
        for i in range(0,N):
            sum+=abs(A[i]-B[i])
        
        return sum