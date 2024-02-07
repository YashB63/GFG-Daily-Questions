class Solution:
    def minOperation(self, s): 
        
        x = 0
        n = len(s)
        for i in range(1, n//2+1):
            if s[:i] == s[i:i*2]:
                x = i
        if x == 0:
            
            return n
        
        return n - x + 1