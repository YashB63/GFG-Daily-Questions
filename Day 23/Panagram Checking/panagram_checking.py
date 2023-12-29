class Solution:
    
    def checkPangram(self,s):
        #code here
        s = s.lower()
        
        x = [0 for i in range(26)]
        
        for y in s:
            n = ord(y)
            diff = n - 97
            
            if(diff >= 0):
                x[diff] = 1
        
        for y in x:
            if(y != 1):
                return 0
        
        return 1