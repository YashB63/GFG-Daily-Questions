class Solution:
    
    def sortAbs(self,a, n, k):
        
        def compare(x):
            return abs(x - k)
        
        a.sort(key=compare)
        
        return a