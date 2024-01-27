class Solution:
    def isTriangular(self, N):
        
        x = ((8*N) + 1)**0.5
        if x == int(x):
            return 1
        return 0