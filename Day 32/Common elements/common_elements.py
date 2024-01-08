class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        
        A = set(A)
        B = set(B)
        C = set(C)
        
        x  = list(A.intersection(B.intersection(C)))
        x.sort()
        return x