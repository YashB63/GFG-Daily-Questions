class Solution:
    def setSetBit(self, x, y, l, r):
        
        m = x
        
        for i in range(l,r+1):
            
            if y & (1 << (i-1)):
                
                m = m | (1<<(i-1))
        
        return m