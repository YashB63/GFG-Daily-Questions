class Solution:
    
   
    def isAnagram(self,a,b):
       
        if len(a) != len(b):
            return False
            
        x = {}
        for char in a:
            x[char] = x.get(char, 0) + 1
        
        y = {}
        for char in b:
            y[char] = y.get(char, 0) + 1
            
        return x == y