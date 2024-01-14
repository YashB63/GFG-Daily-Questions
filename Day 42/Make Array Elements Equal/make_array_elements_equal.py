class Solution:
    def minOperations(self, N):
        
        x = N//2
        if N%2 == 0:
            return x**2
        else:
            return x*(x+1)