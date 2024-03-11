class Solution:
    def MinRemove(self, n, s): 
        
        if s == s[::-1]:
            return 1
        return 2