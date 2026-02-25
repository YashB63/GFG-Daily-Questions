class Solution:
    def isBitSet (self, N):
        return 1 if N!=0 and N&(N+1)==0 else 0