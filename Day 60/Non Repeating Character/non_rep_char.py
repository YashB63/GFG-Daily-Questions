class Solution:
    
    def nonrepeatingCharacter(self,s):
        
        x = set()
        repeated = set()
        
        for char in s:
            if char in x:
                repeated.add(char)
            else:
                x.add(char)
                
        for char in s:
            if char not in repeated:
                return char
                
        return -1