class Solution:
    
    def minIndexChar(self,Str, pat): 
        
        for i in range(len(Str)):
            if Str[i] in pat:
                return i
                break
        
        return -1