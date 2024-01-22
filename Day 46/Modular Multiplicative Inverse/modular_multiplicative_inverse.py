class Solution:    
    
    def modInverse(self,a,m):
        
        for i in range(1, m+1):
            if (i*a)%m == 1:
                return i
        else:
            return -1