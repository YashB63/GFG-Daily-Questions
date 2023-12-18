class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        
        set_a = set(a)
        set_b = set(b)
        
        return len(set_a.intersection(set_b))