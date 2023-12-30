class Solution:
    def inSequence(self, A, B, C):
        
        if C == 0:
            if A == B:
                return 1
            return 0
            
        x = (B - A)/C + 1
        
        if int(x) == x and x > 0:
            return 1
        return 0