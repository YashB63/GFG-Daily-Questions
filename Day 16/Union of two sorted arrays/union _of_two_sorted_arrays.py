class Solution:
    
    def findUnion(self,a,b,n,m):
        
        return sorted(set(a) | set(b)) 