class Solution:
    def canReach(self, A, N):
         
        finalposition = N-1
        
        for i in range(N-2,-1,-1):
            if i + A[i] >= finalposition:
                finalposition = i
                
        return 1 if finalposition == 0 else 0