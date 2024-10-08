class Solution:
    def possible(self, arr):
        s=sum(arr)
        
        n=len(arr)
        sn=(n*(n+1))/2
        
        if s==sn:
            return True
        return False