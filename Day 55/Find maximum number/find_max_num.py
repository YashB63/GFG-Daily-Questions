class Solution:
    def findMax(self, N):
        
        N = sorted(str(N))[::-1]
        return int(''.join(N))