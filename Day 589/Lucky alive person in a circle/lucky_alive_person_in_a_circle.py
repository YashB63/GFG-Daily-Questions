class Solution:
    def find(self,N):
        p = 1
        while (p <= N):
            p *= 2
        
        return (2 * N) - p + 1