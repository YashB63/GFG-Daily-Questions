class Solution:
    
    def posOfRightMostDiffBit(self,m,n):
        xor_result = m ^ n
        
        if xor_result == 0:
            return -1
            
        pos = 1
        while xor_result:
            if xor_result & 1:
                return pos
            xor_result >>= 1
            pos += 1
        return pos