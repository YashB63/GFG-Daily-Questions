class Solution:
    def areRotations(self,s1,s2):
        m = len(s1)
        n = len(s2)
        
        if m != n:
            return False
            
        comb = s1 + s1
        
        return s2 in comb