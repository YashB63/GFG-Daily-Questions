class Solution:

    def swapBits(self, X, P1, P2, N):
        mask1 = (X >> P1) & ((1 << N) - 1)
        mask2 = (X >> P2) & ((1 << N) - 1)
        
        if mask1 == mask2:
            return X
        
        xor_mask = (mask1 ^ mask2)
        
        xor_mask1 = xor_mask << P1
        xor_mask2 = xor_mask << P2
        
        X = X ^ xor_mask1
        X = X ^ xor_mask2
        
        return X